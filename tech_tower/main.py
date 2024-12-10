import sys
from stable_quicksort import QuickSort
from dfs import DFS

class TechTower():
    def __init__(self) -> None:
        self.matrix = []
        self.room_amount = None
        self.emergency_exits_amount = None
        self.dangerous_rooms_amount = None
        self.emergency_exits = []
        self.dangerous_rooms = []
        self.emergency_routes = []

        self.read_and_validate_input()
        self.calculate_emergency_routes()

        print(self)

    def read_and_validate_input(self):
        first_line = input()
        try:
            #read first 3 numbers (nkm)
            nkm_list = list(map(int, first_line.split()))
            self.room_amount = nkm_list[0]
            self.emergency_exits_amount = nkm_list[1]
            self.dangerous_rooms_amount = nkm_list[2]

            if self.room_amount < 2 or self.room_amount > 30:
                raise ValueError("incorrect room amount / n")
            if self.emergency_exits_amount < 1 or self.emergency_exits_amount > 5:
                raise ValueError("incorrect emergency exits amount / k")
            if self.dangerous_rooms_amount < 1 or self.dangerous_rooms_amount > 3:
                raise ValueError("incorrect dangerous rooms amount / m")
            

            #read matrix
            for _ in range(self.room_amount):
                row = input()
                row = list(map(int, row.split()))

                for value in row:
                    if value not in (0, 1):
                        raise ValueError("only 0's and 1's are accepted as matrix values")
                if len(row) != self.room_amount:
                    raise ValueError(f"each row is supposed to have {self.room_amount} elements")

                self.matrix.append(row)
            

            #read emeregency exits
            second_to_last_line = input()
            self.emergency_exits = list(map(int, second_to_last_line.split()))
            if len(self.emergency_exits) != self.emergency_exits_amount:
                raise ValueError(f"wrong number of emergency exits, expected {self.emergency_exits_amount}")
            QuickSort(self.emergency_exits).sort()
            # temp = self.emergency_exits[:]
            # if self.emergency_exits != QuickSort(temp).sort():
            #     raise ValueError("emergency exits should be sorted")
            
            #this onyl works because we already checked if the list is sorted
            if self.emergency_exits[0] < 1 or self.emergency_exits[-1] > self.room_amount:
                raise ValueError("emeregency exits cant be in nonexisting rooms")
            

            #read dangerous rooms
            last_line = input()
            self.dangerous_rooms = list(map(int, last_line.split()))
            if len(self.dangerous_rooms) != self.dangerous_rooms_amount:
                raise ValueError(f"wrong number of dangerous rooms, expected {self.dangerous_rooms_amount}")
            QuickSort(self.dangerous_rooms).sort()
            # temp = self.dangerous_rooms[:]
            # if self.dangerous_rooms != QuickSort(temp).sort():
            #     raise ValueError("dangerous rooms should be sorted")
            
            if self.dangerous_rooms[0] < 1 or self.dangerous_rooms[-1] > self.room_amount:
                raise ValueError("dangerous rooms have to exist in the tower")


        except ValueError:
            print('BŁĄD')
            sys.exit(1)

    def calculate_emergency_routes(self):
        for dangerous_room in self.dangerous_rooms:
            does_path_exist, path = DFS(self.matrix, dangerous_room, self.emergency_exits).run_dfs()
            self.emergency_routes.append([does_path_exist, path])

    def calculate_if_safe(self):
        path_counter = 0
        for result in self.emergency_routes:
            path = result[1]
            if path is not None:
                path_counter += 1
        return path_counter == len(self.emergency_routes)

    def __str__(self) -> str:
        output = []

        if self.calculate_if_safe() == True:
            output.append("BEZPIECZNY")
        else:
            output.append("NIEBEZPIECZNY")

        #emergency routes length is the same as dangerous rooms so they can share an index since emeregency routes were calculate
        #from dangerous rooms from first to last and appended in the same order
        for danger_room_index, result in enumerate(self.emergency_routes):
            path = result[1]
            if path is None:
                output.append(f"BRAK DROGI Z POMIESZCZENIA {self.dangerous_rooms[danger_room_index]}")
            else:
                output.append(" ".join(list(map(str,path))))

        if output[0] == "BEZPIECZNY":
            path_in_str_format = list(map(str,(DFS(self.matrix,self.dangerous_rooms[0],check_connectivity=True).run_dfs()[1])))
            output.append(" ".join(path_in_str_format))


        
        return "\n".join(output)


TechTower()
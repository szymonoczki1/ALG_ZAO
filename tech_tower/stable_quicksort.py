class QuickSort():
    def __init__(self,arr) -> None:
        self.arr = arr
        
    def sort(self):
        self._quicksort(self.arr, 0, len(self.arr) - 1)
        return self.arr
    
    def _partition(self, arr, first_index, last_index):
        pivot_index = first_index + (last_index - first_index) // 2
        pivot_value = arr[pivot_index]
        smaller = []
        bigger = []
        
        for i in range(first_index, last_index+1):
            #dont touch the pivot
            if i != pivot_index:
                if arr[i] < pivot_value:
                    smaller.append(arr[i])
                elif arr[i] > pivot_value:
                    bigger.append(arr[i])
                #if pivot value is the same as arr[i] go into else
                else:
                    if i < pivot_index:
                        smaller.append(arr[i])
                    elif i > pivot_index:
                        bigger.append(arr[i])


        arr[first_index:last_index+1] = smaller + [pivot_value] + bigger
        #recalculate pivot index
        pivot_index = first_index + len(smaller)
        return pivot_index



    def _quicksort(self, arr, first_index, last_index):
        #if makes sure that array has to have at least 2 elements for it to be sorted
        #if first_index is equal or higher(notgoingtohappen) it shouldnt call anymroe recursions
        if first_index < last_index:
            pivot_index = self._partition(arr, first_index, last_index)
            #pivot_index -1 and +1 is because pivot is already at the correct place and is not to be included in next part of sorting
            self._quicksort(arr,first_index,pivot_index-1)
            self._quicksort(arr,pivot_index+1,last_index)
        #no return bcs quicksort rearranges the array that is given 
        


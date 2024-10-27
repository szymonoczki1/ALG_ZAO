def checkIfSequenceCanBeGraphic():
    sequence = input()
    sequence = list(map(int, sequence.split()))

    sequence.sort(reverse=True)

    while sequence:
        firstDeg = sequence.pop(0)
        if firstDeg > len(sequence):
            return False

        for i in range(firstDeg):
            sequence[i] -= 1
            if sequence[i] < 0:
                return False
        sequence.sort(reverse=True)
    return True

if checkIfSequenceCanBeGraphic() == True:
    print('TAK')
else:
    print('NIE')
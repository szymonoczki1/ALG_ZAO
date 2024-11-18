def partition(arr, first_index, last_index):
    pivot_index = first_index + (last_index - first_index) // 2
    pivot_value = arr[pivot_index]
    #move pivot to last index so i cant lose track of it if i becomes pivot index
    arr[pivot_index], arr[last_index] = arr[last_index], arr[pivot_index]
    #after the line above pivot index will no longer be index of our pivot thats why we need to assign pivot value to compare in for loop
    i = first_index - 1
    for j in range(first_index, last_index): 
    # do not iterate through last index bcs we dont want to mess with pivot
        if arr[j] < pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    #swap pivot which is at last_index with i+1 which tells us that everything before that i+1 index is lower than pivot
    arr[last_index], arr[i+1] = arr[i+1], arr[last_index]

    pivot_index = i+1
    return pivot_index



def quicksort(arr, first_index, last_index):
    #if makes sure that array has to have at least 2 elements for it to be sorted
    #if first_index is equal or higher(notgoingtohappen) it shouldnt call anymroe recursions
    if first_index < last_index:
        pivot_index = partition(arr, first_index, last_index)
        #pivot_index -1 and +1 is because pivot is already at the correct place and is not to be included in next part of sorting
        quicksort(arr,first_index,pivot_index-1)
        quicksort(arr,pivot_index+1,last_index)
    #no return bcs quicksort rearranges the array that is given 
    
array = [8, 3, 7, 6, 4, 5, 2]
quicksort(array,0,len(array)-1)
print(array)
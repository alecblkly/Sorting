# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        place_holder = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = place_holder

    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # Setting swapped to True to be able to utilize in the while
    # Unable to utilize swapped if it is not declared before assignment
    swapped = True

    while swapped:
        # Setting swapped to False, loop will continue to run
        # Once swapped does not equal true, it goes to the next if
        # and hits break
        swapped = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                print("Left Side: ", arr[i], arr[i + 1])
                print("Right Side: ", arr[i + 1], arr[i])
        if swapped == False:
            break
    print("arr: ", arr)
    return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr

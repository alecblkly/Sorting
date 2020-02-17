# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        print("cur_index, i loop: ", cur_index)
        print("smallest_index, i loop: ", smallest_index)
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                print("arr[smallest_index], j loop: ", arr[smallest_index])
                print("arr[j], j loop: ", arr[j])
                print("arr[smallest_index] > arr[j], j loop: ",
                      arr[smallest_index] > arr[j])
                smallest_index = j
                print("J, j loop: ", j)
                print("-----------------------------------------")

        # TO-DO: swap
        place_holder = arr[smallest_index]
        print("arr[smallest_index], swap: ",
              arr[smallest_index])
        arr[smallest_index] = arr[cur_index]
        print("arr[cur_index], swap: ", arr[cur_index])
        arr[cur_index] = place_holder
        print("place_holder, swap: ", place_holder)

    print("Final arr: ", arr)
    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr

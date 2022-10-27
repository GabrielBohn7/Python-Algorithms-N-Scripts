class InsertionSort:
    # Python implementation of Insertion Sort
    def insertionSort(self, arr):
        # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):
            j = i - 1
            while j >= 0 and arr[j + 1] < arr[j]:
                # arr[j] and arr[j + 1] are out of order so swap them
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp
                j -= 1
        return arr


if __name__ == '__main__':
    arr = [9,2,5,3,4]
    sortedArr = InsertionSort().insertionSort(arr)
    print(sortedArr)

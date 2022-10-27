class QuickSort:
    def quickSort(arr, s, e):
        if e - s + 1 <= 1:
            return

        pivot = arr[e]
        left = s  # pointer for left side

        # Partition: elements smaller than pivot on left side
        for i in range(s, e):
            if arr[i] < pivot:
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1

        # Move pivot in-between left & right sides
        arr[e] = arr[left]
        arr[left] = pivot

        # Quick sort left side
        QuickSort().quickSort(arr, s, left - 1)

        # Quick sort right side
        QuickSort().quickSort(arr, left + 1, e)

        return arr

if __name__ == '__main__':
    arr = [9,2,5,3,4]
    sortedArr = QuickSort().quickSort(arr)
    print(sortedArr)

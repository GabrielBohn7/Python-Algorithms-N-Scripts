class BinarySearchRange:
    def binarySearch(self, arr, target):
        L, R = 0, len(arr) - 1

        while L <= R:
            mid = (L + R) // 2

            if target > arr[mid]:
                L = mid + 1
            elif target < arr[mid]:
                R = mid - 1
            else:
                return mid
        return -1

    # Binary search on some range of values
    def binarySearchRange(self, low, high):

        while low <= high:
            mid = (low + high) // 2

            if BinarySearchRange().isCorrect(mid) > 0:
                high = mid - 1
            elif BinarySearchRange().isCorrect(mid) < 0:
                low = mid + 1
            else:
                return mid
        return -1

    # Return 1 if n is too big, -1 if too small, 0 if correct
    def isCorrect(n):
        if n > 10:
            return 1
        elif n < 10:
            return -1
        else:
            return 0

if __name__ == '__main__':
    arr = [0,2,6,8,23]
    arrPosition = BinarySearchRange().binarySearch(arr, 8)
    print(arrPosition)

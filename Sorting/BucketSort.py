class BucketSort:
    def bucketSort(arr):
        # Assuming arr only contains 0, 1 or 2
        counts = [0, 0, 0]

        # Count the quantity of each val in arr
        for n in arr:
            counts[n] += 1

        # Fill each bucket in the original array
        i = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                arr[i] = n
                i += 1
        return arr

if __name__ == '__main__':
    arr = [9,2,5,3,4]
    sortedArr = BucketSort().bucketSort(arr)
    print(sortedArr)

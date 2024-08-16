import random
import sys
import time

def kthOrderStatistic(k, size, arr):
    if k < 0 or k >= size:
        return -1

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def partition(left, right):
        pivot_index = random.randint(left, right)
        pivot_value = arr[pivot_index]
        swap(pivot_index, right)
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot_value:
                swap(i, store_index)
                store_index += 1
        swap(store_index, right)
        return store_index

    def select(left, right, k_smallest):
        if left == right:
            return arr[left]
        pivot_index = partition(left, right)
        if k_smallest == pivot_index:
            return arr[k_smallest]
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)

    return select(0, size - 1, k)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python roll_no.py K size arr[1] arr[2] ... arr[size]")
        sys.exit(1)

    k = int(sys.argv[1])
    size = int(sys.argv[2])
    args = sys.argv[3:]
    arr = [int(arg) for arg in args]

    start_time = time.time()
    result = kthOrderStatistic(k, size, arr)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Kth Order Statistic: {result} (Execution Time: {execution_time} seconds)")


#python .\m22ai608-BigdataAssignment-Ans.py 2 10 5 6 8 5 8 4 7 1 5 9
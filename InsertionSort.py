# INSERTION-SORT For Monotonically Decreasing Order

def insertion_sort_monotonically_decreasing(A):

    n = len(A)

    for j in range(1, n):
        key = A[j]
        i = j - 1

        while i >= 0 and A[i] < key:
            A[i + 1] = A[i]
            i = i - 1

        A[i + 1] = key

    return A


if __name__ == "__main__":
    # arr = [31, 23, 17, 14, 9, 5, 2]
    arr = [31, 23, 17, 14, 9, 5, 2]
    print("Original given array (monotonically decreasing):", arr)
    sorted_arr = insertion_sort_monotonically_decreasing(arr)
    print("Sorted array via insertion sort :", sorted_arr)

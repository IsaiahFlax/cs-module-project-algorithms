'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    arr2 = [0] * len(arr)
    i = 0
    for n in arr:
        if n != 0:
            print(arr2)
            arr2[i] = n
            i = i+1
    return arr2


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
'''
Input: a List of integers
Returns: a List of integers
'''
import math
def product_of_all_other_numbers(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    if len(arr) > 1:
        i = 0
        arr2 = [0]*len(arr)
        for n in arr:
            if arr[i] == n:
                left = arr[:i]
                right = arr[i+1:]
                print("left", math.prod(left))
                print("right", right)
                print("i", i)
                arr2[i] = math.prod(left) * math.prod(right)
                print("arr2", arr2)
            i = i+1
        return arr2

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [20, 4, 3, 8, 5]
    
    #arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

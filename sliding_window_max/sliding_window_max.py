'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    if len(nums) < k:
        return max(nums)
    start = 0
    end = k
    arr2 = [0]*(len(nums)-k+1)
    while end < len(nums)+1:
        window = nums[start:end]
        print("w", window)
        arr2[start] = max(window)
        print(arr2)
        
        start = start + 1
        end = end + 1
    return arr2
        

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

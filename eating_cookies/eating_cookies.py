'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # if n == 2:
    #     return 2
    arr = [0, 1, 1,]
    while len(arr) < n +2:
        arr2 = arr[-3:]
        #print(arr2)
        arr.append(sum(arr2))
        #print(arr)
    return arr[-1:].pop()
if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    print(eating_cookies(50))
    print(eating_cookies(100))
    print(eating_cookies(500))
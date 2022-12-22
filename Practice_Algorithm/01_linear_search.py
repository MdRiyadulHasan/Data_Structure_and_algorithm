def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
if __name__ == '__main__':
    arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
    target = 110
    index = linear_search(arr,target)
    if index!=-1:
        print(f'{target} found at {index}')
    else:
        print(f'{target} not found')
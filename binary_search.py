def binary_search(numbers_list,number_to_search):
    numbers_list.sort()
    print(numbers_list)
    left_index=0
    right_index=len(numbers_list)-1
    mid_index=0
    while(left_index<right_index):
        mid_index=(left_index+right_index)//2
        mid_number = numbers_list[mid_index]
        if mid_number==number_to_search:
            return mid_index
        elif mid_number<number_to_search:
            left_index=mid_index+1
        else:
            right_index=mid_index-1
    return -1

if __name__ == '__main__':
    numbers_list = list(map(int,input().strip().split()))
    number_to_search = int(input().strip())
    index = binary_search(numbers_list,number_to_search)
    if index !=-1:
        print(f'{numbers_list[index]} is found in position {index}')
    else:
        print(f'{number_to_search} not found')

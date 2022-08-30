def linear_search(numbers_list,number_to_search):
    for index, element in enumerate(numbers_list):
        if(numbers_list[index]==number_to_search):
            return index
    return -1

if __name__ == '__main__':
    numbers_list = list(map(int,input().strip().split()))
    number_to_search = int(input().strip())
    index = linear_search(numbers_list,number_to_search)
    if index !=-1:
        print(f'{numbers_list[index]} is found in position {index}')
    else:
        print(f'{number_to_search} not found')


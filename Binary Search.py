def binary_search(search_list, number_to_find):

    left_index = 0
    right_index = len(search_list) - 1
    mid_index = 0



    while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            mid_number = search_list[mid_index]

            if mid_number == number_to_find:
                return mid_index

            if mid_number < number_to_find:
                left_index = mid_index + 1

            else:
                right_index = mid_index - 1

    return -1



def binary_search_recursive(search_list, number_to_find, left_index, right_index):

    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_number = search_list[mid_index]

    if mid_number == number_to_find:
        return mid_index


    if mid_number < number_to_find:
        left_index = mid_index + 1


    else:
        right_index = mid_index - 1



    return binary_search_recursive(search_list,number_to_find,left_index,right_index)

def get_reoccuring_numbers(search_list, number_to_find):

    index = binary_search(search_list,number_to_find)

    indicies = [index]

    i = index - 1

    while i >= 0:
        if search_list[i] == number_to_find:
            indicies.append(i)
        else:
            break
        i = i - 1

    #right_side search

    i = index + 1

    while i < len(search_list):
        if search_list[i] == number_to_find:
            indicies.append(i)
        else:
            break
        i += 1

    return sorted(indicies)





if __name__ == '__main__':

    search_list = [5,5,10,15,15,15,20,25]

    number = 25

    index = get_reoccuring_numbers(search_list,number)

    print(f"The number: {number} was found at index(s): {index} using binary search")


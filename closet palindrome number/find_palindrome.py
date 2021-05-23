
def closest_palindrome(num):
    num = str(num)
    length_number = len(num)
    left_shift_index = length_number/2
    # print(str(num)[:left_shift_index])
    if (left_shift_index % 2) == 0:
        return int(num[:left_shift_index]+num[:left_shift_index][::-1])
    else:
        return int(num[:left_shift_index+1]+num[:left_shift_index][::-1])


if __name__ == '__main__':
    for number in [123, 1222]:
        print(closest_palindrome(number))

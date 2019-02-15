def five_digit_code():
    print('Insert a 5 digit code')
    times = 0
    while times < 5:
        num = input('')
        if int(num)-1 != times:
            print('incorrect code, try again')
            times = 0
        else:
            times += 1
    print('Correct code!')

five_digit_code()

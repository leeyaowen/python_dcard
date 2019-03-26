while True:
    inputn = input('輸入1<N<100, N=?\n')
    if inputn == '0':
        break
    ans = 0
    numlist = ''
    try:
        if 3 < int(inputn) < 100:
            for i in range(1, int(inputn), 1):
                if str(i)[-1:] == '3':
                    numlist = numlist + '(' + str(i) + '*' + str(i) + ')' + '+'
                    squarei = i*i
                    ans = ans + squarei
            print('output = ' + numlist[:-1] + ' = ' + str(ans))
        elif 1 < int(inputn) <= 3:
            print('output = 0')
        else:
            print('請輸入範圍內的數字!')
    except ValueError:
        print('請輸入範圍內的數字!')

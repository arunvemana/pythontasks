def wordPositionShit(inputs:list):
    for s in inputs:
        b = ''
        s = s[::-1]
        for i in range(len(s)):
            b = b + s[i]
            if s[i] == " " or i == len(s)-1:
                c = b[::-1]
                if len(s)-1 == i:
                    c = ' ' +c
                print(c,end="")
                b = ''
        print('\n')
wordPositionShit(inputs=["this is very simple ","life is boring all the time"])


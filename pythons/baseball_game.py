A,B,C = map(int, input("상대방의 예상 숫자 : ").split())
count = int(input("play 숫자 : "))
a,b,c = map(int, input("나의 예상 숫자 : ").split()) 

def strike_sign_fun() :
    if A==a and B==b and C==c :
        strike_sign="3S"
    elif A!=a and B!=b and C!=c :
        strike_sign="0S"
    elif A==a and B==b :
        strike_sign="2S"
    elif C==c and B==b :
        strike_sign="2S"
    elif C==c and A==a :
        strike_sign="2S"
    elif A==a or B==b or C==c :
        strike_sign="1S"
    return strike_sign

def ball_sign_fun() :
    if A==(b or c) and B==(a or c) and C==(a or b):
        ball_sign="3B"
    elif A!=(b or c) and B!=(a or c) and C!=(a or b) :
        ball_sign="0B"
    elif A==(b or c) and B==(a or c) :
        ball_sign="2B"
    elif C==(a or b) and B==(a or c) :
        ball_sign="2B"
    elif C==(a or b) and A==(b or c) :
        ball_sign="2B"
    elif A==(b or c) or B==(a or c) or C==(a or b) :
        ball_sign="1S"
    return ball_sign


for x in range(count-1) :

    strike_sign=strike_sign_fun()
    ball_sign = ball_sign_fun()
    sign = print("{}{}".format(strike_sign, ball_sign))

    if sign == "0S0B" :
        print("out")
        break
    elif sign == "3S0B" :
        break
    else :
        A,B,C = map(int, input("상대방의 예상 숫자 : ").split())
        a,b,c = map(int, input("나의 예상 숫자 : ").split())
        sign = print("{}{}".format(strike_sign, ball_sign))



    


def strike_sign_fun(A,B,C,a,b,c) :
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

def ball_sign_fun(A,B,C,a,b,c) :
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

def score_cal(a,b,c) :
    strike_sign=strike_sign_fun(A,B,C,a,b,c)
    ball_sign = ball_sign_fun(A,B,C,a,b,c)
    sign = "{} {}".format(strike_sign, ball_sign)
    print("score : {}".format(sign))
    return sign

def intro() :
    try :
        A,B,C = map(int, input("상대방의 예상 숫자 : ").split())
    except :
        A,B,C = map(int, input("상대방의 예상 숫자 : ").split())
    try : 
        count = int(input("play 숫자 : "))
    except :
        count = int(input("play 숫자 : "))
    while count > 9 :
        count = int(input("play 숫자 : "))
    return A,B,C,count

def intro_sec():
    try :
        a,b,c = map(int, input("나의 예상 숫자 : ").split())
    except :
        a,b,c = map(int, input("나의 예상 숫자 : ").split())
    while a==b==c or (a>9 or b>9 or c>9) or (a==b or a==c or b==c) :
        try :
            a,b,c = map(int, input("나의 예상 숫자 : ").split())
        except :
            a,b,c = map(int, input("나의 예상 숫자 : ").split())
    return a,b,c

def game_start(count) :
    for x in range(count) :
        a,b,c = intro_sec()
        strike_sign_fun(A,B,C,a,b,c)
        ball_sign_fun(A,B,C,a,b,c)
        sign=score_cal(a,b,c)
        if sign == "0S 0B" :
            print("아웃")
        elif sign == "3S 0B" :
            print("Win!")


A,B,C,count=intro()
game_start(count)





    


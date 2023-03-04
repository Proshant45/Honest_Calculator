msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

def is_integer(v):
    try:
        float(v)
    except ValueError:
        return False
    else:
        return float(v).is_integer()


def is_one_digit(v):

    try:
        if -10 < v < 10 and is_integer(v):
            return True

    except TypeError:
        return False


memory = 0.0

while True:
    calc = input(msg_0, )
    calc = calc.split()
    x = calc[0]
    oper = calc[1]
    y = calc[2]
    msg = ""

    try:
        if x == "M" and y =="M":
            m=memory
            t= memory

        elif x == "M":
            m = memory
            t = float(y)
        elif y == "M":
            t = memory
            m=float(x)
        else:
            m = float(x)
            t = float(y)
    except ValueError:
          print(msg_1)
          continue

    if (is_one_digit(m) and is_one_digit(t)) == True:
        msg = msg + msg_6

        if ((m == 1 or t == 1) and oper =="*" ) == True  :
            msg = msg + msg_7

        if ((m == 0 or t==0) and (oper == "+" or oper=="-" or oper=="*" ))==True:
                    msg = msg + msg_8
    elif ((m == 1 or t == 1) and oper =="*" ) == True:
        msg = msg + msg_7
        if ((m == 0 or t == 0) and (oper == "+" or oper == "-" or oper == "*")) == True:
            msg = msg + msg_8
    elif ((m == 0 or t == 0) and (oper == "+" or oper == "-" or oper == "*")) == True:
        msg = msg + msg_8

    if msg != "":
         print(msg_9 + msg)




    if oper == "+" or oper == "-" or oper == "*" or oper == "/":
        if oper == "+":

            result = m + t
            print(result)
            answer = input(msg_4,)

            if answer == "y":
                if is_one_digit(result) == True :
                    ms = input(msg_10,)
                    if ms == "y":
                        ms1 = input(msg_11,)
                        if ms1 == "y":
                            ms2 = input(msg_12,)
                            if ms2 == "y":
                                memory= result

                else:
                     memory = result


                ac = input(msg_5,)
                if ac == "y":
                    continue
                elif ac == "n":
                    break
            elif answer == "n" :
                ac = input(msg_5)
                if ac == "y":
                    continue
                elif ac == "n":
                    break

        elif oper == "-":
            result = m-t
            print(result)
            answer=input(msg_4,)
            if answer == "y":
                if is_one_digit(result) == True:
                    ms = input(msg_10, )
                    if ms == "y":
                        ms1 = input(msg_11, )
                        if ms1 == "y":
                            ms2 = input(msg_12, )
                            if ms2 == "y":
                                memory = result
                else:
                    memory=result

                ac = input(msg_5,)
                if ac == "y":
                    continue
                elif ac == "n":
                    break
            elif answer == "n" :
                ac = input(msg_5)
                if ac == "y":
                    continue
                elif ac == "n":
                    break
        elif oper == "*":
            result= m * t
            print(result)
            answer=input(msg_4,)
            if answer == "y":
                if is_one_digit(result) == True :
                    ms = input(msg_10,)
                    if ms == "y":
                        ms1 = input(msg_11,)
                        if ms1 == "y":
                            ms2 = input(msg_12,)
                            if ms2 == "y":
                                memory= result
                else:
                    memory = result

                ac = input(msg_5,)
                if ac == "y":
                    continue
                elif ac == "n":
                    break
            elif answer == "n" :
                ac = input(msg_5)
                if ac == "y":
                    continue
                elif ac == "n":
                    break
        elif oper == "/" and t != 0.0:
            result = m/t
            print(result)
            answer=input(msg_4,)
            if answer == "y":
                if is_one_digit(result) == True:
                    ms = input(msg_10, )
                    if ms == "y":
                        ms1 = input(msg_11, )
                        if ms1 == "y":
                            ms2 = input(msg_12, )
                            if ms2 == "y":
                                memory = result
                else:
                    memory = result

                ac = input(msg_5,)
                if ac == "y":
                    continue
                elif ac == "n":
                    break
            elif answer == "n" :
                ac = input(msg_5)
                if ac == "y":
                    continue
                elif ac == "n":
                    break
        else:
            print(msg_3)
            continue

        break
    else:
        print(msg_2)
        continue






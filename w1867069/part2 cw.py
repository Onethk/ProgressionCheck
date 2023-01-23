pass_credits = 0
defer_credits = 0
fail_credits = 0
total = 0
another_set = 'y'
progress = 0
trailer = 0
retriever = 0
excluded = 0
flag_credit = False
flag_defer = False
flag_fail = False

while another_set == 'y':
    while flag_credit == False:
        try:
            pass_credits = int(input("Please enter your credits at pass :  "))
            flag_credit = True
            if pass_credits not in range(0,121,20):
                print('Out of range')
                flag_credit = False
        except ValueError:
            print('Integer Required')
            flag_credit = False

    while flag_defer == False:
        try:
            defer_credits = int(input("Please enter your credits at defer :  "))
            flag_defer = True
            if pass_credits not in range(0, 121, 20):
                print('Out of range')
                flag_defer = False
        except ValueError:
            print('Integer Required')
            flag_defer = False

    while flag_fail == False:
        try:
            fail_credits = int(input("Please enter your credits at fail : "))
            flag_fail = True
            if pass_credits not in range(0, 121, 20):
                print('Out of range')
                flag_fail = False
        except ValueError:
            print('Integer Required')
            flag_fail = False
            
    total = pass_credits + defer_credits + fail_credits

    if total != 120:
        print('Total incorrect')
    else:
        if pass_credits == 120:
            print("Progress")
            progress = progress + 1


        elif pass_credits == 100:
            print("Progress (module trailer)")
            trailer = trailer + 1


        elif pass_credits == 80:
            print("Do not Progress – module retriever")
            retriever = retriever + 1


        elif pass_credits == 60:
            print("Do not Progress – module retriever")
            retriever = retriever + 1

        elif pass_credits == 40:
            if fail_credits == 80:
                print("Exclude")
                excluded = excluded + 1
            else:
                print("Do not Progress – module retriever")
                retriever = retriever + 1

        elif pass_credits == 20:
            if defer_credits >= 40:
                print("Do not Progress – module retriever")
                retriever = retriever + 1
            else:
                print("Exclude")
                excluded = excluded + 1

        else:
            if pass_credits == 0:
                if defer_credits >= 60:
                    print("Do not Progress – module retriever")
                    retriever = retriever + 1
                else:
                    print("Exclude")
                    excluded = excluded + 1
                    
    flag_credit = False
    flag_defer = False
    flag_fail = False
    
    print()
    
    print("Would you like to enter another set of data?")
    another_set = input("Enter 'y' for yes or 'q' to quit and view results : ")

    print()

#line = " "*3

print("Progress ","Trailing ","Retriever ","Excluded")

while (progress!=0) or (trailer!=0) or (retriever!=0) or (excluded!=0):
    if(progress!=0):
        line = "*" + " "*10
        progress = progress - 1
    else:
        line = " " + " "*10

    if (trailer!=0):
        line = line+"*"+ " "*10
        trailer = trailer - 1
    else:
        line = line+" " + " "*10
    if(retriever!=0):
        line = line+"*"+ " "*10
        retriever = retriever - 1
    else:
        line = line+" " + " "*10
    if(excluded!=0):
        line=line+"*"+ " "*10
        excluded = excluded - 1
    else:
        line = line+" " + " "*10
    print(line)


    

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

progress_list = []
module_trailer_list = []
module_retriever_list = []
exclude_list = []


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

    if pass_credits == 120:
        print("Progress")
        progress = progress + 1
        progress_list.append(pass_credits)
        progress_list.append(defer_credits)
        progress_list.append(fail_credits)


    elif pass_credits == 100:
        print("Progress (module trailer)")
        trailer = trailer + 1
        progress = progress + 1
        module_trailer_list.append(pass_credits)
        module_trailer_list.append(defer_credits)
        module_trailer_list.append(fail_credits)

    elif pass_credits == 80:
        print("Module retriever")
        retriever = retriever + 1
        module_retriever_list.append(pass_credits)
        module_retriever_list.append(defer_credits)
        module_retriever_list.append(fail_credits)

    elif pass_credits == 60:
        print("Module retriever")
        retriever = retriever + 1
        module_retriever_list.append(pass_credits)
        module_retriever_list.append(defer_credits)
        module_retriever_list.append(fail_credits)

    elif pass_credits == 40:
        if fail_credits == 80:
            print("Exclude")
            excluded = excluded + 1
            exclude_list.append(pass_credits)
            exclude_list.append(defer_credits)
            exclude_list.append(fail_credits)
        else:
            print("Module retriever")
            retriever = retriever + 1
            module_retriever_list.append(pass_credits)
            module_retriever_list.append(defer_credits)
            module_retriever_list.append(fail_credits)

    elif pass_credits == 20:
        if defer_credits >= 40:
            print("Module retriever")
            retriever = retriever + 1
            module_retriever_list.append(pass_credits)
            module_retriever_list.append(defer_credits)
            module_retriever_list.append(fail_credits)
        else:
            print("Exclude")
            excluded = excluded + 1
            exclude_list.append(pass_credits)
            exclude_list.append(defer_credits)
            exclude_list.append(fail_credits)


    else:
        if pass_credits == 0:
            if defer_credits >= 60:
                print("Module retriever")
                retriever = retriever + 1
                module_retriever_list.append(pass_credits)
                module_retriever_list.append(defer_credits)
                module_retriever_list.append(fail_credits)
            else:
                print("Exclude")
                excluded = excluded + 1
                exclude_list.append(pass_credits)
                exclude_list.append(defer_credits)
                exclude_list.append(fail_credits)


    flag_credit = False
    flag_defer = False
    flag_fail = False
    
    print()
    
    print("Would you like to enter another set of data?")
    another_set = input("Enter 'y' for yes or 'q' to quit and view results : ")

    print()


# Display Progress

p_length = int(len(progress_list) / 3)

a = 0

for i in range(p_length):
    print("Progress - ",progress_list[a],",",progress_list[a+1],",",progress_list[a+2])
    a = a + 3

# Display module trailer

mt_length = int(len(module_trailer_list) / 3)

b = 0

for i in range(mt_length):
    print("Progress (module trailer) - ",module_trailer_list[b],",",module_trailer_list[b+1],",",module_trailer_list[b+2])
    b = b + 3

# Display module retriever

mr_length = int(len(module_retriever_list) / 3)

c = 0

for i in range(mr_length):
    print("Module retriever - ",module_retriever_list[c],",",module_retriever_list[c+1],",",module_retriever_list[c+2])
    c = c + 3

# Display Exclude

e_length = int(len(exclude_list) / 3)

d = 0

for i in range(e_length):
    print("Exclude - ",exclude_list[d],",",exclude_list[d+1],",",exclude_list[d+2])
    d = d + 3
    

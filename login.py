print("1.Login\n2.Register")
choice = int(input())


def validateEmail(mailid):
    valid = True
    index_of_at = -1
    index_of_dot = -1
    index_of_at = mailid.index('@')
    index_of_dot = mailid.index('.')
    splChar = ['!', '@', '#', '$', '%', '^', '*', '(', ')', '-', '+', '=', '_']
    if mailid[0] in splChar or mailid[0].isdigit():
        print("first char")
        valid = False
    if (index_of_dot < index_of_at) or abs(index_of_dot - index_of_at) == 1:

        valid = False

    return valid



def validatePass(p):
    valid = True
    if len(p) < 5 or len(p) > 16:
        valid = False

    no_digit = 0
    no_upper = 0
    no_lower = 0
    for ele in p:
        if ele.isdigit():
            no_digit += 1
        elif ele.isupper():
            no_upper += 1
        elif ele.islower():
            no_lower += 1

    if no_digit < 1 or no_upper < 1 or no_lower < 1:
        print('Pass fail')
        valid = False
    return valid


if choice == 2:
    mail = input("Enter the email ID: ")
    password = input('Enter the password: ')
    is_mail_valid = validateEmail(mail)
    is_pass_valid = validatePass(password)
    print(is_pass_valid)
    print(is_mail_valid)
    if is_pass_valid and is_mail_valid:
        print('hello')
        with open('./users_list.txt', 'a') as f:
            print(mail, file=f)
            print(password, file=f)
            print('Data successfully written to the file.')
elif choice == 1:
    user_dict = {}
    with open('./users_list.txt', 'r') as f:
        i = 0
        mail = ""
        passw = ""
        for line in f:
            if i % 2 == 0:
                mail = line[:len(line)-1]
            else:
                passw = line[:len(line)-1]
            i += 1
            user_dict[mail] = passw

    user_mail = input("Enter your mail ID: ")
    user_pass = input("Enter your password: ")
    for key in user_dict:
        if key == user_mail and user_dict[key] == user_pass:
            print('Login Successful.')
        else:
            print('Login Unsuccessful.')

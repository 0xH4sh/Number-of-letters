my_Dict = {}    # dictionary for saving the number of letters
while True:
    user_text = input('please enter a text or sentence (To exit, press "exit"): ')  # user text or sentence

    if user_text.lower() == 'exit':
        print('See You Later <3')
        break


    # for char in user_text:
    #     if char in my_Dict:
    #         my_Dict[char] += 1
    #     elif char not in my_Dict:
    #         my_Dict[char] = 1
    #     else:
    #         print('Umm')


    j = 0
    while j < len(user_text):
        char = user_text[j]     # "j" assigned to "char"
        if char in my_Dict:
            my_Dict[char] += 1  # Add if available
        else:
            my_Dict[char] = 1   # Add if not present
        j += 1


if not my_Dict:     # check for non-empty
    print('Nothing Added!')
else:
    print(my_Dict)



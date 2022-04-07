import os
from traceback import print_tb
os.system('cls')

my_str = 'lkjsdfkljsfl;ksdf;ls;lsdkjsdfhellosdfsdd'
char_1_H = []
char_2_E = []
char_3_L = []
char_4_L = []
char_5_O = []
found_hello = 0
while my_str != '':
    if char_1_H == ['h']:
        if char_2_E == ['e']:
            if char_3_L == ['l']:
                if char_4_L == ['l']:
                    if char_5_O == ['o']:
                        char_1_H = []
                        char_2_E = []
                        char_3_L = []
                        char_4_L = []
                        char_5_O = []
                    elif my_str[0] == 'o':
                        char_5_O.append('o')
                        found_hello += 1
                    else:
                        my_str = my_str[1:]
                        char_1_H = []
                        char_2_E = []
                        char_3_L = []
                        char_4_L = []
                        char_5_O = []
                elif my_str[0] =='l':
                    char_4_L.append('l')
                    my_str = my_str[1:]
                else:
                    my_str = my_str[1:]
                    char_1_H = []
                    char_2_E = []
                    char_3_L = []
                    char_4_L = []
            elif my_str[0] == 'l':
                char_3_L.append('l')
                my_str = my_str[1:]
            else:
                my_str = my_str[1:]
                char_1_H = []
                char_2_E = []
                char_3_L = []
        elif my_str[0] == 'e':
            char_2_E.append('e')
            my_str = my_str[1:]
        else:
            my_str = my_str[1:]
            char_1_H = []
            char_2_E = []
    elif my_str[0] == 'h':
        char_1_H.append('h')
        my_str = my_str[1:]
    else:
        my_str = my_str[1:]
        char_1_H = []

if found_hello >= 1:
    print(f"I found {found_hello} number hello")
else:
    print("i do not found any hello")

# my_str = 'sdiffgdfgsgsgsidhsghsfsidfgedhgrhgsi'

# lst_s = []
# lst_i = []

# found_the_si = 0

# while my_str != '':
#     if lst_s == ['s']:
#         if my_str[0] == 'i':
#             my_str = my_str[1:]
#             found_the_si += 1
#         else:
#             my_str = my_str[1:]
#             lst_s = []
#     elif my_str[0] == 's':
#             lst_s.append('s')
#             my_str = my_str[1:]
#     else:
#         my_str = my_str[1:]

# if found_the_si >= 1:
#     print(f"I found {found_the_si} number si")
# else:
#     print("i do not found any si")

        

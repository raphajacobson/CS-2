import random

user_name = input("What is your name?")

def reverse_and_display(user_name):
    '''
    Takes in name and then prints it backwards
    Args:
        user_name (string): any given word
    Returns:
        print: The name backwards
    '''
    return(user_name[::-1])

def count_vowels(user_name):
    '''
    Takes in a name and then prints the number of vowels in it
    Args:
        user_name (string): any given word
    Returns:
        print: The number of vowels in the name
    '''
    vowel_list = ["a", "e", "i", "o", "u"]
    count = 0

    for letter in user_name:
        if letter in vowel_list:
            count += 1
    return(count)

def consonant_frequency(user_name):
    '''
    takes in a name and then prints the number of consonants in it
    Args:
        user_name (string): any given word
    Returns:
        print: number of consonants in name
        '''
    consonant_list = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    consonant_count = 0

    for letter in user_name:
        if letter in consonant_list:
            consonant_count+= 1
    return(consonant_count)

def first_name(user_name):
    '''
    gives user only first name
    Args:
        user_name (string): any given word
    Returns:
        First name of user
    '''
    space = 0
    for i in range(len(user_name)):
        if user_name[i] == " ":
            break
        else: 
            space = space +1
    first = user_name[: space]
    return first
                   

def middle_name(user_name):
    '''
    prints user's middle name(s)
    Args:
        user_name (string): any given word
    Returns:
        the user's middle name(s)
    '''
    lastspace = len(user_name)-1
    for i in range(len(user_name)-1, -1, -1):
        if user_name[i] == " ":
            break
        else: 
            lastspace = lastspace -1

    firstspace = 0
    for i in range(0,len(user_name)):
        
        if user_name[i] == " ":
            firstspace = firstspace+1
            break
        else: 
            firstspace = firstspace +1

    middle = user_name[firstspace:lastspace]
    return middle

def last_name(user_name):
    '''
    prints user's last name
    Args:
        user_name (string): any given word
    Returns:
        the user's last name
    '''
  
    finalspace = len(user_name)-1
    for i in range(len(user_name)-1, -1, -1):
        if user_name[i] == " ":
            finalspace = finalspace +1
            break
        else: 
            finalspace = finalspace -1
    return user_name[finalspace :]

def hyphen(user_name):
    '''
    Defines if there is a hyphen in the name or not
    Args:
        user_name (string): any given word
    Returns:
        A boolean value whether or not a hyphen is detected
    '''
    if "-" in user_name:
        return True
    else:
        return False 


def convert_upper(user_name):
    output = ""
    for char in user_name:
        num = ord(char)
    if 97 < num < 122:
        converted_num = ord(char) - 32
        for i in range(user_name):
            output += converted_num
            print(output)
    #elif 65 < num < 90:
        

        

def scramble_name(user_name):
    '''
    Scrambles letters in user's name
    Args:
        user_name (string): any given word
    Returns:
        the user's name randomly scrambled
    '''
    char_list = list(user_name)
    random.shuffle(char_list)
    new_word = ""
    for char in char_list:
        new_word += char
    return new_word

def palindrome(user_name):
    '''
    Confirms if a name is a palindrome or not
    Args:
        user_name (string): any given word
    Returns:
        A boolean value
    '''
    if user_name == user_name[: : -1]:
        return True
    else:
        return False

def main():
    while True:
        choice = input("what would you like to do with your name? (insert number) 1. print name backwards 2. count vowels 3. count consonants 4. return first name 5. return last name 6. return middle name(s) 7. identify if there is a hyphen in your name 8. make name lowercase 9. make name uppercase 10. scramble letters in name 11. identify if name is a palindrome: ")
        if choice == "1":
            print(reverse_and_display(user_name))
        elif choice == "2":
            print(count_vowels(user_name))
        elif choice == "3":
            print(consonant_frequency(user_name))
        elif choice == "4":
            print(first_name(user_name))
        elif choice == "5":
            print(last_name(user_name))
        elif choice == "6":
            print(middle_name(user_name))
        elif choice == "7":
            print(hyphen(user_name))
        #elif choice == "8":
            #print(convert_lower(user_name))
        elif choice == "9":
            print(convert_upper(user_name))
        elif choice == "10":
            print(scramble_name(user_name))
        elif choice == "11":
            print(palindrome(user_name))
        else:
            print("invalid response... try again")


main()

'''


elif choice == "9":
    convert to upper
'''

        


        




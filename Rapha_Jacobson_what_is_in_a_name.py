#Name: Rapha Jacobson
#Description: Asks user for their name and gives them a list of multiple ways they can manipulate their name
#Bonuses: Return boolean if name contains a title/distinction, remove_title function, Build a menu, Return name as sorted array of characters
#Bugs: Code does not work for special characters, code does not account for some titles which I did not define in the "titles" list
#1.0 LRJ
import random                                                                                                   #import random library


def split_name(user_name):
    parts = []                                                                                                  #define variable "parts" as an empty list
    current = ""                                                                                                #define variable "current" as an empty string
    for char in user_name:                                                                                      #for every character in the user's name
        if char == " ":                                                                                         #if a character in the user's name is a space
            if len(current) > 0:                                                                                #if the length of the current string is greater than 0
                parts.append(current)                                                                           #add everyting in the "current" string to the "parts" list
                current = ""                                                                                    #empty the current string
        else:                                                                                                   #otherwise (if the character is not a space)
            current += char                                                                                     #add the character to the current string
    if len(current) > 0:                                                                                        #if the length of the "current" string is greater than 0                                                                                         
        parts.append(current)                                                                                   #add everyting in the "current" string to the "parts" list

    return parts                                                                                                #return "parts" list to the function


def reverse_and_display(user_name):                                                                             #define reverse and display function with user_name as an argument
    '''
    Takes in name and then prints it backwards                                                                  
    Args:
        user_name (string): any given word
    Returns:
        print: The name backwards
    '''
    return(user_name[::-1])                                                                                     #return to the function the user's name backwards

def count_vowels(user_name):                                                                                    #define count vowels function with user_name as an argument
    '''
    Takes in a name and then prints the number of vowels in it
    Args:
        user_name (string): any given word
    Returns:
        print: The number of vowels in the name
    '''
    vowel_list = ["a", "e", "i", "o", "u"]                                                                      #create a list of vowels
    count = 0                                                                                                   #set vowel count to 0

    for letter in convert_lower(user_name):                                                                                    #for loop
        if letter in vowel_list:                                                                                #if a letter in the user's name matches a letter in the vowel list
            count += 1                                                                                          #add one to the vowel count
    return(count)                                                                                               #return the vowel count

def consonant_frequency(user_name):                                                                             #create consonant frequency function with user_name as an argument
    '''
    takes in a name and then prints the number of consonants in it
    Args:
        user_name (string): any given word
    Returns:
        print: number of consonants in name
        '''
    consonant_list = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"] #list of all consonants
    consonant_count = 0                                                                                         #set consonant count to 0

    for letter in convert_lower(user_name):                                                                                    #for loop
        if letter in consonant_list:                                                                            #if a letter in the user's name matches a letter in the consonant count
            consonant_count+= 1                                                                                 #add one to the consonant count
    return(consonant_count)                                                                                     #retur the consonant count to the function

def first_name(user_name):                                                                                      #define first name function with user_name as an argument
    '''
    gives user only first name
    Args:
        user_name (string): any given word
    Returns:
        First name of user
    '''
    user_name = remove_title(user_name)                                                                         #redefine user_name as the user's name without a title (useing remove_title function)
    space = 0                                                                                                   #define the space (index of space) as 0
    for i in range(len(user_name)):                                                                             #for loop (for every character in the length of the user's name)
        if user_name[i] == " ":                                                                                 #if a character is  a space
            break                                                                                               #end for loop
        else:                                                                                                   #otherwise
            space = space +1                                                                                    #add one to the space (index of space) count
        first = middle_name
    first = user_name[: space]                                                                                  #define the variable "first" as the user name until the first space (aka the user's first name)
    return first                                                                                                #return the user's first name to the function
                

def middle_name(user_name):                                                                                     #define the middle name(s) function with user_name as an argument
    '''
    prints user's middle name(s)
    Args:
        user_name (string): any given word
    Returns:
        the user's middle name(s)
    '''
    user_name = remove_title(user_name)                                                                         #redefine user_name as the user's name without a title (useing remove_title function)
    space = 0
    for char in user_name:
        if char == " ":
            space += 1
    if space < 2:
        middle = ("no middle name")
    else:
        lastspace = len(user_name)-1                                                                            #define variable "lastspace" as the length of the user's name
        for i in range(len(user_name)-1, -1, -1):                                                               #for loop (for every character in the length of the user's name going from the last character to first)
                if user_name[i] == " ":                                                                         #if a character is a space
                    break                                                                                       #end for loop
                else:                                                                                           #otherwise
                    lastspace = lastspace -1                                                                    #subtract one from the index of the lastspace
        firstspace = 0                                                                                          #set firstspace counter (index of the first space in the user's name) to 0
        for i in range(0,len(user_name)):                                                                       #for loop (for every character in the length of the user's name)    
            if user_name[i] == " ":                                                                             #if a character is a space
                firstspace = firstspace+1                                                                       #add one to the index of the first space 
                break                                                                                           #end for loop
            else:                                                                                               #otherwise
                firstspace = firstspace +1                                                                      #add one to the firstspace counter

        middle = user_name[firstspace:lastspace]                                                                #define variable "middle" as the characters between the first and last space (the user's middle name(s))
    return middle                                                                                               #return the user's middle name to the function

def last_name(user_name):                                                                                       #define the last_name function with user_name as an argument
    '''
    prints user's last name
    Args:
        user_name (string): any given word
    Returns:
        the user's last name
    '''
    space = 0
    for char in user_name:
        if char == " ":
            space += 1
    if space < 1:
        last = "no last name"
    else:
        user_name = remove_title(user_name)                                                                         #redefine user_name as the user's name without a title (useing remove_title function)
        finalspace = len(user_name)-1                                                                               #define the variable "finalspace" as the length of the user's name starting from the last character and ending at the first character
        for i in range(len(user_name)-1, -1, -1):                                                                   #for loop (for every character in the length of the user's name going backwards)
            if user_name[i] == " ":                                                                                 #if a character in the user's name is a space
                finalspace = finalspace +1                                                                          #add one to the finalspace counter
                break                                                                                               #end for loop
            else:                                                                                                   #otherwise
                finalspace = finalspace -1                                                                          #subtract one from the finalspace counter
            last = user_name[finalspace :] 
    return last                                                                                              #return the user's name from the last space to the end of their name (aka their last name)

def hyphen(user_name):                                                                                          #define the hyphen function with user_name as an argument
    '''
    Defines if there is a hyphen in the name or not
    Args:
        user_name (string): any given word
    Returns:
        A boolean value whether or not a hyphen is detected
    '''
    if "-" in user_name:                                                                                        #if there is a hyphen in the user's name                                                                                                                                                                                    
        return True                                                                                             #return a true boolean value
    else:                                                                                                       #otherwise
        return False                                                                                            #return a false boolean value


def convert_upper(user_name):                                                                                   #define convert_upper function with user_name as an argument
    '''
    converts user's entire name to uppercase
    Args:
        user_name (string): any given word
    Returns:
        the user's name in uppercase
    '''                                                                                  
    output = ""                                                                                                 #define the variable "output" as an empty string
    for char in user_name:                                                                                      #for loop (for every character in the user's name)
        num = ord(char)                                                                                         #create variable "num" defined as the ordinal variable for every character in the user's name
        if num >= 97 and num <= 122:                                                                            #if the ordinal value is greater than 97 and less than 122 (if the number is lowercase)
            converted_num = ord(char) - 32                                                                      #create variable "converted_num" and define it as the ordinal value of the character - 32 (newly defines the number as its uppercase counterpart)
            output = output + chr(converted_num)                                                                #convert the character's new ordinal value back into its character and add it to "output"
        else:                                                                                                   #otherwise (if the character is uppercase already)
            output = output + char                                                                              #add the character straight to the output
    return output                                                                                               #return the output (the user's name in all uppercase)

 
def convert_lower(user_name):                                                                                   #define convert_lower as a function with user_name as an argument
    '''
    converts user's entire name to lowercase
    Args:
        user_name (string): any given word
    Returns:
        the user's name in all lowercase
    '''                                                                                  
    output = ""                                                                                                 #define the variable "output" as an empty string
    for char in user_name:                                                                                      #for loop (for every character in the user's name)
        num = ord(char)                                                                                         #create variable "num" defined as the ordinal variable for every character in the user's name                                                                                                                  
        if num >= 65 and num <= 90:                                                                             #if the ordinal value is greater than 65 and less than 90 (if the number is uppercase)
            converted_num = ord(char) + 32                                                                      #create variable "converted_num" and define it as the ordinal value of the character + 32 (newly defines the number as its lowercase counterpart)
            output = output + chr(converted_num)                                                                #convert the character's new ordinal value back into its character and add it to "output"
        else:                                                                                                   #otherwise (if the character is already lowercase)
            output = output + char                                                                              #add the character straight to the output
    return output                                                                                               #return the output (the user's name in all lowercase)

        

def scramble_name(user_name):                                                                                   #define the scramble_name function with user_name as an argument
    '''
    Scrambles letters in user's name
    Args:
        user_name (string): any given word
    Returns:
        the user's name randomly scrambled
    '''
    char_list = list(user_name)                                                                                 #create the "char_list" variable and define it as all of the characters in the user's name converted to a list
    random.shuffle(char_list)                                                                                   #randomly shuffle the character list
    new_word = ""                                                                                               #create the variable "new_word" and define it as an empty string
    for char in char_list:                                                                                      #for loop (for every character in the character list)
        new_word += char                                                                                        #add every character in the character list to the new word string
    return new_word                                                                                             #return the scrambled user's name (new_word)

def palindrome(user_name):                                                                                      #define the palindrome function with user_name as an argument
    '''
    Confirms if a name is a palindrome or not
    Args:
        user_name (string): any given word
    Returns:
        A boolean value
    '''
    user_name = remove_title(user_name)                                                                         #redefine user_name as the user's name without a title (useing remove_title function)
    if user_name == user_name[: : -1]:                                                                          #if the user name printed forwards is the same as the username printed backwards
        return True                                                                                             #return a true boolean value
    else:                                                                                                       #otherwise
        return False                                                                                            #return a false boolean value


def get_initials(user_name):
    '''
    Finds initials of user
    Args:
        first - variable defined in first_name function
        middle - variable defined in middle_name function
        last - variable defined in last_name function
    Returns:
        The user's initials
    '''
    parts = split_name(user_name)
    initials = []
    for item in parts:
        initials.append(item[0])
    return "".join(convert_upper(initials))
    

def remove_title(user_name):
    '''
    Removes title from name if there is one
    Args:
        user_name (string): any given word
    Returns:
        Name without title
    '''
    titles = ["Dr.", "dr.", "dr", "sir", "Sir ", "Jr.", "jr", "Ph.d", "phd", "ph.d", "esq", "mr.", "mr", "mrs", "mrs.", "ms.", "ms" "Esq ", "Mr. ", "Mrs. ", "Ms. "]                                         #define variable "titles" as a list with all possible titles
    
    parts = split_name(user_name)                                                                               #create variable "parts" as the user's name split into a list at every space                                                                                      #create variable "first_part" and define it as the first index of the "parts" list (the first word of the user's name)                  
    
    for title in titles:
        if title in parts:
            parts.remove(title)                                                                                #remove the title from the parts list
    user_name = " ".join(parts)
    return user_name                                                                                     #return the user's name without a title

def find_title(user_name):
    '''
    Identifys if there is a title in user's name
    Args:
        user_name (string): any given word
    Returns:
        Boolean value if there is a title or not
    '''
    titles = ["Dr. ", "dr.", "dr" "sir", "Sir ", "Jr.", "jr", "Ph.d", "phd", "ph.d", "esq", "mr.", "mr", "mrs", "mrs.", "ms.", "ms" "Esq ", "Mr. ", "Mrs. ", "Ms. "]                                             #define variable "titles" as a list with all possible titles

    firstspace = 0                                                                                                  #create variable "firstspace" and set it to 0
    for i in range(0,len(user_name)):                                                                               #for loop (for every character in the length of the user's name)    
            if user_name[i] == " ":                                                                                 #if a character is a space
                firstspace = firstspace+1                                                                           #add one to the index of the first space 
                break                                                                                               #end for loop
            else:                                                                                                   #otherwise
                firstspace = firstspace+1                                                                           #add one to firstspace count
    first_word = user_name[: firstspace]                                                                            #create "first_word" variable and define it as the user's name from the start to the first space
    if first_word in titles:                                                                                        #if the first word is in the list of titles
        return True                                                                                                 #return a true boolean value
    else:                                                                                                           #otherwise
        return False                                                                                                #return a false boolean value

def sort_name(user_name):                                                                                           #define sort_name function with user_name as an argument
    '''
    sorts name alphabetically in all lowercase
    Args:
        user_name (string): any given word
    Returns:
        name with all characters in alphabetical order
    '''
    new_list = []                                                                                                   #create variable "new_list" and define it as an empty list
    for i in user_name:                                                                                             #for every character in the user's name
        new_list.append(i)                                                                                          #add every character to new_list

    new_list = convert_lower(new_list)                                                                              #redefine new_list as all lowercase using the convert_lower function previously defined
    return ''.join(sorted(new_list))                                                                                #return the new_list sorted alphabetically and joined together as one word



def main():                                                                                                         #define main function (where every function is called and executed)
    user_name = input("What is your name?")                                                                         #ask user what their name is
    while True:
        choice = input("what would you like to do with your name? (insert number) \n 0. remove title from name \n 1. print name backwards \n 2. count vowels \n 3. count consonants \n 4. return first name \n 5. return last name \n 6. return middle name(s) \n 7. identify if there is a hyphen in your name \n 8. make name lowercase \n 9. make name uppercase \n 10. scramble letters in name \n 11. identify if name is a palindrome \n 12. Get initials of user's name \n 13. identify if the name includes a title \n 14. split name into list \n 15. sort name's characters alphabetically \n :")
        if choice == "0":
            user_name = remove_title(user_name)
            print(f"Your user_name from now on is: {user_name}")
        elif choice == "1":
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
        elif choice == "8":
            print(convert_lower(user_name))
        elif choice == "9":
            print(convert_upper(user_name))
        elif choice == "10":
            print(scramble_name(user_name))
        elif choice == "11":
            print(palindrome(user_name))
        elif choice == "12":
            print(get_initials(user_name))
        elif choice == "13":
            print(find_title(user_name))
        elif choice == "14":
            print(split_name(user_name))
        elif choice == "15":
            print(sort_name(user_name))
        else:
            print("invalid response... try again")


main()        


        




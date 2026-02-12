import string

def create(file):
    with open("shakespeare_word_frequency_outputs.csv", "w") as output:                                             #create file to write in
        counts = dict()                                                                                             #create a dictionary called counts
        for line in file:
            line = line.strip()                                                                                     #removes whitespaces from beginning and end of strings
            line = line.translate(line.maketrans('', '', string.punctuation))                                       #removes punctuation
            line = line.lower()                                                                                     #makes everything lowercase 
            words = line.split()                                                                                    #split each word by every space
            for word in words:                                                                                      #This for loop creates dictionary item for every new word and add one to the value if it already exists
                if word not in counts:                                                                              
                    counts[word] = 1
                else:
                    counts[word] += 1
        w = ["the", "of", "to", "and", "every", "caesars", "speak", "doth", "here", "stand", "hath", "first", "hear", "tis", "second", "should", "enter", "her", "done", "shall", "thou", "go", "a", "in", "is", "it", "you", "that", "he", "was", "for", "on", "are", "with", "as", "I", "his", "they", "be", "at", "one", "have", "this", "from", "or", "had", "by", "but", "some", "what", "there", "we", "can", "out", "other", "were", "all", "your", "when", "up", "use", "word", "how", "said", "an", "each", "she", "which", "do", "their", "time", "if", "will", "way", "about", "many", "then", "them", "would", "i", "you", "that", "a", "not", "he", "me", "my", "for", "this", "him", "will", "his", "with", "be", "have", "but", "so", "as", "do", "what", "all", "are", "by", "we", "no", "our", "come", "did", "o", "know", "then", "let", "was", "well", "they", "now", "us", "their", "them", "jere", "at", "am", "man", "thy", "thee", "from", "upon", "there", "which", "would", "gp", "or", "why", "than", "some", "yet", "these", "like", "say", "may", "see", "tell", "such", "must", "were", "more", "give", "up", "how", "an", "where", "most", "tpp", "who", "out", "any", "had", "make", "nor", "can", "about", "even"]
        good = counts.copy()                                                                                        #create a copt of the counts dictionary
        for k in good.keys():                                                                                       #this for loop deletes any of the words in list 2 from the dictionary in order to clean it                                                                                  
            if k in w:                          
                del counts[k]                                                                                       
        sorted_items = sorted(counts.items(), key=lambda item: item[1], reverse = True)                             #sorts the dictionary in descending order of frequency (most frequent first and least frequent last)
        sorted_dict = dict(sorted_items)
        wcount = 0
        for key, value in sorted_dict.items():                                                                      #for every key, value pair in the dorted dictionary                                
            k = str(key)    
            v = str(value)
            out = k + "," + v
            if wcount < 20:                                                                                         #this if, else statement writes to the file the 20 most frequent words used and then breaks once 20 are written
                output.write(out + "\n")
                wcount += 1
            else:
                break
            

def main():
    while True:
        output = input("Would you like to explore the word frequencies for Macbeth or Julius Caesar?\n" \
        "input 'm' for Macbeth and 'j' for Julius Caesar (If you would like to exit the program enter 'x'): ")
        
        #main function interperts user's input and uses either Macbeth or Julius Caesar text to explore the word frequency
        #if an invalid input is entered or an error opening the file occurs, an error will print
        #if the user enters "x", the program will end
        if output == "m" or output == "M":
            try:
                m_data = open('Macbeth.txt', 'r')
            except FileExistsError:
                print("File does not exist - try again")
                exit()
            create(m_data)
        elif output == "j" or output == "J":
            try:
                jc_data = open('Julius Caesar.txt', 'r')
            except FileExistsError:
                print("File does not exist - try again")
                exit()
            create(jc_data)
        elif output == "x" or output == "X":
            exit()
        else:
            print("Invalid response - Try again")

main()

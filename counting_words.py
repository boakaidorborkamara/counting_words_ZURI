def count_words(text):
    counter = 0
    last_letter = text[-1]

    for letter in text:
        if(letter == " " or letter == last_letter):
            counter+=1

    print("There are %d words in this sentence.\n" %counter)


# invoke function 
count_words("Write a python program that counts and returns the number of words in a given text.")


from termFinder import TermFinder

texts = [
    'art-and-heart.txt',
    'brothers-karamoz.txt',
    'japanese-fairy-tales.txt',
    'metamorphosis.txt',
    'thus-spake-zathustra.txt',
    ]

def main():

    while True:
        # to limit input errors, input is converted to lower case.
        # in the class, all text is converted to lower case as well.
        term = input("What word do you want to search for?  ").lower()
        tf = TermFinder(texts, term)
        tf.printTermFreq()
        # For user experience, only entering 'q' will quit the program:
        # in this way, even if a user forgets and inputs the next word,
        # The program will continue. This allows the user to just hit enter to continue.
        runAgain = input("Would you like to search for another term?\nq to quit or any key to continue:  ")
        if runAgain == 'q':
            print("Goodbye!")
            break
        else:
            continue
print('______________________________________________')
print('^!^!^!^!^!^!^!^!^!^!^!^^!^!^!^!^!^!^!^!^!^!^!^')
print('------------------TERM FINDER-----------------')
print('______________________________________________')
print('^!^!^!^!^!^!^!^!^!^!^!^^!^!^!^!^!^!^!^!^!^!^!^\n')
main()
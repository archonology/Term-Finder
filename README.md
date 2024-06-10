# TERM FINDER: A PYTHON PROGRAM

By Reed Meher | 2024

## TABLE of CONTENTS

- [Summary](#summary)
- [Program Structure](#program-structure)
- [Purpose of Program Files](#purpose-of-program-files)
- [How to Use the Program](#how-to-use-the-program)
- [Future Development and Improvement](#future-development-and-improvement)
- [About the Author](#about-the-author)

## SUMMARY

Term Finder is a python program that searches a given set of text documents for single word occurances. The program allows the user to input a word to search for in the documents and the program returns the frequency results in percentages, rounded to the nearest 5th decimal.

### Quick Facts:

- Only if the word is found somewhere in the document will results for that document be displayed.
- Results are returned sorted from highest frequency to lowest.
- Punction is removed from the texts before the search occurs(reduces search errors).
- Users may replace the text files in the text folder with their own .txt files.

## PROGRAM STRUCTURE

- `final_project` folder:
  - `text` folder:
    - `.txt` files
  - `README.md` file
  - `main.py` file
  - `termFinder.py` file:
    - `TermFinder` class

## PURPOSE of PROGRAM FILES

- Term Finder is run from `main.py` in the root folder.
- `main.py` imports the TermFinder class from the `termFinder.py` file.
- The TermFinder class takes in the user input gathered in the `main.py` function.
- The TermFinder class reads the .txt files from the `text` folder.

## HOW TO USE the PROGRAM

To use Term-Finder you will need to download both main.py and termFinder.py to a folder on your local device or in Python supported application like [pythonanywhere](https://www.pythonanywhere.com), as long as the environment you are loading them to has Python3 available. You can learn more about downloading Python and setting up a Python environment in the [Python source docs](https://python.org).

Once your environment is ready to go, you can run this program. Make sure both the files are in the same folder. Make sure that folder has a folder titled `texts` and the texts you have added to the folder are `.txt` files.

You can get free classic literate from [Project Gutenberg](https://www.gutenberg.org/). All you need to do is select the Plain Text UTF-8 version, open it, and save it to your text folder. I've included a sample of text files in the text folder that you are free to use.

Once you have your texts in the text folder, go back to the main folder and open the `main.py` file: you need to add the exact names of the text files to the texts array at the top of `main.py' if you are using your own text files and not the demo ones provided.

Now you are ready to run the `main.py` file! The Python console will guide you through adding terms and ask you if you would like to keep going or end the function after each submitted prompt.

## FUTURE DEVELOPMENT and IMPROVEMENT

- Program will return exact word counts in addition to frequency percentages.
- Program will generate tables, graphs, or scatter plots for multiple queries upon request.
- Program will allow user to search for the most frequent word used in any given .txt document.

## ABOUT the AUTHOR

Reed Meher is a web developer based in Minnesota. See his portfolio at [meherdevs.com](https://www.meherdevs.com), follow him on [LinkedIn](https://www.linkedin.com/in/reed-meher), or reach out with questions via [email](mailto:reed@meherdevs.com).

---

Made with ❤️ by Reed Meher | 2024

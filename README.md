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

1. Navigate to the `final_project` folder and then to the `main.py` file.
2. run `main.py`.
3. The python CLI will prompt you to enter a term, and the program will guide you from there to continue, or end the program.

## FUTURE DEVELOPMENT and IMPROVEMENT

- Program will return exact word counts in addition to frequncy percentages.
- Program will generate tables, graphs, or scatter plots for multiple queries upon request.
- Program will allow user to search for the most frequent word used in any given .txt document.

## ABOUT the AUTHOR

Reed Meher is a web developer based in Minnesota. See his portfolio at [meherdevs.com](https://www.meherdevs.com), follow him on [LinkedIn](https://www.linkedin.com/in/reed-meher), or reach out with questions via [email](mailto:reed@meherdevs.com).

---

Made with ❤️ by Reed Meher | 2024

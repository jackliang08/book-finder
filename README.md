This python program is intended to find a book based on a selection of **authors, titles, and/or genres.** <br/>

# Programs
It contains three smaller programs, a main file and two libraries:<br/>
- ## main:
  - This is where the site is built, and all of the setup for the site is structured.
  - The program uses Tkinter to build the website and all its functionalities.
  - It also utilizes Pandas for the data management through DataFrames.

- ## book_filter:
  - Used for handling genre counting and eliminating duplicates from the dataset.
  - It is suggested that this library is used before the separately and before the main's execution.
  - **Note that the genre types must be manually entered into the genres list, and the library counts the number of occurrence for each genre.**
  - filter_dupes specifically reads book_data.csv and modifies new_data.csv, the data processed into new_data is to be manually pasted back to book_data.

- ## book_finder:
  - Made to actually find the book based on user input.
  - Main purpose is to find common books that fulfill the requirements inputted.
 
# Functionalities on the site

* There are three different input boxes, a search button, and arrows to select the book.
* In each input box, the full name is not required to be entered for the program to work, and the field could be left blank.
* If the field is left blank, then the program will not consider that field as a requirement, and will only filter based on the other ones.
* The inputs are not case sensitve.
* The search button updates the recommended list.
* The left and right arrows allow the user to traverse the list of books which meet the requirements.

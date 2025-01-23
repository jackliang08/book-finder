# **SETUP**
import pandas as pd
import tkinter as tk
from book_filter import BookFilter
from book_finder import BookFinder
df = pd.read_csv("book_data.csv")

cleaner = BookFilter(df)  # Class for filtering and cleaning data / only for the beginning
finder = BookFinder(df)  # Class for displaying data / main class to use

#self.genres = {'signal_processing': 3, 'data_science': 17, 'mathematics': 5, 'economics': 10, 'history': 26, 'science': 37, 'psychology': 1, 'fiction': 141, 'computer_science': 11, 'nonfiction': 88, 'philosophy': 34, 'comic': 13, 'tech': 36}



recommend_indexes = []
current_index = 0

# **FUNCTIONS**



def set_outputs(dataFrame,index:int) -> None:
    title_var.set(dataFrame.iloc[index]["Title"])
    author_var.set(dataFrame.iloc[index]["Author"])
    genre_var.set(dataFrame.iloc[index]["Genre"])

def index_right():
    global current_index
    if current_index < len(recommend_indexes) - 1:
        current_index += 1
    else:
        current_index = 0
    set_outputs(df,recommend_indexes[current_index])
def index_left():
    global current_index
    if current_index > 0:
        current_index -= 1
    else:
        current_index = len(recommend_indexes) - 1
    set_outputs(df,recommend_indexes[current_index])

# Takes in user input for each section and processes them
# Modifies the recommend_indexes list with all indexes that the three sections have in common
def get_inputs() -> None:
    global recommend_indexes
    global current_index
    title_index = finder.get_title(titleInput.get("1.0","end-1c"))
    author_index = finder.get_author(authorInput.get("1.0", "end-1c"))
    genre_index = finder.get_genre(genre_value.get())

    recommend_indexes = finder.get_common_index(title_index,author_index,genre_index)

    # Updates the outputs
    current_index = 0
    set_outputs(df,recommend_indexes[current_index])



# **WINDOW**

window = tk.Tk()
window.title("Book Recommender")
window.geometry("700x400")

searchLabel = tk.Label(window,text="Search:",height=8,width=8)
titleLabel = tk.Label(window,text="Title:")
authorLabel = tk.Label(window,text="Author:")
genreLabel = tk.Label(window,text="Genre:")
pad1 = tk.Label(window,text="",width=4)
pad2 = tk.Label(window,text="",width=4)

titleInput = tk.Text(window,height=5,width=30)
authorInput = tk.Text(window,height=2,width=20)

genre_value = tk.StringVar(window)
genres_list = ['signal_processing', 'data_science', 'mathematics', 'economics', 'history', 'science', 'psychology', 'fiction', 'computer_science', 'nonfiction', 'philosophy', 'children']
#print([key for key in cleaner.genres.keys()])
genreDropdown = tk.OptionMenu(window,genre_value,*genres_list)
searchButton = tk.Button(window,text="Search",height=2,width=10,command=get_inputs)

title_var = tk.StringVar()
titleOutput = tk.Label(textvariable=title_var)
author_var = tk.StringVar()
authorOutput = tk.Label(textvariable=author_var)
genre_var = tk.StringVar()
genreOutput = tk.Label(textvariable=genre_var)

leftButton = tk.Button(window,text="<-",height=2,width=5,command=index_left)
rightButton = tk.Button(window,text="->",height=2,width=5,command=index_right)


searchLabel.grid(column=1,row=1)
titleLabel.place(x=100,y=100)
authorLabel.place(x=350,y=100)
genreLabel.place(x=475,y=100)

titleInput.grid(column=1,row=2)
pad1.grid(column=2,row=2)
authorInput.grid(column=3,row=2)
pad2.grid(column=4,row=2)
genreDropdown.grid(column=5,row=2)

searchButton.grid(column=3,row=3)

titleOutput.place(x=20,y=300)
authorOutput.place(x=350,y=300)
genreOutput.place(x=550,y=300)

leftButton.place(x=5,y=360)
rightButton.place(x=650,y=360)

window.mainloop()

# FOR SETTING UP DATA
class BookFilter:
    def __init__(self,data):
        self.data = data
        # Creates a count for genres
        self.genres = {'signal_processing': 3, 'data_science': 17, 'mathematics': 5, 'economics': 10, 'history': 26, 'science': 37, 'psychology': 1, 'fiction': 141, 'computer_science': 11, 'nonfiction': 88, 'philosophy': 34, 'nonfiction': 137, 'fiction': 703, 'children': 11}
    # Counts the amount of each genre
    # Alters self.genres
    def genre_counter(self) -> None:
        for genre in self.genres:
            self.genres[genre] = 0  # Resets all genres to 0

        for type in self.data["Genre"]:
            self.genres[type] += 1

    # Eliminates duplicates from the csv
    # Accesses book_data.csv
    # Alters new_data.csv
    def filter_dupes(self):  # Stores unique titles to new_data.csv
        new_df_index = []
        counter = 0
        for i in range(0,len(self.data.index)):  # Runs  index * (index+1)/2  times  O(n^2)
            prev = i-1
            while (prev >= 0):
                if self.data.iloc[prev]["Title"] == self.data.iloc[i]["Title"]:
                    new_df_index.append(i)
                    break
                prev -= 1
        # Opening up "new_data.csv" and replacing its contents
        self.data.drop(index=new_df_index,inplace=True)
        print(self.data)
        self.data.to_csv("new_data.csv",index=False)



class BookFinder:
    def __init__(self, book_data):
        self.data = book_data


    # SEARCH BAR FUNCTIONS

    # Get titles: finds information on title inputted by user
    def get_title(self,title: str):
        return self.data[self.data["Title"].str.slice(start=0,stop=len(title)).str.upper() == title.upper()].index
    def get_author(self,author: str):
        return self.data[self.data["Author"].str.slice(start=0,stop=len(author)).str.upper() == author.upper()].index
    def get_genre(self,genre:str):
        return self.data[self.data["Genre"] == genre].index


    def get_common_index(self,index1,index2,index3):
        common_indexes = []
        for i in index1:
            if i in list(index2) and i in list(index3):
                common_indexes.append(i)
        return common_indexes

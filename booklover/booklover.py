#!/usr/bin/env python
# coding: utf-8

# In[125]:

class BookLover:
    name = "name"
    email = "email"
    fav_genre = "genre"
    num_books = 0
    book_list = []
    bookName = "book name"
    rating = 0
    newBook = ()
    
    def __init__(self, name, email, fav_genre, num_books=0, book_list=[]):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = len(book_list)
        self.book_list = book_list
    
    def addBook(self, bookName, rating):
        self.bookName = bookName
        self.rating = rating
        self.newBook = (bookName, rating)
        if self.newBook in self.book_list:
            self.book_list
        else:
            self.book_list.append(self.newBook)
            
    def hasRead(self, bookName):
        self.bookName = bookName
        if len([item for item in self.book_list if item[0] == bookName]) != 0:
            return True
        else:
            return False
    
    def numBooksRead(self):
        return self.num_books
    
    def favBooks(self):
        return [item for item in self.book_list if item[1] > 2]
    


# In[ ]:





# In[126]


# In[ ]:





# In[ ]:





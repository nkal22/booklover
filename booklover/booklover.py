#!/usr/bin/env python
# coding: utf-8

# In[125]:


import pandas as pd
import numpy as np

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





# In[126]:


import unittest



class BookLoverTestSuite(unittest.TestCase): 
    
    # create a book lover
    reader = BookLover('Nick','nickthebooklover@gmail.com','sports')
    
    def test_1_add_book(self):        
        self.reader.addBook('Great Gatsby',5)
        expected = ('Great Gatsby', 5)
        print(self.assertEqual(self.reader.book_list[0], expected))
    
    def test_2_add_book_twice(self):
        self.reader.addBook('Great Gatsby',5)
        self.reader.addBook('Great Gatsby',5)
        expected2 = 1
        print(self.assertEqual(len([item for item in self.reader.book_list if 
                                    item[0] == "Great Gatsby"]), expected2))
    
    def test_3_has_read(self):
        self.reader.hasRead('Great Gatsby')
        expected3 = True
        print(self.assertEqual(self.reader.hasRead('Great Gatsby'), expected3))
    
    def test_4_has_read_false(self):
        self.reader.hasRead('Pride and Prejudice')
        expected4 = False
        print(self.assertEqual(self.reader.hasRead('P&P'), expected4))
    
    def test_5_num_books(self):
        self.reader.addBook('Book One', 2)
        self.reader.addBook('Book Two', 4)
        expected5 = 3
        print(self.assertEqual(self.reader.num_books, 3))
    
    def test_6_num_fav_books(self):
        self.reader.favBooks()
        expected6 = 2
        print(self.assertEqual(len(self.reader.favBooks()), 2))
    
    if __name__ == '__main__':
        unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[ ]:





# In[ ]:





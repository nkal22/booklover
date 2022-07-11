#!/usr/bin/env python
# coding: utf-8

# In[6]:


import unittest
import unittest

from montecarlo import Die, Game, Analyzer

class DieTestSuite(unittest.TestCase):
    
    def test_1_change_weight(self):
        dice1 = Die(["1", 2, "3", 4, 5.0, 6])
        dice1.change_weight(2, 4)
        expected = 4
        self.assertEqual(dice1.facesFrame['weights'][1], expected)
    
    def test_2_dice_roll(self):
        dice2 = Die(["1", 2, "3", 4, 5.0, 6])
        roll = dice2.dice_roll(15)
        expected2 = 15
        self.assertEqual(len(roll), expected2)
        
    def test_3_current_frame(self):
        dice3 = Die(["1", 2, "3", 4, 5.0, 6])
        curr_frame = dice3.current_frame()
        expected3 = dice3.facesFrame
        self.assertEqual(len(curr_frame), len(expected3))
    
    def test_4_change_weight_false(self):
        dice4 = Die(["1", 2, "3", 4, 5.0, 6])
        invalid = dice4.change_weight(8,3)
        self.assertIsNone(invalid)



class GameTestSuite(unittest.TestCase):
    
    def test_5_roll(self):
        dice1 = Die([1,2,3,4,5,6])
        dice2 = Die([1,2,3,4,5,6])
        dice2.change_weight(4, 5)
        dice1.change_weight(2, 7)
        dieList = [dice1, dice2]
        newGame = Game(dieList)
        game1 = newGame.play(10)
        expected = 10
        self.assertEqual(len(game1), expected)
    
    def test_6_return_frame(self):
        dice1 = Die([1,2,3,4,5,6])
        dice2 = Die([1,2,3,4,5,6])
        dice2.change_weight(4, 5)
        dice1.change_weight(2, 7)
        dieList = [dice1, dice2]
        newGame = Game(dieList)
        newGame.play(10)
        new_frame = newGame.return_frame("N")
        expected2 = 1
        self.assertEqual(len(new_frame.columns), expected2)
    
    def test_7_return_wide_frame(self):
        dice1 = Die([1,2,3,4,5,6])
        dice2 = Die([1,2,3,4,5,6])
        dice2.change_weight(4, 5)
        dice1.change_weight(2, 7)
        dieList = [dice1, dice2]
        newGame = Game(dieList)
        newGame.play(10)
        new_frame = newGame.return_frame("W")
        expected3 = 2
        self.assertEqual(len(new_frame.columns), expected3)



class AnalyzerTestSuite(unittest.TestCase):
    
    def test_8_jackpot(self):
        dice1 = Die([1,2,3,4,5,6])
        dice2 = Die([1,2,3,4,5,6])
        dice2.change_weight(4, 5)
        dice1.change_weight(4, 7)
        dieList = [dice1, dice2]
        newGame = Game(dieList)
        newGame.play(10)
        newAnalyzer = Analyzer(newGame)
        jackpot = newAnalyzer.jackpot()
        expected = 0
        self.assertGreater(len(jackpot), expected)
    
    def test_9_combos(self):
        dice1 = Die([1,2,3,4,5,6])
        dice2 = Die([1,2,3,4,5,6])
        dice2.change_weight(4, 5)
        dice1.change_weight(4, 7)
        dieList = [dice1, dice2]
        newGame = Game(dieList)
        newGame.play(10)
        newAnalyzer = Analyzer(newGame)
        combos = newAnalyzer.combos()
        expected2 = 0
        self.assertGreater(len(combos), expected2)
    
    def test_ten_face_counts(self):
        dice1 = Die([1,2,3,4,5,6])
        dice2 = Die([1,2,3,4,5,6])
        dice2.change_weight(4, 5)
        dice1.change_weight(4, 7)
        dieList = [dice1, dice2]
        newGame = Game(dieList)
        newGame.play(10)
        newAnalyzer = Analyzer(newGame)
        face_counts = newAnalyzer.face_counts()
        expected3 = 0
        self.assertGreater(sum(face_counts.iloc[0]), expected3)
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[ ]:





# In[ ]:





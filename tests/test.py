import timeit
import unittest

from algorithms.a_satar import A_Star_Algo

class test_all(unittest.TestCase):

    def test_everything(self): 
        H_dist = {
            'A': 11,
            'B': 6,
            'C': 99,
            'D': 1,
            'E': 7,
            'G': 0,
        }
        
        graph = {#Describe your graph here, each neighbor and their distance
            'A': [('B', 2), ('E', 3)],
            'B': [('A', 2), ('C', 1), ('G', 9)],
            'C': [('B', 1)],
            'D': [('E', 6), ('G', 1)],
            'E': [('A', 3), ('D', 6)],
            'G': [('B', 9), ('D', 1)]
        }
        starttime = timeit.default_timer()
        print("The start time is :",starttime)
        A_Star_Algo('A', 'G')
        print("The end time is :",timeit.default_timer())
        print("The time difference is :", timeit.default_timer() - starttime)
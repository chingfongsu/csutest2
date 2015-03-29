'''
Created on Mar 29, 2015

@author: csu
'''
import unittest
import recommendations


class Test(unittest.TestCase):
    def test_sim_pearson(self):
        prefs = {}
        prefs['alice'] = []
        prefs['brian'] = []
        self.assertEqual(recommendations.sim_pearson(prefs, 'alice', 'brian'), 0, 'no common interest')
        prefs = {
        'alice': {'Lady in the Water': 2, 'Snakes on a Plane': 3, 'Just My Luck': 5},
        'brian': {'Lady in the Water': 3, 'The Night Listener': 3, 'Just My Luck': 1},
        }
        print recommendations.sim_pearson(prefs, 'alice', 'brian')
        self.assertAlmostEqual(recommendations.sim_pearson(prefs, 'alice', 'brian'), -0.9486, places=3, msg='Both like two movies but different rating')

    def test_sim_distance(self):
        prefs = {}
        prefs['alice'] = []
        prefs['brian'] = []
        self.assertEqual(recommendations.sim_distance(prefs, 'alice', 'brian'), 0, 'no common interest')
        prefs['alice'] = ['']
        prefs = {
        'alice': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5},
        'brian': {'Lady in the Water': 4.5, 'The Night Listener': 3.5},
        }
        self.assertAlmostEqual(recommendations.sim_distance(prefs, 'alice', 'brian'), 0.2, msg='Both like Lady in the Water')
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_add']
    unittest.main()
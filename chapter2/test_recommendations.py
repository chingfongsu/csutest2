'''
Created on Mar 29, 2015

@author: csu
'''
import unittest
import recommendations

critics={
 'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}
}

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
    
    def test_top_match(self):
        matches = recommendations.topMatches(critics, "Mick LaSalle", 3, recommendations.sim_distance)
        self.assertEqual(matches[0][1], 'Lisa Rose', "Lisa and Mick are close")
        self.assertAlmostEqual(matches[0][0], 0.3333, places=3, msg="Lisa and Mick are close")
    
    def test_getRecommendations(self):
        rec = recommendations.getRecommendations(critics, "Toby", recommendations.sim_distance)
        self.assertEqual(rec[0][1], 'The Night Listener', "The Night Listener")
    
    def test_transformPrefs(self):
        pref = {'abc':{'123': 1}, 'xyz':{'123':2, '456':3}}
        got = recommendations.transformPrefs(pref)
        expected = {'123':{'abc':1, 'xyz':2}, '456':{'xyz':1}}
        self.assertEqual(got, expected, "transformation is correct")
        print got
        
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_add']
    unittest.main()
import unittest
def isPalindrome(word):
    newWord = ""
    for i in range(len(word)):
        newWord += word[-i-1]
    
    if word == newWord:
        return True
    else:
        return False

class isPalindromeTests(unittest.TestCase):
    
    def testw1(self):
        self.assertEqual(isPalindrome("racecar"), True)

    def testw2(self):
        self.assertEqual(isPalindrome("rawqewqr"), False)
    
    def testw3(self):
        self.assertTrue(isPalindrome("qwqwqwq"))
    
    def testw4(self):
        self.assertFalse(isPalindrome("yuiopqwxzs"))
    
    def testw5(self):
        self.assertTrue(("abracarba"))

    # any task you want run before any method above is executed, put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main() # this runs our tests

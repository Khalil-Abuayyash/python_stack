import unittest

def coins(cents):
    quarters = int(cents/25)
    cents = cents % 25
    dimes = int(cents/10)
    cents = cents%10
    nickels = int(cents/5)
    pennies = cents % 5
    return [quarters, dimes, nickels, pennies]

class coinsTests(unittest.TestCase):
    
    def test1(self):
        self.assertEqual( coins(87), [3,1,0,2] )

    def test2(self):
        self.assertEqual( coins(100), [4,0,0,0] )
    
    def test3(self):
        self.assertEqual( coins(5), [0,0,1,0] )
    
    def test4(self):
        self.assertEqual( coins(70), [2,2,0,0] )
    
    def test5(self):
        self.assertEqual( coins(30), [1,0,1,0] )
    
    def test6(self):
        self.assertEqual( coins(47), [1,2,0,2] )

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

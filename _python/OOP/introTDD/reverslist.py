import unittest
def reverse(list):
    for i in range(int(len(list)/2)):
        temp = list[-i-1]
        list[-i-1] = list[i]
        list[i] = temp
    return list

class IsReversedTests(unittest.TestCase):
    
    def test_odd_arr(self):
        self.assertEqual(reverse([1,2,3,4,5]), [5,4,3,2,1])

    def test_even_arr(self):
        self.assertEqual(reverse([1,2,3,4,5,6]), [6,5,4,3,2,1])

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


import unittest

class MathDojo:

    def __init__(self):
    	self.result = 0

    def add(self, num, *nums):
    	# your code here
        self.result += num 
        if len(nums) > 0:
            for i in nums:
                self.result += i
        return self

    def subtract(self, num, *nums):
    	# your code here
        self.result -= num 
        if len(nums) > 0:
            for i in nums:
                self.result -= i
        return self


md = MathDojo()
class mathDojoTests(unittest.TestCase):
    
    def testAdd1(self):
        self.assertEqual( md.add(5).result, 5 )

    def testAdd2(self):
        self.assertEqual( md.add(5,2).result, 12 )
    
    def testAdd3(self):
        self.assertEqual( md.add(5,6,7).result, 30 )
    
    def testChain(self):
        self.assertEqual(md.subtract(5).add(10).add(10,20).subtract(10).result, 55)

    def testSubtract1(self):
        self.assertEqual( md.subtract(5).result, 50 )
    
    def testSubtract2(self):
        self.assertEqual( md.subtract(5,10,6).result, 29 )
    
    def testSubtract3(self):
        self.assertEqual( md.subtract(20,30).result, -21 )



    # any task you want run before any method above is executed, put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        md = MathDojo()
        print("running setUp")
        return md
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main() # this runs our tests

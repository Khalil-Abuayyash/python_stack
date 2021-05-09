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



class mathDojoTests(unittest.TestCase):
    
    def testAdd1(self):
        md = MathDojo()
        self.assertEqual( md.add(5).result, 5 )

    def testAdd2(self):
        md = MathDojo()
        self.assertEqual( md.add(5,2).result, 7 )
    
    def testAdd3(self):
        md = MathDojo()
        self.assertEqual( md.add(5,6,7).result, 18 )
    
    def testSuntract1(self):
        md = MathDojo()
        self.assertEqual( md.subtract(5).result, -5 )
    
    def testSuntract2(self):
        md = MathDojo()
        self.assertEqual( md.subtract(5,10,6).result, -21 )
    
    def testSuntract3(self):
        md = MathDojo()
        self.assertEqual( md.subtract(20,30).result, -50 )

    def testChain(self):
        md = MathDojo()
        self.assertEqual(md.subtract(5).add(10).add(10,20).subtract(10).result, 25)

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

import unittest
import calc

class TestCalc(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Set up once\n")

    @classmethod
    def tearDownClass(cls):
        print("Tear down in the end")
    
    def setUp(self):
        print("Setup\n")
    
    def tearDown(self):
        print("TearDown\n")
    
    def test_add(self):
        print("testing Add")
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(0,0),0)
        print("")
    def test_multiply(self):
        print("testing multiply")
        self.assertEqual(calc.multiply(10,5),50)
        self.assertEqual(calc.multiply(-1,1),-1)
        self.assertEqual(calc.multiply(0,0),0)
        print("")
    def test_subtract(self):
        print("testing subtract")
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(-1,1),-2)
        self.assertEqual(calc.subtract(0,0),0)
        print("")
    def test_divide(self):
        print("testing divide")
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-1,1),-1)
        self.assertRaises(ValueError, calc.divide, 0,0)     
        
        with self.assertRaises(ValueError):
            calc.divide(10,0)
if __name__ == "__main__":
    unittest.main()
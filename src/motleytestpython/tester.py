"""Simple and quick sanity check that Python is working correctly."""
import unittest
import sys
import operator
import datetime
class Tester(unittest.TestCase):

    def assert_equal(self,expected,actual,message=None):
        # assert exactly equal
        self.assertEqual(expected,actual,message)
        self.assertEqual(expected.__class__.__name__,actual.__class__.__name__,message)

    def test_addition(self):
        self.assert_equal(4,2+2)
        self.assert_equal(4.0,2+2.0)
        self.assert_equal(42,operator.add(20,22))
        self.assert_equal(-2.5,operator.add(0.5,-3.0))

    def test_subtraction(self):
        self.assert_equal(0,2-2)
        self.assert_equal(-2,3-5)
        self.assert_equal(-16,operator.sub(16,32))
        self.assert_equal(-16.0,operator.sub(16.0,32))
        self.assert_equal(4.0,6-2.0)

    def test_multiplication(self):
        self.assert_equal(16,8*2)
        self.assert_equal(16,-8*-2)
        self.assert_equal(-16,8*-2)
        self.assert_equal(-16,operator.mul(8,-2))
        self.assert_equal(-4.2,operator.mul(-2.1,2.0))
        self.assert_equal(4.2,operator.mul(2.1,2))
        self.assert_equal(27.0,9.0*3)

    def test_division(self):
        self.assert_equal(2,int(5/2))
        self.assert_equal(-2,int(-5/2))
        self.assert_equal(0,int(1/3))
        self.assert_equal(0,int(2/3))
        self.assert_equal(0,int(-1/3))
        self.assert_equal(0,int(-2/3))
        self.assert_equal(2.0,6.0/3.0)
        self.assertAlmostEqual(0.333333333,1.0/3.0,7)
        self.assertAlmostEqual(0.333333333,1/3,7)

    def test_floor_division(self):
        self.assert_equal(2,5//2)
        self.assert_equal(-3,5//-2)

    def test_zero_division(self):
        try:
            a = 1 / 0
            self.fail("Unexpected lack of ZeroDivisionError exception.")
        except ZeroDivisionError as e:
            self.assertTrue(True)
        except:
            e = sys.exc_info()[0]
            self.fail("Unexpected exception: " + str(e))
        try:
            a = 1.0 / 0.0
            self.fail("Unexpected lack of ZeroDivisionError exception.")
        except ZeroDivisionError as e:
            self.assertTrue(True)
        except:
            e = sys.exc_info()[0]
            self.fail("Unexpected exception: " + str(e))

    def test_modulo(self):
        self.assert_equal(0,16%8)
        self.assert_equal(0,16%8)
        self.assert_equal(7,16%9)
        self.assert_equal(1,16%5)
        self.assert_equal(4,-16%5)
        self.assert_equal(-4,16%-5)
        self.assert_equal(-1,-16%-5)
        self.assert_equal(1.0,16.0%5)
        self.assert_equal(4,-16%5)
        self.assert_equal(-4,16%-5)
        self.assert_equal(-1,-16%-5)

    def test_exponentiation(self):
        self.assert_equal(8,2**3)
        self.assert_equal(8.0,2**3.0)
        self.assert_equal(8.0,2.0**3)
        self.assert_equal(8.0,2.0**3.0)
        self.assert_equal(1,2**0)
        self.assert_equal(1.0,2.0**0)
        self.assert_equal(1.0,2**0.0)
        self.assert_equal(-8,-2**3)
        self.assert_equal(0.5,2**-1)

    def test_bit_and(self):
        self.assert_equal(1,5&3)
        self.assert_equal(5,5&-1)
        self.assert_equal(0,5&8)

    def test_bit_or(self):
        self.assert_equal(7,5|3)
        self.assert_equal(-1,5|-1)
        self.assert_equal(13,5|8)

    def test_xor(self):
        self.assert_equal(1,2^3)

    def test_right_shift(self):
        self.assert_equal(4,16>>2)

    def test_left_shift(self):
        self.assert_equal(16,4<<2)

    def test_assignment(self):
        i = 5
        self.assert_equal(5,i)
        x = 5.3
        self.assert_equal(5.3,x)
        s = "abc"
        self.assert_equal("abc",s)
        i = 2
        i += 1
        self.assert_equal(3,i)
        i = 2.0
        i += 1
        self.assert_equal(3.0,i)
        i = 2
        i *= 3
        self.assert_equal(6,i)
        i = 2.0
        i *= 3
        self.assert_equal(6.0,i)
        i = 6
        i /= 3
        self.assert_equal(2.0,i)
        i = 2.0
        i /= 3
        self.assertAlmostEqual(.666666667,i,7)
        x = 5
        x //= 2
        self.assert_equal(2,x)
        x = -5
        x //= 2
        self.assert_equal(-3,x)
        x = 5
        x &= 3
        self.assert_equal(1,x)
        x = 5
        x |= 3
        self.assert_equal(7,x)
        x = 2
        x ^= 3
        self.assert_equal(1,x)
        x = 16
        x >>= 2
        self.assert_equal(4,x)
        x = 4
        x <<= 2
        self.assert_equal(16,x)

    def test_comparison(self):
        self.assertTrue(3>2.5)
        self.assertFalse(3>3.0)
        self.assertFalse(3>4.0)
        self.assertFalse(3<2.5)
        self.assertFalse(3<3.0)
        self.assertTrue(3<4.0)
        self.assertFalse(3==2.5)
        self.assertTrue(3==3.0)
        self.assertFalse(3==4.0)
        self.assertTrue(3>=2.5)
        self.assertTrue(3>=3.0)
        self.assertFalse(3>=4.0)
        self.assertFalse(3<=2.5)
        self.assertTrue(3<=3.0)
        self.assertTrue(3<=4.0)
        self.assertTrue(3!=2.5)
        self.assertFalse(3!=3.0)
        self.assertTrue(3!=4.0)

    def test_logical_operators(self):
        t = True
        f = False
        self.assertFalse(f and f)
        self.assertFalse(f and t)
        self.assertFalse(t and f)
        self.assertTrue(t and t)
        self.assertFalse(f or f)
        self.assertTrue(f or t)
        self.assertTrue(t or f)
        self.assertTrue(t or t)
        self.assertFalse(not t)
        self.assertTrue(not f)

    def test_is(self):
        dt1 = datetime.datetime.utcnow()
        dt2 = dt1
        dt3 = datetime.datetime.utcnow()
        self.assertTrue(dt1 is dt2)
        self.assertFalse(dt1 is dt3)
        self.assertFalse(dt1 is not dt2)
        self.assertTrue(dt1 is not dt3)

    def test_in(self):
        self.assertTrue("b" in "abc")
        self.assertFalse("x" in "abc")
        self.assertFalse("b" not in "abc")
        self.assertTrue("x" not in "abc")
        self.assertTrue("b" in {"a":"apple", "b":"banana"})
        self.assertFalse("x" in {"a":"apple", "b":"banana"})
        self.assertTrue(2 in (1,2,3))
        self.assertFalse(22 in (1,2,3))
        self.assertTrue(2 in [1,2,3])
        self.assertFalse(22 in [1,2,3])
        self.assertTrue(2 in set((1,2,3)))
        self.assertFalse(22 in set((1,2,3)))

    def test_class_names(self):
        i = 42
        self.assert_equal('int',i.__class__.__name__)
        x = 42.1
        self.assert_equal('float',x.__class__.__name__)
        x = True
        self.assert_equal('bool',x.__class__.__name__)

    def test_str_concat(self):
        self.assert_equal("abcxyz","abc"+"xyz")

    @classmethod
    def run_tester(cls):
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        suite.addTests(loader.loadTestsFromTestCase(Tester))
        runner = unittest.TextTestRunner(verbosity=3)
        result = runner.run(suite)

if __name__=='__main__':
    #loader = unittest.TestLoader()
    #suite  = unittest.TestSuite()
    #suite.addTests(loader.loadTestsFromTestCase(Tester))
    #runner = unittest.TextTestRunner(verbosity=3)
    #result = runner.run(suite)
    Tester.run_tester()

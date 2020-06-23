"""Simple and quick sanity check that Python is working correctly."""
import unittest
import sys
import operator
import datetime
import random
import math
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

    def test_complex(self):
        self.assert_equal(2.0,complex(2,3).real)
        self.assert_equal(3.0,complex(2,3).imag)
        self.assert_equal(2.1,complex(2.1,3.1).real)
        self.assert_equal(3.1,complex(2.1,3.1).imag)
        c = 2.1 + 3.1j
        self.assert_equal(2.1,c.real)
        self.assert_equal(3.1,c.imag)
        self.assert_equal(2.1,c.conjugate().real)
        self.assert_equal(-3.1,c.conjugate().imag)
        c = (2+3j)+(3-2j)
        self.assert_equal(5.0,c.real)
        self.assert_equal(1.0,c.imag)
        c = (2+3j)-(3-2j)
        self.assert_equal(-1.0,c.real)
        self.assert_equal(5.0,c.imag)
        c = (2+3j)*(3-2j)
        self.assert_equal(12.0,c.real)
        self.assert_equal(5.0,c.imag)
        c = (2+3j)/(3-2j)
        self.assert_equal(0.0,c.real)
        self.assert_equal(1.0,c.imag)

    def test_class_names(self):
        i = 42
        self.assert_equal('int',i.__class__.__name__)
        x = 42.1
        self.assert_equal('float',x.__class__.__name__)
        x = True
        self.assert_equal('bool',x.__class__.__name__)
        x = complex(1,1)
        self.assert_equal('complex', x.__class__.__name__)
        x = [1,2,3]
        self.assert_equal('list', x.__class__.__name__)
        x = (1,2,3)
        self.assert_equal('tuple', x.__class__.__name__)
        x = range(0,10,1)
        self.assert_equal('range', x.__class__.__name__)
        x = {1:11, 2:12, 3:13}
        self.assert_equal('dict', x.__class__.__name__)
        x = {1,2,3}
        self.assert_equal('set', x.__class__.__name__)
        x = frozenset({1,2,3})
        self.assert_equal('frozenset', x.__class__.__name__)
        x = bytearray(10)
        self.assert_equal('bytearray', x.__class__.__name__)
        x = bytes(5)
        self.assert_equal('bytes', x.__class__.__name__)
        x = memoryview(bytes(5))
        self.assert_equal('memoryview', x.__class__.__name__)

    def test_random(self):
        random.seed()
        for i in range(0,200):
            x = random.randrange(1,10,1)  # random int from 1 to 9 inclusive.
            self.assertTrue(x>=1 and x<=9)

    def test_type_casting(self):
        self.assert_equal(1,int(1.9))
        self.assert_equal(-1,int(-1.9))
        self.assert_equal(2,int("2"))
        self.assert_equal(1.0,float(1))
        self.assert_equal(2.5,float("2.5"))
        self.assert_equal("2",str(2))
        self.assert_equal("2.5",str(2.5))
        self.assert_equal("(2+3j)",str((2+3j)))

    def test_exponential_notation(self):
        self.assert_equal(35000.0,3.5e4)
        self.assert_equal(2000.0,2e3)
        self.assert_equal(35000.0,3.5E4)
        self.assert_equal(0.35,3.5E-1)

    def test_math_functions(self):
        self.assert_equal(5,abs(5))
        self.assert_equal(5,abs(-5))
        self.assert_equal(5.0,abs(-5.0))
        self.assert_equal(8,pow(2,3))
        self.assert_equal(8.0,pow(2.0,3.0))
        self.assert_equal(42,round(42.3))
        self.assert_equal(42,round(41.5))
        self.assert_equal(42,round(41.7))
        self.assert_equal(-42,round(-42.3))
        self.assert_equal(-42,round(-41.5))
        self.assert_equal(-42,round(-41.7))
        self.assert_equal(3.1416,round(3.14159,4))
        self.assert_equal(99,max(3, 99, 23.3))
        self.assert_equal(99,max([3, 99, 23.3]))
        self.assert_equal(3,min(3, 99, 23.3))
        self.assert_equal(3,min([3, 99, 23.3]))
        self.assert_equal(3,math.floor(3.9))
        self.assert_equal(-4,math.floor(-3.9))
        self.assert_equal(3,math.ceil(2.1))
        self.assert_equal(-3,math.ceil(-3.9))
        self.assert_equal(3.0, math.fabs(-3))
        self.assert_equal(3.0, math.fabs(-3))
        self.assert_equal(0.5, math.sqrt(0.25))
        self.assert_equal(3.14159, round(math.pi,5))
        self.assert_equal(2.71828, round(math.e,5))
        self.assert_equal(0.6931, round(math.log(2),4))
        self.assert_equal(1.0, math.sin(math.pi/2))
        self.assert_equal(1.0, math.cos(0))
        self.assert_equal(90.0, math.degrees(math.pi/2))
        self.assert_equal(math.pi/2, math.radians(90))

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

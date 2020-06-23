import unittest
import motleytestpython.tester as mtp
class TestMotleyTestPython(unittest.TestCase):
    @classmethod
    def test_tester(cls):
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        suite.addTests(loader.loadTestsFromTestCase(mtp.Tester))
        suite.addTests(loader.loadTestsFromTestCase(mtp.Tester))
        runner = unittest.TextTestRunner(verbosity=3)
        result = runner.run(suite)

if __name__=='__main__':
    TestMotleyTestPython.test_tester()

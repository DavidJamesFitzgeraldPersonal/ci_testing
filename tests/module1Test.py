import unittest
from someModule import module1

class TestModule1(unittest.TestCase):
	def setUp(self):
		print("doing setup")

	def tearDown(self):
		print("doing teardown")

	def testTruePass(self):
		uut = module1.module1()
		self.assertEqual(uut.returnsTrue(), True)

	def testFalsePass(self):
		uut = module1.module1()
		self.assertEqual(uut.returnsFalse(), True)

if __name__ == '__main__':
    unittest.main()
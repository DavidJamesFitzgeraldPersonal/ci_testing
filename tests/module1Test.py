import unittest
from someModule import module1

class TestModule1(unittest.TestCase):
	def setUp(self):
		print("doing setup")
		self.uut = module1.module1()

	def tearDown(self):
		print("doing teardown")

	def testTruePass(self):
		self.uut.assertEqual(uut.returnsTrue(), True)

	def testFalsePass(self):
		self.uut.assertEqual(uut.returnsFalse(), False)

if __name__ == '__main__':
    unittest.main()
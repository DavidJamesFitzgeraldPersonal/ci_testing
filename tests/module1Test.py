import unittest
from someModule import module1

class TestModule1(unittest.TestCase):
	def setUp(self):
		print("doing setup")
		self.uut = module1.module1()

	def tearDown(self):
		print("doing teardown")

	# GIVEN
	# WHEN
	# THEN
	def testExpectTrue(self):
		self.assertEqual(self.uut.returnsTrue(), True)

	# GIVEN
	# WHEN
	# THEN
	def testExpectFalse(self):
		self.assertEqual(self.uut.returnsFalse(), True)

if __name__ == '__main__':
    unittest.main()

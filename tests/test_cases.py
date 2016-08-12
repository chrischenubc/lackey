import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
import lackey

class TestLocationMethods(unittest.TestCase):
	def setUp(self):
		self.test_loc = lackey.Location(10, 11)

	def test_getters(self):
		self.assertEqual(self.test_loc.getX(), 10)
		self.assertEqual(self.test_loc.getY(), 11)
		self.assertEqual(self.test_loc.getTuple(), (10,11))
		self.assertEqual(str(self.test_loc), "(Location object at (10,11))")

	def test_set_location(self):
		self.test_loc.setLocation(3, 5)
		self.assertEqual(self.test_loc.getX(), 3)
		self.assertEqual(self.test_loc.getY(), 5)
		self.test_loc.setLocation(-3, 1009)
		self.assertEqual(self.test_loc.getX(), -3)
		self.assertEqual(self.test_loc.getY(), 1009)

	def test_offsets(self):
		offset = self.test_loc.offset(3, -5)
		self.assertEqual(offset.getTuple(), (13,6))
		offset = self.test_loc.above(10)
		self.assertEqual(offset.getTuple(), (10,1))
		offset = self.test_loc.below(16)
		self.assertEqual(offset.getTuple(), (10,27))
		offset = self.test_loc.right(5)
		self.assertEqual(offset.getTuple(), (15,11))
		offset = self.test_loc.left(7)
		self.assertEqual(offset.getTuple(), (3,11))

class TestPatternMethods(unittest.TestCase):
	def setUp(self):
		self.pattern = lackey.Pattern("test_file.png")
	
	def test_defaults(self):
		self.assertEqual(self.pattern.similarity, 0.7)
		self.assertIsInstance(self.pattern.offset, lackey.Location)
		self.assertEqual(self.pattern.offset.getTuple(), (0,0))
		self.assertEqual(self.pattern.path, "test_file.png")

	def test_setters(self):
		test_pattern = self.pattern.similar(0.5)
		self.assertEqual(test_pattern.similarity, 0.5)
		self.assertEqual(test_pattern.path, "test_file.png")
		test_pattern = self.pattern.exact()
		self.assertEqual(test_pattern.similarity, 1.0)
		self.assertEqual(test_pattern.path, "test_file.png")
		test_pattern = self.pattern.targetOffset(3, 5)
		self.assertEqual(test_pattern.similarity, 0.7)
		self.assertEqual(test_pattern.path, "test_file.png")
		self.assertEqual(test_pattern.offset.getTuple(), (3,5))

	def test_getters(self):
		self.assertEqual(self.pattern.getFilename(), "test_file.png")
		self.assertEqual(self.pattern.getTargetOffset().getTuple(), (0,0))

class TestMouseMethods(unittest.TestCase):
	def setUp(self):
		self.mouse = lackey.Mouse()

	def test_movement(self):
		self.mouse.move(lackey.Location(10,10))
		self.assertEqual(self.mouse.getPos().getTuple(), (10,10))
		self.mouse.moveSpeed(lackey.Location(100,200), 1)
		self.assertEqual(self.mouse.getPos().getTuple(), (100,200))
		
	def test_clicks(self):
		"""
		Not sure how to build these tests yet
		"""
		pass

class TestKeyboardMethods(unittest.TestCase):
	def setUp(self):
		self.kb = lackey.Keyboard()

	def test_keys(self):
		self.kb.keyDown("{SHIFT}")
		self.kb.keyUp("{CTRL}")
		self.kb.keyUp("{SHIFT}")
		self.kb.type("%{CTRL}")


if __name__ == '__main__':
	unittest.main()
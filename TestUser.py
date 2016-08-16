import unittest
from user import *

class TestUser(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.danielle = User('danielle duer', 'danyellie')


	def test_user_is_created(self):
		self.assertEqual('danielle duer', self.danielle.full_name)
		self.assertEqual('danyellie', self.danielle.screen_name)
		self.assertIsNotNone(self.danielle.user_id)




if __name__ == '__main__':
    unittest.main()

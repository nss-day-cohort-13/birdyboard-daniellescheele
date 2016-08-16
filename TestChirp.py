import unittest
from chirp import *
from user import *

class TestChirp(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.cindy = User('cindy duer', 'cindysue' )
		self.test_chirp = Chirp("cindysue", self.cindy.user_id, "this is a message")

	def test_chirp_is_created(self):
		self.assertEqual(self.cindy.screen_name, "cindysue")
		self.assertEqual(self.test_chirp.message, "this is a message")
		self.assertEqual(self.test_chirp.user_id, self.cindy.user_id)
		self.assertIsNotNone(self.test_chirp.conversation_id)
		self.assertIsNotNone(self.test_chirp.chirp_id)




if __name__ == '__main__':
    unittest.main()

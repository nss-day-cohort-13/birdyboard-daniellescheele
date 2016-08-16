import unittest
from private_chirp import *
from user import *


class TestPrivateChirp(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.dan = User('dan duer','dannyd')
		self.test_private_chirp = PrivateChirp('lancelot', )


	def test_chirp_has_a_receiver(self):
		pass


	def test_get chirp(self):
		pass

if __name__ == '__main__':
    unittest.main()

import pickle
import uuid
from datetime import datetime
from time import time
from user import *


class Chirp:

	def __init__(self, user_screen_name, user_uuid, user_message):
		self.current_time = time()
		self.timestamp = datetime.fromtimestamp(self.current_time).strftime('%Y-%m-%d %H:%M:%S')
		self.screen_name = user_screen_name
		self.user_id = user_uuid
		self.message = user_message
		self.conversation_id = uuid.uuid4().int
		self.chirp_id = uuid.uuid4().int
		self.chirp_object = {
											'screenname': self.screen_name,
											'user id': self.user_id,
											'message': self.message,
											'conversation id': self.conversation_id,
											'chirp id': self.chirp_id,
											'timestamp': self.timestamp
											}
		self.serialize_chirp()

	def serialize_chirp(self):
		with open("chirp_file.txt", "ab+") as pickled_chirp_file:
			pickle.dump(self.chirp_object, pickled_chirp_file)


	@staticmethod
	def deserialize_chirp():

		chirp_list = []
		with open("chirp_file.txt", "rb+") as pickled_chirp_file:
			while True:
				try:
					chirp_list.append(pickle.load(pickled_chirp_file))
				except EOFError:
					break

			print(chirp_list)
			return chirp_list

if __name__ == '__main__':

	Chirp("blue", 62666258876467859545205171306045707530, "sorry")
	# Chirp("rbooby", 62666258876467859545205171306045707930, "blah blah")
	Chirp.deserialize_chirp()

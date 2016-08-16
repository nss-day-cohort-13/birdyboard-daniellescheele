import pickle
import uuid

class User:

	def __init__(self, name, screenname):
		self.full_name = name
		self.screen_name = screenname
		self.user_id = uuid.uuid4().int
		self.user_object = {
											'name': self.full_name,
											'screenname': self.screen_name,
											'user id': self.user_id
											}
		self.serialize_user()

	def serialize_user(self):
		with open("user_file.txt", "ab+") as pickled_user_file:
			pickle.dump(self.user_object, pickled_user_file)


	@staticmethod
	def deserialize_user():

		user_list = []
		with open("user_file.txt", "rb+") as pickled_user_file:
			while True:
				try:
					user_list.append(pickle.load(pickled_user_file))
				except EOFError:
					break

			print(user_list)
			return user_list

if __name__ == '__main__':
	# User("ricky bobby", "rbooby")
	User("BONNY PRIDE", "bonnny")
	User.deserialize_user()

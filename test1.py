from app import app
import unittest, json, uuid

class AuthTest(unittest.TestCase):
	
	
	def test_create_user(self):
		tester = app.test_client(self)
		response = tester.post('/user', data=json.dumps({'username': str(uuid.uuid4()), 'pwdhash': '2'}), content_type='application/json')
		statuscode = response.status_code

		self.assertEqual(statuscode, 200)
		
	def test_check_json(self):
		tester = app.test_client(self)
		response = tester.post('/user', data=json.dumps({'username': str(uuid.uuid4()), 'pwdhash': '2'}), content_type='application/json')
		self.assertEqual(response.content_type, "application/json")


	def test_check_update(self):
		tester = app.test_client(self)
		response = tester.post('/change_password/1', data=json.dumps({'pwdhash': '5'}), content_type='application/json')
		self.assertTrue(b'pass updated' in response.data)

	
if __name__ == '__main__':
	unittest.main()

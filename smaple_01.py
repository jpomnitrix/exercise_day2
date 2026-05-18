student = {'name': 'Taro', 'age': 20, 'major': 'Computer Science'}
print(student.get('age'))

user_info = {}
user_info['username'] = 'alice123'
user_info['email'] = 'alice@example.com'
print(user_info)
user_info['username'] = 'alice_pro'
print(user_info)

config = {'host': 'localhost', 'port': 8080, 'debug': True}
del config['debug']
print(config)

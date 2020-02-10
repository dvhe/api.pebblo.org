import random
import string
import requests
import time


def randomString(stringLength=25):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


# for i in range(100):
#     emails = ['yahoo.com', 'gmail.com', 'outlook.com', 'aol.com']
#     f = open('emails.txt', 'a')
#     f.write(f'{randomString(10)}@{random.choice(emails)}\n')
#     f.close()
#
# for i in range(100):
#     f = open('passwords.txt', 'a')
#     f.write(f'{randomString(10)}\n')
#     f.close()
#
# for i in range(100):
#     f = open('usernames.txt', 'a')
#     f.write(f'{randomString(10)}\n')
#     f.close()
#
# f = open('usernames.txt')
# lines = f.readlines()
# print(lines)

while True:
    emails = ['yahoo.com', 'gmail.com', 'outlook.com', 'aol.com']
    email = f'{randomString(25)}@{random.choice(emails)}'
    username = randomString(10)
    password = randomString(15)
    requests.post('http://localhost:5000/auth/register', json={
        'email': email,
        'username': username,
        'password': password
    })
    print(f'registering with {email} {username} {password}')


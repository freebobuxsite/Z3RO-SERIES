import requests
import random
import time


"""
import requests
 
def join(token, server_invite):
    header = {"authorization": token}
    r = requests.post("https://discord.com/api/v8/invites/{}".format(server_invite), headers=header)
"""

tokens = []

am = int(input("Enter the amount of tokens you have/want to use."))
amn = am + 1
for y in range(1, amn):
    token = str(input("Token {}: ".format(y)))
    tokens.append(token)

qu = int(input("Do you want to join a specific server? \n1: Yes \n2: No"))
if (qu == 1):
    invite = input("Enter server invite : ")
    def join():
        global auth
        for auth in tokens:
            header = {
                'authorization': auth
            }
            
            requests.post("https://discord.com/api/v8/invites/{}".format(invite), headers=header)
            print("Successfully server with {}".format(auth))
    join()
    print("Enter message: ")
    message = input()
    print("Enter channel ID")
    chanID = input()
    payload = {
        'content': message
    }
    
    while True:
        t = random.choice(tokens)
    
        header = {
            'authorization': t
        }
        url = 'https://discord.com/api/v8/channels/{}/messages'.format( chanID )
        requests.post(url, headers=header, data=payload)        

else:
    print("Enter message: ")
    message = input()
    print("Enter channel ID")
    chanID = input()
    payload = {
        'content': message
    }
    while True:
        t = random.choice(tokens);header = {"authorization": t}
        header = {
            'authorization': t
        }
        url = 'https://discord.com/api/v8/channels/{}/messages'.format( chanID )
        requests.post(url, headers=header, data=payload)

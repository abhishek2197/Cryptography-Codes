import os
import hashlib
import json
import time

def hash_email(email):
    content = json.dumps(email['content'], sort_keys=True)  #dumps to convert to string representation
    digest = hashlib.sha256(content.encode('utf-8')).hexdigest()  #Hashing to create digest
    return digest

def find_valid(email, target=4):
    target_digest = int('0'*target + 'f'*(64-target), 16) #create target value in hexadecimal representation
    digest = int(hash_email(email), 16) # get initial digest value and make it decimal int
    while digest > target_digest: #Check for match
        print ("No match")
        email['content']['nonce'] += 1
        digest = int(hash_email(email), 16)
    digest = hex(digest)[2:] #[2:] is to remove python's 0x prefix
    email['digest'] = '{:0>64}'.format(digest) #pads the leading zeroes if hexadecimal is less than 64 characters
    return email



email = {
    "content": {"from": "abhishek.aa@somaiya.edu",
                "to": "geetanantha@gmail.com",
                "subject": "Hashing for spam detecion",
                "body": "Implementation for checking if the digest matches the target approximately (atleast the beginning 0s)",
                "timestamp": 1103031175, 
                "nonce": 0},
                "digest": None 
}

print(hash_email(email))

final_email = find_valid(email)

print(final_email)

print("Time taken = "+str(time.clock()))

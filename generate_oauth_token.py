#!/usr/bin/env python

# this scrip is for generating oauthtoken for accessing github


import requests
import getpass
import json

GITHUB_API='https://api.github.com'

def main():
        #User Input
        username=raw_input("Enter your GitHub username: ")
        password=getpass.getpass("Github password:")
        note=raw_input('Note (optional):')

        #Compose request
        url=GITHUB_API+"/authorizations"
        payload={}
        if note:
                payload['note']=note
       
        # sends a request for token
        res=requests.post(url,auth=(username,password),data=json.dumps(payload))
        print res.status_code
        print res.headers['content-type']
        print res.text
       
        #Writing json response to a file
        f=open("token_details_v1.txt","w")
        f.write(res.text)

        # parse json response
        j=json.loads(res.text)
        if res.status_code >= 400:
                msg=j.get('message','UNDEFINED ERROR (no error description from the server)')
                print 'ERROR: %s' %msg
                return
        token=j['token']
        
        print "New Token: %s" %token
        print "U can use this token with any of the application"
        print "Token is also written in github_tokens file"

if __name__ == '__main__':
        main()

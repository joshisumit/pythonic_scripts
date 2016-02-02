#!/usr/bin/env python

'''
List GitHub repository of a user

Write a script that queries the Github API for repositories
belonging to the authenticated user.

For each repo, print out:
        -its name,
        -its description,
        -the number of open issues.

Use existing OAuth token
'''

import requests
import json
import sys

GITHUB_API="https://api.github.com"
API_TOKEN="your_token_goes_here"

def main():

        #form a request URL
        #username=raw_input("username for which public repo will be listed")
        url=GITHUB_API+"/user/repos"
        #url=GITHUB_API+"/users/:"
        #url+=username
        #url+="/repos"

        print "Request URL %s"%url

        # if you would like to add HTTP headers to a request, simply pass in a dict to the headers parameter.
        # Pass your token in header
        headers={'Authorization':'token %s' %API_TOKEN}
        params={'type':'all'}

        # Make a request with HTTP header
        r=requests.get(url,params=params,headers=headers)

        print "Status of Request %d" %r.status_code
        print "URL of request %s" %r.url
        print "=========================================="
        print "Printing Response"
        #print r.text

        # Convert JSON to a list
        j=json.loads(r.text)

        print "Total Repositories : %d"%(len(j))
        print ""

        #Print name,desc,open issues of each repository
        #repo is var which traverse the list beacuse j is list
        for repo in range(len(j)):
                print "Repo: %d"%(repo+1)
                print "Repo name: %s"%(j[repo]['name'])
                print "Repo description: %s"%(j[repo]['description'])
                print "Repo open issues: %d"%(j[repo]['open_issues_count'])
                print ""

if __name__=='__main__':
        main()

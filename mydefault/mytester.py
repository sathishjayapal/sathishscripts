import requests
import boto3
print("Hello world")
mylist = [1, 2, 3]
print(mylist)
for x in mylist:
    print("The value of x is {0}".format(x))
session = boto3.Session(profile_name='matty');

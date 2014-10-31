#Cloud Linker is an small script to create a direct link on copy.com and
#dropbox.com. It is based off the Visual Basic app off of techapple (http://bit.ly/1p96e0w)


from urllib.parse import urlparse
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
import sys

i = input("Enter URL: ")
#Dropbox Converter
if i.rfind('dropbox.com') != -1:
  o = urlsplit(i)
  a = list (o)
  a[0] = 'https://'
  a[1] = 'dl.dropbox.com'
  e = "".join(a)
  print(e)
#Copy Converter
elif i.rfind('copy.com') != -1:
  o = urlsplit(i)
  a = list (o)
  a[0] = 'https://'
  a[1] = 'copy.com'
  a[2] = a[2].replace('s/','')
  e = "".join(a)
  print(e)
#The Error Message
else:
  print('Error: Invalid URL')

# Copyright 2014 Keith Hizal (Hunter Nightblood)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#Import Libriaries
from urllib.parse import urlparse
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
import sys

i = input("Enter URL: ")
# Split URL into Parts
o = urlsplit(i)
# Convert tuple to list
a = list (o)
# Remove url query from list
del a[3:5]
#Dropbox Converter
if o.netloc == 'www.dropbox.com' :
  a[0] = 'https://'
  a[1] = 'dl.dropboxusercontent.com'
  e = "".join(a)
  print(e)
#Copy.com Converter
elif o.netloc == 'www.copy.com' :
  a[0] = 'https://'
  a[1] = 'copy.com'
  a[2] = a[2].replace('s/','')
  e = "".join(a)
  print(e)
#The Error Message
else:
  print('Error: Invalid URL')

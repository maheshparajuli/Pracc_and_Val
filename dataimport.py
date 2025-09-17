# from urllib.request import urlretrieve
from urllib.request import urlopen, Request
# url='https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
# urlretrieve(url,'winequality-red')


#1)
# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# This packages the request
request = Request(url)

# Sends the request and catches the response
response=urlopen(request)

# Extract the response: html

html=response.read()

# Print the html
print(html)


#and close the response!
response.close()

#2)

# Import package
# from urllib.request import Request
import requests


# Specify the url: url
url= "http://www.datacamp.com/teach/documentation"


# Packages the request, send the request and catch the response: r
r=requests.get(url)

# Extract the response: text
# text=response.open()
text=r.text


# Print the html
print(text)


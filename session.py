import requests
from time import gmtime, strftime

url = "https://10.9.40.3/api/?type=op&cmd=%3Cshow%3E%3Crunning%3E%3Cresource-monitor%3E%3Cminute%3E%3C%2Fminute%3E%3C%2Fresource-monitor%3E%3C%2Frunning%3E%3C%2Fshow%3E&key=LUFRPT0vTGM1UWp0cUh3cG1vcWxKc1U5dnBTQXc3emc9cVpXcWRXZ3RWOVYvMzcyUnlDOEZYTDU5anNUZXNQellaTVkxV2tveFFTVT0="

response = requests.get(url, verify=False)
filename = strftime("\%Y-%m-%d_%H-%M-%S_Session.xml", gmtime())
file_handle = open("C:\Users\DDuser\Desktop\Log_palo"+filename,"w")
file_handle.write(response.text)
file_handle.close()
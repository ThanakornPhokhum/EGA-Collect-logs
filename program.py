import requests, os
from time import gmtime, strftime


file_path = (strftime("D:\OneDrive - Ascend Corp\ETC\Log_Palo\%Y-%m-%d_resource_monitoring", gmtime()))


def ensure_dir():
    if not os.path.exists(file_path):
        os.mkdir(file_path)
        return "false"

    if os.path.exists(file_path):
        return "ok"

ensure_dir()


url = "https://10.9.40.3/api/?type=op&cmd=%3Cshow%3E%3Crunning%3E%3Cresource-monitor%3E%3Cminute%3E%3C%2Fminute%3E%3C%2Fresource-monitor%3E%3C%2Frunning%3E%3C%2Fshow%3E&key=LUFRPT0vTGM1UWp0cUh3cG1vcWxKc1U5dnBTQXc3emc9cVpXcWRXZ3RWOVYvMzcyUnlDOEZYTDU5anNUZXNQellaTVkxV2tveFFTVT0="

response = requests.get(url, verify=False)
filename = strftime("\%Y-%m-%d_resource_monitoring\%Y-%m-%d_%H-%M-%S_resource_monitoring.xml", gmtime())
file_handle = open("D:\OneDrive - Ascend Corp\ETC\Log_Palo"+filename,"w")
file_handle.write(response.text)
file_handle.close()

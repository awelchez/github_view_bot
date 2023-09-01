import httpx

def viewBot():
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    sec_ch_ua = '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"'
    url = ""
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Sec-Ch-Ua": sec_ch_ua,
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "Windows",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch_user": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": ua
    }
    response = httpx.get(url, headers=headers)

    if response.status_code != 200:
        print("Invalid URL. Please insert a valid Github Profile Views url.")
        quit()
    else:
        pass

    print(f"Botting has started. Please check for results at {url}")
while True:
    viewBot()

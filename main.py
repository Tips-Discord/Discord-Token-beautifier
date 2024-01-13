try:
    import os
    import tls_client
    import requests
    import json
    import random
    from os.path import isfile, join
    import base64
except ModuleNotFoundError:
    i = 0
    imports = [
        "tls_client",
        "requests"
    ]
    for _import in imports:
        i += 1
        print(f"Installing dependencies... ({i}/2)")
        print(f"installing {_import}")
        os.system(f'pip install {_import} > nul')
    import tls_client
    import requests
    import json
    import os
    import random
    from os.path import isfile, join
    import base64

session = tls_client.Session(client_identifier="chrome_120",random_tls_extension_order=True)

class Files:
    @staticmethod
    def write_config():
        if not os.path.exists("config.json"):
            data = {
                "Proxies": False,
            }
            with open("config.json", "w") as f:
                json.dump(data, f, indent=4)

    @staticmethod
    def write_folders():
        folders = [
            "data", 
            "avatars",
        ]
        for folder in folders:
            if not os.path.exists(folder):
                os.mkdir(folder)

    @staticmethod
    def write_files():
        files = [
            "tokens.txt", 
            "proxies.txt"
        ]
        for file in files:
            if not os.path.exists(file):
                with open(f"data/{file}", "a") as f:
                    f.close()

    @staticmethod
    def run_tasks():
        tasks = [Files.write_config, Files.write_folders, Files.write_files]
        for task in tasks:
            task()

Files.run_tasks()

with open("data/proxies.txt") as f:
    proxies = f.read().splitlines()

with open("config.json") as f:
    Config = json.load(f)

with open("data/tokens.txt", "r") as f:
    tokens = f.read().splitlines()



proxy = Config["Proxies"]

if proxy:
    session.proxies = {
        "http": f"http://{random.choice(proxies)}",
        "https": f"http://{random.choice(proxies)}",
    }

class Changer:
    def __init__(self):
        self.cookies = self.get_discord_cookies()

    def Headers(self, token):
        return {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'en',
            'cookie': self.cookies,
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9030 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'Europe/Warsaw',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDMwIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6InBsIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMzAgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMjYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjIyLjMuMjYiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyNTkwNDgsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjQyNjU2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9',
        }
    
    def get_discord_cookies(self):
        response = requests.get("https://canary.discord.com")
        match response.status_code:
            case 200:
                return "; ".join(
                    [f"{cookie.name}={cookie.value}" for cookie in response.cookies]
                ) + "; locale=en-US"
            case _:
                return "__dcfduid=4e0a8d504a4411eeb88f7f88fbb5d20a; __sdcfduid=4e0a8d514a4411eeb88f7f88fbb5d20ac488cd4896dae6574aaa7fbfb35f5b22b405bbd931fdcb72c21f85b263f61400; __cfruid=f6965e2d30c244553ff3d4203a1bfdabfcf351bd-1699536665; _cfuvid=rNaPQ7x_qcBwEhO_jNgXapOMoUIV2N8FA_8lzPV89oM-1699536665234-0-604800000; locale=en-US"
    
    def get_bio(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'pl,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        response = requests.get('https://quotable.io/random', headers=headers)

        content = response.json().get("content")
        author = response.json().get("author")

        bio = f"{content} - {author}"

        return bio

    def Add_HypeSquad(self, token):
        headers = self.Headers(token)
        data = {
            'house_id': random.randint(1, 4),
        }

        respone = session.post("https://discord.com/api/v9/hypesquad/online", headers=headers, json=data)

        match respone.status_code:
            case 204:
                print(f"added HypeSquad {token[:20]}")
            case _:
                print(f"failed adding HypeSquad {token[:20]}")

    def Add_Avatar(self, token):
        headers = self.Headers(token)
        picture = [f for f in os.listdir("avatars/") if isfile(join("avatars/", f))]
        random_picture = random.choice(picture)

        with open(f"avatars/{random_picture}", "rb+") as f:
            encoded_string = base64.b64encode(f.read())

        payload = {'avatar': f"data:image/png;base64,{(encoded_string.decode('utf-8'))}"}

        response = session.patch("https://discord.com/api/v9/users/@me", headers=headers)
        match response.status_code:
            case 200:
                print(f"Added pfp {token[:20]}")
            case _:
                print(f"Failed adding pfp {token[:20]}")

    def Add_Bio(self, token):
        headers = self.Headers(token)

        data = {
            'bio': f'{self.get_bio()}',
        }

        response = requests.patch('https://discord.com/api/v9/users/%40me/profile', headers=headers, json=data)

        match response.status_code:
            case 200:
                print(f"Added Bio {token[:20]}")
            case _:
                print(f"Failded adding bio {token[:20]}")

    def Main(self):
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()

        avatars = [f for f in os.listdir("avatars/") if isfile(join("avatars/", f))]

        print(f"{' '*44}Loaded ‹{len(tokens)}› tokens | Loaded ‹{len(proxies)}> proxies | Loaded <{len(avatars)}> pfps")
        input("Press Enter To Start")

        for token in tokens:
            self.Add_Avatar(token)
            self.Add_HypeSquad(token)
            self.Add_Bio(token)

        input("done")


if __name__ == "__main__":
    Changer().Main()
import requests

target_urls= [
    "https://httpstat.us/101",
    "https://httpstat.us/201",
    "https://httpstat.us/301",
    "https://httpstat.us/404",
    "https://httpstat.us/500",    
]

def make_request(target_url: str):
    response = requests.get(target_url)

    if 100<=response.status_code<=300:
        print(f"OK: {response.status_code}")
        print(f"response body: {response.content}")
    elif 400<=response.status_code<=500:
        raise requests.exceptions.HTTPError(response=response)
    else:
        print(f"Unrecognised status code {response.status_code} for {url}")

if __name__ == "__main__":
    print("Starting requests to httpstat.us")
    for i, url in enumerate(target_urls):
        print(f"-----------REQUEST {i+1} to {url}---------------")
        try:
            make_request(url)
        except requests.exceptions.HTTPError as e:
            print(f"HTTP ERROR")
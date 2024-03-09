import requests
from timer import timer 
from concurrent.futures import ProcessPoolExecutor

URL = "https://httpbin.org/uuid"

def fetch_uuid(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])

@timer(1, 1)
def main():
    with ProcessPoolExecutor(max_workers=100) as executor:
        with requests.Session() as session:
            executor.map(fetch_uuid, [session] * 100, [URL] * 100)
            executor.shutdown(wait=True)
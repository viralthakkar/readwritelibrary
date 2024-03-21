import threading
import requests


def download_page(url):
    response = requests.get(url)
    print(f"Downloaded {url}, length: {len(response.content)}")


urls = [
    'https://example.com/page1',
    'https://example.com/page2',
    'https://example.com/page3',
    'https://example.com/page4'
]

threads = []
for url in urls:
    thread = threading.Thread(target=download_page, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()


from multiprocessing import Pool

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        result = pool.map(fibonacci, [35, 36, 37, 38])
    print(result)


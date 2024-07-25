import multiprocessing
import requests
import os
import concurrent.futures

def downloadFile(url, name):
    print(f"Starting Downloading {name}")
    response = requests.get(url)
    # Ensure the 'files' directory exists
    os.makedirs('files', exist_ok=True)
    with open(f"files/file_{name}.jpg", "wb") as file:
        file.write(response.content)
    print(f"Finished Downloading {name}")

url = "https://picsum.photos/1920/1080"

if __name__ == "__main__":
    # pros = []
    # for i in range(10):
    #     p = multiprocessing.Process(target=downloadFile, args=(url, i))
    #     p.start()
    #     pros.append(p)
        
    # for p in pros:
    #     p.join()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for i in range(10)]
        l2 = [i for i in range(10)]
        results = executor.map(downloadFile, l1, l2)
        for r in results:
            print(r)

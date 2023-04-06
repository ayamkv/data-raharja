import requests
import json
import os

def main():
    url = 'https://ee2poimw.directus.app/items/link'
    response = requests.get(url)
    data = response.json()

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

    print("\nCurrent working dir:")
    print(os.getcwd())

    print("\nList dir:")
    print(os.listdir(os.getcwd()))

    print("\nGit status:")
    os.system('git status')

if __name__ == "__main__":
    main()

import requests
import json
import os

def main():
    url = 'https://linko.pockethost.io/api/collections/link/records'
    response = requests.get(url)
    data = response.json()

    with open('data-pb.json', 'w') as outfile:
        json.dump(data, outfile)

    print("\nCurrent working dir:")
    print(os.getcwd())

    print("\nList dir:")
    print(os.listdir(os.getcwd()))

    print("\nGit status:")
    os.system('git status')

if __name__ == "__main__":
    main()

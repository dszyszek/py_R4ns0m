import requests


def check_connection():
    try:
        try_connection = requests.get('https://google.pl', timeout=10)
        return True

    except:
        return False



if __name__ == '__main__':
    print(check_connection())
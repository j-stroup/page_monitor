import hashlib
import requests
import time


urls = []

def start():
    single_multiple = input('Single URL, Multiple URLs, or File? S/M/F ')
    if single_multiple.lower() == 's':
        url = 'https://' + input('Website to monitor: https://')
        frequency = int(input('How often do you want to check for updates? (Time in seconds) '))
        check_single_site(url, frequency)
    elif single_multiple.lower() == 'f':
        file = input('File name: ')
        frequency = int(input('How often do you want to check for updates? (Time in seconds) '))
        with open(file, 'r', encoding="utf-8") as file:
            for line in file:
                url = line.strip()
                urls.append(url)
        check_sites_file(frequency)
    elif single_multiple.lower() == 'm':
        check_sites_multiple()
    else:
        start()

def check_sites_multiple():
    list = {}
    urls = []
    adding = True
    while adding == True:
        page = input('Website to monitor (leave blank to continue): https://')
        if page != '':
            urls.append('https://' + page)
            adding = True
        else:
            adding = False
    frequency = int(input('How often do you want to check for updates? (Time in seconds) '))
    for item in urls:
        url = item.strip()
        r = requests.get(url)
        response = str(r)
        response = response.strip('<Response []>')
        if response != '200':
            print(url.replace('https://','') + ' - Error')
        else:
            page_source = r.text.encode('utf-8')
            hash = hashlib.sha256(page_source).hexdigest()
            print(f'\n{item}')
            print(hash)
            list.update({url:hash})
    count = 0
    for key in list:
        count = count + 1
    while True:
        time.sleep(frequency)
        for url in urls:
            obj = time.localtime()
            t = time.asctime(obj)
            hash = list.get(url)
            r = requests.get(url)
            response = str(r)
            response = response.strip('<Response []>')
            if response != '200':
                print(t + ' - ' + url.replace('https://','') + ' - Error')
            else:
                page_source = r.text.encode('utf-8')
                hash_check = hashlib.sha256(page_source).hexdigest()
                if hash_check != hash:
                    print(t + ' - ' + url.replace('https://','') + ' has been updated')
                    hash = hash_check
                else:
                    print(t + ' - No update')

def check_single_site(url, frequency):
    r = requests.get(url)
    response = str(r)
    response = response.strip('<Response []>')
    if response != '200':
        print(r + ' - ' + url.replace('https://','') + ' - Error')
    else:
        page_source = r.text.encode('utf-8')
        hash = hashlib.sha256(page_source).hexdigest()
        print(f'\n{url}')
        print(hash)
        print('\n')
        while True:
            time.sleep(frequency)
            r = requests.get(url)
            response = str(r)
            response = response.strip('<Response []>')
            if response != '200':
                print(t + ' - ' + url.replace('https://','') + ' - Error')
            else:
                page_source = r.text.encode('utf-8')
                hash_check = hashlib.sha256(page_source).hexdigest()
                if hash_check != hash:
                    print(t + ' - Page has been updated')
                    hash = hash_check
                else:
                    print(t + ' - No update')

def check_sites_file(frequency):
    list = {}
    for item in urls:
        url = item.strip()
        r = requests.get(url)
        response = str(r)
        response = response.strip('<Response []>')
        if response != '200':
            print(url.replace('https://','') + ' - Error')
        else:
            page_source = r.text.encode('utf-8')
            hash = hashlib.sha256(page_source).hexdigest()
            print(f'\n{item}')
            print(hash)
            list.update({url:hash})
    print('\n')
    count = 0
    for key in list:
        count = count + 1
    while True:
        obj = time.localtime()
        t = time.asctime(obj)
        time.sleep(frequency)
        for url in urls:
            hash = list.get(url)
            r = requests.get(url)
            response = str(r)
            response = response.strip('<Response []>')
            if response != '200':
                print(t + ' - ' + url.replace('https://','') + ' - Error')
            else:
                page_source = r.text.encode('utf-8')
                hash_check = hashlib.sha256(page_source).hexdigest()
                if hash_check != hash:
                    print(t + ' - ' + url.replace('https://','') + ' has been updated')
                    hash = hash_check
                else:
                    print(t + ' - No update')


start()

import time
import csv
import requests   

def claim_request(url, token, proxy):
    
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'de-DE,de;q=0.9',
        'Content-type': 'text/plain;charset=UTF-8',
        'Origin': 'https://onetime.dog',
        'Referer': 'https://onetime.dog/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    
    proxies = {
        'http': proxy,
        'https': proxy
    }  
    response = requests.post(url, headers=headers, proxies=proxies, data=token)
    return response
    
def read_csv(file_path):
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if len(row) == 3:  # Проверяем, что строка содержит 3 поля
                entry = {
                    'discription': row[0],
                    'proxy': row[1],
                    'token': row[2]
                }
                data.append(entry)
    return data
 

def claim_function(file_path):
    while True:
        data = read_csv(file_path)
        for entry in data:
            claim_request("https://bot.pocketfi.org/mining/claimMining", entry['token'], entry['proxy'])
            print(entry['discription'] + " join function отработал")
        time.sleep(6 * 60 * 60)  # Спим 6 часа (6 * 60 минут * 60 секунд)
 
 
if __name__ == '__main__':
    file_path = 'file.csv'
    
    # Запуск функции синхронизации в отдельном потоке
    
    claim_function(file_path) 


 
import random
file = open('../2022_1_24_requests高级/ip_Pool.csv', 'r', encoding='utf-8')
data = file.readlines()
print(data)
file.close()
proxies = {
    'https': random.choice(data).split(',')[1].strip()
}
print(proxies)
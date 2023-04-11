import requests
from time import time

def time_function(func):
    def time_check(*args, **kwargs):
        time1 = time()
        func(*args, **kwargs)
        time2 = time()
        print(f'Request taking {round(time2 - time1, 2)} sec.')
    return time_check

@time_function
def make_request(url='http://learn.di-learning.com/'):
    print(f'Request to {url}')
    requests.get(url)

url = input('Insert a website address (e.g. http://learn.di-learning.com/): ')
make_request(url)
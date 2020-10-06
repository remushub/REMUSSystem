docker pull redis

docker volume create redis-volume

docker run --name redis -p 6379:6379 -v redis-volume:/data -d redis redis-server --appendonly yes

import redis

r = redis.Redis(host='xx.xx.x.xx.x', port=6379, db=0)

items = {
    "202010051234001002001": "1003",
    "202010051234401032001": "10",
    "202010051234001002001": "53",
    "202010051234041002401": "5703",
    "202010051234041052001": "3",
    "202010051234041052341": "234",
    "202010051234041002402": "5703",
}

updated_items = {
    "202010051234001002001": "1003",
    "202010051234401032001": "10",
    "202010051234001002001": "53",
    "202010051234041002401": "5703",
    "202010051234041052001": "3",
    "202010051234041052341": "234",
    "202010051234041002402": "5703",
    "202010051234041052046": "46",
}
def main():
    print('setting items')
    update_items(updated_items)
    print('getting items')
    output = get_items()
    print('output:')
    print(output)

def get_items():    
    output_dict = {}
    for key in r.scan_iter('*'):
        output_dict[key] = r.get(key)
    return output_dict

def set_items(item_dict):
    pipe = r.pipeline()
    for key, value in item_dict.items():
        pipe.set(key, value)
    pipe.execute()


def update_items(item_dict):
    pipe = r.pipeline()
    for key, value in item_dict.items():
        stored = r.get(key)
        if(stored):
            pipe.set(key, str(int(stored) + int(value)))
        else:
            pipe.set(key, value)
    pipe.execute()

if __name__ == "__main__":
    main()

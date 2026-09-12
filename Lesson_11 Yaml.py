import yaml

l_connections = [
    {
        "user_name": "etl_user",
        "password": "123",
        "host": "127.0.0.1"
    },
    {
        "user_name": "test_user",
        "password": "456"
    }
]

with open(r'connections.yaml', 'w') as file:
    documents = yaml.dump(l_connections, file)

with open(r'connections.yaml') as file:
    connections = yaml.load(file, Loader=yaml.FullLoader)
    print(connections)
    print(type(connections))




clients = {'Aldrich': 1.97,
           'Enrico': 8.49,
           'Christoper': 9.79,
           'Cherice': 8.53,
           'Margi': 0.43}

for name in enumerate(clients):
    print(name[1], 'has spend', clients[name[1]])
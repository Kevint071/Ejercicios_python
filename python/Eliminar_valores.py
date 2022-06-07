def clean(arr):
    acc = []

    for i in arr:
        if i != None and i != 0:
            acc.append(i)

    print(acc)

clean([1,None, None, 0, 2, 4]) 

def load_database(filename):
    dic = {}
    myfile = open(filename, "a")
    myfile.close()
    with open(filename, 'r') as f:
        for line in f:
            [user, singers] = line.strip().split(":")
            singersList = singers.split(",")
            dic[user] = singersList
    return dic


def save_database(dic, filename):
    keyList = list(dic.keys())
    keyList = sort(keyList)
    myfile = open(filename, 'w')
    for item in keyList:
        string = item + ":"
        for s in dic[item]:
            string += s + ','
        string = string[:-1] + "\n"
        myfile.write(string)

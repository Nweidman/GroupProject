import sort


def load_database(filename):
    """Takes in a file, filename, and creates it if the filename does not
    already exist. If the file does exist, it opens the file and returns
    a dictionary with the file's contents."""
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
    """Takes in a dictionary and the file you want to save the dictionary to.
    The updated dictionary is then transferred back to the file in the same
    format as before."""
    keyList = list(dic.keys())
    sort.sort(keyList)
    myfile = open(filename, 'w')
    for item in keyList:
        string = item + ":"
        for s in dic[item]:
            string += s + ','
        string = string[:-1] + "\n"
        myfile.write(string)

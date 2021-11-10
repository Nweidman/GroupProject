def sort(artistList):
    """Sorts a list of strings alphabetitcally using merge sort"""
    if len(artistList) > 1: #If the length of the list is greater than 1 run this
        middleIndex = len(artistList) // 2 #Middle Index is halfway point of the list using int division 
        leftList = artistList[:middleIndex]
        rightList = artistList[middleIndex:] #left and right list created by splitting list by that middle index
        sort(leftList)
        sort(rightList) #recursive call of the left and right list to further break down the list till it gets to length 1 where it will no longer run the if statement
        indexMain = 0
        indexLeft = 0
        indexRight = 0 #creation of indexes for each list
        while indexLeft < len(leftList) and indexRight < len(rightList): #Runs through the left and right list at the same time while comparing them until one of the lists reaches the end 
            leftString = leftList[indexLeft].lower()
            leftString = leftString.replace(" ", "")
            rightString = rightList[indexRight].lower()
            rightString = rightString.replace(" ", "") #Right and Left string created by standarizing each string to all lowercase and no spaces
            if leftString <= rightString:
                artistList[indexMain] = leftList[indexLeft]
                indexLeft += 1 #If the leftString is alphabetically before rightString i.e. <= it will set the main string at indexMain to the leftList at indexLeft 
            else:
                artistList[indexMain] = rightList[indexRight]
                indexRight += 1 #If the leftString is alphabetically after rightString i.e. <= it will set the main string at indexMain to the rightList at indexRight 
            indexMain += 1 #Index of main increased by 1 to go to next element
        while indexLeft < len(leftList):
            artistList[indexMain] = leftList[indexLeft]
            indexLeft += 1
            indexMain += 1 #All remaining parts of the left list if left is greater than right at that time, run through here to set remaining values of index main to leftList
        while indexRight < len(rightList):
            artistList[indexMain] = rightList[indexRight]
            indexRight += 1
            indexMain += 1 #All remaining parts of the right list if right is greater than left at that time, run through here to set remaining values of index main to rightList
    else: 
        return artistList

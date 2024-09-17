def func(lst):
    myDct = {}
    for i in range(len(lst)):
        myDct[lst[i]] = lst.count(lst[i])
    print(myDct)

myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]

func(myList)
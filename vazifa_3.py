def func(text):
    myDct = {}
    for i in range(len(text)):
        myDct[text[i]] = text.count(text[i])
    print(myDct)

text = "mississippi"

func(text)
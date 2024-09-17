lst1 = ['olma', 'anor', 'gilos', True, 12, 10, 'olma', 'gilos', 1]
lst2 = ['olma', 'anor', 'gilos', True, 12, 10, 'banan']

def has_dublicat(lst):
    dublicat_bor = False
    for i in range(len(lst)):
        if lst.count(lst[i])>1:
            dublicat_bor = True
    if dublicat_bor:
        print("Dublikat bor")
    else:
        print("Dublikat yo'q")

has_dublicat(lst1)
has_dublicat(lst2)

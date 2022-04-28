#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    prf = "__"
    newlist = [x for x in dir(hidden_4) if not x.startswith(prf)]

    for i in range(len(newlist)):
        print(newlist[i])

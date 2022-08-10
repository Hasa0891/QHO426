with open("song.txt") as song:
    s = song.read()
    s1 = s.lower().replace(",", "").split()
    print(s1)
    print("~"*30)
    print(set(s1))
    print("~"*30)
    dictio = {}
    for token in s1:
        dictio[token] = dictio.get(token, 0) + 1
    print(dictio)
    print("~"*30)
    print(f"To write a viral song, you need {len(set(s1))} unique words")
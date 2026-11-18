word = "sucess"
count = {}
size = len(word)

for x in word:
    count[x] = count.get(x,0)+1

for x,c in count.items():
    print(f"{x} : {c}")
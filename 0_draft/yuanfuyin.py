
word = "ieaouqqieaouqq"
k = 1


vow = ['a','e','i','o','u']
sub = []
l = len(word)
subcount = 0


for i in range(l):

    occur = set()
    fuyincount = 0

    for j in range(i,l):
        if word[j] in vow:
            occur.add(word[j])
        else:
            fuyincount += 1
        
        if len(occur) == 5 and fuyincount == k:
            sub.append(word[i:j+1])
            subcount += 1



print(subcount)
print(sub)
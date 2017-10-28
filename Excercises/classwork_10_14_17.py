word = "Purple banana"
c=0
for i in range (0,len(word)):
    print(word[i])

print("")

while c < len(word):
    print(word[c])
    c = c+1

print("Please enter a word to count")
word3 = input(">>")
x=0
for i in range (0,len(word3)):
    x=x+1
print (x)

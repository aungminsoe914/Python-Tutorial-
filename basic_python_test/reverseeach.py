#reverse each character
p = input("enter character")

x = p.split()
l = []
i = 0
while i<len(x):
    l.append(x[i][::-1])
    i = i+1
opt = ' '.join(l)
print(opt)


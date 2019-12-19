#Задача1
st='Data should be begging of Data and Data should be Data of big'
words=st.split()
print(words)
unique={}
for word in words:
    word=word.lower()
    if unique.get(word) is None:
        unique.setdefault(word,1)
    else:
        unique[word]+=1
print(unique)
#Задача2
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new_a=[x for x in a if x%2!=0]
#Задача3
ls=[(x,x**2) for x in range(1,11)]
print(ls)
#Второй вариант
for i in range(1,11):
    sq=i**2
    ls.append((i,sq))
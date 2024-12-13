x=str(input("enter a string"))
y="aeiou"
count=0
for i in x:
    if i in y:
        count+=1
print("vowels are",count)

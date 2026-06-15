text=(input("Enter string : "))
vowels="aeiouAEIOU"

count=0
i=0

while i<len(text):
    if text[i]in vowels:
        count=count+1
    i=i+1
print("Number of vowels in your string: ",count)

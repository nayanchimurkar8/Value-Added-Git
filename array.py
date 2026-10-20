# count the numbers of alphabetic characters in a string and how many times they repeat in the string
x= "abcadweesdadasd"
arr =[0]*26 
for i in range(len(x)):
    arr[ord(x[i])-97]+=1
for i in range(len(arr)):
    print(chr(i+97),"->",arr[i])
    
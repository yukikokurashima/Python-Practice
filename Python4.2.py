words_num=int(input("Please enter the number of words you want to write to a file:\t"))
words_in_file=''
file1=open('ThreePointOne.txt','w')
for i in range(words_num):
    word=input("Please enter a word:\t")
    file1.write(words_in_file+word+"\n")
file1.close()


#Question 3.2
file2=open('ThreePointOne.txt','r')
line=file2.readline().rstrip("\n")
num=0
Total_len=0
long_len=0
longlen_word=''
try:
    while line!='':
        num+=1
        Total_len+=len(line)
        if len(line)>long_len:
            long_len=len(line)
            longlen_word=line
        line=file2.readline().rstrip("\n")
    print("The number of words is:\t",num)
    print("The average length of all of the words in the file is:\t",Total_len/num)
    print("The longest word in the file is:\t",longlen_word)
except Exception as err:
    print(err)
finally:
    file2.close()
    

    

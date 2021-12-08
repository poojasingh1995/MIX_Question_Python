# import re
# def titlecase(s):
#     return re.sub(r"[A-Za-z]+('[A-Za-z]+)",lambda mo:mo.group(0)[0].upper()+mo.group(0)[1:].lower(),s)
# text="my name is pooja singh"
# print(titlecase(text))

# split function 
# sentence=input("enter some text:-")
# new_list=[]
# string=""
# for i in (sentence+" "):
#     if i==" ":
#         new_list.append(string)
#         string=" "
#     else:
#         string+=i
# print(new_list)


# Title function
# sentence=input("enter the sentence:-")
# words=sentence.split(" ")
# new_list=[]
# for i in words:
#     words_1=i[0].upper()+i[1:]
#     new_list.append(words_1)
# print(" ".join(new_list))

# a=[1,2,34,5]
# print(a[:-1])

# def isHappynumber(n):
#     digit=sum=0
#     while n>0:
#             digit=n%10
#             sum=sum+(digit*digit)
#             n=n//10
#     return sum
# num=int(input("enter the number:"))
# result=num
# while(result!=1 and result!=4):
#     result=isHappynumber(result)
# # # num=int(input("enter the number:"))
# # # result=num
# if(result==1):
#     print(num,"is a happy num")
# else:
#     print(num,"is an unhappy num")


# def isHappynumber(n):
#     num=int(input("enter the number:"))
#     digit=0
#     sum=0
#     i=0
#     while i<=num:
#         digit=num%10
#         sum=sum+(digit*digit)
#         num=num//10
#         print(sum)
# num=int(input("enter the number:"))
# result=num
#     while(result!=1 and result!=4):
#         result=isHappynumber(result)
# num=int(input("enter the number:"))
        # result=num
#         if(result==1):
#           print(num,"is a happy num")
#         else:
#           print(num,"is an unhappy num")
    
#     i+=1

# sum=0
# num=int(input("enter the number: "))
# i=0
# while (sum!=1 and sum!=4):
#     sum=0
#     while (i<=10):
#         temp=i%10
#         sum+=(temp*temp)
#         i=i//10
#         i+=1
#     i=sum
# if (sum==1):
#     print(i,"number is a happy number")
# else:
#     print(i,"number is not happy number")
# i=i+1

# i=0
# while i<=10:
#     sum=0
#     while (sum!=1 and sum!=4):
# #     sum=0
#         # while (i<=10):
#         temp=i%10
#         sum+=(temp*temp)
#         i=i//10
#         # i+=1
#     i=sum
# if (sum==1):
#     print(i,"number is a happy number")
# else:
#     print(i,"number is not happy number")
# i=i+1

# def happy_num(n):
#     past=set()
#     while n!=1:
#         n=sum(int(i)**2 for i in str(n))
#         if n in past:
#             return False
#         past.add(n)
#     return True
# print([x for x in range(500) if happy_num(x)][:10])

# def isHappy_num(num):
#     digit=sum=0
#     while(num>0):
#         digit=num%10
#         sum=sum+(digit*digit)
#         num=num//10
#     return sum
# for i in range(1,50):
#    result=i 
#    while(result!=1 and result!=4):
#         result=isHappy_num(result)
#    if(result==1):
#         print(i,"is happy num")
#    else:
#         print(i,"is not happy num")

# def isHappy_num(num):
#     digit=sum=0
#     while(num>0):
#         digit=num%10
#         sum=sum+(digit*digit)
#         num=num//10
#     return sum
# i=1
# while i<=50:
# # for i in range(1,50):
#     result=i
#     while(result!=1 and result!=4):
#         result=isHappy_num(result)
#     if(result==1):
#         print(i,"is happy num")
#     else:
#         print(i,"is not happy num")
#     i+=1


# year=int(input("enter the year"))
# if year%4==0 or year%100==0:
#     print("leap year")
#     if year%400!=0:
#         print("leap year")
#     else:
#         print("not leap year")
# else:
#     print("no leap year")


# num=int(input("enter the first num"))
# num2=int(input("enter the second num"))
# num3=int(input("enter the third num"))
# if num>num2>num3  :
#     print(num,"greater num")
# elif num2>num3>num  :
#     print(num2, "greater num")
# elif num3>num2>num :
#     print(num3, "greater num")
# else:
#     print("no greater num")


# i=1
# while(i<=6):
#     a=1
#     while(a<i):
#         print(a,end="")
#         a=a+1
#     print()
#     i+=1

# num=int(input("enter the num"))
# a=1
# while(num>0):
#     a=a*num
#     num=num-1
# print("a=",a)


# list_value=[3,4,6,8,2,9,1,7,5]
# new_list=[]
# while list_value:
#     min=list_value[0]
#     for index in list_value:
#         if index<min:
#             min=index
#         list_value.remove(min)                                                                                                                                                                                                                                                                                                                                                                                       
#         new_list.append(min)
# print(new_list) 


# a=[1,8,2,6,3,9,4,5,7]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]<a[j]:
#             temp=a[i]
#             a[i]=a[j]
#             a[j]=temp
#         j+=1
#     i+=1
# print(a)
# b=[]
# i=1
# while i<=len(a):
#     b.append(a[-i])
#     i+=1
# print(b)

# a=[1,-1,-2,3,4,-5,6]
# k=[]
# i=0
# while i<len(a):
#     if a[i]<0:
#         data=a[-1]*0
#         k.append(data)
#     else:
#         # print(a[i],end=" ")
#         k.append(a[i])
#     i=i+1
# print(k)

# list=[1,2,4,8,9,10]
# i=0
# a=0
# n=[]
# while i<10:
#     a=a+1
#     if a not in n:
#         n.append(a)
#     i=i+1
# print(n)


# i=1
# k=1
# while(i<=5):
#     a=1
#     while(a<i):
#         print(a,end="")
#         a=a+1
#     k=i
#     while k>0:
#         print(k,end="")
#         k=k-1
#     print()
#     i=i+1

# def num():
#     num=[50,40,23,70,56,12,89,5,10,7,65]
#     i=0
#     while i<len(num):
#         k=num[i]
#         if k>num[0] and k<num[3]:
#            print("second max",k)
#         i=i+1
# num()


# def prime_or_not(num):
    
#     # for i in range(2,num):
#         if (num%2==0):
#             print(num,"is not a prime num")
#             # print(i,"time",num//i,"is",num)
#             # break
#         else:
#             print(num,"is a prime num")
# prime_or_not(13)

# list=[2,-7,5,-64,-14,-8]
# i=0
# a=0
# k=0
# while i<len(list):
#     if list[i]>0:
#         print(list[i],"postivie num")
#         a=a+1
#     else:
#         print(list[i],"negative num")
#         k=k+1
#     i=i+1
# print(a,"positive")
# print(k,"negative")

# dict1={"India":"Delhi","Foreign":"America","United state":"Washington"} 
# dict2={"France":"Paris","India":"Delhi","U.P":"Lakhnow"} 
# dict3=dict1.copy() 
# for key,value in dict2.items():
#     dict3[key] =value
# print(dict3)

# dict3={**dict1,**dict2} 
# print(dict3)  

# def return_sum(my_dict):
#     list=[]
#     for i in my_dict:
#         list.append(my_dict[i])
#     final=sum(list)
#     return final
# dict={"a":10,"b":20,"c":30}
# print("sum:",return_sum(dict))

# def return_sum(my_dict):
#     sum=0
#     for i in dict.values():
#         sum=sum+i
#     return sum
# dict={"a":10,"b":20,"c":30}
# print("sum:",return_sum(dict))


# num=int(input("input the num"))
# a=dict()
# for x in range(1,num+1):
#     a[x]=x*x
# print(a)

# def add_num_list(list1,list2):
#     i=0
#     sum=0
#     y=[]
#     while i<len(list1):
#         b=(list1[i]+list2[i])
#         y.append(b)
#         i=i+1
#     return(y)
# add_num_list([50,60],[10,20])

# def sum(number):
#     sum=0
#     for i in number:
#         sum=sum+i
#     return sum
# print(sum((12,23,13,6,7)))

# num=[2,8,5,4,0]
# def fun_1():
#     sum=0
#     for i in num:
#         sum=sum+i
#     return sum
# print(fun_1())


# a=[2,4,6,8,9,13]
# i=0
# max=a[0]
# min=a[0]
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     if a[i]<min:
#         min=a[i]
#     i=i+1
# print("maximum num is=",max)
# print("minimum num is=",min)


# var_1=int(input("enter the num"))
# print(var_1)

# a=int(input("enter the num"))
# b=20
# if a in b:
#     print("True")
# else:
#     print("False")

# list1=["pooja","school","college"]
# i=0
# while i<len(list1):
#     if "pooja" in list1[i]:
#         print("yes")
#     else:
#         print("no")
#     i=i+1

# a=input("enter the name")
# print(a[-1])

# a=int(input("enter the num"))
# b=a%10
# print(b)

# sentence=input("enter the words")
# for letter in sentence:
#     if letter in "aious":
#         print("vowel","letter")
# for letter in sentence:
#     if letter not in "aious":
#         print("constant","letter")

# num=int(input("enter the length"))
# num2=int(input("enter the width")),
# parameter=2(num*num)
# print(parameter)

# a=[5,6,8,9,10,43,33,67,2]
# i=0
# while i<len(a):
#     print(a[i])
#     i=i+2

# def numbers(num):
#         result=[[]]
#         for n in num:
#                 new_list=[]
#                 for index in result:
#                         for i in range(len(index)+1):
#                                 new_list.append(index[:i]+[n]+index[i:])
#                                 result=new_list
#         return result
# my_nums=[1,2,3]
# print("original collection:",my_nums)
# print("collection of numbers:\n",numbers(my_nums))

# numbers=[]
# for num in range(1000):
#         num=str(num).zfill(3)
# print(num)
# numbers.append(num)

# for i in range(1,101):
#         print(i,100,sep="  ")

# import platform as pl
# os_profile=[
#         "architecture",
#         "linux_distribution",
#         "mac_ver",
#         "machine",
#         "node",
#         "plateform",
#         "processor",
#         "python_build",
#         "python_compiler",
#         "python_version",
#         "release",
#         "system",
#         "uname",
#         "version",
#     ]
# for key in os_profile:
#         if hasattr(pl,key):
#                 print(key+ ": "+str(getattr(pl,key)()))

# user=input("enter the word")
# if user==user:
#         print(user+"ing"+"ly")
# elif  user=="ing":
#         print(user+"ly")
# elif user=="ly":
#         print(user+"ing")
# if user==user:
#         print(user+"ing"+"ly")
# else:
#         print("word")   


# num=int(input("enter the first num"))
# num2=int(input("enter the second num"))
# num3=int(input("enter the third num"))
# if num>num2>num3  :
#     print(num,"greater num")
# elif num2>num3>num  :
#     print(num2, "greater num")
# elif num3>num2>num :
#     print(num3, "greater num")
# else:
#     print("no greater num")

# num=int(input("enter the num"))
# rev=0
# while (num>0):
#         rev=(rev*10)+num%10
#         num=num//10
# print("reverse",rev)

# name=["m","a","d","a","m"]
# rev=1
# x=name
# y=[]
# while (rev<=len(name)): 
# # while(name>0):
#         r=(name[-rev])
#         y.append(r)
#         rev=rev+1
# print(y)
# if y==name:
#         print("palindrome")
# else:
#         print("not palindrome")

# k=1
# i=1
# while(i<=5):
#         a=1
#         while(a<=i):
#                 print(a,end=" ")
#                 k=k+1
#                 a=a+1
#         print()
#         i=i+1

# num=[[4,3,5,6,8,9],[1,7,12,14,18]]
# i=0
# y=[]
# j=[]
# while i<len(num):
#         k=0 

#         while k<len(num[i]):
#                 a=num[i][k]
#                 if a%2==0:
#                      a.append(y)
#                 else:
#                      a.append(j)
#         i=i+1
# print("even num",y)
# print("odd num",j)

# [list(map(lambda x:"odd" if x%2!=0 else "even",i))for i in num]

# even=[]
# odd=[]
# num_list=[]
# for i in range (len(num)):
#         if num[i]%2==0:
#                 even.append(num_list[i])
#         else:
#                 odd.append(num_list[i])
# print(even)
# print(odd)

# for element in num:
#         for item in element:
#                 if item%2==0:
#                         num[element][x]="even"
#                 else:
#                         num[element][x]="odd"
#                 x+=1

# dict={"name":"pooja","age":"20"}
# for i in dict:
#         print(dict[i],":",i)

# dict={"A":[1,12,13],"B":[23,13,17]}
# for i in dict:
#         for j in range(len(dict[i])):
#                 print(dict[i][j])
#                 break

# sum1=0
# num=int(input("enter the number"))
# temp=num
# while(num):
#         i=1
#         f=1
#         r=num%10
#         while(i<=r):
#                 f=f*i
#                 i=i+1
#         sum1=sum1+f
#         num=num//10
# if(sum1==temp):
#         print("num is a strong num")
# else:
#         print("num is not strong num")

# name=["pooja","singh","priyanka","sharma"]
# i=0
# while i<len(name):
#         if name[i]%2==0:
#                 print(name[i])
#         else:
#                 print(name[i])
#         i=i+1


# food=input("enter the food name")
# if food=="gulabjamun":
#         print("eat")
# else:
#         print("no eat")
# if food=="namkeen":
#         print("wow")
# else:
#         print("crying")

# char_list=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
# i=0
# a=[]
# while i<len(char_list):
#     j=0
#     count=0
#     b=[]
#     while j<len(char_list):
#         if char_list[i]==char_list[j]:
#             count+=1
#         j+=1
#     b.append(char_list[i])
#     b.append(count)
#     if b not in a:
#         a.append(b)
#     i=i+1
# print(a)

# a = ['aaadfghjhfdrftyuikjnvc','prity','neha','aaaaaaaa']
# # output = ['aaaaaaa']

# i=0
# k=[]
# length=0
# while i<len(a):
#         if len(a[i])>length:
#            length=len(a[i])
#            j=a[i]
#         i=i+1
# k.append(j)
# print(k)


# i=0
# k=[]
# while i<len(a):
#     j=a[i]
#     # if j > k:
#     if type(a[i])==str:
#         k.append(j)
#     i=i+1
# print(j)

# a = "prity"
# a=[1,1,2,3,4,2,6,2,3,1,1,]
# output : {p:0,r:1,i:2,t:3,y:4}

# i=0
# k={}
# length=0
# while i<len(a):
#     if len(a[i])==length:
#         length=len(a)
#         j=a[i]
#     i=i+1
# k.append(j)
# print(j)

# a = "prity"
# # output : {p:0,r:1,i:2,t:3,y:4}

# i=0
# k={i}
# while i<len(a):
#     j=0
#     count=0
# #     length=0
#     while j<len(a):
#         if a(len[i])==a:
#             count+=1
#         j+=1
#     # b.append(a[i])
#     k.append(count)
#     if k not in a:
#         a. append(k)
#     i=i+1
# print(k)


# num=int(input("enter the number:-"))
# first=num%10
# second=(num//10)%10
# third=(num//100)%10
# fourth=(num//1000)%10
# reverse=(first*1000)+(second*100)+(third*10)+(fourth*1)

# if num>1000:
#         print(reverse)
# else:
#         print("error")



# num=int(input("enter the number:"))
# num1=int(input("enter the secound number:"))
# num2=int(input("enter the third number:"))
# if num>num1:
#         print(num)
# if (num1<num2):
#         print(num1)
# else:
#         print("fghj")
# if num2<num:
#         print(num2)
# else:
#         print("df")

a=2
b=str(a)
print(b)
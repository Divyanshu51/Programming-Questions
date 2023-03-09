'''sqaure root'''
#a=float(input("Enter no"))
#n=a**0.5
#print('the sqaure root of %0.3f is %0.3f'%(a,n))

'''quadratic question'''
#import cmath
#a=int(input("Enter for a:"))
#b=int(input("Enter for b:"))
#c=int(input("Enter for c:"))
#dis=((b*b)-(4*a*c))
#root1=(-b-cmath.sqrt(dis))/(2*a)
#root2=(-b+cmath.sqrt(dis))/(2*a)
#print(root1)
#print(root2)

'''swap two variables'''
#print("Enter two values respectively:\n")
#a=int(input())
#b=int(input())
#c=a 
#a=b 
#b=c 
#print("After Swapping",a)
#print("After Swapping",b)


#generate a random number
# number of elements
#import random
#n = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function
#a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

#print("\nList is - ", a)
#print("random number:",random.choice(a))
#list input method of taking ls=[]
#n=int(input("Enter the number of elements"))
#for i in range(0,n):
    # ele=int(input())
    #ls.append(ele)
#print(ls)

#leap year
#year=int(input("Enter year:"))
#if(year%400==0 and year%100==0):
    #print("{0} is leap year".format(year))
#elif(year%400==0 and year%100!=0):
    #print("{0} is a format leap year".format(year))
#else:#
    # print("{0} is not a  leap year".format(year))
    
#fact program
#def factorial(n):
    #if (n==0 or n==1):
       # return 1 
   # else:
        #return n*factorial(n-1)
        
'''Driver code'''
#n=int(input("Enter no"))
#print("fac of",n,"is",factorial(n))    

'''fibonnaci using recursion'''
#def fibonnaci(n):
    #if n<0:
        #print("incorrect output")
    #elif n==0:
       # return 0 
    #elif n==1 or n==2:
       # return 1
    #else:
       # return #fibonnaci(n-1)+fibonnaci(n-2)

'''Driver code'''
#n=int(input("Enter the number:\n"))
#print("fibonnaci of",n,"is",fibonnaci(n))

'''multiplication table'''
#n=int(input("Enter the no for which table has to be shown"))
#print("multiplication of the given no:\n")
#for i in range(1,11):
   # print(num,'x',i,'=',num*i)
   
   
'''display calendar'''
#import calendar 
#year=int(input("Enter the year:\n"))
#print(calendar.calendar(year))


'''armstrong number'''
#num=int(input("Enter the number to be checked:\n"))
#sum=0 
#temp=num 
#while temp >0:
    #digit= temp%10 
    #sum +=digit **3 
    #temp //=10 

#if num==sum:
    #print(num,"it is an armstrong number")
#else:
  #  print(num,"not an armstrong number")
'''for interval just run the for loop for i in range(lower,upper+1)for above code '''


'''ascii value using ord function'''
#v=input()
#print("Ascii value is:\n",ord(v))

'''add of two array'''
#import numpy as np
#a=int(input("Enter number of rows:\n"))
#b=int(input("Enter number of column:\n"))
#print("Enter numbers:\n")
#matrix_a=[[int(input("Enter numbers")) for i in range(b)]for i in range(a)]
#print("First matrix is:\n")
#for n in matrix_a:
    #print(n)
    
#print("Enter second matrix:\n")
#matrix_b=[[int(input("enter numbers"))for i in range(b)]for i in range(a)]
#print("elements of matrix_b:\n")
#for n in matrix_b:
    #print(n)
#matrix_a=np.array(matrix_a)
#matrix_b=np.array(matrix_b)
#result=np.add(matrix_a,matrix_b)
#print("Resultant matrix:\n")
#for r in result:
   # print(r)
   

''''Transpose of a matrix'''
#import numpy as np
#a=int(input("Enter number of rows:\n"))
#b=int(input("Enter number of column:\n"))
#print("Enter numbers:\n")
#matrix_a=[[int(input("Enter numbers")) for i in range(b)]for i in range(a)]
#print("First matrix is:\n")
#for n in matrix_a:
    #print(n)
#matrix_a=np.array(matrix_a)
#print(matrix_a.T)


'''multiplication of a matrix'''
#import numpy as np
#a=int(input("Enter number of rows:\n"))
#b=int(input("Enter number of column:\n"))
#print("Enter numbers:\n")
#matrix_a=[[int(input("Enter numbers")) for i in range(b)]for i in range(a)]
#print("First matrix is:\n")
#for n in matrix_a:
   # print(n)
    
#d=int(input("Enter number of rows:\n"))
#c=int(input("Enter number of column:\n"))
#print("Enter second matrix:\n")
#matrix_b=[[int(input("enter numbers"))for i in range(c)]for i in range(d)]
#print("elements of matrix_b:\n")
#for n in matrix_b:
    #print(n)
#matrix_a=np.array(matrix_a)
#matrix_b=np.array(matrix_b)
#result=np.dot(matrix_a,matrix_b)
#print("result matrix:\n")
#for r in result:
    #print(r)
    

'''sort alphabet without using sort() function'''
#print("Enter the string: ", end="")
#st=input()
#str_len=len(st)
#for i in range(str_len):
    #for j in range(str_len-1):
       # if st[j]>st[j+1]:
           # st=st[:j]+st[j+1]+st[j]+st[j+2:]
#print("Sorted alphabet is:",st)

'''to count no of vowels'''
#def count(string,vowels):
    #l=[each for each in string if each in vowels]
    #print(len(l))
   # print(l)

#string=input("Enter the String:")
#vowles="AEIOUaeiou"
#count(string,vowles)

'''to count no of each vowel'''
#st=input("Enter string:")
#st=st.casefold()
#count={x:sum([1 for char in st if char==x])for x in 'AEIOUaeiou'}
#print(count)

'''tp access index of a list using for loop'''
#list=["apple","banana","grapes"]
#for i in enumerate(list):
   # print(i)


'''pyramid pattern'''
#n=int(input("Enter no of rows:"))
#for i in range(n):
   # for j in range(i+1):
       # print("* ",end="")
   # print("\n")

'''right-angled triangle'''
#print("Enter the side to be checked with space in between:\n")
#s=map(int,input().split())
#x,y,z=sorted(s)
#if x**x+y**y==z**z:
    #print("It is a right-angled Triangle")
#else:
    #print("It is not right-angled Triangle")

'''sort a dictionary by value'''
#def dictionary():
    #key_val={}
    #giving values
    #key_val[4]=[45]
    #key_val[3]=[9]
    #key_val[2]=[100]
   # key_val[1]=[1]
    #print("key values are:",key_val)
    #for i in sorted(key_val.keys()):
       # print(i,end="")
#def main():
    #dictionary()
#if __name__=="__main__":
    #main()
'''to check a list is empty'''
#def enquiry(list):
    #if len(list)==0:
        #return 0 
    #else:
        #return 1 
    
#Driver code
#list=[]
#if enquiry(list):
    #print ("Not Empty")
#else:
    #print("Empty")

'''if  a key is present in a dictionary'''
#def check(dic, key):
     
    #if key in dic:
       # print("Present, ", end =" ")
       # print("value =", dic[key])
    #else:
        #print("Not present")
 
# Driver Code
#dic = {'a': 100, 'b':200, 'c':300}
 
#key = 'c'
#check(dic, key)
 
#key = 'w'
#check(dic, key)


'''get substring of a string'''
#st=input("Enter the string:\n")
#print(st)
#print()
#first=st[::2]
#ast=st[::3]
#print("from firs position",first)
#print("from last position",last)


'''count an occurence of an element in a list'''
#def countX(lst,x):
    #return lst.count(x)


#lst=list(map(int,input().split()))
#x=int(input("Enter the no to  be seacrhed"))
#print("{} has occured {} times".format(x,countX(lst,x)))


'''measure elapsed time in python'''
#import time 
#start=time.time()
#print(23*2.3)
#end=time.time()
#print(end-start)

'''print colored text to terminal'''
#import colorama
#from colorama import Fore
#print(Fore.red +"this has red color")

#from colored import fg
#color = fg('blue')
#print (color + 'Hello World !!!')




    
















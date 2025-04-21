#1.3D Prime Number

# n=int(input("Enter any num"))
# res=[]
# a=1
# def is_prime(a):
#     if(a==1):
#         return False
#     for i in range(2):
#         if(a%i == 0):
#             return False
#     return True
# def sum_dig(a):
#     sum =0
#     while(a!=0):
#         sum +=a%10
#         a //= 10
#     return sum
# def num_dig(a):
#     count = 0
#     for i in (a):
#         count +=1
# while(len(res)!=n):
#     if(is_prime(a)):
#         s=sum_dig(a)
#         total=num_dig(a)
#         if(is_prime(s) and is_prime(total)):
#             res.append(a)
#         a=a+1
# print(res)

#2.CO PRIME TRIPLET
#3.Company Question
#4.Password Checker

# n=input("Enter any password")
# dg=0
# sp=0
# up=0
# lo=0
# if(len(n)>7):
#     for i in n:
#         if(i.isupper()):
#             up=up+1
#         elif(i.islower()):
#             lo=lo+1
#         elif(i.isdigit()):
#             dg=dg+1
#         else:
#             sp=sp+1
#     if(up>0 and lo>0 and dg>0 and sp>0):
#         print("Strong password")
#     else:
#         print("Weak password")
# else:
#     print("Weak password due to less number")

#
# a=[[2,3,1,4,5,6,7],
#    [3,4,2,7,1,4,8],
#    [8,3,1,7,8,3,5],
#    [6,2,8,4,5,2,1],
#    [4,6,2,1,8,5,6]]
# top=0
# buttom=len(a)-1
# left=0
# right=len(a[0])-1
# while(left<=right and top<=buttom):
#     for i in range(left, right+1):
#         print(a[top][i])
#     top+=1
#     for i in range(top,buttom+1):
#         print(a[i][right])
#     right-=1
#     for i in range(right,left-1,-1):
#         print(a[buttom][i])
#     buttom-=1
#     for i in range(buttom,top-1,-1):
#         print(a[left][i])
#     left+=1
    
#Recursion
# def flower(a):
#     if(a==4):
#         return
#     print(a+10, end=" ")
#     flower(a+1)
#     print(a, end=" ")
# flower(1)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# n,m = map(int, input().split())
# c='-'
# s='.|.'
# for i in range(n//2):
#     print((s*((i*2)+1)).center(m, c))
# print("WELCOME".center(m, c))
# for i in range(n//2-1,-1,-1):
#     print((s*((i*2)+1)).center(m, c))

# ----------------------------------------------------------------------------------------------------------------------------------------
HACKERANK LOGO
# #Replace all ______ with rjust, ljust or center.
#
# thickness = int(input()) #This must be an odd number
# c = 'H'
#
# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#
# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))
#
# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
# -----------------------------------------------------------------------------------------------------------------------------------------
STRING VALIDATORS
# if __name__ == '__main__':
#     S = input()
#     print (any([char.isalnum() for char in S]))
#     print (any([char.isalpha() for char in S]))
#     print (any([char.isdigit() for char in S]))
#     print (any([char.islower() for char in S]))
#     print (any([char.isupper() for char in S]))
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# def listToString(s):
#     # initialize an empty string
#     str1 = ""
#     # traverse in the string
#     for ele in s:
#         str1 += ele
#     # return string
#     return str1
#
# def swap_case(s):
#     i=0
#     list=[]
#     for element in s:
#         if(element.isupper()):
#             list.append(element.lower())
#         elif(element.islower()):
#             list.append(element.upper())
#         elif (element.isspace() or element=="." or element=="''"):
#             list.append(element)
#             continue
#     s=listToString(list)
#     return s
#
#
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# def printLinkedList(head):
#     if head:
#         present=head
#         print(head + "22")
#
#     while(present):
#         print(present.data)
#         present=present.next
#         print(present + "22")
#
#
# if __name__ == '__main__':
#     llist_count = int(input())
#
#     llist = List()
#
#     for _ in range(llist_count):
#         llist_item = int(input())
#         llist.insert_node(llist_item)
#
#     printLinkedList(llist.head)




# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
TUPLES MAKING
# n = int(input())
# integer_list =[int(i) for i in input().split()]
# t=tuple(integer_list)
# print(hash(t))
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
LISTS IN PYTHON
# N = int(input())
# list=[]
#
# for i in range(N):
#     cmd = input().split()
#
#     if cmd[0] == "insert":
#         list.insert(int(cmd[1]), int(cmd[2]))
#     if cmd[0] == "print":
#         print(list)
#     if cmd[0] == "remove":
#         list.remove(int(cmd[1]))
#     if cmd[0] == "append":
#         list.append(int(cmd[1]))
#     if cmd[0] == 'sort':
#         list.sort()
#     if cmd[0] == "pop":
#         list.pop()
#     if cmd[0] == "reverse":
#         list.reverse()
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
FOR FINDING THE PERCENTAGE OF THE GIVEN STUDENT
# n=int(input())
# student_marks={}
# for i in range(n):
#     name, *line=input().split()
#     # print(name)
#     # print(line)
#     scores=list(map(float,line))
#     student_marks[name]=scores
# student_name=input()
# a=student_marks[student_name]
# # print(a)
# b=sum(a)/3
# # print(b)
# c=round(b,2)
# print("{0:.2f}".format(c))
# ---------------------------------------------------------------------------------------------------------------------------
NESTED LISTS IN PYTHON
# marksheet=[]
# marks=[]
# for i in range(int(input())):
#     name = input()
#     score = float(input())
#     marksheet +=[[name,score]]
#     marks += [score]
# # print(marks)
# # print(set(marks))
# # print(sorted(set(marks)))
# # print(marksheet)
# sl=(sorted(set(marks)))[1]
# # print(sl)
# for i,j in sorted(marksheet):
#     if j==sl:
#         print(i)
# --------------------------------------------------------------------------------------------------------------------------
FOR UNDERSTANDING THE SET FUNCTION
# lis1 = [ 3, 4, 1, 4, 5 ]
#
# # initializing tuple
# tup1 = (3, 4, 1, 4, 5)
#
# # Printing iterables before conversion
# print("The list before conversion is : "  +str(lis1))
# print("The tuple before conversion is : " +str(tup1))
#
# # Iterables after conversion are
# # notice distinct and elements
# print("The list after conversion is : " + str(set(lis1)))
# print("The tuple after conversion is : " + str(set(tup1)))

# -------------------------------------------------------------------------------------------------------------------------
FOR FINDING RUNNER UP SCORE
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     y=list(set(arr))
#     print(y)
#     print(len(y))
#     y.sort()
#
# # printing the last element
#     print( y[len(y)-2])

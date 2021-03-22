# week3 Files and 
# ===================================================
# C: fp = fopen
# python file_object = open(filename,mode) reading only('r'), riting('w'), append('a')
#
# close
# file_object.close()

# Write
# outfile = open('test.txt','w')
# outfile.write("dfdff")

# Read
# readFile = outfile.read()
# line1 = outfile.readline()

# 須自己移除換行符號
# rstrip
# line1 = line1.rstrip('\n')

# 只能寫 string 
# str(num1)
# outfile.write("This is num1: {}\n".format(num1)) #format裡面可放 list dic .... 更加方便

# 透過 while 處理
# line = sales_file.readline()
# while line != '':       #老師不喜歡用while
#     process()
#     line = sales_file.readline()
# sales_file.close()

# 透過 for 處理
# sales_file = open('sales.txt','r')
# for line in sales_file:     #逐行讀取
#     process()
# sales_file.close()




# Exceptions===================================================
# Exceptions 很重要，product 不能fail

# Exception: error that occurs while a program is running 
# Traceback: error messaege that gives inforation regarding line number

# ErrorExample
# n1 = int(input("N1:")) #10
# n2 = int(input("N2:")) #0
# res = n1/n2
# 10/0 ZeroDivisionError

# ===================================================
# Exception handler
# exceptionName => ValueError...
# try:
#     statements
# except exceptionName:
#     statements
#     print("....")

# ===================================================
# try:
#     print("..")
# except IOError:
#     print("..")
# except ValueError:
#     print("..")
# except Exception as e:                                  #好用
#     print("The exception {} occurs.".format(e))         #各種error都會執行，顯示exception是哪種, log, 好用

# ===================================================
# else
# 如果沒有error做else

# finally:

# ===================================================
# 好用流程
# def main():
#     success = True
#     try:
#         input
#     except Exception as e:                                  
#         print("The exception {} occurs.".format(e)) 
#         success = False

#     else:
#         do something
#     finally:
#         print('result')
# main()


# ===================================================
# pass it 能夠pass但該確認的還是要做(try except)

# def main():
#     success = True
#     try:
#         input
#     except Exception as e:                                  
#         pass


# ===================================================

# try:
#     f = open('file','r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# with open('file','r') as f:  #在能開的時候做 bt the 'with', the python will call the close() automatically
    # print(f.read())
# ===================================================
# List 能行 int, string, list, different types
# Numbers = list(range(5))
# Numbers = list(range(1,10,2))
# Numbers = list(range(1,10,2)*3)

# len
# len(list)

# List1=[1,2,3]
# List2=[1,2,3]
# List3 = List1 + List2

# list slicing
# Numbers = list(range(1,11))
# print(Numbers[1:3])   #[2,3]
# print(Numbers[:3])    #[1,2,3]
# print(Numbers[2:])    #[3,4,5...,10]
# print(Numbers[1:8:2]) #[2,4,6,8]
# print(Numbers[:-1])   #[1,2,3,...,9]
# print(Numbers[:-2])   #[1,2,3,...,8]
# print(Numbers[:])     #[1,2,3,...,10]

# ===================================================
# item in list 確認 item 是否有在 list 之內
# item not in list

# ===================================================
# append: 在結尾增加 item
# list.append(item)
# 如果沒找到會有error
# list.index(item)

# insert()
# sorted()
# remove() #remove item by item
# del list[i] # del by index

# ===================================================
# Copying  
# 
# 共用相同的空間，會一起改變
# list1 = [1,2,3,4]
# list2 = list1
# print(list1)
# print(list2)
# list1[0] = 99
# print(list1)
# print(list2)

# list1 = [1,2,3,4]
# list2 = []+list1
# ===================================================
# Two-dimensional List,     no dimension concept, you can put anything to the list

# b_array = [1,2,3,5]
# a = ["test",1]
# a.append(b_array)
# print(a)

# a[2][1] = "change"
# print(a)

# ===================================================
# Tuple: an immutable sequence 不能改變

# ===================================================
# ===================================================
# ===================================================
# ===================================================
# ===================================================

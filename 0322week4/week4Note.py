# ===============================
# a = "test"
# for ch in a:
#     print(ch)
# print(a[2])
# print(a[2]=='s')
# print(len(a))
# print(a + "dd")
# ===============================
# Strings is immutable 不可變更
# a[2] = 's'        #error
# ===============================
# String slice
# print(a[:2])
# print(a[:2] + "S" + a[3:])      變更特定字方式
# ===============================
# 能使用in 去確認字串中某字 p20
# string type 為 class
# a = "hello"
# print('ll' in a)
# print(type(a))
# print(a.isupper())
# print(a.islower())
# print(a.lstrip())
# file_name = "test.py"
# print(file_name.endswith('.py'))
# ===============================
# split
# inputS = "Bill:90"
# print(inputS.split(":"))
# t = "hello world"
# print(len(t.split(" ")))

# ===============================
# Dictionaries  dict = {key:value, key:value}   Value can put everything !!!!
# student = {"name":"Bill","score":90}
# print(student["name"])              #訪問   dict[name] = key
# student["id"] = 109                 #assigment on dict, add new item
# print(student)

# del student["id"]                   # delete
# print(student)
# print(len(student))
# print("name" in student)            #可用 in 去確認
# print("id" in student)
# ===============================
# list 可變更 不能當作key
# studen[[2,2]] = sss
# tuple 不可變更 則可以當作key
# studen[(2,2)] = sss

# ===============================
# test = dict()
# print(type(test))
# test["a"] = "hello"
# student = {"name":"Bill","score":90}
# student["id"] = 109                

# # for key in student:
#     # print(key)

# for key, value in student.items():              #更為方便的方式
#     print(key, value)
# print(student.get("name"))                      #使用 get 去獲取資料 當找不到時會回傳 nothing  而不會error
# print(student.get("nick_name", "not exist"))    #設定找不到時的回傳值
# ===============================
# Serializing objects pickle
import pickle
phonebook = [{'chris':999},{'kevin':555}]
with open('phonebook.dat','wb') as output_file:
    pickle.dump(phonebook,output_file)

with open('phonebook.dat','rb') as input_file:
    pb = pickle.load(input_file)
print(pb)
# ===============================
# ===============================
# ===============================
# ===============================
# ===============================
# ===============================
# ===============================
# ===============================
# ===============================
# ===============================
# ===============================
# ===============================
# ===============================

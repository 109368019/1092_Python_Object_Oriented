def main(student_list):
    print ("\n==== student list ====\n")
    for index in student_list:
        print("")
        print("Name: ",index["name"])
        for key, value in index["score"].items():
            print("subject {}, score: {}".format(key,value))

    print ("======================")

# student_list=[{'name': 'kevin', 'score': {'ch': 34,'en': 25}},{'name': 'jk', 'score': {'ch': 34,'math': 25}}]
# student_list = main(student_list)
# print(student_list)
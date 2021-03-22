def main(student_list):
    # print(student_list)
    name = input("Please input a student's name:")
    found = -1
    for index in range(len(student_list)):
        # print(student_list[index]["name"])
        if name in student_list[index]["name"]:
            found = index
            break

    if found == -1:
        print("The name {} is not found".format(name))
    
    else:
        del student_list[index]
        print("Del {} success".format(name))

    # print(student_list)
    return student_list






# student_list=[{'name': 'kevin', 'score': {'ch': 34,'en': 25}},{'name': 'jk', 'score': {'ch': 34,'math': 25}}]
# main(student_list)


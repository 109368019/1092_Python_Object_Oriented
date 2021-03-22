def main(student_list):
    try:
        name = input("  Please input a student's name: ")
        score = int(input("  Please input a student's score: "))
    except Exception as e:                                  
        print("try again") 
        student_list = main(student_list)
    else:
        print('name',name)
        print('score',score)
        student_list.append((name,score))
    # finally:
    #     print('fin',student_list)

    # try:
    #     student_list.append((name,score))
    # except:
    #     print("The exception {} occurs.".format(e)) 
    # # print(student_list)
    return student_list

# list1 = []
# list2 = main(list1)

# print('fin',list2)






def inputScore():
    try:
        score = int(input("  Please input a student's score: "))
    except Exception as e:                                  
        print("try again") 
        score = inputScore()
    return score
        
def main(student_list):
    det = True

    try:
        name = input("  Please input a student's name: ")
    except Exception as e:                                  
        print("try again") 
        main(student_list)
    else:
        for i in student_list:
            if name in i[0]:
                score = inputScore()
                index = student_list.index(i)
                student_list.remove(i)
                student_list.append((name,score))
                det = False
                break
            
        if det:
            print("The name {} is not found".format(name))
            main(student_list)
            

    return student_list



# list1 = [('ke',100),('er',100)]

# print(list1.index(('ke',100)))
# list1.remove(('ke',100))
# print(list1)
# list2 = main(list1)
# print('liet',list2)
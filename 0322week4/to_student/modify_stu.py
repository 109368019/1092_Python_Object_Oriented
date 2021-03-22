def main(student_list):
    print(student_list)
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
        subjectname_list = []
        for subjectname in student_list[index]["score"].keys():
            subjectname_list.append(subjectname)
        print("current subjects are {} ".format(subjectname_list))
        
        student_list = change_subject(student_list,name,index)
    return student_list

def change_subject(student_list,name,index):
    subject_name = input("  Please input a subject you want to change:")
    if subject_name == 'exit':
        return student_list
    try:
        if subject_name in student_list[index]["score"]:
            # print("find")
            score = int(input("Please input {} {} new score: :".format(name+"'s",subject_name)))
            if score < 0:
                return student_list
        else:
            score = int(input("Add a new subject for {} please input {} score or < 0 for discarding the subject:".format(name,subject_name)))
            if score < 0:
                return student_list
            # print("Add a new subject for {} please input {} score or < 0 for discarding the subject: -1".format(name,subject_name))
    except Exception as e:                                  
        print(e) 
        # student_list = main(student_list)
    else:
        student_list[index]["score"][subject_name] = score
        print('Modify {} {} {} success'.format(name, subject_name , score))
        return student_list

    # print(student_list)
    return student_list




# student_list=[{'name': 'kevin', 'score': {'ch': 34,'en': 25}},{'name': 'jk', 'score': {'ch': 34,'math': 25}}]
# student_list = main(student_list)
# print(student_list)


























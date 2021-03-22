def main(student_list):
    # print(student_list)
    name = input("Please input a student's name:")
    score_dict = dict()
    score_dict = add_subject(student_list,name,score_dict)
    # print("score_dict",score_dict)

    student_list.append({"name":name,"score":score_dict})
    print("Add {} success".format({"name":name,"score":score_dict}))
    # print("ff",student_list)s
    return student_list

def add_subject(student_list,name,score_dict):
    subject_name = input("  Please input a subject name or exit for ending:")
    if subject_name == 'exit':
        # print('exit',score_dict)
        return score_dict
    try:
        score = int(input("Please input {} {} score or < 0 for discarding the subject:".format(name+"'s",subject_name)))
        if score < 0:
            score_dict = add_subject(student_list,name,score_dict)
            return score_dict
    except Exception as e:                                  
        print(e) 
        # student_list = main(student_list)
    else:
        score_dict[subject_name] = score
        score_dict = add_subject(student_list,name,score_dict)

    return score_dict


# student_list=[]
# student_list = {"name":"kevin","score":{"ch":30,"eng":60}}
# main(student_list)















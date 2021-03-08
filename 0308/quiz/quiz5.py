import random

def main():
    init_val = 0
    end_val = 100
    ans = guessing()
    correct_flag = True
    count = 0
    while correct_flag:
        value = int(input('Please guess a number from:{} to {} : '.format(init_val,end_val)))
        if value < end_val and value > init_val:
            if value > ans:
                end_val = value
                count += 1 

            if value < ans:
                init_val = value
                count += 1 

            if value == ans:
                print("You passed")
                break
            if count > 6:
                print("Achieve limitted")
                break
def guessing():
    ans = random.randint(0,100)
    print(ans)
    return ans


# main()

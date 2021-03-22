def main():
    value = int(input('Please enter a value: '))

    for i in range(value,0,-1):
        print("*"*i)

    for i in range(1,value):
        print("*"*(i+1))

# main()

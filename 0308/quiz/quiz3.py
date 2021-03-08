def main():
    value = int(input('Please enter odd value: '))

    if value/2 > value//2:
        for i in range(value,0,-2):
            space = i//2        
            print("{}{}{}".format(" "*space,"*"*(value-(2*space))," "*space))

        for i in range(2,value,2):
            space = i//2        
            print("{}{}{}".format(" "*space,"*"*(value-(2*space))," "*space))
    else:
        main()



# main()

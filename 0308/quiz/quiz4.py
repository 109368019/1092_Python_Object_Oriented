def main():
    rows = int(input('Number of rows: '))
    colume = int(input('Number of colume: '))
    size = int(input('Grid size: '))

    for i in range(rows+1):
        print("{}{}".format(("+"+"-"*size)*colume,"+"))
        if(i == rows):
            break
        for i in range(size):
            print("{}{}".format(("|"+" "*size)*colume,"|"))



# main()

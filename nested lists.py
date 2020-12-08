if __name__ == '__main__':
    n=int(input())
    list1=[]
    for i in range(n):
        name = input()
        score = float(input())
        list1.append([name, score])
        list1.sort()
    
    second= sorted(list(set(marks for name, marks in list1)))[1]
    for i in range(n):
        if list1[i][1]==second:
            print(list1[i][0])
            

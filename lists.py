if __name__ == '__main__':
    N = int(input())
    list1=[]
    for i in range(N):
        cmd=input().split()
        command=cmd[0]
        if command=="insert":
            index=int(cmd[1])
            number=int(cmd[2])
            list1.insert(index,number)
        elif command=="append":
            index=int(cmd[1])
            list1.append(index)
        elif command=="remove":
            index=int(cmd[1])
            list1.remove(index)
        elif command=="sort":
            list1.sort()
        elif command=="pop":
            list1.pop()
        elif command=="reverse":
            list1.reverse()
        elif command=="print":
            print(list1)

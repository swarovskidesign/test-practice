num = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

def index(num):

    for i in range(len(num)):

        if num[i] == 1:
            return i
        
    return -1

index = index(num)

print(index)
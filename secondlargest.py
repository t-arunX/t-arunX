def sl(array):
    count = 0
    for k in range(len(array)):
        for j in range(len(array) - k-1):
            if (array[j] > array[j + 1]):
                # print(let[j])
                array[j], array[j + 1] = array[j + 1], array[j]
            else:
                count+=1
    return array[-2]

def sll(array):
    element = 0
    scnd = 0
    for l in range(len(array)-1):
        if(array[l] > array[l+1]):
            element = array[l]

    for m in range(len(array)-1):
        if(array[m]>scnd and array[m] < element):
            scnd = array[m]
    return scnd

n = int(input())
lst = list()
for i in range(n):
    lst.append(sl(list(map(int, input().split()))))
for i in lst:
    print(i)


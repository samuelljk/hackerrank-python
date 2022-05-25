from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())

#n adalah input
if 1<=n<=150:
    listA = [i+1 for i in range(n)]
    a = ""
    for i in listA:
        a += str(i)
    print(a)

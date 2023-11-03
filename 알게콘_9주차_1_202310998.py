s = [17, 92, 18, 33, 58, 7, 33, 42]
n = len(s)

x = int(input("찾으려고 하는 값을 입력하세요: "))

for i in range(0, n, 1):
    if x == s[i]:
        print("찾으려고 하는 값은", x, "이며 인덱스 값은", i, "이며 위치는", i+1, "입니다.")




def Sequential_Search(a,x):
    n = len(a)
    for i in range(0, n, 1):
        if x==a[i]:
            return i
    
    return -1

s = [17, 92, 18, 33, 58, 7, 33, 42]
print(Sequential_Search(s, 18))
print(Sequential_Search(s, 33))
print(Sequential_Search(s, 100))



def Sequential_Search2(a, x):
    alist = []
    n = len(a)
    for i in range(0, n, 1):
        if x==a[i]:
            alist.append(i)
    return alist

s = [17, 92, 18, 33, 58, 7, 33, 42]

print(Sequential_Search2(s, 18))
print(Sequential_Search2(s, 33))
print(Sequential_Search2(s, 100))



import random
import time

def Sequential_Search3(a, x):
    n = len(a)
    for i in range(0, n, 1):
        if x==a[i]:
            return i
        
s = random.sample(range(1, 1000001), 1000000)

start = time.time()
print(Sequential_Search3(s, 78))
print("time: ", time.time()-start)



def find_name(num, nolist, namelist):
    lens = len(nolist)
    result = "?"
    teamname = "?"

    for i in range(lens):
        if nolist[i] == num:
            result = namelist[i]
            if i%2 != 0:
                teamname = "blackpink"
            else:
                teamname = "newjeans"

    return result, teamname

stu_no = [39, 14, 67, 105, 32, 27,  100, 55, 3]
stu_name = ["민지", "로제", "하니", "제니", "다니엘", "지수", "혜린", "리사", "혜인"]

while True:
    print(stu_no)
    a = int(input("학생 번호를 입력하세요. (-1은 끝내기): "))

    if a != -1:
        print(find_name(a, stu_no, stu_name))

    else:
        break




def find_name(num, nolist, namelist):
    global girlgroup_list
    lens = len(nolist)
    result = "?"
    teamname = "?"

    for i in range(lens):
        if nolist[i] == num:
            result = namelist[i]
            if i%2 != 0:
                teamname = girlgroup_list[0]
            else:
                teamname = girlgroup_list[1]

    return result, teamname

girlgroup_list = ["blackpink", "newjeans"]

stu_no = [39, 14, 67, 105, 32, 27,  100, 55, 3]
stu_name = ["민지", "로제", "하니", "제니", "다니엘", "지수", "혜린", "리사", "혜인"]

while True:
    print(stu_no)
    a = int(input("학생 번호를 입력하세요. (-1은 끝내기): "))

    if a != -1:
        print(find_name(a, stu_no, stu_name))

    else:
        break
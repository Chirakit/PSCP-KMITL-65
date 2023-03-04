'''classify'''
def classify():
    '''_'''
    num = input()
    data, allyears = [], []
    while num != 'END':
        temp = [int(num[:2]), int(num[2:4]), int(num[4:])]
        if int(num[:2]) not in allyears:
            allyears.append(int(num[:2]))
        data.append(temp)
        num = input()
    data.sort()
    allyears.sort()
    result = []
    for yearsrun in allyears:
        currentyear = []
        for j in data:
            if j[0] == yearsrun:
                temp1 = [j[1], j[2]]
                currentyear.append(temp1)
        all_faculty = []
        all_faculty_no_dup = []
        for i in currentyear:
            all_faculty.append(i[0])
            if i[0] not in all_faculty_no_dup:
                all_faculty_no_dup.append(i[0])
        first_line = True
        for i in all_faculty_no_dup:
            count = all_faculty.count(i)
            if first_line:
                block1 = yearsrun
                first_line = False
            else:
                block1 = '--'
            result.append([block1, i, count])
    for i in result:
        print(*i, sep=' ')

classify()

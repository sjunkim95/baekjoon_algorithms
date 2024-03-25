import sys
input = sys.stdin.readline
gpa_list = []
score_list = []

for i in range(20):
    subject, unit, gpa = sys.stdin.readline().split()
    score_list.append(float(unit))
    if gpa == 'A+':
        gpa_list.append(4.5*float(unit))
    elif gpa == 'A0':
        gpa_list.append(4.0*float(unit))
    elif gpa == 'B+':
        gpa_list.append(3.5*float(unit))
    elif gpa == 'B0':
        gpa_list.append(3.0*float(unit))
    elif gpa == 'C+':
        gpa_list.append(2.5*float(unit))
    elif gpa == 'C0':
        gpa_list.append(2.0*float(unit))
    elif gpa == 'D+':
        gpa_list.append(1.5*float(unit))
    elif gpa == 'D0':
        gpa_list.append(1.0*float(unit))
    elif gpa == 'F':
        gpa_list.append(0)
    elif gpa == 'P':
        continue
    
print(sum(gpa_list)/sum(score_list))

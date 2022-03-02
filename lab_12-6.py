# Author: MOG 1/3/22

grades = {"End S1 Labs":100, "Start S2 Labs":100, "Mid-year Project Proposal":100, "Cycle 10 Practice Quiz":100, "Cycle 10 Quiz":100}

print(grades)

for g in grades:
    print(g)

for g, i in grades.items():
    if i >= 70:
        print(g, i)

for g, i in grades.items():
    if i >= 50:
        print(g, i)

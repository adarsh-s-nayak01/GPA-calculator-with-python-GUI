e0=input('Enter your Name :')
e1=input('Enter your SRN :')
e2=input('Enter your Roll.No:')
e3=input('Enter your Registration.No:')

print('------Enter the marks obtained in all the exams conducted--------')
print('------The total marks of ISA-1 is 60, ISA-2 is 40, ESA is 100------')


print('Engineering Mathematics: Subject Code:MA-101')
m1=int(input('MA-101(ISA-1):'))
m2=int(input('MA-101(ISA-2):'))
m3=int(input('MA-101(ESA):'))

if (m1>60)or(m2>40)or(m3>100):
    print('---invalid input! # Marks obtained cannot be greater than total marks')
    exit()


print('Electronic principles and devices: Subject Code:EC-101')
ec1=int(input('EC-101(ISA-1):'))
ec2=int(input('EC-101(ISA-2):'))
ec3=int(input('EC-101(ESA):'))

if (ec1>60)or(ec2>40)or(ec3>100):
    print('---invalid input! # Marks obtained cannot be greater than total marks')
    exit()


print('Engineering Chemistry: Subject Code: CY-101')
c1=int(input('CY-101(ISA-1):'))
c2=int(input('CY-101(ISA-2):'))
c3=int(input('CY-101(ESA):'))

if (c1>60)or(c2>40)or(c3>100):
    print('---invalid input! # Marks obtained cannot be greater than total marks')
    exit()


print('Python for Computational Problem Solvimg: Subject Code : CS-101')
p1=int(input('CS-101(ISA-1):'))
p2=int(input('CS-101(ISA-2):'))
p3=int(input('CS-101(ESA):'))

if (p1>60)or(p2>40)or(p3>100):
    print('---invalid input! # Marks obtained cannot be greater than total marks')
    exit()


print('Engineering Mechanics-Statics : Subject Code : CV-101')
t1=int(input('CV-101(ISA-1):'))
t2=int(input('CV-101(ISA-2):'))
t3=int(input('CV-101(ESA):'))

if (t1>60)or(t2>40)or(t3>100):
    print('---invalid input! # Marks obtained cannot be greater than total marks')
    exit()


print('Constituion,Cyber law and Professional Ethics : Subject Code : CE-101')
r1=int(input('CE-101(ISA-1):'))
r2=int(input('CE-101(ISA-2):'))
r3=int(input('CE-101(ESA):'))

if (r1>60)or(r2>40)or(r3>100):
    print('---invalid input! # Marks obtained cannot be greater than total marks')
    exit()


m=(m1/60)*30+(m2/40)*20+(m3/100)*50

ec=(ec1/60)*30+(ec2/40)*20+(ec3/100)*50

c=(c1/60)*30+(c2/40)*20+(c3/100)*50

p=(p1/60)*30+(p2/40)*20+(p3/100)*50

t=(t1/60)*30+(t2/40)*20+(t3/100)*50

r=(r1/60)*30+(r2/40)*20+(r3/100)*50


l=[m,ec,c,p,t,r]
a=[]
for i in range(len(l)):
    if l[i]>=90:
        a.append("S")
    elif 80<l[i]<=90:
        a.append("A")
    elif 70<l[i]<=80:
        a.append("B")
    elif 60<l[i]<=70:
        a.append("C")
    elif 50<l[i]<=60:
        a.append("D")
    else:
        a.append("F")

G4=a[0]
G5=a[1]
G6=a[2]
G7=a[3]
G8=a[4]
G9=a[5]

print('Grade obtained in subjects :')
print('Engineering Mathematics :',a[0])
print('Electronic devices and principles :',a[1])
print('Engineering Chemistry :',a[2])
print('Python for Computational problem solving :',a[3])
print('Engineering mechanics-Statics :',a[4])
print('Constitution,Cyber law and professional ethics :',a[5])

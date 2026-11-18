"""s1 = "PYTHONPROGRAMMING"
print(s1[0:3])
print(s1[-1:-4:-1])
print(s1[2:8])
print(s1[0:18:+2])"""

name=input("Aharshi")
first=name[0:2]
last=name[-2:]
mid=name[2:-2]

first=first[::-1]
mid=mid[::-1]
last=last[::-1]

sub=first+mid+last
print(sub)
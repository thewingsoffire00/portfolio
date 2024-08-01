
# print(type(a))
# b=30
# k=20
# print(b+k)
# print(b-k)
# print(b*k)
# b="30"
# k="20"
# print(b*3)
# print(k*4)
# print(b+k)
# g='jijujichu'
# print(g)
# print(g[1])
# print(g[0])
# print(g[1:4])
# print(g[0:])
# print(g[0::2])
# print(len(g))
# li=["apple",44,"grape","orange"]
# print(li)
# print(li[2])
# li[2]="gfd"
# print(li)
# li.insert(1,"mango")
# print(li)
# li.append("rint")
# print(li)
# li.pop(3)
# print(li)
# li.remove("apple")
# print(li)

# t=("four","five")
# print(type(t))
# print(t[1])
# o=list(t)
# print(type(o))
# t=tuple(o)
# print(type(t))
# o.insert(0,"kevi")
# print(o)
# o.append("six")
# print(o)
# o.pop(2)
# print(o)
# o.remove("four")
# print(o)


# d={"hai":89,"red":90,"phone":95}
# print(d)
# d["ddd"]=787
# print(d)
# a=6
# if a<=5:
# 	print("hi")
# elif a==5:
# 	print("welcome")
# else:
# 	print("helo")

# 	o=8
# 	n=9
# 	h=10
# if o>n:
# 	print("o is greater")
# elif n>o:
#    print("n is greater")
# else:
#    print("h is greater")a=10


for i in range(10):
	print(i)

for i in range(2,8,2):
	print(i)




i=0
while i<6:
	print(i)
	i+=1


i=0
while i<6:
	print(i)
	if i==3:
		break
	i+=1

i=0
while i<6:
	i+=1
	if i==3:
		continue
	print(i)

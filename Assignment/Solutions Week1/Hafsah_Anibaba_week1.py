#for mean

a=[1,2,3,4,5,6,7,8,9]
b=len(a)
_sum=sum(a)
mean=_sum/b
print(mean)

#for median

a=[1,2,3,4,5,6,7,8,9]
b=len(a)
a.sort()
if b % 2==0:
    c=a[b//2]
    d=a[b//2-1]
    median=(c+d)/2
else:
    median=a[b//2]
    print(median)

#for mode



#paper,scissors and rock game
a=eval(input("enter player 1 hand shape"))
b=eval(input("enter player 2 hand shape"))
c=eval(input("enter player 3 hand shape"))  
e==scissors
s==paper
if a==b:
    print("replay")
elif a==e:
     b==s
     print("a wins b")
elif a==paper:
     b==rock
     print("a wins b")
else:
     print("b wins a")     
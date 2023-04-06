#Fibonacci serisi
# 1,1,2,3,5,8,13,21,34,....

a=1
b=1
fibonacci=[a,b]
for i in range(15):
    a,b=b,a+b
    fibonacci.append(b)

print(fibonacci)
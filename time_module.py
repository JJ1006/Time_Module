
import time
initial=time.time()#time at that particular time
print(initial)
k=0
while(k<5000):
    print("This is a legend")
    k=k+1
print("While loop ran in", time.time() - initial, "seconds")#prints the time taken by while loop

initial1=time.time()#time at that particular time
for i in range(5000):
    print("This is a legend")
print("For loop ran in", time.time() - initial1, "seconds")#prints the time taken by for loop

localtime =time.asctime(time.localtime(time.time())) #calculates the local time
print(localtime)#for local time 
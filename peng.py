x = 1
lr = 0.1 
threshold = 0.01
max_epoch = 1000

y = 2

def sign(x):
    if x>0:
        return 1
    else:
        return -1

for i in range(max_epoch):
    if abs(x**2 -y) <=threshold:
        print(x)
        break
    else:
        x-=lr* (x*2)* sign(x**2 -y)
        print(x) 

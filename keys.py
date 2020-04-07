import numpy as np
import time as tt

def enc():
    t=tt.time()
    t=t-int(t)
    t=t*0.01
    tr=hex(int(t*10**16))
    
    t = int(tr,16)/(10**16)
    

    s=10 + t*10
    r=28 + t*10
    b=2.667 + t
    xs=[0+t]
    ys=[1+t]
    zs=[1.05+t]

    dt = 0.01 + t
    num= 256*256*3+5
    for i in range(0,num):
        x_dot = s*(ys[i] - xs[i])
        y_dot = r*xs[i] - ys[i] - xs[i]*zs[i]
        z_dot = xs[i]*ys[i] - b*zs[i]

        xs.append(xs[i] + (x_dot * dt))
        ys.append( ys[i] + (y_dot * dt))
        zs.append(zs[i] + (z_dot * dt))
        
    xs=np.array(xs)
    ys=np.array(ys)
    zs=np.array(zs)
    xs=xs[5:num]
    ys=ys[5:num]
    zs=zs[5:num]
    


    for i in range(0,len(xs)):
        xs[i]=abs(xs[i]*1000-int(xs[i]*1000)) 
        ys[i]=abs(ys[i]*1000-int(ys[i]*1000))
        zs[i]=abs(zs[i]*1000-int(zs[i]*1000))
    np.save('static/c1.npy',xs)
    np.save('static/c2.npy',ys)
    np.save('static/c3.npy',zs)
    m=max(xs)
    m1=max(ys)
    m2=max(zs)
    for i in range(0,len(xs)): 
        xs[i]=round(abs((xs[i]/m)*14+1))          #diffusion
        ys[i]=round(abs((ys[i]/m1)*14+1))
        zs[i]=round(abs((zs[i]/m2)*14+1))         #diffusion
            #confusion
    np.save('static/d1.npy',xs)
    np.save('static/d2.npy',ys)
    np.save('static/d3.npy',zs)
    print(tr[2:])
    return tr[2:]

def dec(key):
    print(key)
    key= '0x'+key
    t = int(key,16)/(10**16)


    s=10 + t*10
    r=28 + t*10
    b=2.667 + t
    xs=[0+t]
    ys=[1+t]
    zs=[1.05+t]

    dt = 0.01 + t
    num= 256*256*3+5
    for i in range(0,num):
        x_dot = s*(ys[i] - xs[i])
        y_dot = r*xs[i] - ys[i] - xs[i]*zs[i]
        z_dot = xs[i]*ys[i] - b*zs[i]

        xs.append(xs[i] + (x_dot * dt))
        ys.append( ys[i] + (y_dot * dt))
        zs.append(zs[i] + (z_dot * dt))
        
    xs=np.array(xs)
    ys=np.array(ys)
    zs=np.array(zs)
    xs=xs[5:num]
    ys=ys[5:num]
    zs=zs[5:num]
    


    for i in range(0,len(xs)):
        xs[i]=abs(xs[i]*1000-int(xs[i]*1000)) 
        ys[i]=abs(ys[i]*1000-int(ys[i]*1000))
        zs[i]=abs(zs[i]*1000-int(zs[i]*1000))
    np.save('static/c1.npy',xs)
    np.save('static/c2.npy',ys)
    np.save('static/c3.npy',zs)
    m=max(xs)
    m1=max(ys)
    m2=max(zs)
    for i in range(0,len(xs)): 
        xs[i]=round(abs((xs[i]/m)*14+1))          #diffusion
        ys[i]=round(abs((ys[i]/m1)*14+1))
        zs[i]=round(abs((zs[i]/m2)*14+1))         #diffusion
            #confusion
    np.save('static/d1.npy',xs)
    np.save('static/d2.npy',ys)
    np.save('static/d3.npy',zs)






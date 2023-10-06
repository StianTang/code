import PyQt5

P_10=[3,5,2,7,4,10,1,9,8,6]
P_8=[6,3,7,4,8,5,10,9]
LShift_1=[2,3,4,5,1]
LShift_2=[3,4,5,1,2]
IP=[2,6,3,1,4,8,5,7]
IP_1=[4,1,3,5,7,2,8,6]
EP=[4,1,2,3,2,3,4,1]
S1=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,0,2]]
S2=[[0,1,2,3],[2,3,1,0],[3,0,1,2],[2,1,0,3]]
SP=[2,4,3,1]
def p10(K): #        p10
    key = ""
    for x in P_10:
        key = key + K[x - 1]
    return key

def k1_p8(key): #         左移1 与 p8            #得出密钥1
    key11 = key[:5]
    key12 = key[5:]
    key11=key11[1:]+key11[0]
    key12=key12[1:]+key12[0]
    k=key11+key12
    k1 = ""
    for x in P_8:
        k1 = k1 + k[x - 1]
    return k1

def k2_p8(key): #           左移2 与 p8     #得出密钥2
    key11 = key[:5]
    key12 = key[5:]
    key11 = key11[2:]+key11[:2]
    key12 = key12[2:]+key12[:2]
    k = key11+key12
    k2 = ""
    for x in P_8:
        k2 = k2 + k[x - 1]
    return k2

def ip( P ):        #IP
    p = ""
    for x in IP:
        p = p + P[x - 1]

    return p

def ip_1(P):   #IPfu1
    p = ""
    for x in IP_1:
        p = p + P[x - 1]
    #p1,p2=p[:4],p[4:]
    return p

def fk1(p,K):             #交换前fk()的left
    p1, p2 = p[:4], p[4:]
    m = ""
    for x in EP:
        m = m + p2[x - 1]
    print("EP",m)
    k1=k1_p8(p10(K))
    print("密钥",k1)
    m=yihuo(m,k1)
    print("异或",m)
    t1 = m[0]+m[3]
    t2 = m[1:3]
    t3 = m[4]+m[7]
    t4 = m[5:7]
    int1 = to_2_10(t1)
    int2 = to_2_10(t2)
    int3 = to_2_10(t3)
    int4 = to_2_10(t4)
    r1,r2 = S1[int1][int2],S2[int3][int4]
    print("box",r1,r2)
    r1,r2 = to_10_2(r1), to_10_2(r2)
    print("box2", r1, r2)
    r = r1+r2
    r = sp(r)
    print("置换sp",r)
    le = yihuo(r,p1)
    print("异或",le)
    return le

def swap(a,b):           #   交换left right
    x = b+a
    return x

def fk2(p,K):            #   交换前fk()的left
    p1, p2 = p[:4], p[4:]
    m = ""
    for x in EP:
        m = m + p2[x - 1]
    k2=k2_p8(p10(K))
    print("k2",k2)
    m=yihuo(m,k2)
    t1 = m[0] + m[3]
    t2 = m[1:3]
    t3 = m[4] + m[7]
    t4 = m[5:7]
    int1 = to_2_10(t1)
    int2 = to_2_10(t2)
    int3 = to_2_10(t3)
    int4 = to_2_10(t4)
    r1,r2 = S1[int1][int2],S2[int3][int4]
    r1,r2 = to_10_2(r1), to_10_2(r2)
    r = r1+r2
    r = sp(r)
    le = yihuo(r,p1)
    return le

def to_2_10(x):
    i = len(x)
    j = 0
    y = 0
    while i > 0 :
        y = y+int(x[i-1])*2**j
        i = i-1
        j = j+1
    return y

def to_10_2( x ):
    y = ""
    while 1:
        y = str(int(x) % 2) + y
        x = int(x)//2
        if x == 0:
            y = str("{:02d}".format(int(y)))
            break
    return y

def to_10_2_8( x ):
    y = ""
    while 1:
        y = str(int(x) % 2) + y
        x = int(x)//2
        if x == 0:
            y = str("{:08d}".format(int(y)))
            break
    return y

def to_10_2_16( x ):
    y = ""
    while 1:
        y = str(int(x) % 2) + y
        x = int(x)//2
        if x == 0:
            y = str("{:16d}".format(int(y)))
            break
    return y
def sp(k):
    ke2 = ""
    for x in SP:
        ke2 = ke2 + k[x - 1]
    return ke2
def yihuo(x,y):        #异或
    len1=len(x)
    len2=len(y)
    z=""
    if len2 == len1:
        i = 0
        while i < len1:
            if x[i] != y[i]:
                z = z+"1"
            else:
                z = z+"0"
            i=i+1
    return z

# K = input("key:")
# key = p10(K)#1100011100
# k1=k1_p8(key)
# k2=k2_p8(key)
# print(k1,k2)#得出秘钥
def end(s,K):
    p = ip(s)
    k1 = fk1(p,K)
    q = swap(k1,p[4:])
    k2 = fk2(q,K)
    q=ip_1(k2+k1)
    print("end",q)
    return q

def over(s,K):
    p = ip(s)
    k1 = fk2(p, K)
    q = swap(k1, p[4:])
    k2 = fk1(q, K)
    q = ip_1(k2 + k1)
    print("over", q)
    return q

# q=end("01001110","0001101011")
# p=over(q,"0001101011")
# chinese_str = '中国'
# ascii_code = [ord(c) for c in chinese_str]
# print(ascii_code)





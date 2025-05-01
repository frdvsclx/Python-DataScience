#numpy: numeric python
#daha derin mat içeren kısımlarda kulanılır
#listeler her data için ayrı yer tutarken, numpy ise eger bırden fazla aynı cesıt data
# varsa bunu tek bı yere atar ve boylece daha fazla data tutabilir
#yüksek sevıye ıslemler yapar, vektorel

import numpy as np
#with normally:
a=[1,2,3,4,5]
b=[5,77,8,9,1]
ab=[]

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

print(ab) #output: [5, 154, 24, 36, 5] **usual array

#with numpy:
a= np.array([1,2,3,4])
b= np.array([4,5,6,7])
c= a*b #output: array([ 4, 10, 18, 28])
type(c)# ***numpy.ndarray

#creating numpy array
np.array([4,5,6,7])
type(np.array([4,5,6,7])) #-----> numpy.ndarray

np.zeros(5,dtype=int) #array with 5 int zeros ----> output: array([0, 0, 0, 0, 0])
np.ones(10) * 5 #array([5., 5., 5., 5., 5., 5., 5., 5., 5., 5.])
np.random.randint(0,10, 5) #0 ile 10(dahil deil) arası random 5 tane int üretir
np.random.normal(10,4,(2,3)) #ort 10 / standart sapması 4/ boyutu 2,3 olan dizi


A= np.random.randint(10,size=5)
A.ndim #boyut sayısını ifade eder (1,2,3) cıktı: 1
A.shape #boyutunu verir cıktı: (5,)
A.size #TOPLAM ELEMAN SAYISI cikti: 5
A.dtype #tipini belirtir cikti: dtype('int32')

np.random.randint(10,size=6).reshape(2,3) #reshape boyutu değiştirmeye yarar, 2boyutlu
ar= np.random.randint(2,5,4)

ar.reshape(2,2) #gibi de kullanılır, size=a.b olmalı reshape(a.b)
#bu sekılde kalıcı ılarak boyut degızsıtrmesı yapılabilir

#index işlemi:

a= np.random.randint(8,size=(3,4))
a[2,1] #2 mormalde a[2,3]=a ile atama işlemi yapılabilr
a[2,3] = 3,4 #dersek yine de 3 görünüür çünkü numpy tek tür veriyi saklar

a[:,0] #her satır , 0.sutun demektir
a[2,:] #2. satır, bütün sutun demektır
a[0:2,1:3] #

#fancy index:

m= np.arange(3,9,2) #3ten 9a kadar 2şer artan array olustur demektır array([3, 5, 7])

catch=[1,2]
m[catch] #istediğim indexleri verir

m>5 #array([False, False,  True])
m[m!=5] #array([3, 7])
m[m>=5] #array([5, 7])

#bazı işlemler

b= np.random.randint(2,10,6) #array([6, 6, 8, 8, 3, 7])
np.subtract(b,1) #hepsinden 1 cıkarır
np.add(b,4) #hepsine 5 ekler
np.mean(b) #ortalamsını alır 6.33333333333
np.sum(b) #toplamı
np.min(b) #min
np.max(b) #max
np.var(b) #varyansı= ortalamadan uzaklıgının ortalamsı 2.888888888888889

#bu işlemlerin kalıcı olmasını istiyorsak atama yaaorız
b= np.add(b,4) #artık yeni array bu array([10, 10, 12, 12,  7, 11])

#denklem çözme

d= np.random.randint(0,10,4) #array([8, 5, 4, 5])
e= np.random.randint(5,15,4)  #array([10,  9, 10,  7])

#denklem çözme:
k= np.array([[8,5],[4,5],[10,9],[10,7]]) #degıskenlerın katsayısı sırayla yazılır
l= np.array([67,43,45,32]) #denklem sonunclrı sırayla yazılır

np.linalg.solve(k,l) #array([ 17.63636364, -14.81818182]) x1 ve x2 bunlarmıs

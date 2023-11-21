import matplotlib.pyplot as plt
import astropy.io.fits as pyfits


hdulist = pyfits.open("/Users/User/PycharmProjects/pythonProject1/13/v523cas60s-001(1).fit")
scidata = hdulist[0].data

X1 = []
X2 = []
Y1 = [] #изменяем х
Y2 = []#изменяем у

x = int(input('введите координату звезды по оси Х'))
y = int(input('введите координату звезды по оси Y'))
r = int(input('радиус звезды в пикселях'))

for i in range(x-r, x+r):#записываем х
    Y1.append(scidata[y][i])
    temp = i
    X1.append(temp)
for i in range(y-r, y+r):
    Y2.append(scidata[i][x])
    temp = i
    X2.append(temp)

plt.figure() #создает полотно для нескольких графиков
plt.subplot(1, 2, 1) #создает области построения графиков на готовом полотне елим поле 2 на 2 и берем первый график
plt.title('                          Изменение светимости звезды от координаты')
plt.plot(X1, Y1)
plt.xlabel('Изменение координаты Х')
plt.ylabel('Значение энергии')
plt.subplot(1, 2, 2)
plt.plot(X2, Y2)
plt.xlabel('Изменение координаты Y')
plt.ylabel('Значение энергии')
plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()

hdulist.close()
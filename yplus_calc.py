import math;
import sys;


D = 0.3; # Длина хорды, м
ro = 1.225; # Плотность, кг/м^3
mu = 18.6e-6; # Динамическая вязкость
nu = 1.46e-5 # Кинематическая вязкость, м^2/с
H = 0; # Высота, м
T = 288.15; # Температура, К
a = 340.3; # Скорость звука, м/с
P = 101325; # Давление, Па
yplus = 1;
Cp = 1003.62; #
U = 41.3;
n = 35; # Число призматических слоев
k = 1.2
ks = 0

for i in range(n):
    ks += math.pow(k, i)


# Для справки: nu = mu / ro

Re = ro * D * U / mu; # Вычисление Рейнольдса
Cf = 1.328 / math.sqrt(Re);
#Cf = 0.078 / math.pow(Re, 1.0 / 5.0);
#Cf = 2.656 / math.sqrt(Re); # Коэффициент трения
tw = Cf * ro * U * U / 2; # Напряжения сдвига
uz = math.sqrt(tw / ro); # 
y = yplus * mu / (uz * ro); # высота ячейки у стенки



print("Число Рейнольдса", Re);
print("Скорость набегающего потока ", U, "м/с");
print("Коэффициент трения ", Cf);
print("Напряжения сдвига ", tw);
print("Скорость ", uz, "м/с");
print("Высота ячейки у стенки ", 2 * y, "м");
print("Высота призматического слоя ", 2 * y * ks, "м");
print("Высота призматического слоя по формуле ", 0.37 * D * math.pow(Re, -0.2), "м");


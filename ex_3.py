print("Ведите две координаты точки, x и y, и узнаете в какой четверти находится эта точка.")

x=0; y=0

while (x==0 and y==0):
    x = int(input('Введите число: '))
    y = int(input('Введите число: '))
    if x == 0 and y == 0:
        print(f'Точка ({x},{y}) находится в начале координат). Попробуйте еще разок')

if x > 0 and y > 0: z = 'I'
elif x < 0 and y > 0: z = 'II'
elif x < 0 and y < 0: z = 'III'
elif x > 0 and y < 0: z = 'IV'
print(f'Точка с координатам ({x},{y}) находится в {z}-й четверти ')
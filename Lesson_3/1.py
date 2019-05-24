# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

multiplicity = [0] * 8
for digit in range(2, 10):
    m = 0
    for number in range(2, 100):
        if number % digit == 0:
            m += 1
    multiplicity[digit-2] = m

for i in range(2, 10):
    print(f"Числу {i} кратны {multiplicity[i-2]} чисел в диапазоне от 2 до 99")

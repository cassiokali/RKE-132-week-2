goal = 1000
steps = int(input('Mitu sammu oled juba teinud?:'))

percent = (steps/goal) * 100
print(f'{percent}')

if percent < 50:
    print('Alles poolel teel, liigu edasi!')
elif percent < 75:
    print('Tubli, oled peaaegu kohal!')
else:
    print('Palju õnne, oled oma eesmärgi täitnud!')

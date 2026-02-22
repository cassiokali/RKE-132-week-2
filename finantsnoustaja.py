print('Tere tulemast programmi \'Finantsnõustaja\'!')
print('Sinu isklik nõustaja ei tee emotsionaalseid oste.')

money = int(input('Kui palju raha sul on praegu?'))

if money < 2500:
    print('Sul pole piisavalt raha. Ole kannatlik ja kogu edasi!')
elif money == 2500:
    print('Palju õnne, saad osta uue iPhone 17 Pro sularahas!')
else:
    print("Saad osta iPhone 17 Pro ja veel jääb raha üle.")
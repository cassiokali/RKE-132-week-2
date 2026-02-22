Perekonnanimi = str(input('Sisestage enda perekonnanimi: '))
Sugu = input('Sisestage enda sugu (m/n): ')

if Sugu.lower() == 'm':
    print(f'Tere, härra {Perekonnanimi}!')
elif Sugu.lower() == 'n':
    print(f'Tere, proua {Perekonnanimi}!')
else:
    print(f'Tere tulemast, {Perekonnanimi}!')
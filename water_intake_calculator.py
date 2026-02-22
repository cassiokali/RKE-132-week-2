kogus = float(input('Sisestage joodud klaaside vee arv: '))
protsent = kogus * 250 * 100 / 2000

if kogus < 0:
    print('Kuidas?') # :)
    quit()

if protsent < 50:
    print('Joo rohkem vett, keha vajab seda!')
elif 50 <= protsent < 100:
    print("Tubli, jätka samas vaimus!")
else:
    print('Suurepärane, oled oma päevase eesmärgi täitnud!“')
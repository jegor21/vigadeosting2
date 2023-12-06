print("*** ARVUMÄNGUD ***")
print()

while True:
    try:
        a = abs(int(input("Sisestage täisarv => ")))
        break
    except ValueError:
        print("See pole täisarv")

if a == 0:
    print("Nulliga ei ole mõtet midagi teha")
else:
    print("Leiame, mitu paaris- ja paaritut arvu on antud arvus")
    print()
    b = a  #Parandatud
    paaris = 0
    paaritu = 0
    while b > 0:
        if b % 2 == 0:  #Parandatud
            paaris += 1  #Parandatud
        else:
            paaritu += 1  #Parandatud
        b = b // 10

    print("Paarisarve:", paaris)
    print("Paarituid arve:", paaritu)
    print()

    print("*Pöörame ümber* sisestatud arvu")
    print()
    b = 0
    while a > 0:  #Parandatud
        number = a % 10
        a = a // 10
        b = b * 10 + number  #Parandatud
    print("*Ümberpööratud* arv on", b)
    print()

    print("Kontrollime Collatzi hüpoteesi")
    print()
    c = b  #Parandatud
    if c % 2 == 0:  #Parandatud
        print("c - paarisarv. Jagame 2-ga.")
    else:
        print("c - paaritu arv. Korrutame 3-ga, liidame 1 ja jagame 2-ga.")
    while c != 1:
        if c % 2 == 0:  #Parandatud
            c = c // 2  #Parandatud
        else:
            c = (3 * c + 1) // 2  #Parandatud
        print(c, end=" ")
    print()
    print("Hüpotees kehtib")


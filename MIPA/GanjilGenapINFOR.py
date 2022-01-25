print("menentukan bilangan ganjil atau genap")
print(" ")
bil = int(input("Masukan Bilangan: "))

x = bil % 2

if x == 0:
    print(bil,"Adalah Bilangan Genap")
else:
    print(bil,"Adalah Bilangan Ganjil")



while True:
    print("masukan -1 untuk keluar")
    bil = int(input("Masukan Bilangan: "))

    x = bil % 2

    if x == 0:
       print(bil,"Adalah Bilangan Genap")
    
    if bil == -1:
       break

    else:
        print(bil,"Adalah Bilangan Ganjil")

    

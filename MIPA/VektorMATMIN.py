print("Operasi Vektor 2d")

print("1 pengurangan")
print("2 penjumlahan")
print(" ")
op = int(input("Masukan angka: "))

ra1 = int(input("Masukan kiri atas: "))
rb1 = int(input("Masukan kiri Bawah: "))
rk1 = int(input("Dikalikan: "))

ra2 = int(input("Masukan Kanan atas: "))
rb2 = int(input("Masukan Kanan Bawah: "))
rk2 = int(input("Dikalikan: "))

if op == 1:
    print(ra1 * rk1 - ra2 * rk2)
    print("---")
    print(rb1 * rk1 - rb2 * rk2)

elif op == 2:
    print(ra1 * rk1 + ra2 * rk2)
    print("---")
    print(rb1 * rk1 + rb2 * rk2)

else:
    print("Ha?")



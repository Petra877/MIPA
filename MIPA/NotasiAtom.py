print("------Notasi Atom-------")

#Data di input
a = (str(input("Nama Atom : ")))
b = (int(input("Massa Atom: ")))
c = (int(input("Nomor Atom:")))

#Data diolah

nama = a
massa = b
nomor = c

jumproton = nomor #jumlah proton sama dengan elektron
jumelektron = nomor #Nomor atom sama dengan elektron dan proton

jumneutron = massa - jumelektron #jumlah neutron dihitung

#data ditampilkan
print("------------------Hasil Notasi------------------")
print("Jumlah Proton, Elektron dan Neutron Dari Atom",a)
print(" ")
print("Jumlah Elektron =",jumelektron) #menampilkan jumlah elektron
print("-----")
print("Jumlah Proton   =",jumproton) #menampilkan jumlah proton
print("-----")
print("Jumlah Neutron  =",jumneutron) #menampilkan jumlah neutron
print(" ")
print("--Script By, Petra Kharisvanda Cahyadi--")
print(" ")
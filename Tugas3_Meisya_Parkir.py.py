print("="*30)
print("=","                          ","=")
print("=","       Tarif Parkir       ","=")
print("=","                          ","=")
print("="*30)
masuk = int(input("Jam Masuk Kendaraan  : "))
keluar = int(input("Jam keluar Kendaraan : "))
print("="*30)
lama = masuk - keluar
jampertama = 3500
naiktiapjam = 2000
jam = 12
if lama == 0 :
    print(f"Lama parkir {lama}jam,Harga -")
elif lama <= 0 :
    nih = (lama+jam)*1
    if nih <= 0 :
        print("Jam masuk/keluar harus Bernilai antara 1 - 12")
    elif nih <= 12 :
        naik = naiktiapjam*nih
        if nih == 1 :
            print(f"Lama parkir {nih} jam,Harga {jampertama}")
        elif nih != 1 :
            print(f"lama parkir {nih} jam,Harga {jampertama+(naik-2000)}")
elif lama <= 12 :
    naik2=naiktiapjam*lama
    if lama == 1 :
        print(f"lama parkir {lama}jam,Harga{jampertama}")
    elif lama != 1 :
        print(f"lama parkir {lama}jam,Harga{jampertama+(naik2-2000)}")
else:
    print("Jam masuk/keluar harus Bernilai antara 1 - 12")
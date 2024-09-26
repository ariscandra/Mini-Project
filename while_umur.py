while True:
    print("Input Angka 0, Jika Anda Ingin Keluar Dari Program")
    umur = int(input("Masukkan Umur: "))

    if umur <= 5 :
        print("Kategori Umur: Balita")
    elif umur <= 10 :
        print("Kategori Umur: Anak")
    elif umur <= 19 :
        print("Kategori Umur: Remaja")
    elif umur <= 59 :
        print("Kategori Umur: Dewasa")
    elif umur <= 200 :
        print("Kategori Umur: Lansia")
    elif umur == 0 :
        break
    else:
        print("Anda Sudah Mati")

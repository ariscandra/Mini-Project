while True:
    print("Masukkan Angka 1, Jika anda ingin keluar dari program")
    nilai = int(input("Masukkan Nilai: "))

    if nilai >= 90:
        print("Nilai A")
    elif nilai >= 80:
        print("Nilai B")
    elif nilai >= 60:
        print("Nilai C")
    elif nilai == 1:
        break
    else:
        print("Nilai E")
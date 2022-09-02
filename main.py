print("Database :-\n")
N = input('Masukan Nama/Username Mu :-\n')
C = input('Berapa Umur Mu:-\n')
Ph = input('Masukan No Handphone Mu :-\n')
Z = input('Masukan Password Terbaru Mu :-\n')


f = open("database.txt" , "a")
f.write("  ||  ")
f.write(N)
f.write("  ||  ")
f.write(C)
f.write("  ||  ")
f.write(Ph)
f.write("  ||  ")
f.write(Z)

f.write("  ||  \n")
f.close()


k = input("Klik Enter Untuk Menyimpan Data Ke Database.txt")
print("k")
Success = input("Data Tersimpan Klik Enter Untuk Keluar")
print("Success")

from datetime import datetime

def hitung_biaya(jenis, malam):
    if jenis == "Standard":
        harga = 200000
    elif jenis == "Deluxe":
        harga = 350000
    else:
        harga = 0

    return harga * malam


jenis = input("Jenis kamar (Standard/Deluxe): ")
check_in = input("Tanggal check-in (DD-MM-YYYY): ")
check_out = input("Tanggal check-out (DD-MM-YYYY): ")

tanggal1 = datetime.strptime(check_in, "%d-%m-%Y")
tanggal2 = datetime.strptime(check_out, "%d-%m-%Y")

malam = (tanggal2 - tanggal1).days

total = hitung_biaya(jenis, malam)

print("\n=== PEMESANAN HOTEL ===")
print("Jenis kamar   :", jenis)
print("Check-in      :", check_in)
print("Check-out     :", check_out)
print("Lama menginap :", malam, "malam")
print("Total biaya   : Rp", total)


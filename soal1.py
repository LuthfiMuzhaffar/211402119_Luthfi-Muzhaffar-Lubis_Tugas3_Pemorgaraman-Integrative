# Buka file indata.txt 
with open('indata.txt', 'r') as file:
    # Membaca setiap baris dalam file
    lines = file.readlines()

# Inisialisasi variabel untuk menyimpan jumlah
total = 0

# Iterasi melalui setiap baris dalam file
for line in lines:
    # Mengkonversi setiap baris menjadi bilangan bulat
    number = int(line.strip())
    # Menambahkan bilangan bulat ke total
    total += number

# Mencetak jumlah dengan pemisah koma dan dua digit desimal

print('{:,.2f}'.format(total))
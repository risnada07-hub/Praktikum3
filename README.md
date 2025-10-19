# latihan-1
1. Penggunaan `end=''` pada print:
   - print('A', end='') ➜ mencetak "A" tanpa pindah baris.
   - print('B', end='') ➜ mencetak "B" langsung setelah A.
   - print('C', end='') ➜ mencetak "C" langsung setelah B.
   - print() ➜ barulah pindah ke baris baru.
   - Hasil: ABC
            X
            y
            Z

2. Penggunaan `sep` pada print:
   - `sep` mengatur pemisah antar nilai saat dicetak.
   - Contoh:
     - `print(w,x,y,z)` ➜ default pemisah = spasi
     - `print(w,x,y,z, sep=',')` ➜ hasil: 10,15,20,25
     - `print(w,x,y,z, sep=':')` ➜ hasil: 10:15:20:25
     - `print(w,x,y,z, sep='-----')` ➜ hasil: 10-----15-----20-----25

3. Format String (String Formatting):
   - `print('{0:>3} {1:>16}'.format(i, 10**0))`
   - `>3` ➜ rata kanan 3 karakter (untuk index/angka i)
   - `>16` ➜ rata kanan 16 karakter (untuk hasil 10 pangkat 0)
   - Dicetak dari i=0 sampai i=10
   - Semua hasil pangkat tetap 1 karena `10**0 = 1`




# latihan-2
1. Input Nilai
   - Program meminta input dari pengguna:
     a = input("Masukkan nilai a:")
     b = input("Masukkan nilai b:")
   - Input dari fungsi input() selalu berupa string.

2. Menampilkan Nilai
   - print("Variable a =", a)
   - print("Variable b =", b)
   - Menampilkan isi dari variabel a dan b.

3. Penggabungan String
   - print("Hasil penggabungan {1}&{0} = {1}{0}".format(a, b))
   - Menggabungkan string b dan a.
   - Contoh: a = 3, b = 5 ➜ output: Hasil penggabungan 5&3 = 53

4. Konversi Tipe Data
   - a = int(a)
   - b = int(b)
   - Mengubah input string menjadi integer agar bisa dilakukan operasi matematika.

5. Operasi Aritmatika
   - Penjumlahan:
     print("Hasil penjumlahan {1}+{0} = {hasil}".format(a, b, hasil=a + b))
   - Pembagian:
     print("Hasil pembagian {1}/{0} = {hasil}".format(a, b, hasil=a / b))

   - Gunakan parameter `hasil=...` untuk menyisipkan hasil kalkulasi ke dalam string menggunakan format().



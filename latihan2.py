# Input nilai
a = input("Masukkan nilai a:")
b = input("Masukkan nilai b:")

print("Variable a =", a)
print("Variable b =", b)
print("Hasil penggabungan {1}&{0} = {1}{0}".format(a, b))

# Konversi nilai
a = int(a)
b = int(b)

print("Hasil penjumlahan {1}+{0} = {hasil}".format(a, b, hasil=a + b))
print("Hasil pembagian {1}/{0} = {hasil}".format(a, b, hasil=a / b))
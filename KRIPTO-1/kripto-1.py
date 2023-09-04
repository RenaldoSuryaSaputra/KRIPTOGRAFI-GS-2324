# Memetakan nilai untuk kunci yang diambil dari alphabet a-z
nilai_kunci = {}
for i, huruf in enumerate('abcdefghijklmnopqrstuvwxyz'):
    nilai_kunci[huruf] = i

# request input
input_plaintext = input("Plaintext: ")
input_kunci = input("Kunci: ")

# memetakan nilai kunci berdasarkan input kunci dari user
nilai_kunci = [nilai_kunci[huruf] for huruf in input_kunci.lower() if huruf.isalpha()]

if not input_plaintext.isalpha(): # validasi input plaintext harus alphabet
    print("Karakter harus menggunakan alphabet")
else:
    print("Output: ") # bagian output
    ciphertext_str = input_plaintext # deklarasi ulang nilai input plaintext agar bisa dirubah berdasarkan cipher text terkini

    # Nested loop
    for i in range(len(input_kunci)):  # loop berdasarkan jumlah kunci
        ciphertext = []
        for karakter in range (len(ciphertext_str)): # loop berdasarkan char pada string input
            # cek apakah nilai ascii dari masing2 char yang ditambah dengan nilai kunci akan melebihi 122 / "z"
            if ord(ciphertext_str[karakter])+nilai_kunci[i] <= 122: # langsung tambah ke list ciphertext jika tidak melebihi 122
                #Menambahkan value/nilai baru berdasarkan kunci
                ciphertext.append(chr(ord(ciphertext_str[karakter])+nilai_kunci[i])) 
            else:
                kelebihan_alpha = (ord(ciphertext_str[karakter])+nilai_kunci[i] - 122) # diambil kelebihannya dan ditambahkan pada bagian awal alphabet 97
                #Menambahkan value/nilai baru berdasarkan kunci
                ciphertext.append(chr(ord("a")+kelebihan_alpha-1))
        ciphertext_str = ''.join(ciphertext) #menggabungkan list menjadi 1 string
        # Output
        print(f"Karakter ke-{i+1} kunci: {''.join(ciphertext)} ({input_kunci[i]})")
    print(f"Ciphertext {''.join(ciphertext)}")
program = "-----PERPUSTAKAAN KITA-----"
univ = "SEKOLAH VOKASI TEKNOLOGI REKAYASA INTERNET UGM"
str_program = program.center(70)
str_univ = univ.center(70)

class Color:
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    DARKCYAN = '\033[36m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print(Color.BLUE + '='*70 + Color.END)
print(Color.PURPLE + Color.BOLD + str_program + Color.END)
print(Color.PURPLE + str_univ + Color.END)
print(Color.BLUE + '='*70 + Color.END)
print(Color.BOLD + 'Selamat Datang !' + Color.END)

from os import system

# Menunggu pengguna menekan tombol enter
input("\033[92mTekan Enter untuk melanjutkan...\033[0m")

class Buku:
    def __init__(self, kode, judul, pengarang, genre, sinopsis, tahun, jumlah_buku, lama_peminjaman):
        self.kode = kode
        self.judul = judul
        self.pengarang = pengarang
        self.genre = genre
        self.sinopsis = sinopsis
        self.tahun = tahun
        self.jumlah_buku = jumlah_buku
        self.lama_peminjaman = lama_peminjaman

class Anggota:
    def __init__(self, nis, password, nama):
        self.nis = nis
        self.password = password
        self.nama = nama
        self.buku_dipinjam = []
        
from datetime import datetime, timedelta

class MenuAnggota:
    def __init__(self, perpustakaan):
        self.perpustakaan = perpustakaan
    
    def tampilkan_pilihan_genre(self):

        pass

    def tampilkan_menu(self):
        while True:
            print(Color.PURPLE + Color.BOLD + """
            +-----------------------------+
            |        MENU ANGGOTA         |
            |-----------------------------|
            | [1] Lihat Buku              |
            | [2] Pinjam Buku             |
            | [3] Kembalikan Buku         |
            | [4] Keluar                  |
            +-----------------------------+
            """)

            pilihan = input("Pilih menu (1-4): " + Color.END)

            if pilihan == "1":
                self.lihat_buku()
            elif pilihan == "2":
                self.pinjam_buku()
            elif pilihan == "3":
                self.kembalikan_buku()
            elif pilihan == "4":
                konfirmasi = input("\033[93mApakah Anda yakin ingin keluar? (y/n): \033[0m").lower()
                if konfirmasi == 'y':
                    system('cls')
                    print(Color.YELLOW + """
            +-----------------------------------+
            |                                   |
            |           TERIMA KASIH !          |
            |           SAMPAI JUMPA            |
            |                                   |
            +-----------------------------------+
                                    """ + Color.END)
                    exit()
                elif konfirmasi == 'n':
                    system('cls')
                else:
                    print("\033[91mPilihan tidak valid. Silakan coba lagi.\033[0m")   
            else:
                print("\033[91mPilihan tidak valid. Silakan coba lagi.\033[0m")  


    def lihat_buku(self):
        system('cls')
        self.perpustakaan.lihat_semua_buku()

        pilihan_cari = input("\033[94mApakah Anda ingin mencari buku tertentu? (y/n): \033[0m").lower()
        system('cls')
        if pilihan_cari == "y":
            print(Color.PURPLE + Color.BOLD + """
            +------------------------------+
            |     PILIHAN PENCARIAN        |
            |------------------------------|
            | [1] Cari Judul Buku          |
            | [2] Sortir Buku              |
            +------------------------------+
            """)

            pilihan_cari = input("Pilih opsi (1/2): " + Color.END).lower()

            if pilihan_cari == "1":
                judul_cari = input("Masukkan judul buku yang ingin dicari (ketik 'k' untuk kembali): ").lower()

                if judul_cari.lower() == 'k':
                    system('cls')
                    return  # Kembali ke menu utama jika 'k' ditekan

                self.perpustakaan.cari_judul_buku(judul_cari)

            elif pilihan_cari == "2":
                self.sortir_buku()
            else:
                print(f"\033[91mOpsi tidak valid.{Color.END}")

        elif pilihan_cari == "n":
            while True:
                kembali_menu_anggota = input("\033[94m" + "Apakah Anda ingin kembali ke menu anggota? (y/n): " + "\033[0m")
                system('cls')
                if kembali_menu_anggota.lower() == 'y':
                    self.tampilkan_menu()
                elif kembali_menu_anggota.lower() == 'n':
                    system('cls')
                    print(Color.YELLOW + """
            +-----------------------------------+
            |                                   |
            |           TERIMA KASIH !          |
            |           SAMPAI JUMPA            |
            |                                   |
            +-----------------------------------+
                                    """ + Color.END)
                    exit()
                else:
                    print("Pilih 'y' untuk ya atau 'n' untuk tidak.")
        else:
            print("Pilih 'y' untuk ya atau 'n' untuk tidak.")

            
        
    def sortir_buku(self):
        while True:
            system('cls')
            print(Color.PURPLE + Color.BOLD + """
            +-------------------------------+
            |        KRITERIA SORTIR        |
            |-------------------------------|
            | [A] Abjad                     |
            | [B] Genre                     |
            | [C] Pengarang                 |
            | [D] Tahun                     |
            +-------------------------------+
            """)

            pilihan_sortir = input("Pilih kriteria sortir (A-D): " + Color.END).upper()

            if pilihan_sortir == "A":
                self.sortir_abjad()
            elif pilihan_sortir == "B":
                self.sortir_genre()
            elif pilihan_sortir == "C":
                self.sortir_pengarang()
            elif pilihan_sortir == "D":
                self.sortir_tahun()
            else:
                print("\033[91mKriteria sortir tidak valid. Silakan pilih kriteria A, B, C, atau D.\033[0m")
                
                while True:
                    kembali_menu_anggota = input("\033[94m" + "Apakah Anda ingin kembali ke menu anggota? (y/n): " + "\033[0m").lower()
                    system('cls')
                    
                    if kembali_menu_anggota == 'y':
                        self.tampilkan_menu()
                    elif kembali_menu_anggota == 'n':
                        system('cls')
                        print(Color.YELLOW + """
    +-----------------------------------+
    |                                   |
    |           TERIMA KASIH !          |
    |           SAMPAI JUMPA            |
    |                                   |
    +-----------------------------------+
                        """ + Color.END)
                        exit()
                    else:
                        print("Pilih 'y' untuk ya atau 'n' untuk tidak.")
                        continue

            break
        
            
    def sortir_abjad(self):
        system('cls')

        print(Color.PURPLE + Color.BOLD + """
        +-------------------------------+
        |         SORTIR ABJAD          |
        |-------------------------------|
        | [1] A - Z                     |
        | [2] Z - A                     |
        | [3] Abjad Khusus              |
        +-------------------------------+
        """+ Color.END)

        while True:
            pilihan_abjad = input(f"\033[95mPilih opsi (1-3): {Color.END}").lower()

            if pilihan_abjad in ['1', '2', '3']:
                if pilihan_abjad == '1':
                    sorted_books = sorted(self.perpustakaan.buku_list, key=lambda x: x.judul)
                elif pilihan_abjad == "2":
                    sorted_books = sorted(self.perpustakaan.buku_list, key=lambda x: x.judul, reverse=True)
                elif pilihan_abjad == "3":
                    abjad_khusus = input("Masukkan abjad khusus untuk disortir: ").lower()
                    sorted_books = [buku for buku in self.perpustakaan.buku_list if buku.judul.lower().startswith(abjad_khusus)]
                    pass

                # Menampilkan buku setelah diurutkan
                self.perpustakaan.lihat_semua_buku(sorted_books)
                break
            else:
                print("\033[91mOpsi tidak valid. Silakan pilih opsi 1, 2, atau 3.\033[0m")


    def sortir_genre(self):
        system('cls')
        genres = self.perpustakaan.genre_buku()
        
        if genres is not None:
            program = "-----GENRE-----"
            str_program = program.center(70)
        
            print(Color.BLUE + '='*70 + Color.END)
            print(Color.PURPLE + Color.BOLD + str_program + Color.END)
            print(Color.BLUE + '='*70 + Color.END)

            for i, genre in enumerate(genres, start=1):
                print(f" [{i}]   {genre}")
                print(Color.BLUE + '='*30 + Color.END)

            while True:
                kode_genre = input(Color.PURPLE + "Masukkan kode genre yang ingin ditampilkan: " + Color.END)
                if kode_genre.isdigit() and 1 <= int(kode_genre) <= len(genres):
                    genre_terpilih = genres[int(kode_genre) - 1]
                    buku_genre = [buku for buku in self.perpustakaan.buku_list if buku.genre == genre_terpilih]

                    self.perpustakaan.buku_list = buku_genre

                    # Menampilkan buku-buku setelah penggantian
                    system('cls')
                    print("Berikut List buku berdasarkan genre yang dipilih: ")
                    for i, buku in enumerate(self.perpustakaan.buku_list, start=1):
                        print("\033[94m===============================================================================\033[0m")
                        print("\033[93m Kode          :      {}\033[0m".format(buku.kode))
                        print("\033[92m Judul Buku    :      {}\033[0m".format(buku.judul))
                        print("\033[91m Pengarang     :      {}\033[0m".format(buku.pengarang))
                        print("\033[94m Genre         :      {}\033[0m".format(buku.genre))
                        print("\033[96m Sinopsis      :      {}\033[0m".format(buku.sinopsis))
                        print("\033[90m Tahun         :      {}\033[0m".format(buku.tahun))
                        print("\033[95m Jumlah        :      {}\033[0m".format(buku.jumlah_buku))
                        print("\033[94m===============================================================================\033[0m")
        

                    break
                else:
                    print("\033[91mKode genre tidak valid. Silakan coba lagi.\033[0m")
        else:
            # Handle case when genres is None
            self.tampilkan_menu()
            
    def sortir_pengarang(self):
        system('cls')
        pengarangs = set(buku.pengarang for buku in self.perpustakaan.buku_list)

        program = "-----PILIHAN PENGARANG-----"
        str_program = program.center(70)
        
        print(Color.BLUE + '='*70 + Color.END)
        print(Color.PURPLE + Color.BOLD + str_program + Color.END)
        print(Color.BLUE + '='*70 + Color.END)
            
        for i, pengarang in enumerate(pengarangs, start=1):
            print(f" [{i}]   {pengarang}")
            print(Color.BLUE + '='*30 + Color.END)
            
        while True:
            kode_pengarang = input(Color.PURPLE + "Masukkan kode pengarang yang ingin ditampilkan: " + Color.END)
            if kode_pengarang.isdigit() and 1 <= int(kode_pengarang) <= len(pengarangs):
                pengarang_terpilih = list(pengarangs)[int(kode_pengarang) - 1]
                buku_pengarang = [buku for buku in self.perpustakaan.buku_list if buku.pengarang == pengarang_terpilih]

                self.perpustakaan.buku_list = buku_pengarang

                # Menampilkan buku-buku setelah penggantian
                system('cls')
                print("Berikut List buku berdasarkan pengarang yang dipilih: ")
                for i, buku in enumerate(self.perpustakaan.buku_list, start=1):
                    print("\033[94m===============================================================================\033[0m")
                    print("\033[93m Kode          :      {}\033[0m".format(buku.kode))
                    print("\033[92m Judul Buku    :      {}\033[0m".format(buku.judul))
                    print("\033[91m Pengarang     :      {}\033[0m".format(buku.pengarang))
                    print("\033[94m Genre         :      {}\033[0m".format(buku.genre))
                    print("\033[96m Sinopsis      :      {}\033[0m".format(buku.sinopsis))
                    print("\033[90m Tahun         :      {}\033[0m".format(buku.tahun))
                    print("\033[95m Jumlah        :      {}\033[0m".format(buku.jumlah_buku))
                    print("\033[94m===============================================================================\033[0m")

                break
            else:
                print("\033[91mKode pengarang tidak valid. Silakan coba lagi.\033[0m")

    def sortir_tahun(self):
        system('cls')
        # Mendapatkan daftar tahun dari buku_list
        tahun_list = sorted(set(buku.tahun for buku in self.perpustakaan.buku_list))
    
        program = "-----PILIHAN TAHUN-----"
        str_program = program.center(70)
        
        print(Color.BLUE + '='*70 + Color.END)
        print(Color.PURPLE + Color.BOLD + str_program + Color.END)
        print(Color.BLUE + '='*70 + Color.END)
    
        for i, tahun in enumerate(tahun_list, start=1):
            print(f" [{i}]   {tahun}")
            print(Color.BLUE + '='*20 + Color.END)
    
        while True:
            kode_tahun = input("Masukkan kode tahun yang ingin ditampilkan: "+ Color.END)
            if kode_tahun.isdigit() and 1 <= int(kode_tahun) <= len(tahun_list):
                tahun_terpilih = tahun_list[int(kode_tahun) - 1]
                buku_tahun_temp = [buku for buku in self.perpustakaan.buku_list if buku.tahun == tahun_terpilih]
        
                # Menampilkan buku-buku setelah penggantian
                system('cls')
                print("\033[93mBerikut List buku berdasarkan tahun yang dipilih:\033[0m")
                for i, buku in enumerate(buku_tahun_temp, start=1):
                    print("\033[94m===============================================================================\033[0m")
                    print("\033[92m Kode          :      {}\033[0m".format(buku.kode))
                    print("\033[91m Judul Buku    :      {}\033[0m".format(buku.judul))
                    print("\033[94m Pengarang     :      {}\033[0m".format(buku.pengarang))
                    print("\033[96m Sinopsis      :      {}\033[0m".format(buku.sinopsis))
                    print("\033[90m Tahun         :      {}\033[0m".format(buku.tahun))
                    print("\033[95m Jumlah        :      {}\033[0m".format(buku.jumlah_buku))
                    print("\033[94m===============================================================================\033[0m")
        
                break
            else:
                print("\033[91mKode tahun tidak valid. Silakan coba lagi.\033[0m")
        
        # Jika Anda ingin mengganti buku_list dengan hasil filter
        self.perpustakaan.buku_list = buku_tahun_temp
            
    def pinjam_buku(self):
        system('cls')
        self.perpustakaan.lihat_semua_buku()
        program = "-----PINJAM BUKU-----"
        str_program = program.center(104)

        print(Color.BLUE + '=' * 104 + Color.END)
        print(Color.PURPLE + Color.BOLD + str_program + Color.END)
        print(Color.BLUE + '=' * 104 + Color.END)
        print(Color.YELLOW + """
    +--------------------------------------+
    | NOTE :                               |
    |------------------------------------- |
    | BATAS PEMINJAMAN BUKU ADALAH MAKSIMAL|
    |    3 BUAH DENGAN WAKTU PEMINJAMAN    |
    |           SELAMA 7 HARI              |
    |  MOHON KEMBALIKAN BUKU TEPAT WAKTU   |
    |       DAN DALAM KEADAAN BAIK!        |
    +--------------------------------------+
                                  """ + Color.END)

        anggota = self.perpustakaan.logged_in_user

        while len(anggota.buku_dipinjam) < 3:
            kode_buku = input(Color.PURPLE + "Masukkan kode buku yang ingin dipinjam (atau ketik 'k' untuk kembali): " + Color.END).upper()

            if kode_buku.lower() == 'k':
                break  # Kembali ke menu utama jika 'k' ditekan

            buku = self.perpustakaan.cari_buku(kode_buku)

            if buku:
                # Periksa apakah buku sudah dipinjam sebelumnya
                if any(item['kode'] == kode_buku for item in anggota.buku_dipinjam):
                    print(Color.RED + "Maaf, buku ini sudah Anda pinjam sebelumnya." + Color.END)
                else:
                    # Tambahkan waktu saat ini sebagai waktu peminjaman
                    waktu_peminjaman = datetime.now()
                    # Hitung waktu pengembalian (contoh: 7 hari)
                    waktu_pengembalian = waktu_peminjaman + timedelta(days=7)

                    # Tambahkan buku ke daftar buku yang dipinjam oleh anggota
                    anggota.buku_dipinjam.append({
                        'judul': buku.judul,
                        'kode': buku.kode,
                        'waktu_peminjaman': waktu_peminjaman,
                        'waktu_pengembalian': waktu_pengembalian
                    })

                    # Output dengan warna
                    print(Color.BLUE + f"Anda telah berhasil meminjam buku {buku.judul}." + Color.END)
                    print(Color.GREEN + f"Waktu peminjaman: {waktu_peminjaman.strftime('%Y-%m-%d %H:%M:%S.%f')}" + Color.END)
                    print(Color.GREEN + f"Waktu pengembalian: {waktu_pengembalian.strftime('%Y-%m-%d %H:%M:%S.%f')}" + Color.END)

                     # Tampilkan pertanyaan apakah ingin meminjam lagi
                    pilihan = input("Apakah Anda ingin meminjam buku lagi? (y/n): ").lower()
                    if pilihan != 'y':
                        break

            else:
                print(Color.RED + "Buku dengan kode tersebut tidak ditemukan." + Color.END)

        # Tampilkan keranjang buku yang dipinjam
                
        if len(anggota.buku_dipinjam) > 0:
            system('cls')
            
            program = "-----KERANJANG BUKU YANG DIPINJAM-----"
            str_program = program.center(79)

            print(Color.BLUE + '=' * 79 + Color.END)
            print(Color.PURPLE + Color.BOLD + str_program + Color.END)
            print(Color.BLUE + '=' * 79 + Color.END)

            for buku_dipinjam in anggota.buku_dipinjam:
                print("\033[94m===============================================================================\033[0m")
                print("\033[93m Kode          :      {}\033[0m".format(buku_dipinjam['kode']))
                print("\033[92m Judul Buku    :      {}\033[0m".format(buku_dipinjam['judul']))
                # Add other details similarly
                print("\033[94m===============================================================================\033[0m")

            kembali_menu = input(Color.BLUE + "Apakah Anda ingin kembali ke menu anggota? (y/n): " + Color.END).lower()
            system('cls')
            if kembali_menu == 'y':
                return
        else:
            print(Color.YELLOW + """
    +-----------------------------------+
    |                                   |
    |  TERIMAKASIH TELAH MEMINJAM BUKU  |
    |  DI PERPUSTAKAAN KITA !           |
    |                                   |
    +-----------------------------------+
                              """ + Color.END)
            exit()

    def kembalikan_buku(self):
        system('cls')
        
        if len(self.perpustakaan.logged_in_user.buku_dipinjam) > 0:
            program = "-----KERANJANG BUKU YANG DIPINJAM-----"
            str_program = program.center(79)

            print(Color.BLUE + '=' * 79 + Color.END)
            print(Color.PURPLE + Color.BOLD + str_program + Color.END)
            print(Color.BLUE + '=' * 79 + Color.END)

            for buku_dipinjam in self.perpustakaan.logged_in_user.buku_dipinjam:
                print("\033[94m===============================================================================\033[0m")
                print("\033[93m Kode             :      {}\033[0m".format(buku_dipinjam['kode']))
                print("\033[92m Judul Buku       :      {}\033[0m".format(buku_dipinjam['judul']))
                print("\033[95m Waktu Peminjaman :    {}\033[0m".format(buku_dipinjam['waktu_peminjaman']))
                print("\033[94m===============================================================================\033[0m")

            while True:
                kode_buku = input("\033[95mMasukkan kode buku yang ingin dikembalikan: \033[0m").upper()

                judul_buku = self.perpustakaan.cari_judul_buku_dari_kode(kode_buku)

                if judul_buku:
                    anggota = self.perpustakaan.logged_in_user

                    for buku_dipinjam in anggota.buku_dipinjam:
                        if buku_dipinjam['kode'] == kode_buku:
                            # Book found, process return
                            judul_buku = buku_dipinjam['judul']
                            waktu_peminjaman = buku_dipinjam['waktu_peminjaman']
                            waktu_pengembalian = datetime.now()
                            selisih_hari = (waktu_pengembalian - waktu_peminjaman).days

                            print("\033[94m===============================================================================\033[0m")
                            print("\033[93m Kode          :      {}\033[0m".format(buku_dipinjam['kode']))
                            print("\033[92m Judul Buku    :      {}\033[0m".format(buku_dipinjam['judul']))
                            print("\033[95m Waktu Peminjaman:    {}\033[0m".format(waktu_peminjaman))
                            print("\033[94m===============================================================================\033[0m")

                            if selisih_hari > 7:
                                denda = (selisih_hari - 7) * self.perpustakaan.jumlah_hari_terlambat
                                print(f"Jumlah denda yang harus dibayar: Rp {denda}")
                            else:
                                denda = 0
                                print("\033[92mTidak ada denda.\033[0m")

                            # Tambahkan informasi denda ke daftar peminjaman
                            buku_dipinjam['denda'] = denda

                            # Hapus buku dari daftar buku yang dipinjam oleh anggota
                            anggota.buku_dipinjam.remove(buku_dipinjam)

                            # Tambahkan buku yang dikembalikan ke daftar buku
                            buku = self.perpustakaan.cari_buku(kode_buku)
                            buku.jumlah_buku += 1

                            print(f"\033[92mAnda telah berhasil mengembalikan buku {judul_buku}.\033[0m")
                            break  # Exit loop since the book has been found and processed
                    else:
                        # Book not found in the list
                        print(f"\033[91mAnda tidak sedang meminjam buku dengan kode {kode_buku}.\033[0m")

                else:
                    # Invalid book code
                    print("Kode buku tidak valid. Silakan coba lagi.")

                # Tanyakan apakah pengguna ingin mengembalikan buku lagi
                lagi = input("\033[94mApakah Anda ingin mengembalikan buku lagi? (y/n): \033[0m").lower()
                if lagi != 'y':
                    break

            # Kembali ke menu anggota setelah selesai
            system('cls')   
            self.tampilkan_menu()

        
    def cari_peminjaman(self, nis, kode_buku):
        for peminjaman in self.perpustakaan.daftar_peminjaman:
            if peminjaman.nis == nis and peminjaman.kode_buku == kode_buku:
                return peminjaman
        return None

    def login_anggota(self, nis, password):
        anggota = self.perpustakaan.login(nis, password)
        system('cls')
        
        if anggota:
            program = "-----SELAMAT DATANG-----"
            anggota_text = anggota.nama
            str_program = program.center(70)
            str_anggota = anggota_text.center(70)
    
            print(Color.BLUE + '='*70 + Color.END)
            print(Color.PURPLE + Color.BOLD + str_program + Color.END)
            print(Color.YELLOW + str_anggota + Color.END)
            print(Color.BLUE + '='*70 + Color.END)
            
            self.perpustakaan.logged_in_user = anggota
            self.tampilkan_menu()
        else:
            print(Color.RED + f"Anggota Dengan NIS {nis} Tidak Ditemukan!"+ Color.END)

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class MenuAdmin:
    def __init__(self, perpustakaan, admin):
        self.perpustakaan = perpustakaan
        self.admin = admin
        self.anggota_list = []
    
    def login_admin(self):
        program = "-----LOGIN ADMIN-----"
        str_program = program.center(60)
        
        print(Color.BLUE + '='*60 + Color.END)
        print(Color.PURPLE + Color.BOLD + str_program + Color.END)
        print(Color.BLUE + '='*60 + Color.END)  
      
        username = input("\033[95m  Masukkan user      : \033[0m")
        password = input("\033[95m  Masukkan password  : \033[0m")
        system('cls')

        if self.perpustakaan.login_admin(username, password):
            self.tampilkan_menu_admin()
            return True

        print("Login admin gagal. Akses ditolak.")
        return False

    def tampilkan_menu_admin(self):
        while True:
            print(Color.PURPLE + Color.BOLD + """
            +------------------------------+
            |          MENU ADMIN          |
            |------------------------------|
            | [1] Tambah Anggota           |
            | [2] Hapus Anggota            |
            | [3] Edit Anggota             |
            | [4] Lihat Anggota            |
            | [5] Tambah Buku              |
            | [6] Hapus Buku               |
            | [7] Edit Buku                |
            | [8] Lihat Semua Buku         |
            | [9] Keluar                   |
            +------------------------------+
            """)

            pilihan = input("Pilih menu (1-9): " + Color.END)
    
            if pilihan == "1":
                self.tambah_anggota()
            elif pilihan == "2":
                self.hapus_anggota()
            elif pilihan == "3":
                self.edit_anggota()
            elif pilihan == "4":
                self.lihat_anggota()
            elif pilihan == "5":
                self.tambah_buku()
            elif pilihan == "6":
                self.hapus_buku()
            elif pilihan == "7":
                self.edit_buku()
            elif pilihan == "8":
                self.lihat_semua_buku()
            elif pilihan == "9":
                konfirmasi = input("\033[93mApakah Anda yakin ingin keluar? (y/n): \033[0m").lower()
                if konfirmasi == 'y':
                    system('cls')
                    print(Color.YELLOW + """
            +-----------------------------------+
            |                                   |
            |           TERIMA KASIH !          |
            |           SAMPAI JUMPA            |
            |                                   |
            +-----------------------------------+
                                    """ + Color.END)
                    exit()
                elif konfirmasi == 'n':
                    system('cls')
                else:
                    print("\033[91mPilihan tidak valid. Silakan coba lagi.\033[0m")   
            else:
                print("\033[91mPilihan tidak valid. Silakan coba lagi.\033[0m")  
        
    def tambah_anggota(self):
        while True:
            self.lihat_anggota_baru()
            program = "-----TAMBAH ANGGOTA-----"
            str_program = program.center(60)
            
            print(Color.BLUE + '='*60 + Color.END)
            print(Color.PURPLE + Color.BOLD + str_program + Color.END)
            print(Color.BLUE + '='*60 + Color.END)
            nis = input("\033[95m  Masukkan NIS       : \033[0m")
            password = input("\033[95m  Masukkan password  : \033[0m")
            nama = input("\033[95m  Masukkan Nama      : \033[0m")
    
            anggota = Anggota(nis, password, nama)
            self.perpustakaan.tambah_anggota(anggota)
            print("\033[92m" + f"Anggota {nama} dengan NIS {nis} telah ditambahkan." + "\033[0m")

            tampilkan_daftar = input("\033[95m" +"Apakah Anda ingin melihat daftar Anggota terbaru? (y/n): " + "\033[0m").upper()
            if tampilkan_daftar.lower() == 'y':
                self.lihat_anggota_baru()  # Tampilkan seluruh list buku terbaru
                
            while True:
                kembali_ke_menu = input("\033[94m" + "Apakah Anda ingin kembali ke menu admin? (y/n): " + "\033[0m").upper()
                system('cls')

                if kembali_ke_menu == 'Y':
                    self.tampilkan_menu_admin()
                    break
                elif kembali_ke_menu == 'N':
                    system('cls')
                    print(Color.YELLOW + """
            +-----------------------------------+
            |                                   |
            |           TERIMA KASIH !          |
            |           SAMPAI JUMPA            |
            |                                   |
            +-----------------------------------+
                    """ + Color.END)
                    exit()
                else:
                    print("Pilih 'y' untuk ya atau 'n' untuk tidak.")

    def cari_anggota(self, nis):
        for anggota in self.perpustakaan.anggota:
            if anggota.nis == nis:
                return anggota
        return None
    
    
    def edit_buku(self):
        system('cls')
        self.perpustakaan.lihat_semua_buku()
        
        kode_buku = input("\033[95mMasukkan Kode Buku yang akan diubah: \033[0m")
        
        buku = self.perpustakaan.cari_buku(kode_buku)
        if buku:
            print("\033[94m===============================================================================\033[0m")
            print("\033[93m Kode          :      {}\033[0m".format(buku.kode))
            print("\033[92m Judul Buku    :      {}\033[0m".format(buku.judul))
            print("\033[91m Pengarang     :      {}\033[0m".format(buku.pengarang))
            print("\033[94m Genre         :      {}\033[0m".format(buku.genre))
            print("\033[96m Sinopsis      :      {}\033[0m".format(buku.sinopsis))
            print("\033[90m Tahun         :      {}\033[0m".format(buku.tahun))
            print("\033[95m Jumlah        :      {}\033[0m".format(buku.jumlah_buku))
            print("\033[94m===============================================================================\033[0m")

            
            print("\033[95mMasukkan data baru:\033[0m")
            buku.judul = input("Judul Buku  : ")
            buku.jumlah_buku = int(input("Jumlah Buku : "))
            
            print("\033[92m" + f"Data judul dan jumlah buku dengan kode {kode_buku} berhasil diubah." + "\033[0m")
            
            tampilkan_daftar = input("\033[95m" +"Apakah Anda ingin melihat daftar buku terbaru? (y/n): " + "\033[0m")
            if tampilkan_daftar.lower() == 'y':
                self.perpustakaan.lihat_semua_buku()  # Tampilkan seluruh list buku terbaru
    
        else:
            print("\033[91m" + f"Tidak ditemukan buku dengan kode {kode_buku}." + "\033[0m")
            
        while True:
            kembali_ke_menu = input("\033[94m" + "Apakah Anda ingin kembali ke menu admin? (y/n): " + "\033[0m").upper()
            system('cls')

            if kembali_ke_menu == 'Y':
                self.tampilkan_menu_admin()
                break
            elif kembali_ke_menu == 'N':
                system('cls')
                print(Color.YELLOW + """
        +-----------------------------------+
        |                                   |
        |           TERIMA KASIH !          |
        |           SAMPAI JUMPA            |
        |                                   |
        +-----------------------------------+
                """ + Color.END)
                exit()
            else:
                print("Pilih 'y' untuk ya atau 'n' untuk tidak.")


    def hapus_anggota(self):
        system('cls')
        self.lihat_anggota_baru()
        program = "-----HAPUS ANGGOTA-----"
        str_program = program.center(60)
            
        print(Color.BLUE + '='*60 + Color.END)
        print(Color.PURPLE + Color.BOLD + str_program + Color.END)
        print(Color.BLUE + '='*60 + Color.END)
        nis = input("\033[95m" + "Masukkan NIS anggota yang akan dihapus: " + "\033[0m")
    
        anggota = self.cari_anggota(nis)
        if anggota:
            self.perpustakaan.hapus_anggota(nis)
            print("\033[92m" + f"Anggota {anggota.nama} dengan NIS {nis} telah dihapus." + "\033[0m")
       
            tampilkan_daftar = input("\033[95m" + "Apakah Anda ingin melihat daftar anggota terbaru? (y/n): " + "\033[0m")
            if tampilkan_daftar.lower() == 'y':
                self.lihat_anggota_baru()  # Tampilkan seluruh list anggota terbaru
                
        else:
            print("\033[91m" + f"Tidak ditemukan anggota dengan NIS {nis}." + "\033[0m")

        while True:
            kembali_ke_menu = input("\033[94m" + "Apakah Anda ingin kembali ke menu admin? (y/n): " + "\033[0m").upper()
            system('cls')

            if kembali_ke_menu == 'Y':
                self.tampilkan_menu_admin()
                break
            elif kembali_ke_menu == 'N':
                system('cls')
                print(Color.YELLOW + """
        +-----------------------------------+
        |                                   |
        |           TERIMA KASIH !          |
        |           SAMPAI JUMPA            |
        |                                   |
        +-----------------------------------+
                """ + Color.END)
                exit()
            else:
                print("Pilih 'y' untuk ya atau 'n' untuk tidak.")
                    
                    
    def lihat_anggota(self):
        system('cls')
        program = "-----LIST ANGGOTA-----"
        str_program = program.center(60)
        
        print(Color.BLUE + '='*60 + Color.END)
        print(Color.PURPLE + Color.BOLD + str_program + Color.END)
        print(Color.BLUE + '='*60 + Color.END)
        print(" {:^10} || {:^25}               ".format("NIS", "Nama"))
        print('='*60 )
        
        for anggota in self.perpustakaan.anggota:
            print(" {:^10} ||   {:<25}                ".format(anggota.nis, anggota.nama))
            print('='*60 )
        
        while True:
            kembali_ke_menu = input("\033[94m" + "Apakah Anda ingin kembali ke menu admin? (y/n): " + "\033[0m").upper()
            system('cls')

            if kembali_ke_menu == 'Y':
                self.tampilkan_menu_admin()
                break
            elif kembali_ke_menu == 'N':
                system('cls')
                print(Color.YELLOW + """
        +-----------------------------------+
        |                                   |
        |           TERIMA KASIH !          |
        |           SAMPAI JUMPA            |
        |                                   |
        +-----------------------------------+
                """ + Color.END)
                exit()
            else:
                print("Pilih 'y' untuk ya atau 'n' untuk tidak.")

        
    def lihat_anggota_baru(self):
        system('cls')
        program = "-----LIST ANGGOTA-----"
        str_program = program.center(60)
        
        print(Color.BLUE + '='*60 + Color.END)
        print(Color.PURPLE + Color.BOLD + str_program + Color.END)
        print(Color.BLUE + '='*60 + Color.END)
        print(" {:^10} || {:^25}               ".format("NIS", "Nama"))
        print('='*60 )
        
        for anggota in self.perpustakaan.anggota:
            print(" {:^10} ||   {:<25}                ".format(anggota.nis, anggota.nama))
            print('='*60 )
        
    def edit_anggota(self):
        system('cls')
        self.lihat_anggota_baru()
        program = "-----EDIT ANGGOTA-----"
        str_program = program.center(60)
        
        print(Color.BLUE + '='*60 + Color.END)
        print(Color.PURPLE + Color.BOLD + str_program + Color.END)
        print(Color.BLUE + '='*60 + Color.END)
        
        nis = input("\033[95mMasukkan NIS anggota yang akan diubah: \033[0m")
        nama_baru = input("\033[95mMasukkan Nama Baru: \033[0m")
        self.perpustakaan.edit_anggota(nis, nama_baru)
        
        tampilkan_daftar = input("\033[95m" + "Apakah Anda ingin melihat daftar anggota terbaru? (y/n): " + "\033[0m")
        if tampilkan_daftar.lower() == 'y':
            self.lihat_anggota_baru()  # Tampilkan seluruh list anggota terbaru
            
        while True:
            kembali_ke_menu = input("\033[94m" + "Apakah Anda ingin kembali ke menu admin? (y/n): " + "\033[0m").upper()
            system('cls')

            if kembali_ke_menu == 'Y':
                self.tampilkan_menu_admin()
                break
            elif kembali_ke_menu == 'N':
                system('cls')
                print(Color.YELLOW + """
        +-----------------------------------+
        |                                   |
        |           TERIMA KASIH !          |
        |           SAMPAI JUMPA            |
        |                                   |
        +-----------------------------------+
                """ + Color.END)
                exit()
            else:
                print("Pilih 'y' untuk ya atau 'n' untuk tidak.")

    def tambah_buku(self):
        system('cls')
        self.perpustakaan.lihat_semua_buku()
        
        program = "-----TAMBAH BUKU-----"
        str_program = program.center(104)
            
        print(Color.BLUE + '='*104 + Color.END)
        print(Color.PURPLE + Color.BOLD + str_program + Color.END)
        print(Color.BLUE + '='*104 + Color.END)
        
        kode_buku = input("\033[93m" + "Masukkan Kode Buku             : " + "\033[0m")
        judul_buku = input("\033[92m" + "Masukkan Judul Buku            : " + "\033[0m")
        pengarang_buku = input("\033[91m" + "Masukkan Nama Pengarang        : " + "\033[0m")
        genre_buku = input("\033[94m" + "Masukkan Genre Buku            : " + "\033[0m")
        sinopsis_buku = input("\033[96m" + "Masukkan Sinopsis Buku         : " + "\033[0m")
        tahun_terbit_buku = input("\033[90m" + "Masukkan Tahun Terbit Buku     : " + "\033[0m")
        jumlah_buku = int(input("\033[95m" + "Masukkan Jumlah Buku           : " + "\033[0m"))
        lama_peminjaman = int(input("\033[96m" + "Masukkan Lama Peminjaman (hari): " + "\033[0m"))

        buku = Buku(kode_buku, judul_buku, pengarang_buku, genre_buku, sinopsis_buku, tahun_terbit_buku, jumlah_buku, lama_peminjaman)
        self.perpustakaan.tambah_buku(buku)
        print("\033[92m" + f"Buku {judul_buku} dengan kode {kode_buku} telah ditambahkan." + "\033[0m")
        
        tampilkan_daftar = input("\033[95m" +"Apakah Anda ingin melihat daftar buku terbaru? (y/n): " + "\033[0m")
        if tampilkan_daftar.lower() == 'y':
            self.perpustakaan.lihat_semua_buku()  # Tampilkan seluruh list buku terbaru
        
        while True:
            kembali_ke_menu = input("\033[94m" + "Apakah Anda ingin kembali ke menu admin? (y/n): " + "\033[0m").upper()
            system('cls')

            if kembali_ke_menu == 'Y':
                self.tampilkan_menu_admin()
                break
            elif kembali_ke_menu == 'N':
                system('cls')
                print(Color.YELLOW + """
        +-----------------------------------+
        |                                   |
        |           TERIMA KASIH !          |
        |           SAMPAI JUMPA            |
        |                                   |
        +-----------------------------------+
                """ + Color.END)
                exit()
            else:
                print("Pilih 'y' untuk ya atau 'n' untuk tidak.")


    def hapus_buku(self):
        system('cls')
        self.perpustakaan.lihat_semua_buku()
        
        program = "-----HAPUS BUKU-----"
        str_program = program.center(104)
            
        print(Color.BLUE + '='*104 + Color.END)
        print(Color.PURPLE + Color.BOLD + str_program + Color.END)
        print(Color.BLUE + '='*104 + Color.END)
        
        kode_buku = input("\033[95m" + " Masukkan Kode Buku yang akan dihapus: " + "\033[0m ").upper()

        buku = self.perpustakaan.cari_buku(kode_buku)
        if buku:
            self.perpustakaan.hapus_buku(kode_buku)
            print("\033[92m" + f"Buku {buku.judul} dengan kode {kode_buku} telah dihapus." + "\033[0m")

            tampilkan_daftar = input("\033[95m" +"Apakah Anda ingin melihat daftar buku terbaru? (y/n): " + "\033[0m").upper()
            if tampilkan_daftar.lower() == 'y':
                self.perpustakaan.lihat_semua_buku()  # Tampilkan seluruh list buku terbaru

        else:
            print("\033[91m" + f"Tidak ditemukan buku dengan kode {kode_buku}." + "\033[0m")
            
        while True:
            kembali_ke_menu = input("\033[94m" + "Apakah Anda ingin kembali ke menu admin? (y/n): " + "\033[0m").upper()
            system('cls')

            if kembali_ke_menu == 'Y':
                self.tampilkan_menu_admin()
                break
            elif kembali_ke_menu == 'N':
                system('cls')
                print(Color.YELLOW + """
        +-----------------------------------+
        |                                   |
        |           TERIMA KASIH !          |
        |           SAMPAI JUMPA            |
        |                                   |
        +-----------------------------------+
                """ + Color.END)
                exit()
            else:
                print("Pilih 'y' untuk ya atau 'n' untuk tidak.")


    def lihat_semua_buku(self):
        system('cls')
        program = "-----SEMUA BUKU-----"
        str_program = program.center(70)
        
        print(Color.BLUE + '='*70 + Color.END)
        print(Color.PURPLE + Color.BOLD + str_program + Color.END)
        print(Color.BLUE + '='*70 + Color.END)
        for buku in self.perpustakaan.buku_list:
            print("\033[93m Kode          :      {}\033[0m".format(buku.kode))
            print("\033[92m Judul Buku    :      {}\033[0m".format(buku.judul))
            print("\033[91m Pengarang     :      {}\033[0m".format(buku.pengarang))
            print("\033[94m Genre         :      {}\033[0m".format(buku.genre))
            print("\033[96m Sinopsis      :      {}\033[0m".format(buku.sinopsis))
            print("\033[90m Tahun         :      {}\033[0m".format(buku.tahun))
            print("\033[95m Jumlah        :      {}\033[0m".format(buku.jumlah_buku))
            print("========================================================================================================")
        
        while True:
            kembali_ke_menu = input("\033[94m" + "Apakah Anda ingin kembali ke menu admin? (y/n): " + "\033[0m").upper()
            system('cls')

            if kembali_ke_menu == 'Y':
                self.tampilkan_menu_admin()
                break
            elif kembali_ke_menu == 'N':
                system('cls')
                print(Color.YELLOW + """
        +-----------------------------------+
        |                                   |
        |           TERIMA KASIH !          |
        |           SAMPAI JUMPA            |
        |                                   |
        +-----------------------------------+
                """ + Color.END)
                exit()
            else:
                print("Pilih 'y' untuk ya atau 'n' untuk tidak.")
        

class Perpustakaan:
    def __init__(self):
        self.buku_list = [
            Buku("B001", "Harry Potter", "J.K. Rowling", "Fantasi", "Kisah penyihir muda", 2005, 10, 7),
            Buku("B002", "Lord of the Rings", "J.R.R. Tolkien", "Fantasi", "Petualangan di Dunia Tengah", 2003, 7, 7),
            Buku("B003", "To Kill a Mockingbird", "Harper Lee", "Fiksi", "Drama di Maycomb, Alabama", 2010, 5, 10),
            Buku("B004", "1984", "George Orwell", "Fiksi Ilmiah", "Distopia masa depan", 2008, 12, 10),
            Buku("B005", "Pride and Prejudice", "Jane Austen", "Romance", "Kisah cinta Elizabeth Bennet", 2012, 8, 7),
            Buku("B006", "The Great Gatsby", "F. Scott Fitzgerald", "Fiksi", "Kisah cinta dan ketidakpuasan di era 1920-an", 2015, 15, 7),
            Buku("B007", "One Hundred Years of Solitude", "Gabriel Garcia Marquez", "Magis Realisme", "Kisah keluarga Buendia di Macondo", 2018, 10, 7),
            Buku("B008", "Moby-Dick", "Herman Melville", "Petualangan", "Kisah kapten Ahab melawan paus putih", 2006, 5, 7),
            Buku("B009", "Brave New World", "Aldous Huxley", "Fiksi Ilmiah", "Masyarakat futuristik yang terkendali", 2014, 9, 7),
            Buku("B010", "The Hobbit", "J.R.R. Tolkien", "Fantasi", "Petualangan Bilbo Baggins", 2011, 11, 7),
            Buku("B011", "The Chronicles of Narnia", "C.S. Lewis", "Fantasi", "Petualangan di Narnia", 2004, 13, 7),
            Buku("B012", "Crime and Punishment", "Fyodor Dostoevsky", "Drama", "Kisah Raskolnikov dan perasaan bersalah", 2009, 7, 7),
            Buku("B013", "The Catcher in the Rye", "J.D. Salinger", "Fiksi", "Kisah perjalanan Holden Caulfield", 2019, 20, 7),
            Buku("B014", "The Odyssey", "Homer", "Epos", "Kisah Odysseus dalam perjalanan pulang", 2016, 8, 7),
            Buku("B015", "The Grapes of Wrath", "John Steinbeck", "Fiksi", "Kehidupan keluarga Joad selama Depresi Besar", 2013, 11, 7),
            Buku("B016", "The Scarlet Letter", "Nathaniel Hawthorne", "Romantika", "Penderitaan Hester Prynne di Puritan New England", 2017, 9, 7),
            Buku("B017", "War and Peace", "Leo Tolstoy", "Sejarah", "Kisah keluarga dan perang Napoleon", 2015, 15, 7),
            Buku("B018", "The Divine Comedy", "Dante Alighieri", "Epos", "Perjalanan Dante melalui Neraka, Purgatorio, dan Surga", 2018, 10, 7),
            Buku("B019", "Frankenstein", "Mary Shelley", "Horor", "Kisah penciptaan makhluk hidup oleh Victor Frankenstein", 2012, 7, 7),
            Buku("B020", "Great Expectations", "Charles Dickens", "Romantika", "Perjalanan hidup Pip dan hubungannya dengan Miss Havisham", 2019, 12, 7),
            Buku("B021", "The Iliad", "Homer", "Epos", "Kisah Perang Troya", 2016, 8, 7),
            Buku("B022", "One Hundred Years of Solitude", "Gabriel Garcia Marquez", "Magis Realisme", "Kisah keluarga Buendia di Macondo", 2014, 10, 7),
            Buku("B023", "Moby-Dick", "Herman Melville", "Petualangan", "Pengejaran paus raksasa oleh Kapten Ahab", 2016, 14, 7),
            Buku("B024", "Crime and Punishment", "Fyodor Dostoevsky", "Fiksi Psikologis", "Kejahatan, hukuman, dan penebusan", 2013, 9, 7),
            Buku("B025", "The Picture of Dorian Gray", "Oscar Wilde", "Horor", "Misteri dan moralitas di London", 2015, 8, 7),
            Buku("B026", "Brave New World", "Aldous Huxley", "Fiksi Ilmiah", "Distopia masa depan", 2018, 11, 7),
            Buku("B027", "Wuthering Heights", "Emily Bronte", "Romantika", "Kisah cinta di padang gurun Yorkshire", 2017, 10, 7),
            Buku("B028", "Anna Karenina", "Leo Tolstoy", "Romantika", "Kehidupan dan cinta Anna Karenina", 2014, 15, 7),
            Buku("B029", "Les Misérables", "Victor Hugo", "Sejarah", "Pengampunan dan keadilan di Perancis abad ke-19", 2012, 12, 7),
            Buku("B030", "The Great Gatsby", "F. Scott Fitzgerald", "Fiksi", "Misteri dan kegagalan American Dream", 2019, 20, 7),
            Buku("B031", "The Brothers Karamazov", "Fyodor Dostoevsky", "Fiksi Psikologis", "Kisah keluarga Karamazov", 2016, 14, 7),
            Buku("B032", "The Old Man and the Sea", "Ernest Hemingway", "Petualangan", "Pertempuran seorang tua dengan seekor ikan marlin", 2018, 15, 7),
            Buku("B033", "Laskar Pelangi", "Andrea Hirata", "Drama", "Perjuangan anak-anak di Belitung", 2005, 15, 7),
            Buku("B034", "Ayat-Ayat Cinta", "Habiburrahman El Shirazy", "Romance", "Kisah cinta seorang mahasiswa", 2004, 10, 7),
            Buku("B035", "Bumi Manusia II: Pramoedya Ananta Toer", "Pramoedya Ananta Toer", "Sejarah", "Kelanjutan kisah Minke", 2023, 14, 7),
            Buku("B036", "Tenggelamnya Kapal Van Der Wijck", "Hamka", "Romance", "Drama cinta dalam budaya Minang", 1939, 8, 7),
            Buku("B037", "Perahu Kertas", "Dee Lestari", "Drama", "Perjalanan hidup Kugy dan Keenan", 2009, 18, 7),
            Buku("B038", "Hujan Bulan Juni", "Sapardi Djoko Damono", "Puisi", "Kumpulan puisi pilihan", 2020, 12, 7),
            Buku("B039", "Sang Pemimpi", "Andrea Hirata", "Drama", "Perjalanan hidup Ikal setelah Laskar Pelangi", 2006, 12, 7),
            Buku("B040", "Hujan", "Tere Liye", "Drama", "Kisah tentang persahabatan dan perjuangan", 2014, 15, 7),
            Buku("B138", "Sapiens: Yuval Noah Harari", "Yuval Noah Harari", "Sejarah", "Perjalanan panjang manusia", 2023, 18, 7),
            Buku("B042", "Bidadari-Bidadari Surga", "Tere Liye", "Drama", "Persahabatan di sekolah pesantren", 2008, 14, 7),
            Buku("B043", "Laut Bercerita", "Leila S. Chudori", "Drama", "Cerita keluarga di masa Orde Baru", 2014, 12, 7),
            Buku("B044", "Pulang", "Leila S. Chudori", "Sejarah", "Pertemuan dua saudara setelah lama terpisah", 2012, 10, 7),
            Buku("B045", "Aroma Karsa", "Dee Lestari", "Drama", "Perjalanan batin dua sahabat", 2005, 15, 7),
            Buku("B046", "Cinta di Dalam Gelas", "Andrea Hirata", "Romance", "Kisah cinta dan persahabatan", 2005, 12, 7),
            Buku("B047", "Tentang Kamu", "Tere Liye", "Romance", "Kisah percintaan remaja", 2010, 10, 7),
            Buku("B048", "Edensor", "Andrea Hirata", "Biografi", "Kisah kehidupan penulis", 2007, 14, 7),
            Buku("B049", "Sepotong Hati yang Baru", "Tere Liye", "Drama", "Perjuangan seorang perempuan", 2018, 16, 7),
            Buku("B050", "Bumi", "Tere Liye", "Fantasi", "Petualangan di dunia fantasi", 2015, 12, 7),
            Buku("B051", "Senja dan Pagi", "Leila S. Chudori", "Drama", "Cerita cinta di tengah pergolakan politik", 2011, 14, 7),
            Buku("B052", "Perahu Kertas 2", "Dee Lestari", "Drama", "Kisah lanjutan Kugy dan Keenan", 2011, 18, 7),
            Buku("B053", "Sang Pemimpi II: Seperti Dendam, Rindu Harus Dibayar Tuntas", "Andrea Hirata", "Drama", "Perjalanan hidup Ikal setelah Sang Pemimpi", 2021, 12, 7),
            Buku("B054", "Negeri Van Oranje: Catatan Tahun Pertama", "Karya Orang Indonesia", "Drama", "Kisah persahabatan mahasiswa Indonesia di Belanda", 2020, 14, 7),
            Buku("B055", "Lima Detik", "Sitta Karina", "Romance", "Kisah cinta yang bermula dari pertemuan singkat", 2022, 10, 7),
            Buku("B056", "Ketika Cinta Bertasbih: Jangan Pernah Kembali", "Habiburrahman El Shirazy", "Romance", "Kisah cinta yang diuji keimanan", 2023, 10, 7),
            Buku("B057", "Aroma Karsa: Sepotong Karya Terindah", "Dee Lestari", "Drama", "Petualangan batin dua sahabat", 2020, 15, 7),
            Buku("B058", "Melihat Api Bekerja", "Leila S. Chudori", "Drama", "Kisah tentang perempuan dan pekerjaan", 2022, 12, 7),
            Buku("B059", "Tarian Bumi", "Tere Liye", "Fantasi", "Petualangan di dunia fantasi", 2021, 14, 7),
            Buku("B060", "Selimut Debu", "Agustinus Wibowo", "Biografi", "Kisah perjalanan seorang penjelajah", 2023, 16, 7),
            Buku("B061", "Mata yang Enak Dipandang", "Ahmad Fuadi", "Drama", "Kisah persahabatan di tengah pelajaran seni", 2020, 14, 7),
            Buku("B062", "Sampai Akhir Hidupku", "Leila S. Chudori", "Romance", "Cerita cinta yang mengharukan", 2022, 18, 7),
            Buku("B063", "Lelaki Harimau", "Eka Kurniawan", "Drama", "Kisah misterius di desa terpencil", 2023, 12, 7),
            Buku("B064", "Pergi", "Tere Liye", "Drama", "Kisah keberanian seorang pemuda", 2021, 15, 7),
            Buku("B065", "Sekar", "Ayat Ayat Cahyadi", "Drama", "Kisah cinta di tengah krisis air bersih", 2020, 10, 7),
            Buku("B066", "Komet Minor", "Tere Liye", "Drama", "Perjalanan hidup seorang anak", 2023, 12, 7),
            Buku("B067", "Kamera Lestarikan", "Rintik Sedu", "Drama", "Kisah seorang fotografer perempuan", 2022, 14, 7),
            Buku("B068", "Negeri 5 Menara", "Ahmad Fuadi", "Drama", "Pertualangan di pesantren modern", 2021, 14, 7),
            Buku("B069", "9 Summers 10 Autumns", "Iwan Setyawan", "Biografi", "Perjalanan hidup seorang sopir truk", 2022, 16, 7),
            Buku("B070", "Matematika Dasar", "John Doe", "Matematika", "Pengenalan konsep dasar matematika", 2020, 15, 7),
            Buku("B071", "Fisika Modern", "Jane Smith", "Fisika", "Pemahaman teori fisika modern", 2021, 12, 7),
            Buku("B072", "Kimia Organik", "Robert Johnson", "Kimia", "Studi mengenai senyawa kimia organik", 2022, 14, 7),
            Buku("B073", "Biologi Sel", "Emily Davis", "Biologi", "Pemahaman struktur dan fungsi sel", 2020, 18, 7),
            Buku("B074", "Sejarah Indonesia", "Ahmad Basuki", "Sejarah", "Perkembangan sejarah Indonesia", 2021, 14, 7),
            Buku("B075", "Bahasa Indonesia", "Siti Aisyah", "Bahasa", "Pengembangan kemampuan berbahasa Indonesia", 2022, 16, 7),
            Buku("B076", "Ekonomi Makro", "Dwi Susilo", "Ekonomi", "Analisis tentang perekonomian makro", 2020, 12, 7),
            Buku("B077", "Geografi Dunia", "Budi Santoso", "Geografi", "Pemahaman mengenai geografi dunia", 2023, 14, 7),
            Buku("B078", "Seni Rupa", "Diana Putri", "Seni", "Pengenalan seni rupa dan ekspresi", 2022, 15, 7),
            Buku("B079", "Penelitian Sosial", "Rudi Hermawan", "Sosiologi", "Metode penelitian dalam sosiologi", 2020, 18, 7),
            Buku("B080", "Psikologi Perkembangan", "Nina Wijaya", "Psikologi", "Studi mengenai perkembangan psikologis", 2021, 16, 7),
            Buku("B081", "Pendidikan Moral Pancasila", "Andi Pratama", "Pendidikan Moral", "Pengembangan nilai-nilai Pancasila", 2022, 14, 7),
            Buku("B082", "Teknologi Informasi", "Rizki Santoso", "Teknologi", "Pengenalan teknologi informasi", 2020, 12, 7),
            Buku("B083", "Bahasa Inggris", "Linda Johnson", "Bahasa", "Pengembangan kemampuan berbahasa Inggris", 2023, 14, 7),
            Buku("B084", "Manajemen Bisnis", "Yanto Wibowo", "Manajemen", "Prinsip-prinsip manajemen bisnis", 2021, 15, 7),
            Buku("B085", "Hukum Perdata", "Rina Kartika", "Hukum", "Studi mengenai hukum perdata", 2022, 16, 7),
            Buku("B086", "Kesehatan Masyarakat", "Sinta Dewi", "Kesehatan", "Konsep dan aplikasi kesehatan masyarakat", 2020, 18, 7),
            Buku("B087", "Pertanian Modern", "Agus Santoso", "Pertanian", "Teknologi dalam pertanian modern", 2021, 14, 7),
            Buku("B089", "Kewirausahaan", "Diana Putri", "Ekonomi", "Pengembangan jiwa kewirausahaan", 2022, 15, 7),
            Buku("B090", "Teknik Elektro", "Yudi Hermawan", "Teknik", "Dasar-dasar teknik elektro", 2023, 14, 7),
            Buku("B091", "The Da Vinci Code", "Dan Brown", "Mystery", "A murder mystery that leads to a religious conspiracy", 2007, 10, 7),
            Buku("B092", "The Kite Runner", "Khaled Hosseini", "Drama", "A story of redemption and friendship set in Afghanistan", 2008, 12, 7),
            Buku("B093", "The Road", "Cormac McCarthy", "Post-Apocalyptic", "A father and son's journey through a desolate world", 2009, 14, 7),
            Buku("B094", "The Lovely Bones", "Alice Sebold", "Drama", "Told from the perspective of a girl who was murdered", 2006, 15, 7),
            Buku("B095", "Water for Elephants", "Sara Gruen", "Historical Fiction", "A young man's experiences in a traveling circus during the Great Depression", 2010, 16, 7),
            Buku("B096", "A Thousand Splendid Suns", "Khaled Hosseini", "Drama", "The intertwining lives of two Afghan women", 2007, 12, 7),
            Buku("B097", "The Girl with the Dragon Tattoo", "Stieg Larsson", "Thriller", "Investigation into the decades-old disappearance of a wealthy industrialist's niece", 2008, 14, 7),
            Buku("B098", "The Help", "Kathryn Stockett", "Historical Fiction", "A story about African American maids working in white households in Jackson, Mississippi", 2010, 15, 7),
            Buku("B099", "Eat, Pray, Love", "Elizabeth Gilbert", "Memoir", "A woman's journey of self-discovery through travel", 2006, 16, 7),
            Buku("B100", "The Alchemist", "Paulo Coelho", "Fantasy", "A young Andalusian shepherd's journey in search of a worldly treasure", 2009, 18, 7),
        ]

        self.anggota = [
            Anggota("515239", "password", "Yumna Qurattu 'Aini"),
            Anggota("515288", "password", "Marsa Carol Dasilviana"),
            Anggota("515495", "password", "Alexander Justin Hartono"),
            Anggota("515529", "password", "Muhammad Fauzan"),
            Anggota("515963", "password", "Profit Dwi Nugroho"),
            Anggota("515992", "password", "Chaerunnisa Kayla Utami"),
            Anggota("516038", "password", "Defasya Zulsyifah Kanna"),
            Anggota("516054", "password", "Nazril Suandana Putu Wangfud"),
            Anggota("516928", "password", "Kesava Awal Akbari"),
            Anggota("516969", "password", "Novi Sushmita"),
            Anggota("517061", "password", "Abdul Hakeem Putra Porfiriko"),
            Anggota("517361", "password", "Pasha Akmal Ghifary"),
            Anggota("517491", "password", "Alan Jansen Situmorang"),
            Anggota("517551", "password", "Maullana Hidayanto"),
            Anggota("517563", "password", "Pandu Saputra"),
            Anggota("517590", "password", "Isa Maliki"),
            Anggota("517609", "password", "Satria Rezqi Maulana"),
            Anggota("517703", "password", "Dwi Nur Shaleh Slameto Aji"),
            Anggota("517799", "password", "Krisna Budhiantoro Mahdabakti Kusuma"),
            Anggota("518122", "password", "Dini Riyani Oktavia"),
            Anggota("518201", "password", "Saira Fatimah Azzahra"),
            Anggota("518225", "password", "Muhaimin Nur Rasyid"),
        ]
        
        self.admins = [
            Admin("admin1", "adminpass1"),
            Admin("admin2", "adminpass2")
        ]
            
        self.logged_in_user = None
        
        self.daftar_peminjaman = []

    def lihat_buku(self, genre=None, sort_by=None):
        pass
        
    def login(self, nis, password):
        for anggota in self.anggota:
            if anggota.nis == nis and anggota.password == password:
                return anggota
        return None
    
    def hapus_anggota(self):
        print("\033[94m" + "=== HAPUS ANGGOTA ===" + "\033[0m")
        nis = input("\033[95m" + "Masukkan NIS anggota yang akan dihapus: " + "\033[0m")

        anggota = self.perpustakaan.cari_anggota(nis)
        if anggota:
            self.perpustakaan.hapus_anggota(nis)
            print("\033[92m" + f"Anggota {anggota.nama} dengan NIS {nis} telah dihapus." + "\033[0m")
        else:
            print("\033[91m" + f"Tidak ditemukan anggota dengan NIS {nis}." + "\033[0m")

    def lihat_anggota(self):
        print("\033[94m" + "=== LIHAT ANGGOTA ===" + "\033[0m")
        for anggota in self.anggota:
            print(f"NIS: {anggota.nis}")
            print(f"Nama: {anggota.nama}")
            print("")
            
    def lihat_anggota_baru(self):
        print("\033[94m" + "=== LIHAT ANGGOTA ===" + "\033[0m")
        for anggota in self.anggota:
            print(f"NIS: {anggota.nis}")
            print(f"Nama: {anggota.nama}")
            print("")
    
    def edit_anggota(self, nis, nama_baru):
        anggota = self.cari_anggota(nis)
        if anggota:
            anggota.nama = nama_baru
            print("\033[92m" + f"Nama anggota dengan NIS {nis} berhasil diubah menjadi {nama_baru}." + "\033[0m")
        else:
            print("\033[91m" + f"Tidak ditemukan anggota dengan NIS {nis}." + "\033[0m")
    
    def edit_buku(self, kode_buku, judul_baru):
        buku = self.cari_buku(kode_buku)
        if buku:
            buku.judul = judul_baru
            print("\033[92m" + f"Judul buku dengan kode {kode_buku} berhasil diubah menjadi {judul_baru}." + "\033[0m")
        else:
            print("\033[91m" + f"Tidak ditemukan buku dengan kode {kode_buku}." + "\033[0m")
            
    def tambah_buku(self, buku):
        self.buku_list.append(buku)
        
    def hapus_buku(self, kode_buku):
        for buku in self.buku_list:
            if buku.kode.lower() == kode_buku.lower():
                self.buku_list.remove(buku)
                break
            
    def lihat_semua_buku(self, sorted_books=None):
        program = "-----SEMUA BUKU-----"
        str_program = program.center(104)
        
        print(Color.BLUE + '='*104 + Color.END)
        print(Color.PURPLE + Color.BOLD + str_program + Color.END)
        print(Color.BLUE + '='*104 + Color.END)
        
        if sorted_books is None:
            books_to_display = self.buku_list
        else:
            books_to_display = sorted_books

        for buku in books_to_display:
            print("\033[93m Kode          :      {}\033[0m".format(buku.kode))
            print("\033[92m Judul Buku    :      {}\033[0m".format(buku.judul))
            print("\033[91m Pengarang     :      {}\033[0m".format(buku.pengarang))
            print("\033[94m Genre         :      {}\033[0m".format(buku.genre))
            print("\033[96m Sinopsis      :      {}\033[0m".format(buku.sinopsis))
            print("\033[90m Tahun         :      {}\033[0m".format(buku.tahun))
            print("\033[95m Jumlah        :      {}\033[0m".format(buku.jumlah_buku))
            print("========================================================================================================")
            
            
    def sortir_buku(self, sort_by, reverse=False):
        if sort_by.lower() == "abjad":
            sorted_books = sorted(self.buku_list, key=lambda x: x.judul, reverse=reverse)
        else:
            sorted_books = sorted(self.buku_list, key=lambda x: getattr(x, sort_by.lower()), reverse=reverse)
        return sorted_books
    
    def genre_buku(self):
        if hasattr(self, 'buku_list'):
            # Jika daftar_buku sudah ada
            genres = set(buku.genre for buku in self.buku_list)
            return sorted(genres)
        else:
            print("\033[91mData buku tidak tersedia. Kembali ke Menu Anggota...\033[0m")
            return None
  
        return list(genres)
        
    def pengarang_buku(self):
        pengarangs = set()
        for buku in self.buku_list:
            pengarangs.add(buku.pengarang)

        return list(pengarangs)
        
    def cari_judul_buku(self, judul):
        found_books = [buku for buku in self.buku_list if judul.lower() in buku.judul.lower()]

        if not found_books:
            print("\033[91m" + f"Tidak ditemukan buku dengan judul '{judul}'." + "\033[0m")
        else:
            print("\033[94mBuku yang ditemukan:\033[0m")
            for i, buku in enumerate(found_books, start=1):
                print("\033[94m===============================================================================\033[0m")
                print("\033[93m Kode          :      {}\033[0m".format(buku.kode))
                print("\033[92m Judul Buku    :      {}\033[0m".format(buku.judul))
                print("\033[91m Pengarang     :      {}\033[0m".format(buku.pengarang))
                print("\033[94m Genre         :      {}\033[0m".format(buku.genre))
                print("\033[96m Sinopsis      :      {}\033[0m".format(buku.sinopsis))
                print("\033[90m Tahun         :      {}\033[0m".format(buku.tahun))
                print("\033[95m Jumlah        :      {}\033[0m".format(buku.jumlah_buku))
                print("\033[94m===============================================================================\033[0m")


            kembali_menu_anggota = input("\033[94mApakah Anda ingin kembali ke menu anggota? (y/n): " + "\033[0m").lower()
            system('cls')
            if kembali_menu_anggota != 'y':
                print(Color.YELLOW + """
            +-----------------------------------+
            |                                   |
            |           TERIMA KASIH !          |
            |           SAMPAI JUMPA            |
            |                                   |
            +-----------------------------------+
            """ + Color.END)             
                exit()
                
    def cari_judul_buku_dari_kode(self, kode_buku):
        for buku in self.buku_list:
            if buku.kode.lower() == kode_buku.lower():
                return buku.judul
        return None

    def cari_buku(self, kode_buku):
        for buku in self.buku_list:
            if buku.kode == kode_buku:
                return buku
        return None
        
    def cari_buku_dari_kode(self, kode_buku):
        for buku in self.buku_list:
            if buku.kode.lower() == kode_buku.lower():
                return buku
        return None

    
    def cari_peminjaman(self, nis, kode_buku):
        for peminjaman in self.daftar_peminjaman:
            if peminjaman['nis'] == nis and peminjaman['kode_buku'] == kode_buku:
                return peminjaman
        return None

    def pinjam_buku(self, nis, kode_buku, waktu_pengembalian):
        anggota = self.cari_anggota(nis)
        buku = self.cari_buku(kode_buku)

        if anggota and buku:
            if buku.jumlah_buku > 0:
                buku.jumlah_buku -= 1
                waktu_peminjaman = datetime.now()
                waktu_pengembalian = waktu_peminjaman + timedelta(days=7)
               

    def kembalikan_buku(self, nis, kode_buku):
        judul_buku = self.cari_judul_buku_dari_kode(kode_buku)
    
        if judul_buku:
            anggota = self.cari_anggota(nis)
    
            if anggota and kode_buku in anggota.buku_dipinjam:
                # Peminjaman ditemukan
                peminjaman = self.cari_peminjaman(nis, kode_buku)
                waktu_peminjaman = peminjaman['waktu_peminjaman']
                waktu_pengembalian = datetime.now()
                selisih_hari = (waktu_pengembalian - waktu_peminjaman).days
    
                if selisih_hari > 7:
                    denda = (selisih_hari - 7) * self.jumlah_hari_terlambat
                    print(f"Jumlah denda yang harus dibayar: Rp {denda}")
                else:
                    denda = 0
                    print("Tidak ada denda.")
    
                # Tambahkan informasi denda ke daftar peminjaman
                peminjaman['denda'] = denda
    
                # Hapus buku dari daftar buku yang dipinjam oleh anggota
                anggota.buku_dipinjam.remove(kode_buku)
    
                # Tambahkan buku yang dikembalikan ke daftar buku
                buku = self.cari_buku(kode_buku)
                buku.jumlah_buku += 1
    
                print(f"Anda telah berhasil mengembalikan buku {judul_buku}.")
            else:
                print(f"Anda tidak sedang meminjam buku {judul_buku} dengan kode {kode_buku}.")
        else:
            print(f"Tidak ditemukan buku dengan kode {kode_buku}.")


    def hitung_denda(self, nis, judul):
        anggota = self.cari_anggota(nis)
        buku = self.cari_buku(judul)

        if anggota and buku:
            hari_terlambat = int(input("Masukkan jumlah hari terlambat: "))
            denda_per_hari = 1000
            total_denda = max(0, (hari_terlambat - buku.lama_peminjaman) * denda_per_hari)
            return total_denda
        return None
    
    def tambah_anggota(self, anggota):
        self.anggota.append(anggota)
    
    def hapus_anggota(self, nis):
        for anggota in self.anggota:
            if anggota.nis == nis:
                self.anggota.remove(anggota)
                break
            
    def cari_anggota(self, nis):
        for anggota in self.anggota:
            if anggota.nis == nis:
                return anggota
        return None

class MenuUtama:
    def __init__(self, perpustakaan):
        self.perpustakaan = perpustakaan
        self.logged_in_user = None

    def tampilkan_menu(self):
        system('cls')
        while True:
            print(Color.PURPLE + Color.BOLD + """
            +-----------------------------+
            |        MENU UTAMA           |
            |-----------------------------|
            | [1] Log in Admin            |
            | [2] Log in Anggota          |
            | [3] Keluar                  |
            +-----------------------------+
            """)

            pilihan = input("Pilih menu (1-3): " + Color.END)

            if pilihan == "1":
                self.login_admin()
            elif pilihan == "2":
                self.login_anggota()
            elif pilihan == "3":
                konfirmasi = input("\033[93mApakah Anda yakin ingin keluar? (y/n): \033[0m").lower()
                if konfirmasi == 'y':
                    system('cls')
                    print(Color.YELLOW + """
            +-----------------------------------+
            |                                   |
            |           TERIMA KASIH !          |
            |           SAMPAI JUMPA            |
            |                                   |
            +-----------------------------------+
                                    """ + Color.END)
                    exit()
                elif konfirmasi == 'n':
                    system('cls')
                else:
                    print("\033[91mPilihan tidak valid. Silakan coba lagi.\033[0m")   
            else:
                print("\033[91mPilihan tidak valid. Silakan coba lagi.\033[0m")  


    def login_admin(self):
        system('cls')
        program = "-----LOGIN ADMIN-----"
        str_program = program.center(60)
        
        print(Color.BLUE + '='*60 + Color.END)
        print(Color.PURPLE + Color.BOLD + str_program + Color.END)
        print(Color.BLUE + '='*60 + Color.END)  
      
        username = input("\033[95m  Masukkan user      : \033[0m")
        password = input("\033[95m  Masukkan password  : \033[0m")
        system('cls')
        
        for admin in self.perpustakaan.admins:
            if username == admin.username and password == admin.password:
                program = "-----SELAMAT DATANG-----"
                admin_text = admin.username
                str_program = program.center(70)
                str_admin = admin_text.center(70)
    
                print(Color.BLUE + '='*70 + Color.END)
                print(Color.PURPLE + Color.BOLD + str_program + Color.END)
                print(Color.YELLOW + str_admin + Color.END)
                print(Color.BLUE + '='*70 + Color.END)
    
                menu_admin = MenuAdmin(self.perpustakaan, admin)
                menu_admin.tampilkan_menu_admin() 
                return True

        print(Color.RED + f"Login Admin Gagal, Akses ditolak!" + Color.END)
        return False

    def login_anggota(self):
        system('cls')
        program = "-----LOGIN ANGGOTA-----"
        str_program = program.center(60)
        
        print(Color.BLUE + '='*60 + Color.END)
        print(Color.PURPLE + Color.BOLD + str_program + Color.END)
        print(Color.BLUE + '='*60 + Color.END)  
      
        nis = input("\033[95m  Masukkan NIS       : \033[0m")
        password = input("\033[95m  Masukkan password  : \033[0m")
        system('cls')
        MenuAnggota(self.perpustakaan).login_anggota(nis, password)
        
# Membuat objek Perpustakaan
perpustakaan = Perpustakaan()

# Menampilkan menu utama
menu_utama = MenuUtama(perpustakaan)
menu_utama.tampilkan_menu()



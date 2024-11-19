# Nama : Nur Salsabiyla Arzi
# Capstone Project untuk modul 1 - Data Siswa


dataSiswa =[
{
'Nim': 301,
'Nama': 'Lala',
'Kelas': 'A',
'Jenis Kelamin': 'Perempuan',
'Agama': 'Islam'
},
{
'Nim': 302,
'Nama': 'Andi',
'Kelas': 'C',
'Jenis Kelamin': 'Laki-Laki',
'Agama': 'Hindu'
},
{
'Nim': 303,
'Nama': 'Sari',
'Kelas': 'C',
'Jenis Kelamin': 'Perempuan',
'Agama': 'Katolik'
},

]

                     
#Pilihan Untuk  menampilkan Seluruh Data Siswa
def DataSiswa():
    print('''
                = = = = = Report Data Siswa = = = = = 
                      = = = = Siswa Sains Data = = = =\n''')
    
    print('''No \t| Nim \t| Nama  \t\t| Kelas\t| Jenis Kelamin\t | Agama''')
    for i in range(len(dataSiswa)):
     print('{} \t| {} \t| {}  \t\t| {} \t| {}    \t | {}'.format(i+1,dataSiswa[i]['Nim'],dataSiswa[i]['Nama'],dataSiswa[i]['Kelas'],dataSiswa[i]['Jenis Kelamin'],dataSiswa[i]['Agama']))

#Pilihan Menu No. 1 Report Data  Siswa (Read)
def MenuDataSiswa():
    while True:
        print('''
        ===== Menu Report Data Siswa =====
        
              
        1. Menampilkan semua Data Siswa
        2. Menampilkan Data Siswa tertentu
        3. Kembali ke Menu Utama\n''')


        SubMenu = int(input('''Silahkan pilih daftar di atas [1-3] : '''))
        if SubMenu == 1:
           DataSiswa()
        elif SubMenu == 2:
            UnikData()
        elif SubMenu == 3:
            Menu_Awal()
        else:
            print(' Anda memasukkan pilihan yang salah\nSilahkan masukkan pilihan Menu yang benar (1-3): ')    
            continue
# Pilihan No 1.2 Menampilkan Data Siswa tertentu
def UnikData():
    inputNim = int(input('''
       Masukkan Nim Siswa :   ''' ))       
    for i in range (len(dataSiswa)):
        if inputNim == dataSiswa[i]['Nim']:
            print(f'''\n\t\t=== Data Siswa ditemukan ===\n
    === Siswa dengan Nim : {inputNim} datanya adalah sebagai berikut ===\n    
              === Daftar SiSwa Sains Data ===\n''')  
            print('''No \t| Nim \t| Nama  \t\t| Kelas\t| Jenis Kelamin\t | Agama''')
            print('{} \t| {} \t| {}  \t\t| {} \t| {}   \t | {}'.format(i+1,dataSiswa[i]['Nim'],dataSiswa[i]['Nama'],dataSiswa[i]['Kelas'],dataSiswa[i]['Jenis Kelamin'],dataSiswa[i]['Agama']))
            break
        elif (i == len(dataSiswa)-1) and (inputNim != dataSiswa[i]['Nim']):
            print('''\n\t\t=== Daftar Siswa tidak ditemukan ===''')

#Pilihan Menu No.2 Menambahkan Data Siswa (create)  
def TambahData ():
    while  True:
        CreateDataSiswa = input('''
        ===== Menu Menambah Data Siswa =====
                                  
            1. Tambah data siswa 
            2. Kembali ke menu utama  
                                  

        Silahkan pilih menu update data diatas [1-2] : ''')                                                                                                    

        if CreateDataSiswa == '1':
            DataSiswa()
            NimSiswa = int(input('\nMasukkan Nim baru : '))
            for i in range(len(dataSiswa)):
                if NimSiswa == dataSiswa [i]['Nim']:
                        print('''
                === Data Siswa sudah ada di Database ===
                === Silahkan masukkan data baru ===''') 
                        TambahData()
                elif (i == len(dataSiswa)-1) and NimSiswa != dataSiswa[i]['Nim']:
                     NamaSiswa = input('Nama : ').capitalize() 
                     KelasSiswa = input('Kelas : ').capitalize() 
                     JenisKelaminSiswa = input('Jenis Kelamin : ').capitalize() 
                     AgamaSiswa = input('Agama : ').capitalize() 
                     break
            Konfirmasi = input('''
                === Apakah data ini akan ditambahkan (Y/T)?:  ''').capitalize()
            if Konfirmasi == 'Y':
                dataSiswa.append({
                    'Nim': NimSiswa,
                    'Nama': NamaSiswa,
                    'Kelas': KelasSiswa,
                    'Jenis Kelamin': JenisKelaminSiswa,
                    'Agama': AgamaSiswa
                    })
                print('\n=== Data Siswa berhasil ditambahkan ===')
                DataSiswa()
                TambahData()
                continue
            elif Konfirmasi == 'T':
                 print('\n=== Data siswa tidak jadi ditambahkan ===')
                 TambahData()
            else:
                    print('''\n=== Pilihan yang anda masukkan salah ===
                === Silahkan masukkan kembali pilihan yang benar (Y/T):''')   
            TambahData()  
        elif CreateDataSiswa == '2':
          Menu_Awal()
        else:
           print('''
        === Pilihan yang anda masukkan salah ===
        === Silahkan masukkan kembali pilihan yang benar (1-2):''')
           continue  
#Pilihan Menu No. 3 Mengubah Data Siswa (Update)
def UpdateData():
    while True:
        UpdateDataSiswa = input('''
        ===== Menu Ubah Data Siswa =====
                                
            1. Ubah data siswa
            2. Kembali ke menu utama
        Silahkan pilih menu update data diatas [1-2]: ''')

        if UpdateDataSiswa == '1':
            DataSiswa()
            NimSiswa = (int(input('\n\t=== Masukkan Nim Siswa: ')))
            for i in range (len(dataSiswa)):
                if NimSiswa == dataSiswa[i]['Nim']:
                    while True:
                        print('''
                        === Data Siswa ditemukan ===\n''')
                        print('''No. \t|Nim \t| Nama  \t| Kelas\t| Jenis Kelamin\t| Agama''')   
                        print(f'''{i+1} \t| {dataSiswa[i]['Nim']} \t| {dataSiswa[i]['Nama']}  \t|{dataSiswa[i]['Kelas']} \t| {dataSiswa[i]['Jenis Kelamin']} \t| {dataSiswa[i]['Agama']}''')
                        konfirmasi = input('''
                        === Apakah data ingin diubah (Y/T)?: ''').capitalize()
                        if konfirmasi == 'Y' :
                            ubah_kolom = input('Pilih kolom yang ingin di ubah (Nim, Nama, Kelas, Jenis Kelamin, Agama): ').lower()
                            if ubah_kolom == dataSiswa[i]['Nim'] :
                               ubah_kolom = ubah_kolom.upper() 
                            else:
                                ubah_kolom = ubah_kolom.capitalize()   
                            ubah_isi = input(f'Masukkan {ubah_kolom} baru : ').capitalize()  
                            while True:
                                konfirmasi1 = input('Apakah data jadi diubah(Y/T): ').capitalize() 
                                if konfirmasi1 == 'Y':
                                    dataSiswa[i][ubah_kolom] = ubah_isi 
                                    print('''
                                \n\t\t=== Data sudah diubah ===''')
                                    DataSiswa()
                                    UpdateData()
                        elif konfirmasi == 'T':
                            UpdateData()
                        else:
                            print('Masukkan (Y/T)') 
                            break
                elif (i == len(dataSiswa)-1) and (NimSiswa != dataSiswa[i]['Nim']) :
                    print('''
                    === Data siswa tidak ditemukan ===''')

        elif UpdateDataSiswa == '2':
            Menu_Awal() 
        else:
           print('''
        === Pilihan yang anda masukkan salah ===
        === Silahkan masukkan kembali pilihan yang benar (1-2):''')
           continue  

#Pilihan Menu No. 4 Menghapus Data Siswa (Delete)
def DeleteData ():
    while True:
        DeleteDataSiswa = input('''
        ==== Menu Menghapus Data Siswa ====
                                
           1. Hapus data siswa
           2. Kembali ke menu utama
        Silahkan pilih menu hapus data diatas [1-2] : ''')    

        if DeleteDataSiswa == '1':
            DataSiswa()
            NimSiswa = (int(input('\n\t=== Masukkan Nim Siswa: ')))
            for i in range(len(dataSiswa)):
                if NimSiswa == dataSiswa[i]['Nim']:
                    while True:
                        print('''
                        === Data Siswa ditemukan ===\n''')
                        print('''No. \t|Nim \t| Nama  \t| Kelas\t| Jenis Kelamin\t|Agama''')   
                        print(f'''{i+1} \t| {dataSiswa[i]['Nim']} \t| {dataSiswa[i]['Nama']}  \t|{dataSiswa[i]['Kelas']} \t| {dataSiswa[i]['Jenis Kelamin']} \t| {dataSiswa[i]['Agama']}''')
                        konfirmasi = input('''
                        === Apakah data ingin dihapus (Y/T)?: ''').capitalize()
                        if konfirmasi == 'Y':
                                del dataSiswa[i]
                                print(f'''=== Data siswa dengan Nim : {NimSiswa} berhasil dihapus ===''')
                                DataSiswa()
                                DeleteData()
                        elif konfirmasi == 'T':
                             DeleteData()
                        else:
                            print('Masukkan (Y/T)') 
                            break
                elif (i == len(dataSiswa)-1) and (NimSiswa != dataSiswa[i]['Nim']) :
                    print('''
                === Data siswa tidak ditemukan ===\n''')
                    
        elif DeleteDataSiswa == '2':
            Menu_Awal()            
        else:
            print('''
    === Pilihan yang anda masukkan salah ===
    === Silahkan masukkan pilihan yang benar (1-2): ''')
            continue

#MENU UTAMA:
def Menu_Awal():
    print('''
= = = = = Daftar Pilihan : = = = = =

    1. Report Data Siswa 
    2. Menambahkan Data Siswa                      
    3. Mengubah Data Siswa
    4. Menghapus Data Siswa
    5. Exit ''')

    while True :
        PilihanMenu = input('\nMasukkan nomor yang dipilih (1-5): ')
        if PilihanMenu == '1' :
            MenuDataSiswa()
        elif PilihanMenu == '2' :
            TambahData()
        elif PilihanMenu == '3' :
            UpdateData()
        if PilihanMenu == '4' :
            DeleteData()
        if PilihanMenu == '5' :
          print('\n=== Terima Kasih :) ===\n')
          exit()
        else:
            print('Pilihan yang anda masukkan salah\nSilahkan masukkan pilihan menu yang benar (1-5)')   
Menu_Awal()               
        
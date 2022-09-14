# Tugas 2

Link Heroku: [Heroku](https://katalog-shafanajwa.herokuapp.com/katalog)

## 1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya

[![pbp.png](https://i.postimg.cc/Bb0w1bXz/pbp.png)](https://postimg.cc/jwMhps66)

Client memberi request ke server yang akan diterima oleh url lalu request diteruskan ke Django. Dilanjutkan proses ke views.py yang akan memproses mapping URL di file `urls.py`. Fungsi di `views.py` memanggil query dari models yang ada di `models.py`. Jika sudah selesai diproses, hasil akan dirender dari berkas HTML (template yang sudah ada), lalu response akan diterima kembali oleh Client.

## 2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment digunakan agar tidak terjadi tabrakkan dengan versi lain proyek yang ada di komputer kita (dapat menyebabkan error). Virtual environment akan mengisolasi dependency yang ada di proyek. Namun, aplikasi tetap dapat berjalan tanpa virtuan environment, dengan syarat dependency yang ada di global environment sesuai dengan aplikasi web berbasis Django yang dibuat.

## 3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

### views.py
Pada file `views.py`, function dibuat untuk mengambil data yang ada dari model (disimpan dalam context), dan menerima argumen request. Variabel seperti nama dan npm serta data yang ditampilkan akan dirender ke template HTML menggunakan fungsi render.

### urls.py
Pada file `urls.py` routing dilakukan berdasarkan fungsi yang ada (diimport) dari views.py. Path aplikasi didaftarkan pada urlpatterns agar HTML dapat ditampilkan kepada Client.

### katalog.html
Pada file template HTML ini, dilengkapi looping untuk mengambil data katalog yang disimpan ke variabel. Dengan satu baris HTML <`tr`>.

## Deploy
Dalam bagian deployment, akun Heroku disambungkan ke repository Github dengan `HEROKU_API_KEY` dari akun dan `HEROKU_APP_NAME` yaitu nama aplikasi yang dibuat di Heroku. Info ini diatur di dalam settings secrets untuk tab Actions Github (workflow).

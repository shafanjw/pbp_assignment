# To Do List 👋

Link Heroku App : [ShafaTodolist](https://shafatodolist.herokuapp.com/todolist)
## Apa Kegunaan {% csrf_token %} ? Bila tidak ada kode tersebut apa yang terjadi?
Potongan kode tersebut berguna apabila kita ingin memastikan sebuah _request_. Apabila token yang masuk tidak sesuai dengan yang dihasilkan, maka request akan ditolak. Sementara apabila _request_ tersebut cocok maka akan diterima.
Apabila tidak ada potongan kode tersebut, maka orang lain dapat mengakses ke link href tersebut dan membajak data kita (melakukan delete account maupun logout maupun add todolist) dan lain-lain di luar kemauan kita.

## Apakah kita dapat membuat elemen secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat secara manual.
Bisa, tanpa menggunakan generator form as table. Kita dapat menggunakan method POST lalu dengan tag <table> dan <form> memungkinkan kita untuk memasukkan kebutuhan seperti teks, opsi button, dan lain-lain. Kemudian form akan dapat diisi dengan <input> untuk memasukkan elemen seperti username, password, dll. Setelah itu form akan dikembalikan ke fungsi parentnya. Dibuat <input type="submit"> untuk proses submit form.
 
## Jelaskan Proses Alur Data dari submisi pengguna dari _form_, penyimpanan dadta pada database, hingga munculnya data pada template HTML

Data yang disubmisi pengguna dapat diakses dengan POST dan setelah itu dicek validitasnya dengan token. Data disimpan, dengan kita mengakses data tersebut dengan "Models.objects.create(data input)" sesuai user name yang kita buat di models.py.
 Laludata  akan dimasukkan ke dalam databaes dan diakses dengan `Models.objects.filter(user=request.user)`. Difilter sesuai dengan user yang sedang mengakses, dan kemudian akan dimasukkan ke context pada fungsi views
  Agar dapat dirender ke template HTML. Lalu object dilooping agar dapat menampilkan setiap data yg ingin ditampilkan.

## Penjelasan Cara Implementasi Checklist
1. Buat aplikasi baru django dengan command startapp todolist
2. Mendaftarkan path aplikasi todolist pada urls.py di project django saya
3. Mengatur models.py dan membuat kelas Task yg berisi field yg sesuai yaitu user, date, title, description.
4. Pada views.py, menambahkan fungsi untuk keperluan login logout dan register, dan juga untuk bonus yaitu mengubah status.
5. Membuat template html todolist lalu menambahkan username pengguna dengan {{username}} pada context. Membuat beberapa tombol dan input serta table yang berisi data2 todo list.
6. Membuat addtodo htmll untuk menambahkan task to do list pengguna berupa title dan description
7. Melakukan migrasi dengan make migrations dan migrate
8. Mendaftarkan fungsi yang dibuat ke path urls.py dalam direktori app todolist
9. Melakukan git add, commit, dan lalu push dan lalu app akan terdeploy melalui actions di GitHub pada Heroku
10. Buat 2 akun pengguna dan tiga dummy data

# To Do List Responsive Modification (Tugas 5)
## ---------------------------------

## Perbedaan dari Inline, Internal, dan External CSS serta Kelebihan dan kekurangan dari masing-masing style
Inline merupakan metode yang digunakan untuk tag HTML dengan atribut <style>, yang ada di masing masing tag HTML. 
- __Kelebihannya__ adalah lebih mudah untuk mengubah tag HTML tertentu, lalu apabila dibutuhkan request HTTP yang kecil, lebihi efisien.
- __Kekurangannya__ terletak pada keharusan untuk mengisi setiap tag HTML, serta tidak efisien dalam pembuatan web skala besar.

Internal CSS merupakan metode yang digunakan dengan mendefinisikan <style> pada halaman HTML itu sendiri.
- __Kelebihannya__ terletak pada tidak memerlukan proses download file eksternal serta upload file eksternal CSS, serta perubahannya dapat dilihat dengan mudah karena terjadi pada halaman itu saja
- __Kekurangannya__ yaitu CSS hanya dapat digunakan dalam satu file HTML, tidak dapat digunakan pada file HTML lainnya, serta tidak efisien dalam pembuatan web skala besar.

External CSS merupakan metode yang digunakan untuk memberi atribut <style> pada seluruh tag HTML dengan memberi sebuah file eksternal di bagian awal HTML. Ini memungkinkan perubahan yang diberikan pada tag untuk ditampilkan oleh setiap file HTML yang mengupload file CSS pada bagian awal file HTMLnya.
- __Kelebihannya__ terletak pada file HTML yang dapat dibaca dengan mudah karena minim pendefinisian tag serta atribut. Lalu file CSS dapat digunakan dengann mudah untuk setiap file HTML. External CSS juga efektif dalam pemabgnunan web skala besar.
- __Kekurangannya__ terletak pada sulitnya melakukan _debugging_ apabila ada potongan pode yang salah. File CSS harus dapat dipanggil sebellum halaman web dapat ditampilkan.

 
## Tag HTML5
- `<h1>` - `<h6>` , digunakan sebagai header, semakin tinggi angka pada h, semakin kecil ukuran tulisannya.
- `<table>`, tag ini untuk mendefinisikan tabel data.
- `<p>`, digunakan untuk mendefinisikan paragraf.
- `<a>`, tag ini digunakan untuk menambahkan _hyperlink_ .
- `<button>`, tag ini untuk mendefinisikan tombol.
- `<title>`, digunakan untuk mendefinisikan judul.
- `<b>`, digunakan untuk mengubah text menjadi _bold_ .
- `<div>`, sebagai _container bagian halaman pada file HTML.

## Tipe-tipe CSS Selector

- ID Selector, yaitu untuk mendefinisikan elemen HTML tertentu. Digunakan '#' lalu diikuti ID.
- Class selector, berfungsi untuk mendefinisikan class HTML tertentu untuk menambah _style_.
- Type Selector, untuk mendefinisikan tag HTML.
- Element Selector, untuk mendefinisikan style dengan tag _selector_.

## Penjelasan Implementasi Checklist
1. Menggunakan library tailwind untuk _styling_ app todolist. Melakukan _install_ tailwind-django, [link](https://django-tailwind.readthedocs.io/en/latest/installation.html).
2. Melakukan pip freeze untuk requirements.txt yaitu dependencies yang dibutuhkan agar bisa dideploy ke Herokuapp.
3. Melakukan Import Bootstrap untuk file HTML di template root file.
```
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js%22%3E"> </script>
```
4. Melakukan perubahan kepada file HTML template login, register, todolist, dan addtodo. Perubahan dilakukan dengan mendefinisikan atribut untuk tag Inline CSS dan Internal CSS.
5. Inspirasi penyajian card untuk page utama todolist dari bootstrap yaitu dari [link](https://getbootstrap.com/docs/4.3/components/card/)
6. Menambahkan responsive page dengan pendefinisian .submit-hover.

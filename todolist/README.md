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

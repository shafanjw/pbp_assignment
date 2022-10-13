# Todolist dengan AJAX (TASK 6)

## Perbedaan *asynchronous* dan *synchronous programming*
---
Synchronous yaitu operasi dikerjakan secara terurut, apabila suatu pekerjaan dikerjakan secara synchronus pada komputer, maka komputer harus menunggu pekerjaan satu selesai untuk mulai menjalankan operasi selanjutnya. Sedangkan asynchronus berarti operasi dapat dikerjakan secara tak berurut. Komputere tidak harus menunggu suatu pekerjaan satu selesai untuk mulai menjalankan pekerjaan selanjutnya. Penggunaan asynchronus programming pada *website* tepat, agar pengguna tidak perlu menunggu dan mereload suatu operasi untuk selesai untuk dapat menjalankan operasi yang lain.


## Penerapan Paradigma *Event-Driven Programming Paradigm*
---
Event-Driven Programming yaitu paradigma dalam pemrograman di mana pekerjaan yang dijalankan tergantung kepada event yang terjadi. Contoh event yang dimaksud yaitu seperti "onClick", "onSubmit", dan lain-lain. Event tersebut dapat dihubungkan dengan fungsi apabila event terjadi.

Salah satu contoh penerapannya pada tugas ini yaitu:
1. On #Hapus click
    
js
    <a class="btn login_btn btn btn-danger form-control lg mt-2" onclick="deleteTask(${i.pk})">Hapus</a>
    
    Pada kasus ini, saat button Hapus diclick, fungsi deleteTask akan dijalankan untuk menghapus task yang ada dengan menggunakan AJAX request.

2. On #tambahTask submit
    
js
    $(document).on("submit", "#tambahTask", function(e) {
        e.preventDefault();
        $.ajax ({
            url: "{% url 'todolist:add_ajax' %}",
            type: "POST",
            dataType:"json",
            data: {
                title:$("#title").val(),
                description:$("#description").val(),
                csrfmiddlewaretoken: "{{ csrf_token }}"
            },
            success: function(data) {
                show_card();
                const inputs = document.querySelectorAll('#title, #description');
                inputs.forEach(input => {
                    input.value = '';
                });
            }
        })
    })
    
    Pada saat #tambahTask di-submit, fungsi tersebut akan mencegah laman web melakukan refresh dan melakukan AJAX call untuk membuat task baru.

## Penerapan asynchronous programming pada AJAX
---

Dalam AJAX, pada pengiriman request dilakukan asynchronous programminng.
Saat AJAX Request dilakukan, request akan berjalan di belakang layar sehingga user dapat melakukan operasi lain tanpa harus menunggu request tersebut selesai. Lalu, setelah request berhasil dikirim dan respon didapatkan, dilakukan fungsi yang dihubungkan untuk menangani respon yang didapat tersebut.

## Langkah implementasi checklist di atas

---
- Membuat fungsi baru pada views.py untuk memperoleh data semua task di models.py dalam representasi json dan menghubungkannya dengan url
- Membuat fungsi get data dengan AJAX pada html todolist. Lalu akan ditampilkan data dari url yang sudah dihubungkan dalam representasi JSON.
- Membuat new task modal pada todolist.html, sehingga setelah mengklik tombol Create Task, akan menuju target modal.
- Membuat modal dengan template pada Bootstrap.
- Membuat views baru untuk menambahkan data saat Create Task modal disubmit menggunakan AJAX *asynchronous*.
- Membuat fungsi AJAX pada todolist.html dengan POST untuk create new data dari user.
- Membuat fungsi delete task dengan AJAX dan melakukan update laman web secara *asynchronous*.
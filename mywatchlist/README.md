# Assignment 3 PBP

- HTML: https://shafawatchlist.herokuapp.com/mywatchlist/html/
- XML: https://pbp22t2.herokuapp.com/mywatchlist/xml
- JSON: https://pbp22t2.herokuapp.com/mywatchlist/json

## Perbedaan XML, HTML dan JSON

- XML dan HTML adalah markup language, sedangkan JSON notasi objek.
- HTML digunakan untuk menampilkan dokumen di browser, sedangkan XML dan JSON digunakan untuk data.
- XML dan HTML relatif lebih berat daripada JSON.
- XML dan HTML dapat diakses menggunakan DOM, sedangkan JSON diakses seperti key-value pair.

## Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery diperlukan sebab suatu aplikasi perlu melakukan pertukaran data dengan server. Sebab seringkali
data yang diberikan bersifat dinamis, yaitu dapat berubah dengan waktu karena terdapat pengguna yang mengganti
data tersebut (baik melalui server atau aplikasi tersebut). Dengan data delivery ini, data yang diberikan
selalu mencerminkan dengan data terbaru yang ada di server.

## Bagaimana cara mengimplementasikan checklist di atas.

1. Buat app baru Django dengan command `python manage.py startapp mywatchlist`.
2. Tambah aplikasi yang dibuat ke INSTALLED_APPS di `project_django/settings.py`
3. [Create data models in `mywatchlist/models.py`](https://github.com/shafanjw/pbp_assignment/blob/main/mywatchlist/models.py)
4. [Add data to fixtures folder](https://github.com/shafanjw/pbp_assignment/tree/main/mywatchlist/fixtures)
6. Do migration of data, with `python manage.py makemigrations` dan melakukan migration dengan `python manage.py migrate`
7. Load data fixtures, `python manage.py loaddata initial_watchlist.json`

## Postman

### HTML

[![html.jpg](https://i.postimg.cc/90xL8ngN/html.jpg)](https://postimg.cc/Lg1khNpz)

### JSON

[![json.jpg](https://i.postimg.cc/y6rhGcY5/json.jpg)](https://postimg.cc/WtgJFDZ6)

### XML

[![xml.jpg](https://i.postimg.cc/jSyzC1Q0/xml.jpg)](https://postimg.cc/0z26BcBc)

# Assignment 3 PBP

- HTML: https://shafawatchlist.herokuapp.com/mywatchlist/html/
- XML: https://shafawatchlist.herokuapp.com/mywatchlist/xml/
- JSON: https://shafawatchlist.herokuapp.com/mywatchlist/json/

## Perbedaan XML, HTML dan JSON

XML dan HTML lebih berat daripada JSON karena lebih detil dan bisa memuat banyak language, sedangkan JSON berupa objek. XML dan HTML juga dapat diakses dengan dom, sedangkan JSON diakses key-valuenya. HTML is used to show document in browser, sementara XML dan JSON untuk data.

## Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Karena sebuah aplikasi perlu menukar data dengan server. Kadangkala, data yang diberikan dapat berubah sewaktu-waktu karena terdapat yang mengganti data tersebut melalui server maupun aplikasi. Deengan adanya data delivery, data yang ditampilkan selalu data terbaru yang tersedia di server.

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

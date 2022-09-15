# Tugas 2 : Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Creator
Nama : Gabriel Zebaoth Krisopras Putra  

NPM : 2106751480

Kelas : PBP-D

## Output Tugas
Berikut adalah link hasil pengerjaan tugas saya.
[Heroku Link](https://gabing-pbp-tugas2.herokuapp.com/)


# Penjelasan tentang Django MVT *Software Design Pattern*

## Apa itu MVT ?

MVT adalah sebuah arsitektur software design pattern yang digunakan oleh Django sebagai web framework. MVT adalah singkatan dari *Model*, *View*, dan *Template*.

- **Models** ini merupakan salah satu sumber informasi dan data berkaitan dengan proyek Anda. Data yang disimpan di models ini dapat dimuat sebagai tampilan antarmuka yang dapat diakses oleh client. Models juga menentukan struktur data apa yang disimpan selama proyek dikembangkan. Struktur data yang dimaksud adalah seperti, ukuran maksimum, nilai default, opsi pilihan, dan lain sebagainya. Dalam hal komunikasi data, pengembang tidak perlu tahu kerumitannya, Django akan menangani hal tersebut secara otomatis. Django menyediakan  *automatically-generated database-access API* untuk menangani hal tersebut. Tambahan, setiap model merupakan subclass dari Django.db.models.Model. Setiap atribut  dari class tersebut merepresentasikan database field yang telah dikonfigurasi sebelumnya.
- **Views** merupakan penghubung antara Model dan Template. Dalam bagian ini, ada beberapa fungsi Python yang menerima permintaan web dan mengembalikan respons web. Respon untuk klien di web dapat berupa HTML, XML, Error 404, Gambar, Form, Video, dan lainnya. Konfigurasi views dapat dilihat melalui file views.py di bagian folder proyek Django. Ketika pengguna mengunjungi url website kita, views memanggil fungsi yang terkait dengan url tersebut dan melakukan serangkaian proses di back-end untuk mengambil data dari model dan memberikan respon, dapat berupa html, xml, csv, atau sejenisnya. 
- **Template** menangani semua bagian statis dari sebuah halaman web. Template dapat menghasilkan text-based format (HTML, XML, CSV, dan sebagainya)  kepada client web. Template mengandung variabel yang biasanya digantikan oleh sebuah nilai dan juga tags untuk mengatur logika dari template ini.
  



## Bagaimana Cara Kerja Django ?
![MVT diagram](/images/django-mvt-diagram.png)
1. Client akan melakukan request melalui pengaksesan URL pada website. URL akan memilih views yang cocok dengan request client.
2. Views akan menghubungkan request ke template. Namun, views perlu memastikan apakah ada data yang perlu diambil dari model. Jika ada, views akan meminta *QuerySet* ke model. 
3. Models akan membuat struktur data sesuai *request*. Models akan melakukan data transaksi dengan *database*. Models akan mengambil data yang dibutuhkan sesuai permintaan views. Kemudian, data tersebut dikirim ke views.
4. Views akan memilih templates .html  yang tepat untuk ditampilkan ke halaman web sebagai respon atas pengaksesan URL.

## Bagaimana dengan Struktur Django ?
### **Django Project**
Dango telah memiliki sebuah template agar penggunanya tidak perlu membuat website dari awal. Nah, untuk belajar lebih lanjut tentang Django. Kita perlu tahu struktur dari Django itu sendiri.

Project di Django merupakan paket python yang merepresentasikan keseluruhan web aplikasi. Project Django mempunya konfigurasi dan pengaturan terkait dengan webnya. Dalam sebuah project, ada beberapa App yang digunakan untuk fungsionalitas tertentu.

Dalam sebuah website yang menggunakan framework Django, hierarki atau struktur filenya adalah sebagai berikut.
```shell
# ...\Django_website
   \ env				   <= virtual environment
   \django_project         <= ini adalah Django project
   \django_app1            <= ini adalah Django app
   \django_app2 	       <= ini adalah Django app
      db.sqlite3           <= Database
      manage.py            <= Django project management utility

   ```
Kemudian, file yang terdapat pada django_project adalah sebagai berikut.

```shell
# \mywebsite\project_django\
\project_django
    __init__.py
    asgi.py 
    settings.py
    urls.py
    wsgi.py
```
- **\_\_init\_\_.py** memberitahu Python bahwa folder ini adalah paket python.
- **asgi.py** memunginkan server web yang kompatibel dengan ASGI dapat memuat website.
- **settings.py** berisi pengaturan untuk proyek Django
- **urls.py** berisi pengaturan router URL pada website.
- **wsgi.py** memungkinkan server web yang kompatibel dengan WSGI dapat memuat website.

### **Django App**
Aplikasi Django merupakan submodul dari project yang dibuat untuk mengimplementasikan sebuah fungsionalitas tertentu. Django-app bisa berjumlah banyak dan dapat disesuaikan dengan kebutuhan.

Setiap aplikasi yang dibuat perlu dihubungkan dengan projek Django. Hal ini dapat dilakukan dengan mengkonfigurasi file settings.py.
```shell
INSTALLED_APPS = [
   'events.apps.EventsConfig',
   'Django.contrib.admin',
   # tambahkan nama aplikasi disini
]

```
Adapun untuk struktur dari sebuah django_app adalah sebagai berikut.
```shell
\django_app
    \migrations
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```

- **migrations** adalah tempat Django menyimpan migrasi model, atau perubahan ke database. 
- **\_\_init\_\_.py**  menyatakan bahwa ini merupakan paket python.
- **admin.py**  tempat Anda mendaftarkan model dengan aplikasi admin Django.
- **apps.py** file konfigurasi umum untuk aplikasi Django.
- **models.py** file models untuk aplikasi ini.
- **tests.py** file testing untuk pengujian aplikasi.
- **views.py** file untu mengkonfigurasikan models dan templates.

## Django URLConf dan Views 
Django memungkinkan pengembang untuk membuat skema URL yang bersih dan elegan. Setiap aplikasi di proyek Django memiliki sebuah URL. Proyek Django dapat dihubungkan dengan aplikasi lain dengan menggunakan sebuah modul bernama URLconf. Modul ini berfungsi untuk memetakan jalur URL sesuai dengan Views .Di dalam views, ada fungsi-fungsi tertentu untuk menampilkan laman web yang kode filenya terdapat di template. Tampilan dikirim melalui HttpResponse.

> **Bagaimana kedua hal tersebut dapat bekerja?**
1. Client request ke internet untuk membuka URL dari website Django.
2. Internet request ke URLConf sesuai dengan alamat yang dikunjungi.
3. Django akan menentukan modul root URLconf yang akan digunakan
4. Kemudian, Django akan mencari variabel di urlpatterns dari modul tersebut.
5. Ketika pola URL cocok dengan variabel di urlpatterns. Django mengimpor dan memanggil views. 
6. emudian, views akan menghubungkan models dan templates.Lalu, tampilan HTML yang telah dirender akan disajikan kepada client.
7. Ketika tidak ditemukan pola URL yang cocok, Django akan memberitahu client tampilan *error* / penanganan kesalahan.

## Django Views and Templates

Django template adalah sebuah text document atau penandaan python string menggunakan Django template language. Beberapa dibangun dengan menggunakan template engine.DI Django template, kita akan banyak menjumpai variables and tags. 

Template di render dengan sebuah context. Context biasanya dapat diatur di views. Tahapan rendering mengganti variabel yang tertulis di template dengan data yang tersimpan di models.

Proses yang terjadi antara views dan template adalah sebagai berikut.
1. Ada request dari client ke internet untuk mengakses URL website Django.
2. Request tersebut juga akan diteruskan ke dalam Proyek Django.
3. Django akan memeriksa URL yang diakses oleh client apakah ada di urlpatterns > urls.py.
4. Kemudian, Django akan mengekstraksi argumen dari request ke views.  
5. Jika terdapat path di urlpatterns, maka Django akan memeriksa views dan juga Django App yang tersedia.
6. Karena views tidak memerlukan sejumlah data dari models, views akan memilih template yang sesuai. Akhirnya, file HTML disajikan di laman web client.
7. Jika tidak terdapat path di urlpatterns seperti url yang diminta client, maka Django akan merespon dengan menampilkan tampilan penanganan kesalahan (*error*).

## Django Views and Models
> **Apa yang terjadi jika views membutuhkan sejumlah data dari models ?**

Ketika URLConf atau urls.py berhasil memukan fungsi views yang cocok. Views akan melakukan transfer data ke model. Views akan meminta sejumlah QuerySet dari model. Model akan mengambil dan memberikan (Read/Write) data ke views. Views akan menyimpan data tersebut dalam sebuah variabel context, yaitu sebuah variabel dengan tipe data dictionary. Di context, kita memiliki sejumlah data yang dibutuhkan oleh templates yang tepat (file html yang sesuai) untuk menampilkan file html di komputer client.


# Alasan Mengapa *Virtual Environment* Sangat Berguna untuk Proyek Django
> **Mengapa harus menggunakan *virtual environment* ?**
1. Virtual environment digunakan untuk mengatur python packages untuk beberapa proyek sekaligus. Dengan menggunakan *virtual* *environment*, python packages tidak diinstall secara global sehingga proyek dapat berjalan lancar karena *python* *packages* diinstal secara terpisah di masing-masing proyek itu sendiri.
2. Dengan virtual environment, kita dapat mengetahui *packages* apa saja yang kita install di proyek kita. Kita bisa melihat jumlahnya ataupun versi dari masing-masing packages.
3. Proyek Django dapat disesuaikan dengan memilih *library* atau *module* dengan versi yang mendukung.Dengan demikian, proyek Django dapat berjalan tanpa ada issues atau bug yang disebabkan oleh *library* dan/atau *module* tertentu.
4. Proyek Django tidak perlu disesuaikan atau di-*update* secara berkala, jika packages memiliki versi yang baru. Developer bisa memilih package mana yang stabil dan cocok untuk proyeknya. Developer dapat memilih packages dengan versi tertentu secara pasti  di konfigurasi projek Django itu sendiri. Konfigurasi *python* *packages* biasanya tercatat pada file requirements.txt. Dengan demikian, developer tidak melakukan update program ketika ada pembaruan *module* dan/atau *library* tertentu. 
   
> **Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual* *environment*?**

**TIDAK**. 

**Alasan pertama**, Python tidak baik dalam menangani manajemen *dependencies*. Jika kita tidak spesifik melakukan instalasi *python* *packages*, maka pip akan menempatkan semua external packages dalam suatu folder, yaitu site-package/. Hal ini menyebabkan beberapa masalah jika Anda memiliki banyak proyek dengan konfigurasi yang berbeda. Bisa saja, satu proyek dapat berjalan, sedangkan proyek yang lain tidak berjalan.
 
**Alasan kedua**, jika kita ingin membuat aplikasi web berbasis Django, kita pasti ingin website tersebut dapat diakses oleh orang secara global untuk itu kita men-deploy aplikasi kita ke *cloud application platfor*m, seperti Heroku dan lainnya. Untuk membuat aplikasi web berbasis Django berjalan dengan lancar, kita perlu menginstal sejumlah module, library, atau python packages yang lain. Jika kita tidak menggunakan virtual environment, python packages tersebut tidak dikenali oleh cloud application platform. Bisa saja, web kita gagal di-deploy karena tidak memenuhi requirements cloud application platform tersebut. Hal ini dikarenakan server cloud application platform menginstal semua paket yang diperlukan – lagi – di mesin deployment tersebut. Misal, heroku memerlukan packages gunicorn terinstal pada proyek kita Lalu, bagaimana kita memastikan packages tersebut diinstall secara cloud di platform heroku? Cara satu-satunya adalah membuat virtual environment. Virtual environment memungkinkan python packages kita bisa diinstall di platform manapun secara otomatis dan global. Jadi, tidak mungkin rasanya tidak membuat django project tanpa menggunakan virtual environment.

# Penjelasan terkait Pengerjaan tugas


## Langkah-langkah persiapan
1. Membuat repository baru dengan template yang sudah disediakan oleh Asisten Dosen PBP.
2. Membuat local directory untuk menyimpan semua file Anda secara lokal.
3. Melakukan clone repository di local computer dengan perintah: 
   ```shell
   git clone <link-github-repository>
   ```
4.  Membuat virtual environment python dengan perintah:  
      ```shell
      python -m venv env
      ```
5.   Lalu, aktifkan virtual environment dengan mengetik perintah berikut.
      ```shell
      Windows:
      env\Scripts\activate.bat

      Unix (Linux & Mac OS):
      source env/bin/activate
      ```

6. Meng-install dependencies yang diperlukan untuk menjalankan proyek Django dengan perintah ```pip install -r requirements.txt```.
7. Melakukan pengetesan apakah proyek Django sudah bisa dijalankan di local computer atau belum dengan perintah: ```python manage.py runserver```.

## Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
1. Membuat Django app baru dengan perintah ```python manage.py startapp katalog```
2. Daftarkan aplikasi katalog pada proyek django dengan menambahkan “katalog” ke INSTALLED_APPS yang terdapat pada settings.py folder proyek Django.
3. Membuat konfigurasi *class-based models* di models.py pada folder katalog.
4. Melakukan perintah: ```python manage.py makemigrations``` untuk mempersiapkan migrasi skema model yang sudah dibuat ke dalam database Django lokal.
5. Lalu, menjalankan perintah: ```python manage.py migrate``` untuk menerapkan skema model  yang telah dibuat ke dalam database Django lokal.
6. Membuat folder baru bernama fixtures dan buatlah file ```initial_catalog_data.json```.
7. Jalankan perintah: ```python manage.py loaddata initial_catalog_data.json``` untuk memasukkan data tersebut ke dalam database Django lokal.
8. Menjalankan perintah: ```python manage.py loaddata initial_catalog_data.json``` untuk memasukkan data tersebut ke dalam database Django lokal.
9. Sekarang, kita akan masuk ke tahap implementasi views.
10. Di folder katalog, saya membuat folder baru bernama “templates”. Di folder templates, saya membuat file katalog.html yang berisikan kode HTML berikut ini.
   
      ```html
      {% block content %}
      
      <h1>Lab 1 Assignment PBP/PBD</h1>
      
      <h5>Name: </h5>
      <p>Fill me!</p>
      
      <h5>Student ID: </h5>
      <p>Fill me!</p>
      
      <table>
         <tr>
            <th>Item Name</th>
            <th>Item Price</th>
            <th>Item Stock</th>
            <th>Rating</th>
            <th>Description</th>
            <th>Item URL</th>
         </tr>
         {% comment %} Add the data below this line {% endcomment %}
      </table>
      
      {% endblock content %}
      ```
11. Membuat sebuah fungsi yang menerima parameter request dan mengembalikan render(request, "katalog.html") di views.py yang ada pada folder katalog. Contohnya adalah sebagai berikut.
    ```shell
    def show_katalog(request):
         return render(request, "katalog.html")
      ```
12. Kita akan lanjut ke tahap persiapan transfer data dari model ke views.
    
## Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
1. Pada fungsi views yang telah dibuat sebelumnya, import models yang sudah dibuat sebelumnya ke dalam file views.py. Class tersebut akan digunakan untuk  melakukan pengambilan data dari database. Berikut adalah kodenya.
   ```shell
   from django.shortcuts import render
   from catalog.models import CatalogItem
   ...
   ```
2. Menambahkan potongan kode di bawah ini ke dalam fungsi show_catalog. Potongan kode ini berfungsi untuk meminta queryset  ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel. Berikut adalah kodenya.
   ```shell
   ...
   data_catalog = CatalogItem.objects.all()
    context = {
        'list_barang':data_catalog,
        'nama': 'Gabriel Zebaoth Krisopras Putra',
        'student_id' : '2106751480',
    }
   ...
   ```
3. Menambahkan context sebagai parameter ketiga pada pengembalian fungsi render di fungsi show_catalog. Data yang ada pada variabel context tersebut akan ikut di-render oleh Django sehingga nantinya data tersebut muncul pada halaman HTML.
   ```shell
   ...
   return render(request, "catalog.html", context)
   ```
4. Sekarang, kita sudah membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML. Selanjutnya, kita akan membuat sebuah routing untuk memetakan fungsi yang telah dibuat pada views.py.

## Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
1. Membuka kembali folder katalog.

2. Membuat urls.py untuk melakukan routing terhadap fungsi views yang telah dibuat sehingga nantinya halaman HTML dapat ditampilkan lewat browser. Isi dari urls.py tersebut adalah sebagai berikut.
   ```shell
   from django.urls import path
   from katalog.views import show_katalog

   app_name = 'katalog'

   urlpatterns = [
      path('', show_katalog, name='show_katalog'),
   ]
   ```
3. Daftarkan juga aplikasi katalog ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode berikut pada variabel urlpatterns.
   ```shell
   ...
   path('katalog/', include('katalog.urls')),
   ...
   ```
4. Jalankan proyek Django dengan perintah python manage.py runserver dan bukalah http://localhost:8000/wishlist/ di browser untuk melihat halaman yang sudah dibuat.

## Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
1. Sekarang, kita akan melakukan mapping terhadap data yang telah ikut di-render pada fungsi views untuk dapat memunculkannya di halaman HTML. Untuk melakukan mapping tersebut, kita perlu menambahkan  variabel dan tag sesuai dengan dokumentasi django.
2. Kita akan coba mengubah bagian dari file html di folder templates.
   -  <h5>Name: </h5> ubah "Fill me!" menjadi {{nama}}
   -  <h5>Student ID: </h5> ubah "Fill me! menjadi {{student_id}}. 
   Hal ini dilakukan agar parameter nama dan student_id yang ada di variabel context pada views.py dapat dirender dalam template html. 
3. Untuk menampilkan daftar barang ke dalam tabel, kita perlu melakukan iterasi terhadap variabel list_barang yang telah di-*render* ke dalam HTML. Perhatikan bahwa itu  tidak dapat memanggil daftar barang di katalog  tersebut secara langsung sebab variabel list_barang merupakan sebuah kontainer yang berisikan objek. Kita  perlu memanggil nama variabel/atribut spesifik dari objek yang ada dalam kontainer tersebut untuk memanggil data dari objek tersebut. Contohnya adalah sebagai berikut.
   ```shell
   ...
   {% for item in list_barang%}
        <tr>
            <th>{{item.item_name}}</th>
            <th>{{item.item_price}}</th>
            <th>{{item.item_stock}}</th>
            <th>{{item.description}}</th>
            <th>{{item.rating}}</th>
            <th>{{item.item_url}}</th>
        </tr>
   {% endfor %}
   ...
   ```
4. Sekarang, kita telah berhasil memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template. Langkah selanjutnya, kita akan melakukan *deployment* project Django ke Heroku.
   
## Melakukan deployment ke Heroku 
1. Coba jalankan proyek Django dengan perintah python manage.py runserver dan bukalah http://localhost:8000/katalog/ di browser favoritmu untuk melihat halaman yang sudah kamu buat.
2. Cek apakah http://localhost:8000/katalog/ dapat memuat template katalog.html dengan baik. Cek juga apakah data dari model dapat dirender oleh views  ke katalog.html.
3. Jika sudah benar, lakukanlah tahapan ```git add, commit, and push``` terhadap changes yang kamu lakukan.
4. Selanjutnya, folder atau repository proyek Django di akun github akan di deploy ke Heroku. Namun, ada beberapa hal yang harus diperhatikan.
5. Log-in ke halaman web Heroku.
6. Masuk ke dashboard Heroku dan membuat sebuah aplikasi Heroku. Pilih tombol **new > create new app**
7. Lalu, masukkan nama aplikasi sesuai keinginan Anda. Klik Create App.
8. Membuat sebuah file .txt di notepad laptop kesayangan Anda. Selanjutnya, copy dan paste tulisan berikut.
   - HEROKU_APP_NAME: <NAMA_APLIKASI_HEROKU>
   - HEROKU_API_KEY: <VALUE_API_KEY_AKUN_HEROKU>
9. Menulis nama aplikasi yang telah dibuat di samping text berikut ini HEROKU_APP_NAME.
10. Menyalin kode Heroku API key yang didapat di bagian **Account settings > API key**  di kanan HEROKU_API_KEY.
11. Membuka konfigurasi repositori GitHub Anda bagian Secrets untuk GitHub Actions (Settings -> Secrets -> Actions).
12. Menambahkan variabel repository secret baru untuk melakukan deployment. “HEROKU_XXXX” sebagai name dan “xxx-xxx” sebagai value. Contoh:
      ```shell
      (NAME)HEROKU_APP_NAME
      (VALUE)APLIKASI-AKU
      ```
13. Menyimpan variabel-variabel tersebut.
14.  Membuat sebuah file bernama procfile. File ini akan digunakan oleh Heroku untuk membaca log aplikasi ke sistem monitoring internal Heroku. Berkas tersebut diisi dengan text berikut.
      ```
      web: gunicorn project_django.wsgi --log-file -
      ```
15.  Membuat berkas baru dpl.yml di .github/workflows. Berkas ini digunakan untuk mengeksekusi deployment oleh runner dari Github Actions. Adapun isi berkas dpl.yml adalah sebagai berikut.
      ```shell
      name: Deploy

      on:
         push:
            branches-ignore:
               - template
         pull_request:
            branches-ignore:
               - template

      jobs:
         Deployment:
            runs-on: ubuntu-latest
            env:
               HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
               HEROKU_APP_NAME: ${{ secrets.HEROKU_APP_NAME }}
            steps:
            - uses: actions/checkout@v2
            - name: Set up Ruby 2.7
               uses: actions/setup-ruby@v1
               with:
               ruby-version: 2.7
            - name: Install dpl
               run: gem install dpl
            - name: Install Heroku CLI
               run: wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh
            - name: Deploy to Heroku
               run: dpl --provider=heroku --app=$HEROKU_APP_NAME --api-key=$HEROKU_API_KEY
            - name: Run migrations on Heroku
               run: heroku run --app $HEROKU_APP_NAME migrate
            - uses: chrnorm/deployment-action@releases/v1
               name: Create GitHub deployment
               with:
               initial_status: success
               token: ${{ github.token }}
               target_url: https://${{ secrets.HEROKU_APP_NAME }}.herokuapp.com
               environment: production

      ```
    
16.  Untuk memberitahu git berkas atau direktori yang tidak dipush ke repositori daring di github. Adapun isi dari berkas ini dapat di peroleh dari website [ini](https://Djangowaves.com/tips-tricks/gitignore-for-a-Django-project/).
17.  Mengatur dan menambhakan konfigurasi berikut pada file settings.py di proyek Django:
      ```shell
      # Menambahkan STATIC_ROOT
         import os
         PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
         STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
      # Mengatur ALLOWED_HOSTS
         ALLOWED_HOSTS = [“*”]
      # Menambahkan middleware baru pada variabel MIDDLEWARE
         MIDDLEWARE = [
            ...,
            'whitenoise.middleware.WhiteNoiseMiddleware',
         ]
       ```
18.  Lakukan ```git add, commit, dan push``` perubahan di local computer ke repository github .
19.  Buka link aplikasi yang telah dibuat di Heroku.
20.  Connect akun github dengan aplikasi Heroku. Klik **“connect to github”.**
21.  Langkah selanjutnya, kita akan memilih nama repository di github yang akan di-deploy ke aplikasi Heroku.
22.  Di bagian bawah terdapat *manual deploy*. Lalu, ketikkan nama repository github.
23.  Tunggu proses deployment telah selesai.
24.  Akhirnya! proyek Django sudah ter-*deploy* dengan baik di Heroku.

## Credits
Tugas ini dibuat dengan menggunakan template [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage).

Made with <> by [gabiiing](https://github.com/gabiiing/)


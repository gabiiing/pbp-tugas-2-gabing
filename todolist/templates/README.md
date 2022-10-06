# Tugas 4 : Webdesign Using HTML, CSS, and JS

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023


## Creator
> Nama : Gabriel Zebaoth Krisopras Putra  
> 
> NPM : 2106751480
> 
> Kelas : PBP-D
## Output Tugas
Berikut adalah link hasil pengerjaan tugas saya
[Heroku Link](https://gabing-pbp-tugas2.herokuapp.com/todolist/).


# **Jawaban pertanyaan**
### **Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?**
1. ```INLINE CSS```. Pengaturan CSS yang dilakukan didalam tag html dengan menggunakan variabel ```style```
   Contoh: ```<h1 style="color:red;text-align:center;">This is inline css</h1>```
    > Kelebihan
    > - Lebih mudah digunakan untuk mengatur elemen css hanya pada satu bagian saja.
    > - Kita lebih mudah dalam memperbaiki elemen css yang masih salah, jika dan hanya jika elemen yang bermasalah hanya satu.

    > Kekurangan
    > - Akan memakan waktu dan tenaga untuk mengerjakan seluruh komponen dalam website kita.
    > - Kita tidak bisa reuse elemen. Misalnya, kita mengatur tag ```<h1>``` disetiap komponen website harus center, bold, dan berwarna merah. Kita akan mengeluarka banyak tenaga untuk mengatur satu persatu. 

2. ```INTERNAL CSS```. Pengturan CSS yang dilakukan dalam file html didalam tag ```<style> ... </style>```
    contoh:
     ```html
     <html>
    <head>
    <style>
        body {
        background-color: linen;
        }

        h1, h3{
        color: blue;
        }
    </style>
    </head>
    <body>

    <h1>Hallo</h1>
    <h3>This is a internal CSS.</h3>

    </body>
    </html>
     ```

   > Kelebihan
    > - Lebih mudah digunakan untuk mendesign satu tampilan html yang berbeda dari html lain. Misal, untuk navigasi eror, loading dan sebagainya
    > - TIdak perlu mengatur style css di setiap tag html
    > - Tidak perlu membuat file css yang terpisah

    > Kekurangan
    > - Tidak reuseable disemua tampilan, jika design yang diterapkan hampir mirip.
    > - Akan menambah page size dan loading time dari tampilan html yang kita buat.


3. ```EXTERNAL CSS```. Pengaturan CSS yang dilakukan dengan membaut file CSS secara terpisah. Kemudian, file CSS tersebut di hubungkan dengan file HTML dengan tag ```<link>``` .
   
   > Kelebihan
    > - File HTML lebih clean
    > - Kita bisa memperbaiki bagian atau elemen design yang masih salah secara langsung, kita tidak perlu mengubah di masing-masing tag ataupun di masing-masing file html


    > Kekurangan
    > - File Css mungkni belum tertampilkan ke client, padahal file html sudah sedia. Hal ini berlaku untuk pengaturan File CSS sizenya besar

### **Jelaskan tag HTML5 yang kamu ketahui?**
1. ```<code>``` untuk menyisipkan code di html
1. ```<div>``` untuk membuat section atau division pada web
2. ```<footer>``` untuk membuat footer dalm website kita
3. ```<img>``` untuk menyisipkan gambar dalam website kita
4. ```<hr>``` untuk membuat horiziontal line pada website kita
5. ```<cite>``` untuk menambahkan citation dari referensi yang kita gunakan
6. ```<link>``` untuk menambahkan file html dengan source dari external
7. ```<script>``` untuk menambahkan file JS yang berperan dalam client-side website kita
8. ```<table>``` untuk membuat tabel pada website kita
1. ```<u>``` untuk menggarisbawahi text
1. ```<ul>``` untuk membuat unordered list pada website kita


### **Jelaskan CSS selector yang Anda Ketahui?.**
1 .```.class``` untuk memilih semua elemen dengan class="namaclass"
1 .```#id``` untuk memilih semua elemen dengan id="id" 
1 .```*``` untuk memilih semua elemen apapun 
1 .```element, element``` untuk memilih dua elemen sekaligus 
1 .```element.class``` untuk memilih elemen X dengan class="Y" 



<br></br>
# **Penjelasan terkait Pengerjaan tugas**

- [x] Kustomisasi templat untuk halaman login, register, dan create-task semenarik mungkin.
    1.  Menghubungkan file html dengan bootstrap dengan menggunakan tag ```<link>``` untuk setiap file html
    2.  Membuat navigation bar paa base.html untuk diextends ke semua file html
    3.  Menambahkan extends pada setiap bagian awal file html
    4.  Membaut kustom html di tengah elemen django -> {% block content %} ... {% endblock content}
    5.  Menambahkan {{form.astable}} pada sebuah div
    6.  Setiap div diatur dengan inline css bawaan bootstrap agar tepat di tengah dan memilki warna menarik : flex, justify-content-center, dsb

- [x]  Kustomisasi halaman utama todo list menggunakan cards. (Satu card mengandung satu task).
    1. Menggunakan card pada templat yang sudah disediakan oleh bootstrap
    2. Membuat class container
    3. membuat class row untuk mengatur card dengan grid
    4. For loop setiap data pada database proyek django.
    5. Di setiap iterasi loop, 
    6. Menambahkan button pada bagian bawah card dengan class = "btn btn-danger.."
   
        
- [x] Membuat keempat halaman yang dikustomisasi menjadi responsive.
   1. Pada dasarnya, bootstrap telah membuat semua template yang responsive
   2. Mungkin kita perlu menambahkan bagian ini pada tag meta html <meta name="viewport" content="width=device-width, initial-scale=1.0">
   3. Lalu, jika dirasa beberapa bagian html kita masih kurang responsive kita bisa memnggunakan attribute display: flex. Bootstrap juga menyediakan pengaturan untuk beberapa media query: col-sm-6, sm untuk dimensi ≥576px.
  
## Credits
Tugas ini dibuat dengan menggunakan template [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage).

Made with <> by [gabiiing](https://github.com/gabiiing/)


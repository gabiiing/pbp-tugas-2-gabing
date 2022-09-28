# Tugas 4 : Pengimplementasian Form dan Autentikasi Menggunakan Django

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

<br></br>
# **Perbedaan JSON, XML, dan HTML**
## **Apa itu JSON ?**
**JSON** atau ***JavaScript Object Notation***, adalah sebuah format data berbasis teks dengan mengikuti sintaks seperti layaknya objek JavaScript. JSON diperkenalkan di awal tahun 2000 oleh Douglas Crockford. JSON digunakan sebagai alat untuk pertukaran data: memuat dan menampilkan informasi ke web secara responsif, menukarkan data dari website lain, dan menukarkan data antar platform dengan JSON API. JSON mempunyai syntax yang cukup sederhana. JSON menyimpan data dalam format map dengan pasangan key dan value. Key harus berupa String, sedangkan value dapat diisi dengan data primitif JavaScript apapun. JSON juga dapat diubah ke dalam bentuk string sehingga data yang sedang ditukar dapat dipahami dengan mudah. Format JSON adalah sebagai berikut.

## **Apa itu XML?**
**XML** atau ***Extensible Markup Language*** adalah sebuah format untuk membantu proses penyimpanan dan pentransferan data. Format XML hampir mirip dengan HTML. Keduanya sama-sama menggunakan tag untuk mengenali sebuah value dari data. Tetapi, XML memungkinkan developer untuk membuat tagnya sendiri, tidak seperti HTML yang sudah baku dan paten. Dengan format ini, developer dapat mengirimkan atau saling menukar data antar sistem atau platform melalui layanan internet.

## **Apa itu HTML?**
**HTML** atau ***HyperText Markup Language*** adalah sebuah format yang digunakan untuk membuat website atau bisa dibilang HTML ini merupakan pondasi untuk memuat seluruh konten dari sebuah website. HTML biasanya disandingkan dengan CSS (Cascading Style Sheet) untuk “mempercantik” bagian-bagian web. Misalnya, kita bisa membuat tabel di website dengan menggunakan tag HTML dan kita bisa mengubah warna atau teks tabel tersebut dengan menggunakan CSS. HTML menggunakan “markup” untuk membubuhi keterangan teks, gambar dan konten lain untuk ditampilkan di browser Web.HTML menyediakan tag atau elemen khusus, seprti body, div, h1, h2, link, a, ul, th, tr, dan masih banyak lagi

## **Apa perbedaan dari JSON, XML, dan HTML?**
### **Perbedaan HTML dengan JSON dan XML**
HTML memiliki fungsi yang berbeda dengan JSON dan XML. HTML hanya digunakan untuk menampilkan data ke sebuah website. HTML tidak dapat digunakan untuk menyimpan dan mengirim data antar sistem, platform, atau website seperti JSON dan XML. HTML juga bersifat statis karena fungsinya sendiri hanya untuk menampilkan data. HTML tidak dapat diuraikan atau di-parsed  dan digunakan oleh kebanyakan bahasa pemrograman tidak seperti JSON dan XML. 

### **Perbedaan JSON dan XML**
Meskipun JSON dan XML terlihat memiliki fungsionalitas yang sama tersebut tetapi keduanya memiliki karakteristik yang unik. Berikut adalah perbandingan antara JSON dengan XML.
| **Parameter**                     | **XML**                                                                         | **JSON**                                                                                             |
|-----------------------------------|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| **Bahasa**                        | Sebuah markup dengan tag yang didefinisikan secara manual                       | Berupa formata dalam bentuk Objek JavaScript                                                         |
| **Penyimpanan data**              | Data disimpan sebagai tree structure                                            | Data disimpan sebagai map: ada key dan value.                                                        |
| **Pengolahan**                    | Dapat melakukan pemrosesan dan pemformatan dokumen dan objek                    | Tidak dapat melakukan pemrosesan dan perhitungan                                                     |
| **Jenis File**                    | Ukuran besar dan lambat saat parsing                                            | Ukuran besar dan cepat saat parsing                                                                  |
| **Dukungan Namespaces**           | Mendukung namespaces, komentar, dan metadata                                    | Tidak terdapat dukungan tersebut                                                                     |
| **Ukuran dokumen**                | Ukuran dokumen besar degnan struktur tag yang tidak readable                    | Human readable                                                                                       |
| **Jenis Tipe data yang didukung** | Mendukung bagan, charts, dan data non-primitif lain                             | JSON hanya berupa string, angka, boolean, objek, dan array dengan tidak mendukung data non-primitif  |
| **UTF**                           | Mendukung UTF-8 dan UTF-16                                                      | Mendukung UTF dan ASCII                                                                              |
| **Pengolahan data**               | Permintaan AJAX menjadi lambat karena bandwith untuk memproses tag sangat besar | Perminataan Ajak relatif cepat                                                                       |

<br></br>
# **Mengapa kita memerlukan *data* *delivery* dalam pengimplementasian sebuah platform ?**

Dalam mengimplementasikan sebuah platform,  kita sebagai developer pasti ingin membuat semua fungsionalitas dari platform dapat berfungsi dengan baik. Kita tahu bahwa fungsionalitas setiap komponen platform itu berfungsi adalah input (requests) dan output (responses) sinkron. Dalam sebuah web-platform, ada banyak komponen:
- Browser request HTML page, maka server juga harus mengembalikan HTML page.
- Browser request style sheet, maka server juga harus mengembalikan CSS file.
- Seterusnya berkalu untuk file JPG, JS, XML, JSON, dan data lainnya.

Peran data delivery inilah yang menjadi dasar sebuah platform dapat berjalan dengan baik. Tanpa adanya pengiriman data berupa HTML, maka browser milik client tidak dapat memuat informasi dan seluruh komponen dari website milik kita ke local network mereka.



<br></br>
# **Penjelasan terkait Pengerjaan tugas**

- [x] Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.
    1.  Menjalankan perintah ```python manage.py startapp todolist```
    2.  Tambahkan apliasi "mywatchlist" pada variabel INSTALLED_APPS di settings.py folder django-project. Langkah ini digunakan untuk mendaftarkan aplikasi mywatchlist agar dapat di baca oleh django.
        ```python
        INSTALLED_APPS = [
            'events.apps.EventsConfig',
            'Django.contrib.admin',
            'katalog',
            'mywatchlist',
            # tambahkan aplikasi disini
            'todolist'
        ]
        ```
- [x] Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
    1. Membuat folder template. Kemudian, buat```todolist.html``` di dalam folder tersebut dengan berisi code berikut.
        ```html
        {% extends 'base.html' %}
        {% block meta %}
        <title>Todolist</title>
        {% endblock meta %}

        {% block content %}  
            <head>
                {% load static %}
            </head>
            <body>
                <h1>Test</h1>
            </body>

        {% endblock content %}
        ```
    2. Membuat fungsi views ```show_todolist``` untuk menampilkan template html tersebut ke ```{{url}}/todolist/```. Salin dan Tempel kode berikut pada ```todolist/views.py```
        ```python
        def show_todolist(request):
            context = {}
            return render(request, 'todolist.html', context)
        ```

    3. Memetakan fungsi views dan html tersebut ke urls.py agar dapat ditampilkan di website. Pada urls.py tempel dan salin kode berikut.
        ```python
        from django.urls import path
        from todolist.views import show_todolist
        #sesuaikan dengan nama fungsi yang dibuat

        app_name = 'todolist'

        urlpatterns = [
            path('', show_todolist name='show_todolist' ),         
        ]

        ```
   
    4. Setelah itu, daftarkan urls todolist pada urlpatterns di project_django URL.
        ```python
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('example_app.urls')),
            path('katalog/', include('katalog.urls')),
            path('mywatchlist/', include('mywatchlist.urls')),
            # tambahkan path todolist/ yang mengarah pada urls path yang ada diaplikasi todolist
            path('todolist/', include('todolist.urls')),
        ]
        ```
   

- [X] Membuat sebuah model Task yang memiliki atribut sebagai berikut:
    - id berupa foreignkey yang diisi secara otomatis sebagai penanda dari masing-masing tugas yang dibuat
   - user untuk menghubungkan task dengan pengguna yang membuat task tersebut.
   - date untuk mendeskripsikan tanggal pembuatan task.
   - title untuk mendeskripsikan judul task.
   - description untuk mendeskripsikan deskripsi task
   - is_finished merupakan boolean yang menyatakan bahwa tugas tersebut ```Selesai``` atau ```Belum Selesai```.
    1. Buka folder aplikasi ```todolist```
    2. Lalu, buka models.py. Selanjutnya, kita akan membuat sebuah class Task sesuai dengan ketentuan tersebut.
        ```python
        from django.db import models
        from django.contrib.auth.models import User
        # Berguna untuk default value dari date
        from  django.utils import timezone

        class Task(models.Model):
            id = models.AutoField(primary_key=True)
            user = models.ForeignKey(User, default=None, on_delete=models.CASCADE);
            date = models.DateField(default = timezone.now);
            title = models.CharField(max_length=255);
            description = models.TextField();
            is_finished = models.BooleanField(default=False);

            def __str__(self) :
                return self.title
        ```
    3. Agar model tersebut dapat dirubah menjadi query database. Maka, kita akan melakukan migrasi di terminal dengan perintah ```python manage.py makemigrations```. Lalu, jalankah pula ```python manage.py migrate```

 - [x]  Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
    > ```Registrasi```
    1. Buka views.py. Import module agar views yang dibuat tetap berjalan
        ```python
        from django.shortcuts import redirect
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib import messages 
        ```
    2. Membuat fungsi register pada todolist/views.py
        ```python
        def register(request):
            form = UserCreationForm()

            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Akun telah berhasil dibuat!')
                    return redirect('todolist:login')
            
            context = {'form':form}
            return render(request, 'register.html', context)
        ```
    3. Membuat template register.html
        ```html
        {% extends 'base.html' %}

        {% block meta %}
        <title>Registrasi Akun</title>
        {% endblock meta %}

        {% block content %}  

        <div class = "login">
            
            <h1>Formulir Registrasi</h1>  

                <form method="POST" >  
                    {% csrf_token %}  
                    <table>  
                        {{ form.as_table }}  
                        <tr>  
                            <td></td>
                            <td><input type="submit" name="submit" value="Daftar"/></td>  
                        </tr>  
                    </table>  
                </form>

            {% if messages %}  
                <ul>   
                    {% for message in messages %}  
                        <li>{{ message }}</li>  
                        {% endfor %}  
                </ul>   
            {% endif %}

        </div>  

        {% endblock content %}
        ```
   
    > ```Login```
       
    1. Buka views.py. Import module agar views yang dibuat tetap berjalan
        ```python
        from django.contrib.auth import authenticate, login
        ```
    2. Membuat fungsi login pada todolist/views.py
        ```python
        def login_user(request):
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('wishlist:show_wishlist')
                else:
                    messages.info(request, 'Username atau Password salah!')
            context = {}
            return render(request, 'login.html', context)
        ```
    3. Membuat template login.html
        ```html
        {% extends 'base.html' %}

        {% block meta %}
        <title>Login</title>
        {% endblock meta %}

        {% block content %}

        <div class = "login">

            <h1>Login</h1>

            <form method="POST" action="">
                {% csrf_token %}
                <table>
                    <tr>
                        <td>Username: </td>
                        <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                    </tr>
                            
                    <tr>
                        <td>Password: </td>
                        <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                    </tr>

                    <tr>
                        <td></td>
                        <td><input class="btn login_btn" type="submit" value="Login"></td>
                    </tr>
                </table>
            </form>

            {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}     
                
            Belum mempunyai akun? <a href="{% url 'todolist:register' %}">Buat Akun</a>

        </div>

        {% endblock content %}
        ```

    > ```Logout```
        
    1. Buka views.py. Import modul agar fungsi logout dapat berjalan.
        ```python
        from django.contrib.auth import logout
        ```
    2. Membuat fungsi logout di todolist/views.py
        ```python
        def logout_user(request):
            logout(request)
            return redirect('wishlist:login')   
        ```

 - [x] Membuat fitur ```show_todolist```, ```create_task```,```update_task```, ```update_task```, dan ```edit_task```
    1. ```show_todolist``` ----> Sebelum membuat halaman todolist.html memenuhi persyaratan diatas. Kita perlu mengatur fungsi show_todolist di views.py. Kita akan ambil data dari model Task, untuk menampilkan task masing-masing user. Kita juga akan atur bahwa views tersebut dapat digunakan ketika user sudah login. Selain itu, kita juga akan menggunakan cookies untuk menampilkan kapan user X terakhir login ke website kita. Buat fungsi show_todolist seperti berikut ini.
        ```python
        # client dapat mengakses fungsi ini -> todolist.html harus login terlebih dahulu
        @login_required(login_url='/todolist/login/')
        def show_todolist(request):
            # mengambil data tugas dari user yang login
            task_list = Task.objects.filter(user = request.user)
            context = {
                'task_list': task_list,
                # mengambil data user yang
                'last_login': request.COOKIES['last_login']
            }
            return render(request, 'todolist.html', context)
        ```
    2. Agar fitur menampilkan waktu login berhasil kita perlu rubah sedikit bagian fungsi login_user di views.py. Ganti bagian ```if user is not none``` menjadi seperti ini.
        ```python
        ...
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("wishlist:show_wishlist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        ...
        ```
    3. ```Tambah tugas``` ---->  Pertama, kita akan buat file form.py dengan menggunakan syntax dari django. Tambahkan kode berikut pada file tersebut.
        ```python
        from django.forms import ModelForm
        from todolist.models import Task

        class CreateTask(ModelForm):
            class Meta:
                model = Task
                # Form hanya meminta input title dan description
                fields = ['title', 'description' ]
        ```

    4. Langkah terkahir, kita akan membuat fungsi create_task di views. Fungsi tersebut harus berjalan ketika user logged in.
        ```python
            # Harus lgoin terlebih dahulu
            @login_required(login_url='/todolist/login/')
            def create_task(request):
                form = CreateTask()
                if request.method == 'POST':
                    form = CreateTask(request.POST, request.FILES)
                    # Ketika field dari setiap form sudah terisi dengan baik
                    if form.is_valid():
                        # akan dibuat dan disimpan data task ke database
                        task = form.save(commit=False)
                        # attribute user dari task tersebut merupakan task yang sudah login(request.user)
                        task.user = request.user
                        task.save()
                        return redirect('todolist:show_todolist')
                else:
                    form = CreateTask(initial={'user': request.user})
                context = {'form': form}
                return render(request, 'create_task.html', context)
        ```
    5. ```update_task``` ----> kita hanya perlu membuat fungsi update_task pada views.py.
        ```python
        @login_required(login_url='/todolist/login/')
        # Fungsi untuk memperbarui status task
        def update_task(request, pk):
            # parameter pk diperoleh dari url. kemudian akan dicari task dengan attribute id tersebut
            updated_task = Task.objects.get(id=pk)
            
            # attribut is_finished akan diupdate dengan menegeasi valuenya
            if updated_task.is_finished:
                updated_task.is_finished = False
            else:
                updated_task.is_finished = True
            
            updated_task.save() 
            return redirect("todolist:show_todolist")
        ```
    6.  ```delete_task``` ----> kita hanya perlu membuat fungsi delete_task pada views.py
        ```python
        @login_required(login_url='/todolist/login/')
        # Fungsi untuk memperbarui status task
        def delete_task(request, pk):
            # Task dicari dengan Id = pk. Lalu, didelete
            delete_task = Task.objects.get(id=pk)
            delete_task.delete() 
            return redirect("todolist:show_todolist")
        ```
    7.  ```edit_task``` ----> kita hanya perlu membuat fungsi edit_task pada views.py
        ```python
        @login_required(login_url='/todolist/login/')
        # Fungsi untuk memperbarui status task
        def edit_task(request, pk):
            task = Task.objects.get(id=pk)
            # akan membuka kembali form CreateTask() yang telah diisi berdasarkan attribut pada task dengan id = pk
            form = CreateTask(instance=task)
            # fungsionalitas selanjutnya sama seperti create_task
            if request.method == 'POST':
                form = CreateTask(request.POST, instance=task)
                if form.is_valid():
                    task = form.save(commit=False)
                    task.user = request.user
                    task.save()
                    return redirect('todolist:show_todolist')
            context = {'form': form}
            return render(request, 'create_task.html', context)
        ```
 - [x]  Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
    
    1.  Selanjutnya, kita akan membuat tampilan HTML sesuai dengan requirements yang ditentukan. Untuk detail masing-masing bagian, ada komen yang tertulis di masing-masing fitur yang disyaratkan.
        ```html
        {% extends 'base.html' %}
        {% block meta %}
        <title>{{user.username}} Todolist</title>
        <h1>{{user.username}} To-Do's</h1>
        {% endblock meta %}

        {% block content %}  
            <head>
                {% load static %}
            </head>
            <!-- Button untuk membuat tugas Bary -->
            <button><a href="{% url 'todolist:create' %}">Add New Task</a></button>

            <h2>Task List:</h2>
            <table>
                <tr>
                <!-- membuat header table-->
                <th>Create Date</th>
                <th>Title</th>
                <th>Description</th>
                <th>Status</th>
                <th>Update</th>
                <th>Delete</th>
                <th>Edit</th>
                </tr>
                {% comment %} Add the data below this line {% endcomment %}
                <!-- Mengiterasi data tugas pada query database -->
                {% for task in task_list %}
                    <tr>
                        <td>{{task.date}}</td>
                        <th>{{task.title}}</th>
                        <td>{{task.description}}</td>
                        <td> 
                            <!-- Jika is_finished true: tugas Selesai dan vice versa -->
                            {% if task.is_finished %}
                            Selesai
                            {% else %}
                            Belum Selesai
                            {% endif %}
                        </td>
                        <!-- Implementasi fungsi diviews pada button html disetiap task -->
                        <!-- Kegunaan task.id adalah untuk mengupdate data task dengan id tersebut -->
                        <!-- Task.id akan digunakan sebagai parameter pk di fungsi update, delete, dan edit di views.py -->
                        <td><button><a href="{% url 'todolist:update' task.id %}">Update</a></button></td>
                        <td><button><a href="{% url 'todolist:delete' task.id %}">Delete</a></button></td>
                        <td><button><a href="{% url 'todolist:edit' task.id %}">Edit</a></button></td>
                    </tr>
                {% endfor %}
            </table>
            <!-- Implementasi last login -->
            <h3>last login: {{last_login}}</h3>
            <button><a href="{% url 'todolist:logout' %}">Logout</a></button>

        {% endblock content %}
        
        ```

 - [x]  Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.
    1.  Selanjutnya, kita akan membuat sebuah page baru dengan membuat file create_task.html
        ```html
        {% extends 'base.html' %}
        {% block content %}
        <form action="" method="POST">
            {% csrf_token %}
            <h1>Tambah Tugas Baru</h1>
            <table>
                {{form}}
                <tr>
                    <td></td>
                    <td> <input type = "submit" name="submit"> </td>
                </tr>
                
            </table>
        
        </form>

        {% endblock %}
        ```
 - [x]  Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut:
    -  http://localhost:8000/todolist berisi halaman utama yang memuat tabel task.
    -  http://localhost:8000/todolist/login berisi form login
    -  http://localhost:8000/todolist/register berisi form registrasi akun.
    -  http://localhost:8000/todolist/create-task berisi form pembuatan task
    -  http://localhost:8000/todolist/logout berisi mekanisme logout.
    -  http://localhost:8000/todolist/update-task/pk/ berisi mekanisme untuk mengganti status is_finished dari task dengan attribute id=pk.
    - http://localhost:8000/todolist/delete-task/pk/ berisi mekanisme untuk menghapus task dengan attribute id=pk.
    - http://localhost:8000/todolist/edit-task/pk/ berisi mekanisme untuk mengedit title dan description dari  task dengan attribute id=pk.

    Untuk membuat routing ke sejumlah alamat tersebut, kita perlu mengatur sejumlah path pada file urls.py. Berikut adalah kode pada file urls.py.
    ```python
    from django.urls import path
    from todolist.views import create_task, edit_task, register, login_user, logout_user,show_todolist, update_task, delete_task
    #sesuaikan dengan nama fungsi yang dibuat

    app_name = 'todolist'

    urlpatterns = [
        path('', show_todolist, name='show_todolist' ),
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
        path('create-task/', create_task, name='create'),
        path('update-task/<int:pk>/', update_task, name='update'),
        path('delete-task/<int:pk>/', delete_task, name='delete'),
        path('edit-task/<int:pk>/', edit_task, name='edit'),
    ]
    ```
- [x] Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
  Untuk melakukan deployment ke heroku. Kita sebenarnya hanya melakukan ```git add```, ```git commit```, ```git push```. Heroku akan otomatis mengupdate data dari repository kita ke website atau aplikasi kita.
  Berikut adalah tampilan dari website heroku saya ketika sudah login.
- [x] Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
- [x] Membuat sebuah README.md pada folder todolist yang berisi tautan menuju aplikasi Heroku yang sudah kamu deploy serta jawaban dari beberapa pertanyaan berikut
- [x] Melakukan Bonus
- Penjelasan terkait implementasi fitur update status tugas dan delete tugas. Serta, fitur tambahan saya sendiri. Terdapat pada bagian Membuat fitur ```show_todolist```, ```create_task```,```update_task```, ```update_task```, dan ```edit_task```

## Credits
Tugas ini dibuat dengan menggunakan template [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage).

Made with <> by [gabiiing](https://github.com/gabiiing/)


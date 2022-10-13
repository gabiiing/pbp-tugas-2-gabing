# Tugas 6 : Javascript dan AJAX

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
### **Jelaskan perbedaan antara ```asynchronus programming``` dengan ```synchronus programming```?**
```Asynchronus programming``` - Teknik programming yang memungkinkan program dapat menjalankan suatu tugas, yang mungkin itu berjalan lama, dan dapat responsif terhadap tugas lain, alih-alih program tersebut menunggu satu tugas diselesaikan secara terurut. Teknik programming ini memungkinkan untuk menjalankan tugas secara langsung dan mengerjakan tugas lebih cepat.

```Synchronus programming``` - Teknik programming yang memungkinkan program menjalankan tugas dalam satu waktu dan setelah tugas lain diselesaikan, sementara tugas yang dijalankan bersamaan tidak akan dijalankan atau diresponse.

### **Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**
```Event Driven Programming ``` adalah suatu paradigma pemrograman yang mana entitas/objek yang dibuat dalam suatu program atau code berkomunikasi secara tidak langsung tetapi pesan tersebut dikirimkan melalui perantara. Event Driven Programming memungkinkan setiap event yang dipicu oleh pengguna dapat direspon oleh program. Contoh event: Button diclick, form disubmit, tombol di keyboard yang diclick, dan lainnya.

Contoh penerapan event driven programming dalam program saya adalah sebagai berikut.
Ketika button ```Tambah Tugas Baru``` di klik maka website akan memunculkan modal. Pada modal, terdapat button ```Add Task``` dan ```Close```. 

Ketika ```Add Task``` di click akan memanggil fungsi berikut
```javascript
  function loadTaskData() {
    let taskCardHTML = ''
    $("#taskContainer").append('');
    $.ajax({
      url: "/todolist/json/",
      type: "GET",
      dataType: "json",
      success: function (dataList){
        $("#taskContainer").html('');
        for (let data of dataList){
          
          let taskStatus = data.fields.is_finished ? "Selesai" : "Belum Selesai";
          taskCardHTML +=`
              <div class="col-sm-6 col-md-4 col-lg-3 p-1" id="task-${data.pk}">
                <div class="card">
                  <div class="card-body">
                    <h3 class="card-title" id="cardTitle-${data.pk}"> ${ data.fields.title } </h3>
                    <h6 class="card-subtitle" >  ${data.fields.date}</h6>
                    <h6 class="card-subtitle" id="cardSubtitle-${data.pk}"> ${taskStatus}</h6>
                    <p class="card-text">  ${ data.fields.description } </p>
                    <button id="button-update-task-${data.pk}"  class="btn btn-outline-warning p-1 mx-auto my-auto" onClick="updateTaskStatus(${data.pk})" role="button">Update</button>
                    <button id="button-delete-task-${data.pk}"  class="btn btn-outline-danger p-1 mx-auto my-auto" onClick="deleteTask(${data.pk})" role="button">Delete</button>
                  </div>
                </div>
              </div>`
          ;
        }
        $("#taskContainer").html(taskCardHTML);
        
      },
      error: function(response){
        console.log('Eror: ');
      }
    });
  }
  $(document).ready(function () {
    loadTaskData();
  });
```
    
Fungsi tersebut berguna untuk mengambil data dari form input dan menambahkan data pada database. Lalu, data ditampilkan ke html.

Ketika ```Close``` di clik akan memangil fungsi berikut
```javascript
 function closeModal(){
    $("#createTaskForm").trigger('reset');
    $('#createTaskModal').modal("hide")
  }
```
Fungsi tersebut untuk mereset input di form pada modal dan men-close modal.


### **Jelaskan penerapan asynchronous programming pada AJAX.**
AJAX menerapkan asyncrhonus programming yang membuat website dapat memuat data berdasarkan event tertentu tanpa harus mereload ulang halaman web. AJAX juga memungkinkan website dapat memuat data dari backend, meminta data, dan menerima data dibagian server saja. Hal ini berguna ketika pengguna melakukan event tertentu, seperti mengubah text, menambahkan bagian baru dihtml, dan sejenisnya, itu dapat direquest secara langsung. Event tersebut dapat dirsspon oleh AJAX dengan kode javascript dengan mengubah sebagian backend/frontend saja tanpa mengubah backend/frontend. 

Secara mudah, AJAX menerima request berupa event dari client dan mengirimkan response ke client tanpa memuat ulang website.  Request dari user dapat diselesaikan secara langsung dengan mengubah sebagian tampilan dari file html. Hal ini dilakukan oleh Javascript yang mengubabh sebagian tampilan HTML dan mengubah sebagain data di backend(JSON, XML). Kemudian, server merespon dan mengubah sebagian tampilan sesuai request.

<br></br>
# **Penjelasan terkait Pengerjaan tugas**

  
1. Membuat views ```show_json``` untuk mengambil data dari database dan data diserialize dalam bentuk JSON.
2. Membuat views ```save_task``` untuk mengambil data dari form dan membuat objek task baru di database.
3. Memperbarui views ```update_task```, ```delete_task``` agar tidak redirect langsung ke todolist homepage dan menggantinya dengan JSON Response.
4. Membuat file html baru: ```todolist_ajax.html   ``` dan Memperbarui tampilan html dari tugas 5 kemarin. Perubahan: tombol Edit task dihilangkan untuk mempermudah pengerjaan tugas. Lalu, Setiap component pada card diberi ```id``` untuk mempermudah dalam implementasi AJAX GET, POST, DELETE
5. Selanjutnya, saya mengerjakan bagian AJAX atau JavaScript dari website yang saya buat.   
6. Lalu, todolist_ajax.html ditambahkan ```<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>``` agar setiap method AJAX dapat berfungsi dengan baik
7. Membuat fungsi ```GET```:
   ```javascript
   $(document).ready(function () {
    loadTaskData(); --> setiap page reload path todolist maka akan menampilkan semua data card
   });

     function loadTaskData() {
    let taskCardHTML = ''
    $("#taskContainer").append('');
    $.ajax({
      url: "/todolist/json/",
      type: "GET",
      dataType: "json",
      success: function (dataList){
        $("#taskContainer").html('');
        for (let data of dataList){
          
          let taskStatus = data.fields.is_finished ? "Selesai" : "Belum Selesai";
          taskCardHTML +=`
              <div class="col-sm-6 col-md-4 col-lg-3 p-1" id="task-${data.pk}">
                <div class="card">
                  <div class="card-body">
                    <h3 class="card-title" id="cardTitle-${data.pk}"> ${ data.fields.title } </h3>
                    <h6 class="card-subtitle" >  ${data.fields.date}</h6>
                    <h6 class="card-subtitle" id="cardSubtitle-${data.pk}"> ${taskStatus}</h6>
                    <p class="card-text">  ${ data.fields.description } </p>
                    <button id="button-update-task-${data.pk}"  class="btn btn-outline-warning p-1 mx-auto my-auto" onClick="updateTaskStatus(${data.pk})" role="button">Update</button>
                    <button id="button-delete-task-${data.pk}"  class="btn btn-outline-danger p-1 mx-auto my-auto" onClick="deleteTask(${data.pk})" role="button">Delete</button>
                  </div>
                </div>
              </div>`
          ;
        }
        $("#taskContainer").html(taskCardHTML);
        
      },
      error: function(response){
        console.log('Eror: ');
      }
    });
   ```
8. Membuat fungsi ```POST```:
   ```javascript
     $(document).on("submit", "#createTaskForm", function(e) {
        e.preventDefault();
        $.ajax ({
            url: "add/",
            type: "POST",
            dataType:"json",
            data: {
                title:$("#title").val(),
                description:$("#description").val(),
                csrfmiddlewaretoken: "{{ csrf_token }}"
            },
            success: function(data) {
                loadTaskData();
                $("#createTaskForm").trigger('reset');
                $('#createTaskModal').modal("hide")

            }
        })
    })
   ```
10. Membuat fungsi ```DELETE```:
      ```javascript
         function deleteTask(pk){
         $.ajax({
            url: `/todolist/delete-task/${pk}/`,
            type: "DELETE",
            credentials: "include",
            success: function(data) {
                  $(`#task-${pk}`).remove()
            }
         })
      }
      ```
11. Membuat fungsi ```UPDATE```:
   ```javascript
      function updateTaskStatus(pk){
      $.ajax({
         url: `/todolist/update-task/${pk}/`,
         type: "POST",
         credentials: "include",
         success: function(data) {
               let innerHTML = document.getElementById(`cardSubtitle-${pk}`).innerHTML.toString().trim();
               let statusUpdate = (innerHTML == "Belum Selesai") ? "Selesai" : "Belum Selesai"
               let innerHTMLNew = `<h6 class="card-subtitle" id="cardSubtitle-${pk}"> ${statusUpdate}</h6>`
               $(`#cardSubtitle-${pk}`).html(innerHTMLNew);
               loadTaskData();
         }
      })
      }
   ```
12. Git add, commit, push dan perubahan kini sudah tertampil pada aplikasi heroku


## Credits
Tugas ini dibuat dengan menggunakan template [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage).

Made with <> by [gabiiing](https://github.com/gabiiing/)


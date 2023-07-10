# Super Cashier

## Latar Belakang

Andi adalalah seorang pemilik supermarket besar disalah satu kota di Indonesia. andi memiliki
rencana untuk membuat sistem kasir yang self service di supermarket miliknya. sehingga customer bisa
langsung memasukkan item , jumlah serta harga item yang ingin di beli serta dengan fitur lainnya.
andi membutuhkan seorang programmer untuk membuatkan fitur-fitur tersebut agar kasir self service di supermarket miliknya berjalan dengan lancar

## FEATURE REQUIREMENTS

> - User dapat menambah atau memperbarui item
> - User menginput nama item, jumlah item, dan harga barang
> - Membuat inputan pengecekan pesanan oleh user : menambahkan, mengganti, dan membatalkan pesanan.
> - Mengoreksi pesanan oleh user : menghapus salah satu pesanan tanpa menghapus seluruhnya.
> - Menghapus semua pesanan oleh user jika ingin dibatalkan.
> - Menampilkan pesanan yang telah dibuat oleh user.
> - Diskon diterapkan ketika jumlah total tertentu tercapai

## Flowchart

![flowchart super cashier](/img/flowchart.png)

## Penjelasan Code

Function add_item digunakan saat user menambahkan barang,
jumlah barang dan harga barang yang ingin di pesan. untuk class Transaction
itu dibuat untuk menyimpan semua function program.

![flowchart super cashier](/img/additem.png)

Function update_name, update_qty dan update_price digunakan jika user ada kesalahan
pada saat input data. user dapat mengganti nama barang, jumlah barang dan harga barang
tanpa harus menghapus seluruh item yang sudah di input.

![flowchart super cashier](/img/updateitem.png)

Function delete_item digunakan saat user ingin menghapus salah satu item yang
telah di input tanpa harus menghapus seluruh item.

![flowchart super cashier](/img/deleteitem.png)

Function reset_transaction digunakan saat user ingin reset seluruh transaksi

![flowchart super cashier](/img/resettransaksi.png)

Function display_order bertujuan untuk menampilakan seluruh data yang sudah
di input dalam bentuk tabel

![flowchart super cashier](/img/display%20order.png)

function check_order bertujuan untuk check tidak ada kesalahan data 
yang telah di input oleh user

![flowchart super cashier](/img/checkorder.png)

Function total_price bertujuan untuk menghitung seluruh total belanja user
dan otomatis akan ada potongan untuk setiap user yang telah berbelanja lebih dari
Rp. 200.000 dengan diskon 5% , Rp. 300.000 dengan diskon 8% dan berbelanja lebih
dari Rp. 500.000 akan mendapatkan diskon 10%.

![flowchart super cashier](/img/totalprice3.png)

## Cara menjalankan program

1. Download semua file yang tersedia di github
2. Gunakan jupyter notebook untuk menjalankan program
3. Import transaction.py untuk menjalankan data
4. Import tabulate agar saat display_order di run output nya berbentuk tabel

## Hasil Test Case
Pada bagian ini program akan dilakukan beberapa testing berbeda untuk memastikan bahwa program berjalan  dengan lancar.

1. User ingin menambahkan dua item baru menggunakan method add_item(). item yang ditambahkan adalah sebagai berikut:

> - Nama item: Ayam Goreng, Qty: 2 dan harga per item: 20000
> - Nama item: Pasta Gigi, Qty: 3 dan harga per item: 15000

![flowchart super cashier](/img/tescase_additem.png)

2. User ingin menghapus salah satu item yaitu pasta gigi sehingga user menggunakan method delete_item() untuk menghapusnya

![flowchart super cashier](/img/testcase_deleteitem.png)

3. User ingin menghapus seluruh transaksi, maka user  menggunakan method reset_transaction() untuk menghapus semua item yang sudah ditambahkan.

![flowchart super cashier](/img/testcase_reset.png)

4. Setelah user selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method total_price(). Sebelum mengeluarkan output total belanja akan menampilkan item yang telah di input

![flowchart super cashier](/img/hasil%20test.png)


## Kesimpulan
Sistem kasir self-service berfungsi untuk membantu para customer untuk memasukkan pesanan yang diinginkan secara mandiri. Sistem sudah dapat berjalan dengan baik, namun sistem ini dapat dikembangkan dengan lebih baik lagi
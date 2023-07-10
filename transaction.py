from tabulate import tabulate


class Transaction:
  def __init__(self):
    self.order = dict() #untuk menyimpan informasi pesanan


  def add_item(self, item_name, item_qty, item_price): #untuk menambahkan item order customer
    self.order.update({item_name: [item_qty, item_price]})

    try:
      item_qty = int(item_qty)
      item_price = int(item_price)
    except:
      print("jumlah dan harga barang harus berupa angka")
    """
    method diatas digunakan saat customer ingin menambahkan item, jumlah dan
    harga barang yang ingin di pesan
    """
    print(self.order)




  def update_name(self, item_name, new_item_name): #untuk update item_name
    self.order[new_item_name] = self.order.pop(item_name)

  def update_qty(self, item_name, new_qty): #untuk update item_qty
    self.order[item_name][0] = new_qty

  def update_price(self, item_name, new_price): #untuk update item_price
    self.order[item_name][1] = new_price
    """
    method diatas digunakan jika ada kesalahan
    dalam memasukkan nama item atau jumlah item atau
    harga item tanpa harus menghapus seluruh itemnya
    """


  def delete_item(self, item_name): #untuk menghapus salah satu item
    self.order.pop(item_name)
    print('Pesanan berhasil di hapus')

  def reset_transaction(self): #untuk menghapus seluruh transaksi
    Transaction = {}
    self.order = Transaction
    print('Anda tidak memiliki pesanan')


  def display_order(self): #untuk menampilakan data yang sudah dihitung dalam bentuk tabel
      display_order = []
      header = ["No.","Nama", "Jumlah", "Harga", "Total"]


      n = 0

      for key, value in self.order.items():
          n += 1
          table_no = n
          item_name = key
          item_qty = value[0]
          item_price = value[1]
          total = item_qty * item_price
          item_data = [table_no, item_name, item_qty, item_price, total]
          display_order.append(item_data)

      print(tabulate(display_order, header, tablefmt="pretty"))


  def check_order(self): #untuk cek tidak ada kesalahan dalam input data
      for key, value in self.order.items():
        item_name = key
        item_qty = value [0]
        item_price = value [1]

      if type(item_name) == str and type(item_qty) == int and type(item_price) == int:
        print('Seluruh pesanan anda sudah benar')
      else:
        print('Terdapat kesalahan input data')

  def total_price(self): #untuk menghitung total belanja yang sudah dibeli

    total_price = 0
    for i in self.order.keys():
      jumlah = self.order[i][0]
      harga = self.order[i][1]
      total_price = total_price + (jumlah * harga)

    if total_price >=  200_000 and total_price <=299_000:
      dapat_diskon = total_price * 0.05
      total_harga = total_price - dapat_diskon
      print(f'anda telah mendapatkan diskon 5%! total belanja anda sebesar Rp.{total_harga:,}');
    elif total_price >= 300_000 and total_price <= 399_000:
      dapat_diskon = total_price * 0.08
      total_harga = total_price - dapat_diskon
      print(f'anda telah mendapatkan diskon 8%! total belanja anda sebesar Rp.{total_harga:,}');
    elif total_price >= 500_000 and total_price <= 599_000:
      dapat_diskon = total_price * 0.1
      total_harga = total_price - dapat_diskon
      print(f'anda telah mendapatkan diskon 10%! total belanja anda sebesar Rp.{total_harga:,}');
    else:
      print(f'total belanja anda sebesar Rp.{total_price:,}')

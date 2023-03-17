class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        print("Nomor antrian anda adalah:", self.size)

    def dequeue(self):
        if self.front is None:
            print("Antrian kosong")
        else:
            removed_data = self.front.data
            self.front = self.front.next
            self.size -= 1
            if self.front is None:
                self.rear = None
            print("Nomor antrian yang dipanggil:", removed_data)

    def display(self):
        if self.front is None:
            print("Antrian kosong")
        else:
            current = self.front
            antrian_str = str(current.data)
            current = current.next
            while current is not None:
                antrian_str += ", " + str(current.data)
                current = current.next
            print("Nomer antrian yang tersedia : ", antrian_str)


# Membuat objek queue
q = Queue()

# Loop utama
while True:
    print("===== Selamat Datang =====")
    print("""
    1. Ambil nomor antrian
    2. Panggil nomor antrian
    3. Menampilkan nomor antrian
    4. Keluar""")
    pilihan = int(input("Masukkan pilihan: "))
    
    if pilihan == 1:
        nomor_antrian = q.size + 1
        q.enqueue(nomor_antrian)
        print()
    elif pilihan == 2:
        q.dequeue()
        print()
    elif pilihan == 3:
        q.display()
        print()
    elif pilihan == 4:
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi")

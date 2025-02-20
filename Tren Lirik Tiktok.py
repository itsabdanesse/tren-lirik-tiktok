import sys
import time


def lirik():
    lirik = [
        ("Sayangnya", 0.18),
        ("Semua Tak Berjalan", 0.22),
        ("Sedangkan", 0.18),
        ("Bertahan Bukan Satu Pilihan", 0.22),
    ]

    
    delay = [0.3, 0.6, 0.3, 0.6, 0.6, 0.3, 0.3]
    print("\n== Sayangnya - Juicy Luicy ==")
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    
    print("// Code by itabdanesse")


lirik()
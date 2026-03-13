from book import Book
import datetime

buku1 = Book(1, "Belajar Python", "Heri", 2025)
buku2 = Book(2, "Belajar Java", "Andi", 2026)

print(buku1.judul)
print(buku1.get_update_terakhir())

buku1.update_judul("python part 1")

print(buku1.judul)
print(buku1.get_update_terakhir())

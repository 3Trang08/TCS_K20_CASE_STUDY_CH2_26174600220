from datetime import datetime

# 1. Lay thoi diem hien tai va chuyen sang dang chuoi (str)
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print("Thoi diem hien tai (datetime):", thoi_diem)
print("Kieu cua thoi_diem:", type(thoi_diem))
print("Thoi diem dang text (str):", thoi_diem_text)
print("Kieu cua thoi_diem_text:", type(thoi_diem_text))

# 2. Tinh thoi luong su dung (ket_thuc - bat_dau)
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau

print("\nThoi luong su dung (timedelta):", thoi_luong)
print("Kieu cua thoi_luong:", type(thoi_luong))

# GIAI THICH KHAC NHAU GIUA CAC KIEU DU LIEU
# datetime: Doitruong thoi gian (ngay, thang, nam, gio, phut, giay) dung de tinh toan thoi gian.
# str: Chuoi ky tu hien thi thoi gian dang van ban, khong tinh toan duoc.
# timedelta: Khoang thoi gian (do chech lech giua 2 moc datetime).
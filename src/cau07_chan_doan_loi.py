
ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: "))  # Da sua: Ep kieu sang float
so_phut = int(input("Nhap so phut: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000

print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f} kWh")  # Da sua: Them dau ngoac ')' va sua ten bien thanh dien_nang_kwh

# CAC LOI DA PHAT HIEN VA CHAN DOAN 
# Loi 1: SyntaxError tai dong 6 (missing closing parenthesis). Nguyen nhan: Thieu dau ngoac dong ')' o cuoi lenh print.
# Loi 2: TypeError tai dong 4 (unsupported operand type for /). Nguyen nhan: cong_suat_w chua duoc chuyen sang kieu so (float) nen khong chia duoc.
# Loi 3: NameError tai dong 6 (name 'dien_nang' is not defined). Nguyen nhan: Goi sai ten bien dien_nang thay vi dien_nang_kwh.
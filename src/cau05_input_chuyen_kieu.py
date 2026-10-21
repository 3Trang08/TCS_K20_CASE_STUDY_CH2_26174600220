
ma_may = input("Nhap ma may: ")
print("Kieu cua ma_may:", type(ma_may))

cong_suat_raw = input("Nhap cong suat (W): ")
print("Kieu cua cong_suat_raw:", type(cong_suat_raw))

so_phut_raw = input("Nhap so phut su dung: ")
print("Kieu cua so_phut_raw:", type(so_phut_raw))

don_gia_raw = input("Nhap don gia dien (VND/kWh): ")
print("Kieu cua don_gia_raw:", type(don_gia_raw))

cong_suat_w = float(cong_suat_raw)
so_phut = int(so_phut_raw)
don_gia_kwh = float(don_gia_raw)

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print(" KET QUA TINH TOAN ")
print("Ma may:", ma_may)
print("Dien nang tieu thu (kWh):", dien_nang_kwh)
print("Chi phi dien (VND):", chi_phi)

tong_phut = 135
cong_suat_w = 250

so_gio = tong_phut // 60
so_phut_du = tong_phut % 60
print("So gio tron ven:", so_gio)
print("So phut con lai:", so_phut_du)

su_dung_lau = tong_phut > 60
print("Su dung lau (> 60 phut):", su_dung_lau)

du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Du lieu hop le:", du_lieu_hop_le)

# Du doan va kiem chung hai bieu thuc
bieu_thuc_1 = 100 + 20 * 3
bieu_thuc_2 = (100 + 20) * 3
print("Ket qua 100 + 20 * 3:", bieu_thuc_1)
print("Ket qua (100 + 20) * 3:", bieu_thuc_2)
diem_mau = [7.5, 8.0, 4.5, 9.0, 6.0, 5.5, 8.5, 3.0]

# Danh sách điểm đạt (>= 5)
diem_dat = [d for d in diem_mau if d >= 5]
print(f"Danh sách các điểm đạt: {diem_dat}")

# Bình phương của các điểm đạt
binh_phuong_diem = [round(d**2, 2) for d in diem_dat]
print(f"Bình phương của các điểm đạt: {binh_phuong_diem}")

# Hàm phụ trợ để xếp loại
def phan_loai(diem):
    if diem >= 8: return 'A'
    elif diem >= 6.5: return 'B'
    elif diem >= 5: return 'C'
    else: return 'F'

# Từ điển khóa là số thứ tự (bắt đầu từ 1) và giá trị là xếp loại
tu_dien_xep_loai = {i+1: phan_loai(diem) for i, diem in enumerate(diem_mau)}
print(f"Xếp loại của từng sinh viên: {tu_dien_xep_loai}")
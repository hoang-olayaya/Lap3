import csv

# ==================== BÀI 5 ====================
# 1. Tạo file sinhvien.txt mẫu
with open("sinhvien.txt", "w", encoding="utf-8") as f:
    f.write("SV01, Nguyen Van A, 8.5\n")
    f.write("SV02, Tran Thi B, 4.0\n")
    f.write("SV03, Le Van C, 7.0\n")

# 2. Đọc file sinhvien.txt và thống kê
ds_sv_txt = []
with open("sinhvien.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(',')
        if len(parts) == 3:
            ds_sv_txt.append(float(parts[2].strip()))

so_luong = len(ds_sv_txt)
dtb_txt = sum(ds_sv_txt) / so_luong
sv_dat = len([d for d in ds_sv_txt if d >= 5])
sv_khong_dat = so_luong - sv_dat

# 3. Ghi kết quả ra baocao.txt
with open("baocao.txt", "w", encoding="utf-8") as f:
    f.write(f"Số lượng sinh viên: {so_luong}\n")
    f.write(f"Điểm trung bình: {dtb_txt:.2f}\n")
    f.write(f"Số sinh viên đạt: {sv_dat}\n")
    f.write(f"Số sinh viên không đạt: {sv_khong_dat}\n")


# ==================== BÀI 6 ====================
# 1. Tạo file diemlop.csv mẫu có chứa dữ liệu lỗi
with open("diemlop.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["MaSV", "HoTen", "Diem"])
    writer.writerow(["SV01", "Hoa", "8.5"])
    writer.writerow(["SV02", "Lan", "11"])   # Lỗi: Điểm ngoài khoảng 0-10
    writer.writerow(["SV03", "Mai", "abc"])  # Lỗi: Điểm không phải số
    writer.writerow(["SV04", "Trúc", "7.0"])

# 2. Đọc file CSV, xử lý lỗi bằng try/except
diem_hop_le = []
loi = []

with open("diemlop.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            diem = float(row["Diem"])
            if 0 <= diem <= 10:
                diem_hop_le.append(diem)
            else:
                loi.append(f"Lỗi: {row['MaSV']} có điểm ({diem}) ngoài khoảng 0-10.")
        except ValueError:
            loi.append(f"Lỗi: {row['MaSV']} có dữ liệu điểm ({row['Diem']}) không phải là số.")

# Tính điểm trung bình hợp lệ
if diem_hop_le:
    dtb_csv = sum(diem_hop_le) / len(diem_hop_le)
    print(f"\nĐiểm trung bình của sinh viên hợp lệ trong CSV: {dtb_csv:.2f}")

# 3. Ghi dữ liệu lỗi ra loi.txt
with open("loi.txt", "w", encoding="utf-8") as f:
    for l in loi:
        f.write(l + "\n")
        
print("Đã hoàn tất quá trình ghi dữ liệu ra các file baocao.txt và loi.txt.")
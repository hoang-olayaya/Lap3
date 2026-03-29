# Tạo danh sách gồm 8 sinh viên (Mã SV, Họ tên, Điểm)
danh_sach_sv = [
    ("SV01", "Nguyễn Văn A", 7.5),
    ("SV02", "Trần Thị B", 8.5),
    ("SV03", "Lê Văn C", 9.0),
    ("SV04", "Phạm Thị D", 6.5),
    ("SV05", "Hoàng Văn E", 4.0),
    ("SV06", "Đỗ Thị F", 8.0),
    ("SV07", "Vũ Văn G", 5.5),
    ("SV08", "Ngô Thị H", 9.5)
]

# In toàn bộ danh sách sinh viên
print("--- TOÀN BỘ DANH SÁCH SINH VIÊN ---")
for sv in danh_sach_sv:
    print(sv)

# Tìm sinh viên có điểm cao nhất
sv_max = max(danh_sach_sv, key=lambda x: x[2])
print(f"\nSinh viên có điểm cao nhất: {sv_max}")

# Tính điểm trung bình của cả lớp
diem_trung_binh = sum(sv[2] for sv in danh_sach_sv) / len(danh_sach_sv)
print(f"Điểm trung bình của cả lớp: {diem_trung_binh:.2f}")

# In danh sách sinh viên có điểm >= 8
print("\n--- SINH VIÊN CÓ ĐIỂM >= 8 ---")
for sv in danh_sach_sv:
    if sv[2] >= 8:
        print(sv)
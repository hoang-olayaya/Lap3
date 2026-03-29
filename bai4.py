def nhap_danh_sach():
    # Trả về một danh sách sinh viên mẫu bằng dictionary để dễ truy xuất
    return [
        {"MaSV": "SV01", "HoTen": "An", "Diem": 7.5},
        {"MaSV": "SV02", "HoTen": "Bình", "Diem": 9.0},
        {"MaSV": "SV03", "HoTen": "Cường", "Diem": 4.5}
    ]

def tinh_diem_trung_binh(ds):
    if not ds: return 0
    return sum(sv["Diem"] for sv in ds) / len(ds)

def tim_sv_max(ds):
    if not ds: return None
    return max(ds, key=lambda x: x["Diem"])

def xep_loai(diem):
    if diem >= 8: return 'A'
    elif diem >= 6.5: return 'B'
    elif diem >= 5: return 'C'
    else: return 'F'

def in_bao_cao(ds):
    print("\n--- BÁO CÁO TỔNG HỢP (BÀI 4) ---")
    for sv in ds:
        loai = xep_loai(sv["Diem"])
        print(f"{sv['MaSV']} - {sv['HoTen']} - Điểm: {sv['Diem']} - Xếp loại: {loai}")
    
    dtb = tinh_diem_trung_binh(ds)
    print(f"Điểm trung bình cả lớp: {dtb:.2f}")
    
    sv_max = tim_sv_max(ds)
    print(f"Sinh viên điểm cao nhất: {sv_max['HoTen']} ({sv_max['Diem']} điểm)")

# Chương trình chính
ds_sinh_vien = nhap_danh_sach()
in_bao_cao(ds_sinh_vien)
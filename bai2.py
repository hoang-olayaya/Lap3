du_lieu_mau = ["Python", "CSDL", "Python", "Java", "CSDL", "AI", "Python"]

# Loại bỏ phần tử trùng lặp bằng set
mon_hoc_set = set(du_lieu_mau)
print(f"Danh sách các môn học (không trùng lặp): {mon_hoc_set}")

# Đếm số lần xuất hiện của từng môn bằng dict
thong_ke = {}
for mon in du_lieu_mau:
    thong_ke[mon] = thong_ke.get(mon, 0) + 1
print(f"Số lần xuất hiện của từng môn: {thong_ke}")

# Môn học được đăng ký nhiều nhất
mon_nhieu_nhat = max(thong_ke, key=thong_ke.get)
print(f"Môn học được đăng ký nhiều nhất: {mon_nhieu_nhat}")

# Sắp xếp kết quả đếm theo số lần giảm dần
thong_ke_sap_xep = dict(sorted(thong_ke.items(), key=lambda x: x[1], reverse=True))
print(f"Kết quả sắp xếp giảm dần: {thong_ke_sap_xep}")
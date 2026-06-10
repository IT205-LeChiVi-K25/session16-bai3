# (1) Phân tích và thiết kế giải pháp
# ---------------------------------------------------------
# Hàm chính:
# - display_patients(patient_list)
#   Input: list bệnh nhân (list of lists)
#   Output: None (in ra màn hình)
#   Luồng xử lý: nếu list rỗng thì báo không có dữ liệu, ngược lại duyệt và in từng bệnh nhân.
#
# - validate_gender(gender_input)
#   Input: chuỗi giới tính
#   Output: True/False
#   Luồng xử lý: strip() và lower(), nếu là "nam" hoặc "nu" thì hợp lệ.
#
# - add_patient(patient_list)
#   Input: list bệnh nhân
#   Output: None (thêm bệnh nhân mới vào list nếu hợp lệ)
#   Luồng xử lý: nhập mã BN, tên, giới tính, chẩn đoán. Chuẩn hóa chuỗi:
#       Mã BN: strip() + upper()
#       Tên BN: strip() + title()
#       Giới tính: strip() + capitalize()
#       Bệnh: strip() + capitalize()
#   Kiểm tra trùng mã bằng find_patient_index. Nếu hợp lệ thì append().
#
# - find_patient_index(patient_list, patient_id)
#   Input: list bệnh nhân, mã BN
#   Output: index hoặc -1
#   Luồng xử lý: chuẩn hóa mã BN, duyệt list, so sánh, trả về index nếu thấy.
#
# - update_diagnosis(patient_list)
#   Input: list bệnh nhân
#   Output: None (cập nhật chẩn đoán bệnh)
#   Luồng xử lý: nhập mã BN, tìm index. Nếu thấy thì nhập chẩn đoán mới, chuẩn hóa, gán lại vào list con.
#
# - search_by_disease(patient_list)
#   Input: list bệnh nhân
#   Output: None (in danh sách bệnh nhân có bệnh chứa từ khóa)
#   Luồng xử lý: nhập từ khóa, strip() + lower(). Nếu rỗng thì báo lỗi. Duyệt list, kiểm tra từ khóa có trong bệnh.lower().
#   In kết quả và tổng số lượng.
#
# Giải pháp tổng thể:
# - Truyền patient_list vào hàm là truyền tham chiếu (reference), nên các hàm thao tác trực tiếp trên list gốc.
# - String là immutable, nên mọi chuẩn hóa phải gán lại.
# - List là mutable, nên append() sẽ thay đổi trực tiếp danh sách.
# ---------------------------------------------------------

patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]

def display_patients(patient_list):
    """Hiển thị danh sách bệnh nhân"""
    if not patient_list:
        print("Hiện không có bệnh nhân nào đang điều trị.")
    else:
        print("----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")
        for i, p in enumerate(patient_list, start=1):
            print(f"{i}. Mã: {p[0]} | Tên: {p[1]} | Giới tính: {p[2]} | Bệnh: {p[3]}")

def validate_gender(gender_input):
    """Kiểm tra giới tính hợp lệ"""
    g = gender_input.strip().lower()
    return g in ["nam", "nu"]

def find_patient_index(patient_list, patient_id):
    """Tìm index bệnh nhân theo mã"""
    pid = patient_id.strip().upper()
    for i, p in enumerate(patient_list):
        if p[0] == pid:
            return i
    return -1

def add_patient(patient_list):
    """Tiếp nhận bệnh nhân mới"""
    print("----- TIẾP NHẬN BỆNH NHÂN MỚI -----")
    pid = input("Nhập mã bệnh nhân: ").strip().upper()
    if not pid:
        print("Mã bệnh nhân không được để trống!")
        return
    if find_patient_index(patient_list, pid) != -1:
        print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return
    name = input("Nhập tên bệnh nhân: ").strip().title()
    if not name:
        print("Tên bệnh nhân không được để trống!")
        return
    gender = input("Nhập giới tính Nam/Nu: ")
    while not validate_gender(gender):
        print("Giới tính không hợp lệ, vui lòng nhập lại!")
        gender = input("Nhập giới tính Nam/Nu: ")
    gender = gender.strip().capitalize()
    diagnosis = input("Nhập chẩn đoán bệnh: ").strip().capitalize()
    if not diagnosis:
        print("Chẩn đoán bệnh không được để trống!")
        return
    patient_list.append([pid, name, gender, diagnosis])
    print("Tiếp nhận bệnh nhân thành công!")

def update_diagnosis(patient_list):
    """Cập nhật chẩn đoán bệnh theo mã BN"""
    print("----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")
    pid = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()
    if not pid:
        print("Mã bệnh nhân không được để trống!")
        return
    idx = find_patient_index(patient_list, pid)
    if idx == -1:
        print(f"Không tìm thấy hồ sơ mang mã {pid}!")
        return
    print(f"Tìm thấy bệnh nhân: {patient_list[idx][1]}")
    print(f"Chẩn đoán hiện tại: {patient_list[idx][3]}")
    new_diag = input("Nhập chẩn đoán mới: ").strip().capitalize()
    if not new_diag:
        print("Chẩn đoán bệnh không được để trống!")
        return
    patient_list[idx][3] = new_diag
    print("Cập nhật chẩn đoán bệnh thành công!")

def search_by_disease(patient_list):
    """Tìm kiếm và thống kê theo tên bệnh"""
    print("----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")
    keyword = input("Nhập từ khóa tên bệnh: ").strip().lower()
    if not keyword:
        print("Từ khóa tìm kiếm không được để trống!")
        return
    results = []
    for p in patient_list:
        if keyword in p[3].lower():
            results.append(p)
    if results:
        print("Kết quả tìm kiếm:")
        for i, p in enumerate(results, start=1):
            print(f"{i}. Mã: {p[0]} | Tên: {p[1]} | Giới tính: {p[2]} | Bệnh: {p[3]}")
    else:
        print("Không tìm thấy bệnh nhân nào phù hợp.")
    print(f"Có tổng cộng {len(results)} bệnh nhân mắc bệnh liên quan đến '{keyword}'.")

# Vòng lặp chính
while True:
    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
    print("1. Hiển thị danh sách bệnh nhân")
    print("2. Tiếp nhận bệnh nhân mới")
    print("3. Cập nhật chẩn đoán bệnh theo mã BN")
    print("4. Tìm kiếm và thống kê theo tên bệnh")
    print("5. Thoát chương trình")
    choice = input("Nhập lựa chọn của bạn: ")
    if choice == "1":
        display_patients(patients)
    elif choice == "2":
        add_patient(patients)
    elif choice == "3":
        update_diagnosis(patients)
    elif choice == "4":
        search_by_disease(patients)
    elif choice == "5":
        print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")

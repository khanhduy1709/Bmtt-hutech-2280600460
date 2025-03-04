from Snhvien import QLSinhVien

def menu():
    qlsv = QLSinhVien()
    while True:
        print("\nChương trình quản lý sinh viên")
        print("1. Thêm sinh viên")
        print("2. Cập nhật thông tin sinh viên theo ID")
        print("3. Xóa sinh viên theo ID")
        print("4. Tìm kiếm sinh viên qua tên")
        print("5. Sắp xếp danh sách sinh viên theo điểm trung bình")
        print("6. Sắp xếp danh sách sinh viên theo tên chuyên ngành")
        print("7. Hiển thị danh sách sinh viên")
        print("0. Thoát")
        choice = input("Nhập lựa chọn của bạn: ")
        
        if choice == '1':
            qlsv.nhap_sinhvien()
        elif choice == '2':
            id_sv = int(input("Nhập ID sinh viên cần cập nhật: "))
            qlsv.update_sinhvien(id_sv)
        elif choice == '3':
            id_sv = int(input("Nhập ID sinh viên cần xóa: "))
            qlsv.delete_by_id(id_sv)
        elif choice == '4':
            ten_sv = input("Nhập tên sinh viên cần tìm: ")
            ket_qua = qlsv.find_by_name(ten_sv)
            if ket_qua:
                qlsv.show_sinhvien()
            else:
                print("Không tìm thấy sinh viên với tên đã nhập.")
        elif choice == '5':
            qlsv.sort_by_id()
            print("Danh sách sinh viên sau khi sắp xếp theo ID:")
            qlsv.show_sinhvien()
        elif choice == '6':
            qlsv.sort_by_name()
            print("Danh sách sinh viên sau khi sắp xếp theo tên:")
            qlsv.show_sinhvien()
        elif choice == '7':
            qlsv.show_sinhvien()
        elif choice == '0':
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    menu()
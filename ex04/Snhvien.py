class SinhVien:
    def __init__(self, id, name, sex, major, diemTB):
        self._id = id
        self._name = name
        self._sex = sex
        self._major = major
        self._diemTB = diemTB
        self.hocLuc = ""    

class QLSinhVien:
    listSinhvien = []

    def generate(self):
        maxId = 1
        if self.soluong_sinhvien() > 0:
            maxId = self.listSinhvien[0]._id
            for sv in self.listSinhvien:
                if maxId < sv._id:
                    maxId = sv._id
            maxId += 1
        return maxId

    def soluong_sinhvien(self):
        return len(self.listSinhvien)

    def nhap_sinhvien(self):
        id = self.generate()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành học: ")
        diemTB = float(input("Nhập điểm trung bình: "))
        sv = SinhVien(id, name, sex, major, diemTB)
        self.xep_loai_hoc_luc(sv)
        self.listSinhvien.append(sv)

    def update_sinhvien(self, id):
        sv = self.tim_sinhvien(id)
        if sv is not None:
            name = input("Nhập tên mới: ")
            sex = input("Nhập giới tính mới: ")
            major = input("Nhập chuyên ngành mới: ")
            diemTB = float(input("Nhập điểm trung bình mới: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xep_loai_hoc_luc(sv)
            print("Cập nhật thông tin sinh viên thành công!")
        else:
            print(f"Sinh viên có ID = {id} không tồn tại")

    def tim_sinhvien(self, id):
        for sv in self.listSinhvien:
            if sv._id == id:
                return sv
        return None

    def find_by_name(self, keyword):
        listSV = []
        for sv in self.listSinhvien:
            if keyword.upper() in sv._name.upper():
                listSV.append(sv)
        return listSV

    def delete_by_id(self, id):
        sv = self.tim_sinhvien(id)
        if sv is not None:
            self.listSinhvien.remove(sv)
            print("Xóa sinh viên thành công!")
            return True
        print(f"Sinh viên có ID = {id} không tồn tại")
        return False

    def xep_loai_hoc_luc(self, sv):
        if sv._diemTB >= 9:
            sv.hocLuc = "Xuất sắc"
        elif sv._diemTB >= 8:
            sv.hocLuc = "Giỏi"
        elif sv._diemTB >= 7:
            sv.hocLuc = "Khá"
        elif sv._diemTB >= 5:
            sv.hocLuc = "Trung bình"
        else:
            sv.hocLuc = "Yếu"

    def show_sinhvien(self):
        print("{:<8} {:<18} {:<8} {:<18} {:<8} {:<10}".format("ID", "Tên", "Giới tính", "Chuyên ngành", "Điểm TB", "Học lực"))
        for sv in self.listSinhvien:
            print("{:<8} {:<18} {:<8} {:<18} {:<8} {:<10}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv.hocLuc))
        print("\n")

    def get_list_sinhvien(self):
        return self.listSinhvien

    def sort_by_id(self):
        self.listSinhvien.sort(key=lambda x: x._id)

    def sort_by_name(self):
        self.listSinhvien.sort(key=lambda x: x._name)
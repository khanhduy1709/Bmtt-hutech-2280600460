def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
try:
    input_string = input("nhập từ danh sách các từ, cacj1 nhau bằng dấu chấm cách:")
    words_list = input_string.split()
    dem_so_lan_xuat_hien = dem_so_lan_xuat_hien(words_list)
    print("Số lần xuất hiện của mỗi từ trong list:", dem_so_lan_xuat_hien)
except Exception as e:
    print("Đã xảy ra lỗi:", e)
    
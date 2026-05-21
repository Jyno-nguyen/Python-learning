#* Input: cu=[11,56,11, 14, 756, 34, 90,11, 11, 65, 0, 33,11]
#* Output: cu=[11,0,11, 14, 33, 34, 56,11, 11, 65, 90, 756,11]
#! Ngoài s ố 11 thì các vị tríkhác sắp xếp theo thứ tự từ bé đến lớn
data=[11,56,11, 14, 756, 34, 90,11, 11, 65, 0, 33,11]
sx=sorted(x for x in data if x!=11)
final=[x if x==11 else sx.pop(0) for x in data ]

#? .sort():CHỈ DÙNG CHO LIST VÀ THAY ĐỔI LUÔN TRÊN LIST CHỨ KHÔNG TẠO LIST MỚI
           #? CÚ PHÁP: list.sort(key=,reverse=) 
           #? key=hàm có sẵn của Python(len,str.lower(),...) hoặc do bạn tự viết bằng lambda

#? sorted(): DÙNG CHO MỌI KIỂU DỮ LIỆU CÓ THỂ LẶP (List, Tuple, String, Dictionary, Set) và tạo ra "LIST MỚI"
             #? CÚ PHÁP: sx=sorted(danh_sach,key=,reverse=)
    #! Riêng với dict
kho = {"cam": 10, "tao": 5, "xoai": 20, "oi": 15}
ket_qua = sorted(kho) #*['cam', 'oi', 'tao', 'xoai']. phần values bị ngó lơ hoàn toàn
ket_qua = sorted(kho.items, key=lambda x:x[1]) #* [('tao', 5), ('cam', 10), ('oi', 15), ('xoai', 20)] 
                                               #* Tạo thành list các tuple với so sánh x[1]




#!PHƯƠNG THỨC XOÁ
#? pop(): Chỉ dùng được cho các kiểu dữ liệu có thể chỉnh sửa (Mutable) trừ tuple, string
          #?list: truyền vào index, nếu không sẽ tự động trừ phần tử cuối
          #?Dict: truyền vào key 
          #?Set: không truyền gì vào () vì set không quan tâm đến index và nó sẽ tự trừ ngẫu nhiên 1 phần tử

#? remove(): Tương tự như pop() nhưng không dùng được cho dict
             #? truyền vào value

#! del: một statement(Câu lệnh của hệ thống)
        #? có thể xoá MỌI BIẾN NHƯNG MUỐN XOÁ PHẦN TỬ BÊN TRONG THÌ CHỈ NHỮNG KIỂU DỮ LIỆU CÓ THỂ CHỈNH SỬA
        #? list: del ds[1], del ds[1:6], del ds[1:-1:1]
        #? dict: del ds["ten"]
        #! không xoá được phần tử trong set vì không có key và không có index
a=[1,2,3]
b=a
del a
print(b) #![1,2,3]: vì a,b cùng trỏ vào 1 list nhưng del CHỈ XOÁ SỢI DÂY LIÊN KẾT







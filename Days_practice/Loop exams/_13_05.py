"""
?Đề bài 1: Hệ thống lọc kết quả huấn luyện AI
Bạn đang xây dựng một công cụ để đọc báo cáo từ các mô hình AI được lưu trong file văn bản. Tuy nhiên, file dữ liệu này (dataset.txt) không phải lúc nào cũng hoàn hảo; có những dòng đầy đủ thông tin, có những dòng bị thiếu, và đôi khi file thậm chí còn không tồn tại.

!Yêu cầu:
?Hãy viết một chương trình Python thực hiện các tác vụ sau:

!Quản lý file an toàn:
Mở file dataset.txt ở chế độ đọc.
Đảm bảo file được đóng tự động sau khi xử lý xong (sử dụng từ khóa as và trình quản lý ngữ cảnh).
Nếu không tìm thấy file, chương trình không được "crash" mà phải in ra thông báo: "Không tìm thấy file dữ liệu!".

!Xử lý dữ liệu từng dòng (Iteration):
Lặp qua từng dòng trong file.
Tách mỗi dòng thành các từ riêng biệt.

!Trích xuất thông tin thông minh (Unpacking):
Mỗi dòng hợp lệ được quy ước gồm: Tên mô hình, Điểm số, và các Tham số cấu hình đi kèm phía sau.
Sử dụng kỹ thuật Asterisk (*) để lấy Tên vào biến name, Điểm vào biến score, và tất cả các tham số còn lại vào một danh sách tên là params.

!Bảo vệ chương trình (Exception Handling):
Dữ liệu hợp lệ phải có ít nhất 2 thành phần (Tên và Điểm).
Nếu một dòng không đủ dữ liệu để gỡ gói (ví dụ chỉ có 1 từ), hãy sử dụng try...except để bắt lỗi ValueError, in thông báo "Bỏ qua một dòng dữ liệu lỗi..." và tiếp tục xử lý dòng tiếp theo thay vì dừng chương trình.

!Định dạng đầu ra:
Với mỗi dòng hợp lệ, in ra màn hình theo định dạng: Mô hình: [tên] | Điểm: [điểm] | Tham số: [danh sách tham số]."""

try:
    with open("dataset_13_15.txt") as f:
        for line in f: #chia thành các list[dòng]
            data=line.split() #tách thành Tên, điểm,.....
            try:
                name,score,*params = data #unpacking
                print(f"Mô hình: {name} | Điểm: {score} | Tham số: {params}")
            except ValueError:
                print("Bỏ qua một dòng dữ liệu lỗi")        
                continue
except FileNotFoundError :
    print("File not found")





#? Đề bài 2: Cho một file text tên draft.txt như sau:
"""
an so dfn Kteam odsa in fasfna Kteam mlfjier
as dfasod nf ofn asdfer fsan dfoans ldnfad Kteam asdfna
asdofn sdf pzcvqp Kteam dfaojf kteam dfna Kteam dfaodf
afdna Kteam adfoasdf ncxvo aern Kteam dfad
"""
#! Trong file này có một số chữ Kteam (Kteam sẽ không xuất hiện ở đầu dòng), và trước nó là một chữ ngẫu nhiên nào đó và nhiệm vụ của bạn là đổi chữ đó thành How. Nhớ là sử dụng vòng lặp.
#!Sau khi đổi thành công, bạn lưu nội dung đó vào file tên kteam.txt.
new=[]
with open("draft.txt") as f:
    for line in f: #lấy ra từng dòng vậy muốn lấy ra từng chữ thì sao
                   #lấy ra từng chữ cái for word in f.read():
        data=line.split()
        for i in range(1,len(data)):
            if data[i]=="Kteam":
                data[i-1]="How"
        new.append(" ".join(data)) #append(): thêm đúng kiểu dữ liệu của " ".join(data): tạo thành 1 chuỗi
                                   #VD: " ".join(an) = an
        #sau cùnng new=['dong1','dong2',...]  
#!Lưu ý: ['an', 'so', 'ofm'] nếu lấy từng phần tử rồi append(word) thì sẽ tạo ra: ['an', 'so', 'ofm']
#!       ['an', 'so', 'ofm'] nếu lấy từng phần tử rồi append(" ".join(word)) thì sẽ tạo ra: ['an so ofm']

with open("kteam.txt","w") as f_new:
    f_new.write("\n".join(new))
    #!Hàm write() từng chuỗi vào file / writelines(): thêm được list

new1=["How" if(i<len(data)-1 and data[i+1]=="Kteam") else data[i] for i in range(len(data))]
        
        



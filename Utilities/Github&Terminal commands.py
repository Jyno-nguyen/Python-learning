#GITHUB   
"""
    *git config: cài đặt thông tin cá nhân cho github
git config --global user.name "Jyno-nguyen"
git config --global user.email "jyno.nguyenviet@gmail.com"

    *git clone — tải repo từ GitHub về máy
git clone https://github.com/Jyno-nguyen/python-learning.git
Giống như download cả folder về, kèm theo lịch sử commit.

    !git add . — chọn tất cả file đã thay đổi để chuẩn bị commit
git add .       # thêm tất cả
git add hello.py  # chỉ thêm 1 file cụ thể

    !git commit — lưu snapshot tại thời điểm đó
git commit -m "mô tả ngắn"
Giống như chụp ảnh code lúc đó, có thể quay lại bất cứ lúc nào.

    !git push — đẩy code lên GitHub
git push
Đồng bộ từ máy lên internet.

    !cp ~/Documents/Jyno-code/hello.py .
Giải thích:

cp = copy
~/Documents/Jyno-code/hello.py = đường dẫn file gốc
. = paste vào đây (folder đang đứng)
~ là ký tự tắt của /Users/nguyenvietha — tiện hơn phải gõ hết!


    ?Những lệnh nên biết thêm:
git status        # xem file nào đã thay đổi chưa commit
git log          # xem lịch sử commit 
git pull          # kéo code mới nhất từ GitHub về máy
git diff          # xem thay đổi cụ thể trong file
git branch        # xem đang ở nhánh nào

   ?Quy trình hàng ngày chỉ cần nhớ 3 lệnh:
git add .
git commit -m "hôm nay làm gì"
git push

 !git add . && git commit -m "Day n update" && git push
"""


#TERMINAL
"""
*DI CHUYEN & XEM THU MUC   
    pwd: Xem dang dung o dau
    ls: Xem danh sach file trong thu muc
    cd ten-folder:Vao trong folder
    cd ..:Ra folder cha (len 1 cap)
    cd ~: Ve thu muc goc (home)
    cd Documents/jyno-code: Vao folder cu the

*TAO & XOA FILE / FOLDER
    mkdir ten-folder: Tao folder moi
    touch ten-file.py: Tao file moi trong thu muc
    rm ten-file.py: Xoa file (khong bung rac)
    rm -rf ten-folder: Xoa ca folder (can than!)

*CHAY PYTHON
    python3 ten-file.py: Chay file Python
    python3 --version: Kiem tra phien ban Python
    python3: Mo Python shell (goi lenh truc tiep)
    pip3 install ten-thu-vien: Cai them thu vien Python

"""
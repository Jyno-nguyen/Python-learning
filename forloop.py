# for variable_1, variable_2, .. variable_n in sequence:
    # for-block
#!Sequence ở đây là một iterable object (có thể là iterator hoặc object cho phép sử dụng indexing hoặc thậm chí không phải hai kiểu trên).
#!với iterator oject thì việc sử dụng for giống sử dụng next() 

#? UNPACKING:
points = [(1, 5), (10, 20), (30, 45)]
for x, y in points:
    print(f"Toạ độ X là {x}, Toạ độ Y là {y}")


students = [("Hoàng", 20, "AI Research"),("Nam", 21, "Data Science"),("An", 19, "Software Engineering")]
for name, age, major in students:
    print(f"Sinh viên {name} ({age} tuổi) học ngành {major}")


    it = [[1, 2, 4], [5, 6, 7], [10, 44, 23, 5]] #!it[2] có 4 phần tử 
    it = [[1, 2, 4], [5, 6, 7], [10, 44]]
    for x, y, *z in it: # Asterisk*: x lấy giá trị đầu tiên
                                # y lấy giá trị thứ 2
                                # *z gom giá trị còn lại lấy toàn bộ (nếu thiếu thì *z ưu tiên lấy[])
        print(x, y, z) #z=[23,5]
                    #z=[]



        #? "Trải" danh sách (Unpacking trong hàm)
        brands = ["Louis Vuitton", "Roja", "Dior"]

        # In bình thường: nó in cả cái list kèm ngoặc vuông
        print(brands) 

        # Dùng asterisk: nó "trải" các phần tử ra như các đối số riêng lẻ
        print(*brands, sep=" --- ") 
        # Kết quả: Louis Vuitton --- Roja --- Dior



        tech_stack = ["Python", "Git"]
        ai_tools = ["TensorFlow", "PyTorch"]

        combined = [*tech_stack, "SQL", *ai_tools]
        print(combined)
        # Kết quả: ['Python', 'Git', 'SQL', 'TensorFlow', 'PyTorch']


#! KHI LẶP TRỰC TIẾP QUA DICT THÌ FOR CHỈ LẤY CÁC KEY, MUỐN LẤY CẢ VALUE THÌ CẦN DÙNG items()
ds={"h":1,"n":2,"z":4}
for k,v in ds: #!ERROR
    print(k,"=>",v)

ds={"h":1,"n":2,"z":4}
for k,v in ds.items():
    print(k,"=>",v)
#!HOẶC
ds={"h":1,"n":2,"z":4}
for k in ds:
    print(k,"=>",ds[k])




#!Unpacking kết hợp với BIẾN RÁC (_).
data = [["10:00", "Error", "404", "Admin", "Page not found"],["10:05", "Warning", "200", "User1", "Slow connection"]]
for time, _, _, _, message in data:
    print(f"Lúc {time}, có tin nhắn: {message}")




#? enumerate(): biến mỗi phần tử thành một cặp: (index, value).
lessons = ["Biến", "Kiểu dữ liệu", "Vòng lặp", "Xử lý file"]
for i, bài in enumerate(lessons, start=1): #Bài 1,....
    print(f"Bài {i}: {bài}")
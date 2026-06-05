
#*polymorphism: tính đa hình 
# Đa hình là khả năng hệ thống cho phép các đối tượng thuộc các Class khác nhau phản hồi theo các cách khác nhau trước CÙNG MỘT lời gọi hàm (phương thức).
# CODE CỰC KHỔ (Nếu không có đa hình)
class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
    def speak(self):
        return f"{self.name} ({self.age} tuổi) {self.sound}!"
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, sound="Gâu Gâu!")
    def sua(self):
        return f"{self.name} ({self.age} tuổi) {self.sound}!"
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, sound="Meo Meo!")
    def meo(self):
        return f"{self.name} ({self.age} tuổi) {self.sound}!"

if __name__ == "__main__":
    so_thu = [Dog("Cậu Vàng", 3),Cat("Miu Miu", 2),Dog("Mực", 5)]
    for con_vat in so_thu:
        if isinstance(con_vat, Dog):
            con_vat.sua()
        elif isinstance(con_vat, Cat):
            con_vat.meo()
    # CODE ĐA HÌNH (Polymorphism) - Chuẩn bài
    for con_vat in so_thu:
        con_vat.speak()  # Chỉ gọi ĐÚNG một tên hàm này thôi!
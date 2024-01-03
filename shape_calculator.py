class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        text = f"Rectangle(width={self.width}, height={self.height})" 
        return text

    def set_width(self, new_width):
        self.width = new_width
    
    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        area = (self.width * self.height)
        return area

    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter

    def get_diagonal(self):
        diagonal_size = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal_size

    def get_picture(self):
        message = ""
        if self.width > 50 or self.height > 50:
            message = "Too big for picture."
        else:
            character = "*"
            line_break = "\n"
            for h in range(self.height):
                for w in range(self.width):
                    message += character
                message += line_break

        return message

    def get_amount_inside(self, shape):
        amount = 0
        if self.width >= shape.width and self.height >= shape.height:
            this_area = self.get_area()
            other_area = shape.get_area()
            amount = int(this_area / other_area)
        return amount


class Square(Rectangle):
    def __init__(self, length):
        self.width = length
        self.height = length

    def __str__(self):
        text = f"Square(side={self.width})"
        return text

    def set_side(self, new_length):
        self.width = new_length
        self.height = new_length
        
    def set_width(self, new_length):
        self.set_side(new_length)
        
    def set_height(self, new_length):
        self.set_side(new_length)

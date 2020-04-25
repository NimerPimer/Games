from PIL import Image, ImageDraw, ImageFont

class Board():
    def __init__(self, board_size):
        self.board_size = board_size
        self.rect_size = 50
        self.board = self.createBoard()
        self.knight = Image.open("knight.jpg")
        self.knight = self.knight.resize((self.rect_size, self.rect_size))
        
    def createBoard(self):
        img_size = self.rect_size * self.board_size
        img = Image.new("RGB", (img_size, img_size), (128, 128, 128)) 
        img1 = ImageDraw.Draw(img)

        for i in range(self.board_size):
            for j in range(self.board_size):
                top = i * self.rect_size
                left = j * self.rect_size
                shape = [(top, left), (top + self.rect_size, left + self.rect_size)]
                if (i + j) % 2 == 0:
                    color = "white"
                else:
                    color = "green"
                img1.rectangle(shape, fill =color)
        return img

    def addKnightToBoard(self, i, j):
        new_im = self.board.copy()
        knight_position_x = i * self.rect_size
        knight_position_y = j * self.rect_size
        new_im.paste(self.knight, (knight_position_x, knight_position_y))
        new_im.save("with_knight.bmp")

    def addNumberToBoard(self, coords, num):
        i, j = coords
        new_im = self.board.copy()
        draw = ImageDraw.Draw(new_im)
        num_position_x = i * self.rect_size
        num_position_y = j * self.rect_size
        font = ImageFont.truetype("Verdana.ttf", 20)
        #w, h = draw.textsize(str(num), font)
        #draw.text((num_position_x + w, num_position_y + h), str(num),(0,0,0), font=font)
        draw.text((num_position_x, num_position_y), str(num),(0,0,0), font=font)
        new_im.save("with_digit.bmp")
        self.board = new_im

    def fillBoard(self, sol):
        for i, coords in enumerate(sol):
            self.addNumberToBoard(coords, i)
        self.board.save("board.bmp")

if __name__ == "__main__":
    board = Board(8)
    #board.addKnightToBoard(0,0)
    #board.addNumberToBoard(1, 1, 2)
    
    

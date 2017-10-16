from PIL import Image, ImageDraw, ImageFont, ImageOps


def get_image(board):
    x = board.num_cols*10
    y = board.num_rows*10
    matrix = board.matrix
    image = Image.new('RGB', (x, y))
    d = ImageDraw.Draw(image)
    font = ImageFont.truetype("Arial.ttf", 9)

    colors = {'A': 'red', 'B': 'yellow', '#': 'black', 'r': 'sienna', 'g': 'limegreen', 'f': 'green', 'm': 'grey',
            'w': 'dodgerblue', '.': 'white'}
    for i in range(0, x, 10):
        for j in range(0, y, 10):
            char = matrix[int(j/10)][int(i/10)].char
            status = matrix[int(j/10)][int(i/10)].status
            fill = colors[char]
            ImageDraw.Draw(image).rectangle(((i, j), (i + 10, j + 10)), fill=fill)
            if char == 'A':
                d.text((i+2,j+1), "A", font=font, fill="Black")
            elif char == 'B':
                d.text((i+3,j+1), "B", font=font, fill="Black")
            elif status == 'open':
                d.text((i+3,j), "+", font=font, fill="Black")
            elif status == "closed":
                d.text((i+4,j+1), "-", font=font, fill="Black")
            elif status == "path":
                d.text((i+3,j+1), "o", font=font, fill="Black")
            d.line((i, j, i, j + 10), fill="black")
            d.line((i+10, j, i, j), fill="black")
    image = ImageOps.expand(image, border=3, fill='black')
    image = image.resize((x*2, y*2))
    return image



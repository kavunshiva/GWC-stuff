image_height = 9
lines = []
char = False

for i in range(image_height):
    lines.append(input("Enter line data: "))

for li in lines:
    char = True
    for px in li:
        if char:        
            print("x"*px)
        else:
            print(" "*px)
        char = not char

#Title:
#    Custom image format
#Credits:
#    Indodapro
#Description:
#    There was no reason to make this but i just decided to. The image itself has 3 numbers at the start of the file, there are for 'Width', 'Height' and 'Pixel_Density' in that order, also thats the named given to the variables in the code. Starting on line 4 is the RGB values, there is not realty a limit to how many you want, pygame will just draw them off screen. I tryed to make a command promt argument so that you could specify the file path upon opening but for now you just have to update the path manualy in the 'ipx_opener.py'. IPX stands for 'Indodapro Pixel'. The test image is very bad, I might try to make a .png converter or something later but for now you're on your own. Thanks, Indodapro.
#Use:
#    Change the 'File_Path' variable in the code the real file path of your Test.ipx
#
#    Keeping in mind that the pixels are drawn from right to left based width ('Width' is the first line in the 'Test.ipx'), height ('Height' is the second line in the 'Test.ipx') and pixel size ('Pixel_Size' is the third line in the 'Test.ipx) you can now begin to edit the RGB values and create as many as you want
#
#    Good luck!

import pygame

pygame.init()

File_Path = 'Test.ipx' #Use full path if needed (idk sometime just that won't work)
Line = 0
X = 0
Y = 0

Screen_Width = 1000
Screen_Height = 1000

screen = pygame.display.set_mode((Screen_Width, Screen_Height))

def read_specific_line(file_path, line_number):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if 0 <= line_number < len(lines):
                return lines[line_number].strip()  # Remove any trailing newline characters
            else:
                return f"Error: Line number {line_number} is out of range."
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    except Exception as e:
        return f"Error: {e}"

def parse_color(color_string):
    try:
        r, g, b = map(int, color_string.split(','))
        return (r, g, b)
    except ValueError:
        return (0, 0, 0)  # Default to black if there is an error

Width = int(read_specific_line(File_Path, 0))
Height = int(read_specific_line(File_Path, 1))
Pixel_Size = int(read_specific_line(File_Path, 2))
Line = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    while Y < Height:
        while X < Width:
            color_string = read_specific_line(File_Path, Line)
            if not color_string.startswith("Error"):
                color = parse_color(color_string)
                pygame.draw.rect(screen, color, (X, Y, Pixel_Size, Pixel_Size))
            Line += 1
            X += Pixel_Size
        X = 0
        Y += Pixel_Size

    pygame.display.flip()

pygame.quit()

from PIL import Image, ImageFilter
import sys, os

jpg_folder = sys.argv[1]
png_folder = sys.argv[2]

if not os.path.exists(png_folder):
    os.mkdir(png_folder)

for file in os.listdir(jpg_folder):
    img = Image.open(f'{jpg_folder}{file}')
    img = img.convert("L")
    clean_name= os.path.splitext(file)[0]
    img.save(f"{png_folder}{clean_name}.png", "png")


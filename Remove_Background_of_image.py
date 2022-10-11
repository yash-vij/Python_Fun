from rembg import remove
from PIL import Image
input_path = 'img2.jpg'
output_path = 'back_removed.jpg'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
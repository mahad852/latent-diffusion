from PIL import Image
import os

NEW_IMAGE_SIZE = (256, 256)
CURRENT_PATH = 'val2017'
NEW_PATH = 'val2017_resized'

os.makedirs(NEW_PATH, exist_ok = True)

print('Resizing Images...')

for file_name in os.listdir(CURRENT_PATH):
    im = Image.open(os.path.join(CURRENT_PATH, file_name))
    im = im.resize(NEW_IMAGE_SIZE)
    im.save(os.path.join(NEW_PATH, file_name))

    print('Image:', file_name, 'resized successfully.')

print('--------------------------')
print('All images resized. Saved to:', NEW_PATH)
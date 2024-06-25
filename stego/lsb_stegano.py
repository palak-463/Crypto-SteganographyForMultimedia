# lsb_stegano.py
from PIL import Image

def lsb_encode(image_path, data):
    print("Encoding LSB...")
    img = Image.open(image_path)
    binary_data = ''.join(format(byte, '08b') for byte in data.encode('utf-8'))
    _, width = img.size
    pixels = list(img.getdata())

    binary_index = 0
    new_pixels = []
    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):  # Iterate over R, G, B values
            if binary_index < len(binary_data):
                new_pixel[i] = (new_pixel[i] & 0xFE) | int(binary_data[binary_index])
                binary_index += 1
        new_pixels.append(tuple(new_pixel))

    img.putdata(new_pixels)
    output_path = image_path.split('.')[0] + '_lsb.png'
    img.save(output_path)
    print("LSB encoded image saved at:", output_path)
    return output_path

def lsb_decode(image_path):
    print("Decoding LSB...")
    img = Image.open(image_path)
    pixels = list(img.getdata())

    binary_data = ''
    for pixel in pixels:
        for i in range(3):  # Iterate over R, G, B values
            binary_data += str(pixel[i] & 1)

    # Convert binary data to bytes
    binary_data = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_data = bytes([int(b, 2) for b in binary_data])

    # Try to decode the data to a string
    try:
        decoded_text = decoded_data.decode('utf-8')
    except UnicodeDecodeError as e:
        print(f"Error decoding text: {e}")
        decoded_text = "Failed to decode hidden message."

    print("Decoded text:", decoded_text)
    return decoded_text.split('\x00')[0]  # Return up to the first null character

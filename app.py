from flask import Flask, render_template, request , flash ,url_for , redirect
from PIL import Image
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

app = Flask(__name__)

# Replace this key with your own 256-bit AES key
static_key = b'\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10' \
             b'\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10'

class LSBWithEncryption():
    def __init__(self, key):
        self.key = key

    def encrypt_message(self, msg):
        padded_msg = msg.ljust((len(msg) // 16 + 1) * 16, b'\0')
        cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_msg = encryptor.update(padded_msg) + encryptor.finalize()
        return encrypted_msg

    def decrypt_message(self, encrypted_msg):
        cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_msg = decryptor.update(encrypted_msg) + decryptor.finalize()
        return decrypted_msg.rstrip(b'\0')

    def encode_image(self, img, msg):
        encrypted_msg = self.encrypt_message(msg.encode())
        length = len(encrypted_msg)
        if length > 255:
            return None  # Text too long
        encoded = img.copy()
        width, height = img.size
        index = 0
        for row in range(height):
            for col in range(width):
                pixel = img.getpixel((col, row))
                if isinstance(pixel, int):
                # Handle grayscale images
                   r, g, b = pixel, pixel, pixel
                else:
                # Handle RGB images
                   r, g, b = pixel[:3]
                if row == 0 and col == 0 and index < length:
                   asc = length
                elif index <= length:
                   asc = encrypted_msg[index - 1]
                else:
                   asc = b
                encoded.putpixel((col, row), (r, g, asc))
                index += 1
        return encoded

    def decode_image(self, img):
        width, height = img.size
        encrypted_msg = b""
        index = 0
        for row in range(height):
            for col in range(width):
                r, g, b = img.getpixel((col, row))
                if row == 0 and col == 0:
                    length = b
                elif index <= length:
                    encrypted_msg += bytes([b])
                index += 1
        decrypted_msg = self.decrypt_message(encrypted_msg)
        return decrypted_msg.decode()

    def encode_image_rlsb(self, img, msg):
        encrypted_msg = self.encrypt_message(msg.encode())
        length = len(encrypted_msg)
        if length > 255:
            return None  # Text too long
        encoded = img.copy()
        width, height = img.size
        index = 0
        for row in range(height):
            for col in range(width):
                r, g, b = img.getpixel((col, row))
                if row == 0 and col == 0 and index < length:
                    asc = length
                elif index <= length:
                    asc = encrypted_msg[index - 1]
                else:
                    asc = b
                encoded.putpixel((col, row), (r, g, asc))
                index += 1
        return encoded

    def decode_image_rlsb(self, img):
        width, height = img.size
        encrypted_msg = b""
        index = 0
        for row in range(height):
            for col in range(width):
                r, g, b = img.getpixel((col, row))
                if row == 0 and col == 0:
                    length = b
                elif index <= length:
                    encrypted_msg += bytes([b])
                index += 1
        decrypted_msg = self.decrypt_message(encrypted_msg)
        return decrypted_msg.decode()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['GET', 'POST'])
def encode():
    if request.method == 'POST':
        text_message = request.form['text_message']
        image_file = request.files['image_file']


        # Check if the image file is selected
        if image_file and image_file.filename != '':
            # Read the image and perform encoding
            combined_image = Image.open(image_file)
            width, height = combined_image.size

            # Divide the image into two equal parts
            part1 = combined_image.crop((0, 0, width // 2, height))
            part2 = combined_image.crop((width // 2, 0, width, height))

            # Encode text using LSB and RLSB techniques
            lsb_with_encryption = LSBWithEncryption(static_key)
            encoded_part1 = lsb_with_encryption.encode_image(part1, text_message)
            encoded_part2 = lsb_with_encryption.encode_image_rlsb(part2, text_message)

            if encoded_part1 and encoded_part2:
                # Combine the encoded parts into a single image
                combined_encoded_image = Image.new('RGB', (width, height))
                combined_encoded_image.paste(encoded_part1, (0, 0))
                combined_encoded_image.paste(encoded_part2, (width // 2, 0))

                # Save the combined encoded image
                output_filename = "combined_encoded_image.png"
                combined_encoded_image.save(output_filename)

                return render_template('index.html', result=f"Image successfully encoded and saved as {output_filename}")

            return render_template('index.html', result="Text too long! (Don't exceed 255 characters)")

    return render_template('index.html')

@app.route('/decode', methods=['GET', 'POST'])
def decode():
    decoded_text = None

    if request.method == 'POST':
        image_file = request.files['image_file']

        # Check if the image file is selected
        if image_file and image_file.filename != '':
            # Read the image and perform decoding
            combined_encoded_image = Image.open(image_file)
            width, height = combined_encoded_image.size

            # Divide the combined image into two parts
            part1 = combined_encoded_image.crop((0, 0, width // 2, height))
            part2 = combined_encoded_image.crop((width // 2, 0, width, height))

            # Decode text from each part using LSB and RLSB techniques
            lsb_with_encryption = LSBWithEncryption(static_key)
            decoded_text1 = lsb_with_encryption.decode_image(part1)
            decoded_text2 = lsb_with_encryption.decode_image_rlsb(part2)

            if decoded_text1 and decoded_text2:
                # Combine the decoded texts
                decoded_text = decoded_text1 

    return render_template('index.html', decoded_msg=decoded_text)

if __name__ == '__main__':
    app.run(debug=True)

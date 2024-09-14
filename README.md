# 🔒 Crypto-Steganography For Multimedia

**Crypto-Steganography For Multimedia** is a secure system designed to allow users to hide and retrieve sensitive information within images and audio files. This system uses advanced cryptographic algorithms and steganographic techniques to ensure the safety of the data while preserving the integrity of the media files.

<br>

## 🎯 System Overview

The system offers an intuitive interface where users can input sensitive text data and select the media type (image or audio) to use as the carrier. The data is encrypted, embedded into the media file, and can later be decrypted without compromising the quality of the file.

<br>

## 🔑 Specifications

- **AES Encryption**: Data is securely encrypted using the **AES (Advanced Encryption Standard)** symmetric encryption algorithm.
- **Image Steganography**: Utilizes hybrid techniques like **LSB (Least Significant Bit)** and **RLSB (Random LSB)** for hiding data in images.
- **Audio Steganography**: Implements the **Phase Coding** technique for embedding encrypted data into audio files.
- **Data Integrity**: Ensures that the encrypted data is seamlessly embedded while maintaining the original quality of the image or audio file.
- **Decryption**: Provides secure decryption, allowing users to retrieve the hidden message without tampering with the media file.
  
<br>

## 📋 System Flow

1. **Data Input**: User inputs sensitive text data.
2. **Media Selection**: User selects the desired media type (image or audio) for embedding the encrypted data.
3. **Encryption**: The text data is encrypted using the **AES** algorithm.
4. **Steganography**:
   - For **images**: A combination of **LSB** and **RLSB** techniques is used.
   - For **audio**: The **Phase Coding** technique is employed.
5. **Embedding**: The encrypted data is embedded into the selected media file.
6. **Decryption**: The hidden message is retrieved by decrypting the encoded multimedia file.

<br>

## ✨ Technologies Used

|------------|
| **Python** | 
| **C**      | 

<br>

## 🚀 Features

- 🔐 **Secure Data Hiding**: Encrypt and embed sensitive information into multimedia files seamlessly.
- 🖼️ **Multi-Media Support**: Works with both image and audio files for data embedding.
- 🛡️ **High Security**: Leverages AES encryption and advanced steganographic techniques for maximum security.
- 🎛️ **User-Friendly Interface**: Simple and intuitive interface for encrypting, embedding, and retrieving hidden data.

<br>

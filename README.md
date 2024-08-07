# Crypto-Steganography For Multimedia

A secure system that allows users to hide and retrieve sensitive information through images and audio files, employing advanced cryptographic algorithms and steganographic techniques. Users interact with the system via an intuitive interface to input text data and select the desired media type. Employing advanced cryptographic algorithms and steganographic techniques, the system ensures the encrypted data is seamlessly embedded within the media files while maintaining their integrity. 

<br>

System Flow:<br><br>
The user provides the data to be hidden and selects the type of media (image or audio) for embedding which is used as a carrier.<br>
The data is encrypted using the AES for symmetric encryption, and then prepared for embedding.<br>
Depending on the selected media type, appropriate steganographic techniques are applied; for images, hybridization of algorithms like LSB and RLSB is used, while audio employs Phase Coding technique.<br>
Message is decrypted when the encoded multimedia file is provided without tampering the quality of the image or audio file.

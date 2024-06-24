# Crypto-Steganography For MultiMedia

A secure system that allows users to hide sensitive information within images and audio files, employing advanced cryptographic algorithms and steganographic techniques.

System Flow:<br>
The user provides the data to be hidden and selects the type of media (image or audio) for embedding which is used as a carrier.<br>
The user data is encrypted using the AES for symmetric encryption, and then prepared for embedding.<br>
Depending on the selected media type, appropriate steganographic techniques are applied; for images, hybridization of algorithms like LSB and RLSB is used, while audio employs phase coding technique.

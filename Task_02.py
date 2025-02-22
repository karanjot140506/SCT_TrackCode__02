from PIL import Image # type: ignore

def encrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()
    
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            encrypted_pixel = (b, g, r)  # Swapping red and blue channels
            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            decrypted_pixel = (b, g, r)  # Swapping back red and blue
            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")

# File paths
input_image = input("Enter the path for the input image: ")
encrypted_image = input("Enter the path for the encrypted image output: ")
decrypted_image = input("Enter the path for the decrypted image output: ")

# Encrypt the image
encrypt_image(input_image, encrypted_image)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image)
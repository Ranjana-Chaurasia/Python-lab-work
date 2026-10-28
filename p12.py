# Digital Image Filter and Color Converter Utility
from PIL import Image, ImageFilter

# Open an image
path = input("Enter image path: ")

try:
    image = Image.open(path).convert("RGB")
    print("Image loaded successfully!")
    while True:
        print("\n1. Grayscale")
        print("2. Black and White")
        print("3. Blur")
        print("4. Save and Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            image = image.convert("L").convert("RGB")
            print("Grayscale filter applied.")

        elif choice == "2":
            gray = image.convert("L")
            image = gray.point(
                lambda pixel: 255 if pixel > 128 else 0
            ).convert("RGB")
            print("Black and white filter applied.")

        elif choice == "3":
            image = image.filter(ImageFilter.BLUR)
            print("Blur filter applied.")

        elif choice == "4":
            output = input("Enter output filename (e.g., result.png): ")
            image.save(output)
            print("Image saved successfully!")
            break

        else:
            print("Invalid choice!")

except FileNotFoundError:
    print("Error: Image file not found.")

except (OSError, ValueError) as error:
    print("Error processing image:", error)
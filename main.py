import cv2
import numpy as np

def restore_image(image_path, denoising_method='fastNlMeansDenoisingColored', denoising_strength=10, show_images=True):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Perform denoising
    if denoising_method == 'fastNlMeansDenoisingColored':
        restored_image = cv2.fastNlMeansDenoisingColored(image, None, denoising_strength, denoising_strength, 7, 21)
    elif denoising_method == 'fastNlMeansDenoising':
        restored_image = cv2.fastNlMeansDenoising(image, None, denoising_strength, 7, 21)
    elif denoising_method == 'medianBlur':
        restored_image = cv2.medianBlur(image, denoising_strength)
    else:
        raise ValueError('Invalid denoising method specified')

    if show_images:
        # Display the input and restored images
        cv2.imshow("Input Image", image)
        cv2.imshow("Restored Image", restored_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return restored_image

def save_image(image, output_path):
    cv2.imwrite(output_path, image)

if __name__ == "__main__":
    input_image_path = "input_image.jpg"
    output_image_path = "restored_image.jpg"

    # Choose the denoising method
    denoising_method = input('Choose denoising method (fastNlMeansDenoisingColored/fastNlMeansDenoising/medianBlur): ')

    # Choose the denoising strength
    denoising_strength = int(input('Enter denoising strength (integer value): '))

    # Call the restore_image function
    restored_image = restore_image(input_image_path, denoising_method=denoising_method, denoising_strength=denoising_strength)

    # Save the restored image
    save_image(restored_image, output_image_path)
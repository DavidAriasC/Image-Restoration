# Image Restoration

This Python script provides a simple way to restore images using OpenCV. It offers three denoising methods: `fastNlMeansDenoisingColored`, `fastNlMeansDenoising`, and `medianBlur`. Users can choose the denoising method and strength to apply to the input image.

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy

## Usage

1. Place the input image in the same directory as the script and name it `input_image.jpg`.
2. Run the script: `python image_restoration.py`.
3. Choose the denoising method by entering one of the following options: `fastNlMeansDenoisingColored`, `fastNlMeansDenoising`, or `medianBlur`.
4. Enter the denoising strength as an integer value.
5. The script will display the input and restored images. Press any key to close the windows.
6. The restored image will be saved in the same directory as `restored_image.jpg`.

## Functions

### restore_image

```python
def restore_image(image_path, denoising_method='fastNlMeansDenoisingColored', denoising_strength=10, show_images=True):
```

- `image_path`: Path to the input image.
- `denoising_method`: Denoising method to use. Options: `'fastNlMeansDenoisingColored'`, `'fastNlMeansDenoising'`, `'medianBlur'`.
- `denoising_strength`: Strength of the denoising effect. Integer value.
- `show_images`: If `True`, displays the input and restored images.

Returns the restored image.

### save_image

```python
def save_image(image, output_path):
```

- `image`: Image to save.
- `output_path`: Path to save the image.

Saves the image to the specified path.
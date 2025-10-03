<p align="center">
  <img src="https://drive.google.com/uc?id=1-X-AEQALq_NXrq2kZq3-NeLVBsbvzJd7" alt="Dibcode Data Augmentation Logo" width="600"/>
</p>

# dibcode-data-augmentation
Open-source tool to generate 20+ augmented images per dataset image.

# Dibcode Data Augmentation

A Python library for automated image data augmentation to expand your datasets. Generate multiple variations of each image using flips, rotations, and transformations.

## Features

- 🔄 **7 transformation types**: Horizontal/vertical flips, 90°/180°/270° rotations, transpose, and transverse
- 📁 **Batch processing**: Process entire directories automatically
- 🎯 **Multiple formats**: Supports JPG, JPEG, and PNG images
- 🛡️ **Error handling**: Robust processing with detailed feedback
- 📊 **Statistics tracking**: See exactly how many images were processed
- 🎨 **Organized output**: Keeps augmented images in separate directories

## Installation

1. Clone the repository:

git clone https://github.com/yourusername/dibcode-data-augmentation.git
cd dibcode-data-augmentation

2. Create a virtual environment:

python -m venv venv

# Activate it:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

## Quick Start

### Basic Usage

from src.augmentation import augment_images
augment_images(input_dir="./images", output_dir="./augmented")

## Transformations

The library applies these transformations to each image:

| Transformation | Description |
|---------------|-------------|
| FLIP_LEFT_RIGHT | Mirror horizontally |
| FLIP_TOP_BOTTOM | Mirror vertically |
| ROTATE_90 | Rotate 90° clockwise |
| ROTATE_180 | Rotate 180° |
| ROTATE_270 | Rotate 270° clockwise |
| TRANSPOSE | Flip over main diagonal |
| TRANSVERSE | Flip over anti-diagonal |

Each input image generates **7 augmented versions** (one per transformation).

## Project Structure

dibcode-data-augmentation/
├── images/
├── src/
│   ├── __init__.py
│   └── augmentation.py       # Main augmentation module
├── run.py
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── LICENSE                    # MIT License

## Usage Example

1. Put your images in the `images/` folder
2. Run the script: python run.py 

(test_env) PS C:\ .. \dibcode-data-augmentation> python run.py

Example output:

Found 3 images. Starting augmentation...
✓ Processed: image1.jpg (7 augmented images created)
✓ Processed: image2.jpg (7 augmented images created)
✓ Processed: image3.jpg (7 augmented images created)

Completed! Processed: 3, Augmented: 21, Failed: 0
Augmented images saved to: ./augmented

## Requirements

- Python >=3.9
- Pillow (PIL)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

Created by Zandor Y. Sanchez Agreda
Dibcode 2025

Open Source Developers:



If you use this project, please give credit by linking back to this repository.

## Roadmap

### Phase 1: Color & Intensity (Easy to implement)
- [ ] Brightness adjustment (5 levels: very dark to very bright)
- [ ] Contrast adjustment (3 levels: low, normal, high)
- [ ] Saturation changes (desaturated, normal, oversaturated)
- [ ] Grayscale conversion

### Phase 2: Noise Addition (Medium difficulty)
- [ ] Gaussian noise (light, medium, heavy)
- [ ] Salt and pepper noise
- [ ] Speckle noise

### Phase 3: Geometric Transformations (Medium difficulty)
- [ ] Random crops (multiple per image)
- [ ] Scaling (zoom in/out)
- [ ] Shearing transformations
- [ ] Elastic deformation

### Phase 4: Occlusion/Cutout (Medium difficulty)
- [ ] Random rectangular cutouts (various sizes)
- [ ] Circular cutouts (various sizes)
- [ ] Grid mask pattern

### Phase 5: Blur & Effects (Easy to implement)
- [ ] Motion blur
- [ ] Sharpening

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Star ⭐ this repo if you find it useful!**
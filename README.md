<p align="center">
  <img src="https://drive.google.com/uc?id=1-X-AEQALq_NXrq2kZq3-NeLVBsbvzJd7" alt="Dibcode Data Augmentation Logo" width="250"/>
</p>

# Dibcode Data Augmentation

A Python library for automated image data augmentation to generate 20+ augmented images per dataset image. Generate multiple variations of each image using flips, rotations, and transformations.

## Features

- 🔄 **7 transformation types**: Horizontal/vertical flips, 90°/180°/270° rotations, transpose, and transverse
- 📁 **Batch processing**: Process entire directories automatically
- 🎯 **Multiple formats**: Supports JPG, JPEG, and PNG images
- 🛡️ **Error handling**: Robust processing with detailed feedback
- 📊 **Statistics tracking**: See exactly how many images were processed
- 🎨 **Organized output**: Keeps augmented images in separate directories

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/dibcode-data-augmentation.git
cd dibcode-data-augmentation
```

2. Create a virtual environment:

```bash
python -m venv venv
```

### Windows:

```bash
venv\Scripts\activate
```

### Mac/Linux:

```bash
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Quick Start

### Basic Usage

```python
from src.augmentation import augment_images
augment_images(input_dir="./images", output_dir="./augmented")
```

## Transformations

The library applies these transformations to each image:

```
| Transformation | Description |
|---------------|-------------|
| FLIP_LEFT_RIGHT | Mirror horizontally |
| FLIP_TOP_BOTTOM | Mirror vertically |
| ROTATE_90 | Rotate 90° clockwise |
| ROTATE_180 | Rotate 180° |
| ROTATE_270 | Rotate 270° clockwise |
| TRANSPOSE | Flip over main diagonal |
| TRANSVERSE | Flip over anti-diagonal |
```

Each input image generates **7 augmented versions** (one per transformation).

## Project Structure

```
dibcode-data-augmentation/
├── images/
├── src/
│   ├── __init__.py
│   └── augmentation.py       # Main augmentation module
├── run.py
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── LICENSE                    # MIT License
```

## Usage Example

1. Put your images in the `images/` folder
2. Run the script: python run.py 

```bash
(test_env) PS C:\ .. \dibcode-data-augmentation> python run.py
```

Example output:

```
Found 3 images. Starting augmentation...
✓ Processed: image1.jpg (7 augmented images created)
✓ Processed: image2.jpg (7 augmented images created)
✓ Processed: image3.jpg (7 augmented images created)

Completed! Processed: 3, Augmented: 21, Failed: 0
Augmented images saved to: ./augmented
```

## Requirements

- Python >=3.9
- Pillow (PIL)

## Contributing

Thank you for your interest in contributing! Follow these steps to submit your changes.

### Prerequisites
- Install [GitHub Desktop](https://desktop.github.com/)
- Create a free [GitHub account](https://github.com/join) if you don't have one

### Step-by-Step Guide for Contributing

#### 1. Fork the Repository
1. Go to the main repository page on GitHub
2. Click the **"Fork"** button in the top-right corner
3. GitHub will create a copy of the repository in your own account

#### 2. Clone Your Fork Using GitHub Desktop
1. Open **GitHub Desktop**
2. Go to **File** → **Clone Repository**
3. Click on the **GitHub.com** tab
4. Find your forked repository in the list (it will be under your username)
5. Choose where to save it on your computer
6. Click **Clone**

#### 3. Create a New Branch
1. In GitHub Desktop, click on **Current Branch** (shows "main")
2. Click **New Branch**
3. Give your branch a descriptive name (e.g., `add-new-feature` or `fix-bug-123`)
4. Click **Create Branch**

#### 4. Make Your Changes
1. Open the project folder on your computer
2. Make your changes using your preferred code editor
3. Save your files

#### 5. Commit Your Changes
1. Go back to **GitHub Desktop**
2. You'll see all your changed files listed on the left
3. Review the changes (green = added, red = removed)
4. Write a **commit message** describing what you changed:
   - Summary (required): Brief description (e.g., "Add data augmentation for images")
   - Description (optional): More details if needed
5. Click **Commit to [your-branch-name]**

#### 6. Push Your Branch to GitHub
1. Click **Publish branch** (if it's your first push)
   - OR click **Push origin** if you've already published it
2. This uploads your changes to your fork on GitHub

#### 7. Create a Pull Request
1. GitHub Desktop will show a button: **Create Pull Request**
   - OR go to your fork on GitHub.com in your web browser
2. Click **Create Pull Request**
3. You'll see a form with:
   - **Title**: Describe your changes briefly
   - **Description**: Explain what you did and why
4. Click **Create Pull Request**

#### 8. Wait for Review
The project maintainer will review your changes. They may:
- ✅ Approve and merge your changes
- 💬 Ask questions or request modifications
- ❌ Close the PR if it doesn't fit the project

#### 9. If Changes Are Requested
1. Make the requested changes in your local files
2. Save the files
3. Go back to **GitHub Desktop**
4. Commit the new changes (repeat step 5)
5. Push to GitHub (repeat step 6)
6. The Pull Request will automatically update!

### Important Notes
- ⚠️ **Always create a new branch** - never work directly on the `main` branch
- 🔄 **One branch per feature** - create separate branches and PRs for unrelated changes
- 📝 **Write clear commit messages** - help others understand what you changed

Thank you for contributing! 🎉

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

Created by Zandor Y. Sanchez Agreda

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

© 2025 Dibcode

**Star ⭐ this repo if you find it useful!**
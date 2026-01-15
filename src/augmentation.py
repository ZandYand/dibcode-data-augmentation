from PIL import Image, ImageEnhance
import os
from typing import List, Tuple, Optional
import numpy as np


class ImageAugmenter:
    TRANSFORMATIONS = {
        "FLIP_LEFT_RIGHT": Image.FLIP_LEFT_RIGHT,
        "FLIP_TOP_BOTTOM": Image.FLIP_TOP_BOTTOM,
        "ROTATE_90": Image.ROTATE_90,
        "ROTATE_180": Image.ROTATE_180,
        "ROTATE_270": Image.ROTATE_270,
        "TRANSPOSE": Image.TRANSPOSE,
        "TRANSVERSE": Image.TRANSVERSE
    }

    contrast_levels_rgb = {
        "LOW": 0.5,
        "MEDIUM": 1,
        "HIGH": 1.5,
        "VERY_HIGH": 2,
        "TOO_HIGH": 2.5
    }
    
    contrast_levels_white_and_black = {
        "LOW": 2,
        "MEDIUM": 4,
        "HIGH": 8,
        "VERY_HIGH": 16,
        "TOO_HIGH": 32
    }

    brightness_levels = {
        "LOW": 0.5,
        "MEDIUM": 1,
        "HIGH": 1.5,
        "VERY_HIGH": 2,
        "TOO_HIGH": 2.5
    }

    def __init__(self, input_dir: str = ".", output_dir: Optional[str] = None):
        self.input_dir = input_dir
        self.output_dir = output_dir or os.path.join(input_dir, "augmented")
        os.makedirs(self.output_dir, exist_ok=True)

    def get_image_files(self, extensions: Tuple[str, ...] = ('.jpg', '.jpeg', '.png')) -> List[str]:
        try:
            files = [
                f for f in os.listdir(self.input_dir)
                if f.lower().endswith(extensions)
            ]
            return files
        except FileNotFoundError:
            raise FileNotFoundError(f"Input directory '{self.input_dir}' not found")

    def contrast_image(self, image: Image.Image, filename: str) -> int:
        base_name, extension = os.path.splitext(filename)
        count = 0
        
        if image.mode != 'RGB':
            if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
                image = image.convert('RGBA')  # Primero a RGBA
                background = Image.new('RGB', image.size, (100, 100, 100))  # Fondo gris
                background.paste(image, (0, 0), image)
                image = background
            else:
                image = image.convert('RGB')
                
        for level_name, level_value in self.contrast_levels_rgb.items():
            enhancer = ImageEnhance.Contrast(image)
            new_img = enhancer.enhance(level_value)
            output_filename = f"{base_name}_contrast_rgb_{level_name.lower()}{extension}"
            new_img.save(os.path.join(self.output_dir, output_filename))
            count += 1
        return count

    def brightness_image(self, image: Image.Image, filename: str) -> int:
        base_name, extension = os.path.splitext(filename)
        count = 0
        
        if image.mode != 'RGB':
            if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
                image = image.convert('RGBA')  # Primero a RGBA
                background = Image.new('RGB', image.size, (100, 100, 100))  # Fondo gris
                background.paste(image, (0, 0), image)
                image = background
            else:
                image = image.convert('RGB')
                
        for level_name, level_value in self.brightness_levels.items():
            enhancer = ImageEnhance.Brightness(image)
            new_img = enhancer.enhance(level_value)
            output_filename = f"{base_name}_brightness_{level_name.lower()}{extension}"
            new_img.save(os.path.join(self.output_dir, output_filename))
            count += 1
        return count

    def quantize_image(self, image: Image.Image, filename: str) -> int:
        base_name, extension = os.path.splitext(filename)
        count = 0
        
        if image.mode != 'RGB':
            if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
                image = image.convert('RGBA')  # Primero a RGBA
                background = Image.new('RGB', image.size, (100, 100, 100))  # Fondo gris
                background.paste(image, (0, 0), image)
                image = background
            else:
                image = image.convert('RGB')
        
        img_array = np.array(image, dtype=np.uint8)
        
        for level_name, n_levels in self.contrast_levels_white_and_black.items():
            quantized = (img_array // (256 // n_levels)) * (256 // n_levels)
            
            quantized_img = Image.fromarray(quantized.astype(np.uint8), 'RGB')
            output_filename = f"{base_name}_quantized_{level_name.lower()}{extension}"
            quantized_img.save(os.path.join(self.output_dir, output_filename))
            count += 1
        
        return count

    def augment_image(self, image: Image.Image, filename: str) -> int:
        base_name = os.path.splitext(filename)[0]
        extension = os.path.splitext(filename)[1]
        count = 0
        for transform_name, transform_method in self.TRANSFORMATIONS.items():
            try:
                augmented = image.transpose(transform_method)
                output_filename = f"{transform_name}_{base_name}{extension}"
                output_path = os.path.join(self.output_dir, output_filename)
                augmented.save(output_path)
                count += 1
            except Exception as e:
                print(f"Warning: Failed to apply {transform_name} to {filename}: {e}")
        return count

    def process_directory(self, extensions: Tuple[str, ...] = ('.jpg', '.jpeg', '.png')) -> dict:
        image_files_names = self.get_image_files(extensions)
        if not image_files_names:
            print(f"No images found in '{self.input_dir}' with extensions {extensions}")
            return {"processed": 0, "augmented": 0, "failed": 0}
        
        statistics = {"processed": 0, "augmented": 0, "failed": 0}
        print(f"Found {len(image_files_names)} images. Starting augmentation...")
        
        for filename in image_files_names:
            try:
                image_path = os.path.join(self.input_dir, filename)
                with Image.open(image_path) as img:
                    count = self.augment_image(img, filename)
                    count += self.contrast_image(img, filename)
                    count += self.brightness_image(img, filename)
                    count += self.quantize_image(img, filename)
                    
                    statistics["processed"] += 1
                    statistics["augmented"] += count
                    print(f"✓ Processed: {filename} ({count} augmented images created)")
            except Exception as e:
                statistics["failed"] += 1
                print(f"✗ Failed to process {filename}: {e}")
        
        print(f"\nCompleted! Processed: {statistics['processed']}, Augmented: {statistics['augmented']}, Failed: {statistics['failed']}")
        print(f"Augmented images saved to: {self.output_dir}")
        return statistics


def augment_images(input_dir: str = ".", output_dir: Optional[str] = None) -> dict:
    augmenter = ImageAugmenter(input_dir, output_dir)
    return augmenter.process_directory()

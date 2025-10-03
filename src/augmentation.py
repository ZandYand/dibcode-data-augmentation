from PIL import Image
import os
from typing import List, Tuple, Optional

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
    
    def __init__(self, input_dir: str = ".", output_dir: Optional[str] = None):
        """
        Args:
            input_dir: Directory containing input images (default: current directory)
            output_dir: Directory to save augmented images (default: input_dir/augmented)
        """
        self.input_dir = input_dir
        self.output_dir = output_dir or os.path.join(input_dir, "augmented")
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
    
    def get_image_files(self, extensions: Tuple[str, ...] = ('.jpg', '.jpeg', '.png')) -> List[str]:
        """
        Args:
            extensions: Tuple of valid image extensions
        """
        try:
            files = [
                f for f in os.listdir(self.input_dir)
                if f.lower().endswith(extensions)
            ]
            return files
        except FileNotFoundError:
            raise FileNotFoundError(f"Input directory '{self.input_dir}' not found")
    
    def augment_image(self, image: Image.Image, filename: str) -> int:
        """
        Args:
            image: PIL Image object
            filename: Original filename
            
        Returns:
            Number of augmented images created
        """
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
        """
        Process all images in the input directory.
        
        Args:
            extensions: Tuple of valid image extensions
            
        Returns:
            Dictionary with processing statistics
        """
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
                    statistics["processed"] += 1
                    statistics["augmented"] += count
                    print(f"✓ Processed: {filename} ({count} augmented images created)")
            except Exception as e:
                statistics["failed"] += 1
                print(f"✗ Failed to process {filename}: {e}")
        
        print(f"\nCompleted! Processed: {statistics['processed']}, "
              f"Augmented: {statistics['augmented']}, Failed: {statistics['failed']}")
        print(f"Augmented images saved to: {self.output_dir}")
        
        return statistics


def augment_images(input_dir: str = ".", output_dir: Optional[str] = None) -> dict:
    """
    Args:
        input_dir: Directory containing input images
        output_dir: Directory to save augmented images
    """
    augmenter = ImageAugmenter(input_dir, output_dir)
    return augmenter.process_directory()
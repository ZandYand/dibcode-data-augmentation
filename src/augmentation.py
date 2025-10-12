from PIL import Image
import os
from typing import List, Tuple, Optional, Dict
import numpy as np

"""
This module converts images to grayscale and optionally to binary (black & white) mode.
It reduces color distractions while preserving visual details, ideal for accessibility or
contrast testing in low-light or high-contrast conditions.
"""

class ImageAugmenter:
    GRAYSCALE_MODES = {
        "weighted": [0.299, 0.587, 0.114],      # Estándar BT.601
        "average": [0.333, 0.333, 0.333],       # Promedio simple
        "luminosity": [0.2126, 0.7152, 0.0722]  # Estándar BT.709
    }

    def __init__(self, input_dir: str = ".", output_dir: Optional[str] = None,
                 enable_grayscale: bool = True, grayscale_method: str = "weighted",
                 enable_blackwhite: bool = True, detail_threshold: float = 0.95,
                 analyze_intensity: bool = True):
        """
        Args:
            input_dir: Directory containing input images
            output_dir: Directory to save augmented images
            enable_grayscale: Whether to apply grayscale transformations
            grayscale_method: Method for grayscale conversion
            enable_blackwhite: Whether to create black & white (binary) images
            detail_threshold: Max allowed proportion of fully black/white pixels before warning
            analyze_intensity: Whether to analyze pixel intensity
        """
        self.input_dir = input_dir
        self.output_dir = output_dir or os.path.join(input_dir, "augmented")
        self.enable_grayscale = enable_grayscale
        self.grayscale_method = grayscale_method
        self.enable_blackwhite = enable_blackwhite
        self.detail_threshold = detail_threshold
        self.analyze_intensity = analyze_intensity

        os.makedirs(self.output_dir, exist_ok=True)

    # ------------------------------
    # ESCALA DE GRISES
    # ------------------------------
    def apply_grayscale(self, image: Image.Image, filename: str) -> int:
        if not self.enable_grayscale:
            return 0

        base_name, extension = os.path.splitext(filename)
        count = 0

        try:
            if image.mode != "RGB":
                rgb_image = image.convert("RGB")
            else:
                rgb_image = image

            if self.grayscale_method in self.GRAYSCALE_MODES:
                gray_image = self._weighted_grayscale(rgb_image, self.GRAYSCALE_MODES[self.grayscale_method])
            else:
                gray_image = rgb_image.convert("L")

            if self.analyze_intensity:
                self._analyze_pixel_intensity(gray_image, filename)

            output_filename = f"GRAYSCALE_{self.grayscale_method.upper()}_{base_name}{extension}"
            gray_path = os.path.join(self.output_dir, output_filename)
            gray_image.save(gray_path)
            count += 1

            # Si está habilitado, crear versión binaria (B/W)
            if self.enable_blackwhite:
                bw_image = self._convert_to_blackwhite(gray_image)
                bw_filename = f"BLACKWHITE_{base_name}{extension}"
                bw_path = os.path.join(self.output_dir, bw_filename)
                bw_image.save(bw_path)
                count += 1

                # Revisar pérdida de detalle
                self._analyze_detail_loss(bw_image, filename)

        except Exception as e:
            print(f"⚠️  Warning: Failed to apply grayscale to {filename}: {e}")

        return count

    # ------------------------------
    # ANÁLISIS DE INTENSIDAD
    # ------------------------------
    def _analyze_pixel_intensity(self, gray_image: Image.Image, filename: str):
        try:
            pixels = gray_image.load()
            width, height = gray_image.size
            print(f"\n--- Análisis de intensidad para {filename} ---")
            print(f"Dimensiones: {width}x{height}")
            print(f"Modo: {gray_image.mode}")

            center_x, center_y = width // 2, height // 2
            print("Muestra 5x5 píxeles del centro:")
            for y in range(center_y - 2, center_y + 3):
                row_vals = []
                for x in range(center_x - 2, center_x + 3):
                    if 0 <= x < width and 0 <= y < height:
                        intensity = pixels[x, y]
                        row_vals.append(f"{intensity:3d}")
                print("  " + " ".join(row_vals))

            intensities = [pixels[x, y] for x in range(0, width, max(1, width // 10))
                           for y in range(0, height, max(1, height // 10))]
            print(f"Rango de intensidad: {min(intensities)} - {max(intensities)}")
            print(f"Intensidad promedio: {sum(intensities) // len(intensities)}")

        except Exception as e:
            print(f"⚠️  No se pudo analizar intensidad para {filename}: {e}")

    # ------------------------------
    # CONVERSIÓN A ESCALA DE GRISES (NUMPY)
    # ------------------------------
    def _weighted_grayscale(self, image: Image.Image, coefficients: List[float]) -> Image.Image:
        img_array = np.array(image)
        gray_array = np.dot(img_array[..., :3], coefficients)
        gray_array = np.clip(gray_array, 0, 255).astype(np.uint8)
        return Image.fromarray(gray_array, mode="L")

    # ------------------------------
    # CONVERSIÓN A BLANCO Y NEGRO
    # ------------------------------
    def _convert_to_blackwhite(self, gray_image: Image.Image, threshold: int = 127) -> Image.Image:
        """
        Convierte una imagen en escala de grises a blanco y negro (binaria).
        """
        gray_array = np.array(gray_image)
        bw_array = (gray_array > threshold).astype(np.uint8) * 255
        return Image.fromarray(bw_array, mode="L")

    # ------------------------------
    # DETECCIÓN DE PÉRDIDA DE DETALLE
    # ------------------------------
    def _analyze_detail_loss(self, bw_image: Image.Image, filename: str):
        """
        Detecta si la imagen binaria perdió demasiados detalles (demasiado negra o blanca).
        """
        bw_array = np.array(bw_image)
        total_pixels = bw_array.size
        black_ratio = np.sum(bw_array == 0) / total_pixels
        white_ratio = np.sum(bw_array == 255) / total_pixels

        if black_ratio > self.detail_threshold or white_ratio > self.detail_threshold:
            print(f"⚠️  Advertencia: {filename} podría haber perdido detalles.")
            print(f"    Negros: {black_ratio:.2%}, Blancos: {white_ratio:.2%}")

    # ------------------------------
    # PROCESAMIENTO GENERAL
    # ------------------------------
    def get_image_files(self, extensions: Tuple[str, ...] = (".jpg", ".jpeg", ".png")) -> List[str]:
        try:
            return [f for f in os.listdir(self.input_dir) if f.lower().endswith(extensions)]
        except FileNotFoundError:
            raise FileNotFoundError(f"Input directory '{self.input_dir}' not found")

    def augment_image(self, image: Image.Image, filename: str) -> int:
        return self.apply_grayscale(image, filename)

    def process_directory(self, extensions: Tuple[str, ...] = (".jpg", ".jpeg", ".png")) -> dict:
        image_files = self.get_image_files(extensions)
        if not image_files:
            print(f"No se encontraron imágenes en '{self.input_dir}' con extensiones {extensions}")
            return {"processed": 0, "augmented": 0, "failed": 0}

        stats = {"processed": 0, "augmented": 0, "failed": 0}
        print(f"Encontradas {len(image_files)} imágenes. Iniciando conversión...")

        for filename in image_files:
            try:
                image_path = os.path.join(self.input_dir, filename)
                with Image.open(image_path) as img:
                    count = self.augment_image(img, filename)
                    stats["processed"] += 1
                    stats["augmented"] += count
                    print(f"✓ {filename} procesada ({count} variantes creadas)")
            except Exception as e:
                stats["failed"] += 1
                print(f"✗ Falló {filename}: {e}")

        print(f"\nCompletado. Procesadas: {stats['processed']}, "
              f"Aumentadas: {stats['augmented']}, Fallidas: {stats['failed']}")
        print(f"Imágenes guardadas en: {self.output_dir}")

        return stats


# ------------------------------
# FUNCIÓN PRINCIPAL (ENTRY POINT)
# ------------------------------
def augment_images(input_dir: str = ".", output_dir: Optional[str] = None,
                   enable_grayscale: bool = True, grayscale_method: str = "weighted",
                   enable_blackwhite: bool = True, detail_threshold: float = 0.95,
                   analyze_intensity: bool = True) -> dict:
    augmenter = ImageAugmenter(
        input_dir=input_dir,
        output_dir=output_dir,
        enable_grayscale=enable_grayscale,
        grayscale_method=grayscale_method,
        enable_blackwhite=enable_blackwhite,
        detail_threshold=detail_threshold,
        analyze_intensity=analyze_intensity
    )
    return augmenter.process_directory()

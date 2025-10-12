from src.augmentation import augment_images
resultados = augment_images(input_dir="./images", output_dir="./augmented")

print(f"\n✅ ¡Proceso completado!")
print(f"📊 Estadísticas: {resultados}")
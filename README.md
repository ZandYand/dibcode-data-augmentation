# 🖼️ Data Augmentation: Conversión a Escala de Grises

Este proyecto realiza un **aumento de datos (data augmentation)** mediante la **transformación de imágenes a escala de grises**.  
El objetivo es generar versiones simplificadas de las imágenes originales, eliminando la información de color para resaltar el contraste, facilitar el análisis visual y preparar los datos para modelos de visión por computadora.

---

## 🎯 Objetivo

Transformar un conjunto de imágenes de entrada en versiones monocromáticas (escala de grises y blanco y negro), con el fin de:

- Reducir distracciones visuales.
- Mejorar el contraste para tareas de análisis o accesibilidad.
- Ampliar el conjunto de datos (_data augmentation_) sin alterar el contenido semántico de las imágenes.

---

## ⚙️ Estructura del Proyecto

dibcode-data-augmentation/
│
├── run.py # Script principal de ejecución
├── src/
│ ├── init.py
│ └── augmentation.py # Lógica de procesamiento y análisis
│
├── images/ # Carpeta con imágenes originales
└── augmented/ # Carpeta donde se guardan las imágenes procesadas

---

## 🚀 Ejecución

Para iniciar el procesamiento:

````bash
python3 run.py

## 🚀 Ejecución del Proyecto

```bash
🚀 Iniciando aumento de datos con escala de grises...
Encontradas 3 imágenes. Iniciando conversión...

--- Análisis de intensidad para HappyDoginPetStore.jpeg ---
Dimensiones: 1200x1200
Modo: L
Rango de intensidad: 3 - 251
Intensidad promedio: 109
✓ HappyDoginPetStore.jpeg procesada (2 variantes creadas)

--- Análisis de intensidad para UH60BlackHawk.jpg ---
Dimensiones: 1280x853
Modo: L
Rango de intensidad: 26 - 249
Intensidad promedio: 138
✓ UH60BlackHawk.jpg procesada (2 variantes creadas)

--- Análisis de intensidad para GithubIcon.png ---
Dimensiones: 512x512
Modo: L
Rango de intensidad: 0 - 0
Intensidad promedio: 0
⚠️ Advertencia: GithubIcon.png podría haber perdido detalles.
✓ GithubIcon.png procesada (2 variantes creadas)

Completado. Procesadas: 3, Aumentadas: 6, Fallidas: 0
Imágenes guardadas en: ./augmented
````

import numpy as np
from PIL import Image
from config import OUTPUT_FORMAT, OUTPUT_QUALITY

def read_image(image_path):
    """Загрузка изображения"""
    try:
        return Image.open(image_path)
    except Exception as e:
        print(f"Ошибка загрузки изображения: {e}")
        return None

def solarize(image, threshold):
    """Соляризация изображения"""
    img_array = np.array(image)
    solarized = np.where(img_array > threshold, 255 - img_array, img_array)
    return Image.fromarray(solarized.astype('uint8'))

def log_contrast(image, c):
    """Логарифмическое контрастирование"""
    img_array = np.array(image).astype('float32')
    log_transformed = c * np.log(1 + img_array)
    log_transformed = (log_transformed / log_transformed.max()) * 255
    return Image.fromarray(log_transformed.astype('uint8'))

def save_result(image, filename):
    """Сохранение результата"""
    try:
        image.save(filename, format=OUTPUT_FORMAT, quality=OUTPUT_QUALITY)
        print(f"Изображение сохранено как {filename}")
    except Exception as e:
        print(f"Ошибка сохранения: {e}")

def process_image(input_path, solar_threshold, log_c):
    """Основная функция обработки"""
    img = read_image(input_path)
    if img is None:
        return
    
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Соляризация
    solarized = solarize(img, solar_threshold)
    save_result(solarized, "solarized_output.jpg")
    
    # Логарифмическое контрастирование
    log_processed = log_contrast(img, log_c)
    save_result(log_processed, "log_contrast_output.jpg")
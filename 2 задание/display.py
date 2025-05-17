import matplotlib.pyplot as plt
from image_processor import read_image

def show_results():
    original = read_image("input.jpg")
    solarized = read_image("solarized_output.jpg")
    log_contrast = read_image("log_contrast_output.jpg")
    
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(original)
    plt.title("Оригинал")
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.imshow(solarized)
    plt.title("Соляризация")
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(log_contrast)
    plt.title("Логарифмическое контрастирование")
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    show_results()
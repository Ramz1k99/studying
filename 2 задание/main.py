from image_processor import process_image
from config import INPUT_IMAGE, SOLAR_THRESHOLD, LOG_C

def main():
    process_image(
        input_path=INPUT_IMAGE,
        solar_threshold=SOLAR_THRESHOLD,
        log_c=LOG_C
    )

if __name__ == "__main__":
    main()
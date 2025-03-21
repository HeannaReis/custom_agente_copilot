from core.handlers.signal_handler import setup_signal_handler
from services.image_processor import ImageProcessor

def main():
    setup_signal_handler()
    processor = ImageProcessor()
    processor.process_images()

if __name__ == "__main__":
    main()
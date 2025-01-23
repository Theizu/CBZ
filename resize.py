import fitz  # PyMuPDF
import os
import zipfile
from PIL import Image


def save_resized_image(pix, save_path, max_width, max_height):
    """Resize a Pixmap object and save it as an image."""
    # Convert Pixmap to a PIL Image
    image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    # Resize the image if it exceeds the max dimensions
    if pix.width > max_width or pix.height > max_height:
        image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
    
    # Save the resized image
    image.save(save_path, "JPEG")


def pdf_to_cbz(pdf_path, cbz_path, max_width=1448, max_height=1072):
    # Ensure the CBZ file has the correct extension
    if not cbz_path.endswith('.cbz'):
        cbz_path += '.cbz'

    # Create a temporary directory to store the extracted images
    temp_dir = "temp_images"
    os.makedirs(temp_dir, exist_ok=True)

    try:
        # Open the PDF
        pdf_document = fitz.open(pdf_path)
        num_pages = pdf_document.page_count

        # Iterate through the pages and save them as images
        for page_num in range(num_pages):
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap()

            # Generate file name with zero padding
            if page_num == 0:
                image_filename = os.path.join(temp_dir, "0000.jpg")
            else:
                image_filename = os.path.join(temp_dir, f"{page_num:04}.jpg")

            # Save the resized image
            save_resized_image(pix, image_filename, max_width, max_height)

        # Create the CBZ file
        with zipfile.ZipFile(cbz_path, "w", zipfile.ZIP_DEFLATED) as cbz:
            for root, _, files in os.walk(temp_dir):
                for file in sorted(files):
                    cbz.write(os.path.join(root, file), file)

        print(f"CBZ file created successfully: {cbz_path}")

    finally:
        # Clean up temporary files
        for root, _, files in os.walk(temp_dir):
            for file in files:
                os.remove(os.path.join(root, file))
        os.rmdir(temp_dir)


def convert_all_pdfs_in_current_folder():
    # Get the current working directory
    current_folder = os.getcwd()

    # Get all PDF files in the current folder
    pdf_files = [f for f in os.listdir(current_folder) if f.lower().endswith('.pdf')]

    if not pdf_files:
        print("No PDF files found in the current folder.")
        return

    # Process each PDF file
    for pdf_file in pdf_files:
        pdf_path = os.path.join(current_folder, pdf_file)
        cbz_filename = os.path.splitext(pdf_file)[0] + ".cbz"
        cbz_path = os.path.join(current_folder, cbz_filename)

        print(f"Processing: {pdf_file}")
        pdf_to_cbz(pdf_path, cbz_path)


# Run the script
if __name__ == "__main__":
    convert_all_pdfs_in_current_folder()

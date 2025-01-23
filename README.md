# Full Image Ebook for EBook Readers
Converting PDF and resize the images for ebook. This is useful for pdf that is full of images eg. Kids Books, Manga, Comic

This has been tested with Kobo Clara Color

This guide explains how to convert PDF files into CBZ format, resizing images to a maximum resolution of `1448 x 1072` pixels while maintaining the aspect ratio. 

---

## Dependencies

To use this script, you need the following:

1. **Python 3.7 or later**  
   Download it from the [official Python website](https://www.python.org/).

2. **Python Libraries**  
   Install the required libraries:
   - [PyMuPDF](https://pymupdf.readthedocs.io/): For extracting images from PDFs.
   - [Pillow](https://python-pillow.org/): For resizing images.

---

## Installation Steps

1. **Install Python**  
   Download and install Python 3.7 or later from [python.org](https://www.python.org/). Ensure `pip` is included in the installation.

2. **Install Required Libraries**  
   Use the following command in your terminal or command prompt:
   ```bash
   pip install pymupdf pillow

## Usage
1. **Convert PDF to CBZ**
   Place all your PDF file in the same folder as the python files.
   Use the following command to convert all PDF in the same folder to CBZ
   ```bash
   python pdftocbz.py

2. **Resize CBZ**
   To reduce the size of the CBZ files use the following command. By default all images resized to a maximum of 1448 x 1072 pixels.
   ```bash
   python resize.py


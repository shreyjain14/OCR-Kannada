# Image Text Extractor

A Flask web application that uses Google's Gemini AI model to extract text from uploaded images.

## Features

- Upload images in various formats (jpg, jpeg, png, gif, svg, bmp)
- Automatic text extraction from uploaded images
- Clean interface with form validation
- Automatic cleanup of processed images

## Prerequisites

- Python 3.7 or higher
- Google Cloud API key for Gemini AI

## Installation

1. Clone the repository:
```bash
git clone https://github.com/shreyjain14/Kannada-OCR.git
cd Kannada-OCR
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Copy the `.env.example` file to `.env`
   - Fill in the required environment variables:
     ```
     SECRET_KEY=your_flask_secret_key
     GOOGLE_API_KEY=your_google_api_key
     ```

## Project Structure

```
├── app.py              # Main Flask application
├── ai.py               # AI functionality using Google Gemini
├── requirements.txt    # Python dependencies
├── .env                # Environment variables
├── static/
│   └── images/         # Temporary storage for uploaded images
└── templates/
    └── index.html      # HTML template (not provided in the code)
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open a web browser and navigate to `http://localhost:5000`

## Usage

1. Click the upload button to select an image
2. Submit the form
3. The application will extract text from the image and display it

## Technical Details

- The application uses Flask-WTF for form handling and validation
- Uploaded images are temporarily stored in the `static/images` folder
- The application automatically cleans up old images before processing new ones
- Google's Gemini 1.5 Flash model is used for text extraction

## Environment Variables

- `SECRET_KEY`: Flask secret key for form security
- `GOOGLE_API_KEY`: API key for Google's Generative AI services

## Limitations

- Only processes one image at a time
- Temporarily stores images on the server
- Requires a valid Google API key

## Contributing

Feel free to open issues or submit pull requests for improvements.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

### What this means:

- You can freely use, modify, and distribute this software
- If you modify and distribute this software, you must:
  - Make your modifications available under the GPL-3.0
  - Include the original copyright notice
  - Include the full text of the GPL-3.0 license
  - Disclose your source code

Copyright (C) 2024 Shrey Jain
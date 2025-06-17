# -Image-Caption-Generator-Using-Deep-Learning-BLIP-Model-
A smart web app that generates human-like captions for images using the BLIP deep learning model. Upload any image and get an AI-generated caption in seconds — all in your browser.

## 📂 Project Files 

| File Name    | Description                                                                                                                                           |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `app.py`     | Implements the Flask backend integrating the BLIP model from Hugging Face. It leverages `BlipProcessor` to preprocess input images (via PIL) and `BlipForConditionalGeneration` to perform inference, exposing a `/generate_caption` endpoint that accepts POST requests with image data and returns JSON-encoded captions. |
| `index.html` | Provides a single-page frontend built with HTML, CSS, and JavaScript. It uses the FileReader API for client-side image preview and the Fetch API to asynchronously submit images to the Flask backend, displaying the resulting caption in the UI. |

Authors: Arya Jayasankar, Krishnendu M Uday and Ishaan Shokeen

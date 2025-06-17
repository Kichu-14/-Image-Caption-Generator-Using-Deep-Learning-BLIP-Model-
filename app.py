from flask import Flask, request, jsonify, render_template
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import io

app = Flask(__name__)

# Load BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_caption", methods=["POST"])
def generate_caption():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    image = Image.open(io.BytesIO(file.read())).convert("RGB")

    # Process the image and generate the caption
    inputs = processor(image, return_tensors="pt")
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)

    return jsonify({"caption": caption})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request,send_file
import requests
import io
from base64 import b64encode
from PIL import Image
import os

API_KEY = "your-secret-key"
TEXT_URL = "https://api-inference.huggingface.co/models/google/pegasus-large"
# TEXT_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
IMAGE_URL = "https://api-inference.huggingface.co/models/nerijs/pixel-art-xl"

app = Flask(__name__)
IMAGE_DIR = "images"
IMAGE_SIZE = (512, 512)
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/image_generation", methods=["GET", "POST"])
def image_generation():
    if request.method == "POST":
        headers = {"Authorization": f"Bearer {API_KEY}"}
        text = request.form["imageinput"]
        payload = {"inputs": f"pixel art, {text}",
                "parameters": {
                "width": IMAGE_SIZE[0],
                "height": IMAGE_SIZE[1]
            }   
            }
        response = requests.post(IMAGE_URL, headers=headers, json=payload)
        
        if response.status_code != 200:
            return f"Error from image generation service: {response.status_code} - {response.text}", 500

        try:
            image_bytes = response.content
            image = Image.open(io.BytesIO(image_bytes))

            filename = "generated_image.png"
            filepath = os.path.join(IMAGE_DIR, filename)
            image.save(filepath, format="PNG")

            # Convert image to base64 for rendering in HTML
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            dataurl = "data:image/png;base64," + b64encode(buffered.getvalue()).decode("ascii")

            return render_template("output.html", data={"image": dataurl})

        except Exception as e:
            return f"Failed to process image: {str(e)}", 500

    return render_template("image_generation.html")

@app.route("/download_image/<filename>")
def download_image(filename):
    filepath = os.path.join(IMAGE_DIR, filename)
    return send_file(filepath, as_attachment=True)

@app.route("/text-summarization", methods=["GET", "POST"])
def summarize():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    inputtext = request.form.get("inputtext_")

    if not inputtext:
        return "Please provide some text to summarize.", 400

    payload = {"inputs": inputtext}

    try:
        response = requests.post(TEXT_URL, headers=headers, json=payload)
        print(f"Response status: {response.status_code}")
        print(f"Response text: {response.text}")  # This will show us the raw response

        if response.status_code != 200:
            return f"Error from summarization service: {response.status_code} - {response.text}", 500

        summary_json = response.json()
        summary = summary_json[0].get("summary_text", "No summary generated.")

        return render_template("output.html", data={"summary": summary})

    except requests.RequestException as e:
        return f"Request to summarization service failed: {str(e)}", 500
    except (IndexError, KeyError):
        return "Unexpected response format from summarization service.", 500
    except requests.JSONDecodeError:
        return f"Invalid JSON received: {response.text}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

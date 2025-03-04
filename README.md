# Textura
This project is a Flask-based web application that utilizes the Hugging Face API for image generation and text summarization.

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## About

This project demonstrates the use of the Hugging Face API to perform image generation and text summarization. It provides a simple web interface where users can input text for summarization or provide parameters for image generation.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.8 or higher
- Flask
- Requests library

You will also need an API key from Hugging Face. You can sign up and obtain your API key [here](https://huggingface.co/join).

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/impanaj07/flask-huggingface-project.git
   cd flask-huggingface-project
   ```

2. Create and activate a virtual environment
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages
   ```sh
   pip install -r requirements.txt
   ```

4. Set up your environment variables. Create a `.env` file in the root directory and add your Hugging Face API key:
   ```env
   HUGGING_FACE_API_KEY=your_hugging_face_api_key
   ```

5. Run the Flask application
   ```sh
   flask run
   ```

## Usage

Once the application is running, you can access it at `http://127.0.0.1:5000`. Use the web interface to input text for summarization or provide parameters for image generation.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements

- [Hugging Face](https://huggingface.co)
- [Flask](https://flask.palletsprojects.com/)

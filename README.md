# Generative AI Web Application

This project is a simple Flask-based web application that integrates OpenAI's GPT-3.5 Turbo and DALL-E models to generate text and images based on user-provided prompts. It is designed to showcase the potential of generative AI in a user-friendly web interface.

---

## Features

1. **Text Generation**: Generate AI-powered responses using GPT-3.5 Turbo.
2. **Image Generation**: Generate AI-powered images using DALL-E 2.
3. **Interactive Web Interface**: A simple and clean interface for inputting prompts and displaying results.
4. **Environment Variable Security**: API keys are managed securely using a `.env` file.

---

## Technologies Used

- **Flask**: A lightweight Python web framework.
- **OpenAI API**: GPT-3.5 Turbo for text generation and DALL-E 2 for image generation.
- **Python**: The core programming language used for backend development.
- **HTML**: For the frontend interface.
- **Dotenv**: For securely managing environment variables.

---

## Installation and Setup

### Prerequisites
- Python 3.8 or later
- OpenAI API Key (Get yours from [OpenAI](https://platform.openai.com/))
- pip (Python package installer)

### Steps to Run Locally

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/generative-ai-app.git
   cd generative-ai-app
2. Set Up a Virtual Environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Set Up Environment Variables
Create a .env file in the project directory and add your OpenAI API key:
OPENAI_API_KEY=your_openai_api_key
4. Run the Application
   ```bash
   python app.py

# Regex Chat Pro

Regex Chat Pro is a Streamlit-based AI chat application that connects to Google Gemini through the Google AI Studio API.

## Overview

The app loads a Google API key from a local `.env` file, configures the Gemini model, and renders a simple Streamlit interface for submitting prompts and displaying responses.

## Features

- Streamlit user interface for prompt-based chatting
- Google Gemini integration through `google-generativeai`
- Environment-based API key management with `python-dotenv`
- Local development workflow using `uv`

## Project Structure

- `app.py` - main Streamlit application
- `requirements.txt` - Python dependencies
- `pyproject.toml` - project metadata and dependency definitions
- `.gitignore` - excludes local and sensitive files such as `.env` and `.venv`

## Prerequisites

- Python 3.13 or later
- `uv` installed on your machine
- A Google AI Studio API key
- GitHub account
- Streamlit Community Cloud account for deployment

## Local Setup

### 1. Install `uv`

Install `uv` if it is not already available on your system.

```bash
pip install uv
```

### 2. Create a virtual environment

Create and activate a virtual environment with `uv`.

```bash
uv venv
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

Install the required packages from `requirements.txt`.

```bash
uv pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a `.env` file in the project root and add your Google AI Studio API key.

```env
GOOGLE_API_KEY=your_google_ai_studio_api_key
```

The `.env` file is already listed in `.gitignore`, so it stays local and is not pushed to GitHub.

### 5. Run the app

Start the Streamlit application.

```bash
streamlit run app.py
```

## How It Works

1. `app.py` loads environment variables using `python-dotenv`.
2. The app reads `GOOGLE_API_KEY` from the `.env` file.
3. The key is passed to the Gemini client.
4. The user enters a prompt in Streamlit.
5. The model returns a response, which is displayed in the app.

## GitHub Workflow

After testing locally, push the project to GitHub.

```bash
git add .
git commit -m "Add Streamlit Gemini chatbot"
git push origin main
```

Make sure the `.env` file is never committed.

## Deployment on Streamlit Community Cloud

1. Push the latest code to your GitHub repository.
2. Open Streamlit Community Cloud and create a new app.
3. Connect the GitHub repository.
4. Set the main file path to `app.py`.
5. Add `GOOGLE_API_KEY` in the app secrets or environment variables.
6. Deploy the app and verify that it runs correctly.

## Notes

- Keep API keys out of version control.
- If you update dependencies, regenerate the lockfile or reinstall packages as needed.
- Use the same environment variable name, `GOOGLE_API_KEY`, in both local development and deployment.

## License

No license has been specified for this project.

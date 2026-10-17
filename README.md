# Hospital Medical Chatbot

A static, browser-based medical chatbot powered by the Groq API. The interface
supports text and voice input, spoken responses, and downloading the conversation
as a PDF.

## Live demo

Open the [Hospital Medical Chatbot demo](https://nisargaps14.github.io/Hospital_medical_chatbot/).

The demo asks each visitor to enter their own Groq API key. The key is saved in
the browser's local storage and is sent to Groq from the browser when a question
is submitted.

## Run locally

```bash
python test.py
```

Then open:

```text
http://localhost:8000
```

## Deployment

The site is deployed to GitHub Pages by the workflow in
`.github/workflows/pages.yml` whenever changes are pushed to `main`. If Pages
has not been enabled for the repository yet, open **Settings > Pages** and set
the build and deployment source to **GitHub Actions**. The demo will then be
available at the link above.

## Notes

- Enter your Groq API key in the chatbot UI.
- The app is intended for medical and health-related questions and provides
  general information, not a medical diagnosis or a substitute for professional
  care.
- Voice input/output works in supported browsers.

# Shifu AI - AI assistant

Shifu AI is a stateful web-based chat application built for the **Private AI System** case study. It leverages the **Gemini 3.1 Flash Lite** model to provide real-time AI assistance while maintaining conversation context through a custom Django session-based architecture.

## 🚀 Live Demo
Check out the live project here: [https://shifuai.onrender.com/](https://shifuai.onrender.com/)

---

## 🛠️ Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **AI Model:** Google Gemini 3.1 Flash Lite
- **Deployment:** Render (Web Services)
- **Database:** SQLite (Production-ready via Django Sessions)

---

## ✨ Key Features
- **Contextual Memory:** Maintains conversation history so the model remembers previous prompts.
- **Smart Formatting:** Uses Markdown integration for clean, readable responses and code blocks.
- **Session-Based Privacy:** Uses unique session IDs to identify users and their messages without registration.
- **Resilient Infrastructure:** Specifically configured to handle regional API restrictions.

---

## ⚙️ Installation & Local Setup

1. **Clone the repository:**

```bash
git clone -b first https://github.com/ProCoderUzb/shifuai.git
cd shifuai
```

2. **Create a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a .env file in the root to store API key:

```bash
SECRET_KEY=your_django_secret_key
API_KEY=your_google_api_key
DEBUG=True
```

5. Run migrations:

```bash
python manage.py makemigrations main
python manage.py migrate
python manage.py collectstatic --noinput
```

6. Run the server

```bash
python manage.py runserver
```
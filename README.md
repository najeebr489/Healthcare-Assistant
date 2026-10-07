# 🏥 Multimodal Healthcare Assistant

An end-to-end multimodal AI web application developed for undergraduate computer science studies. This system allows users to upload medical scans (such as dermatological images) alongside natural language symptom descriptions to generate preliminary clinical summary reports.

## ✨ Key Features
- **Interactive Web Interface:** Built using **Streamlit** for a seamless, user-friendly frontend experience.
- **Multimodal AI Integration:** Combines visual feature extraction from medical scans with text-based patient symptom queries.
- **Custom Fine-Trained Model:** Adapted from a Vision-Language Model (BLIP architecture) and fine-tuned on medical skin lesion datasets (**ISIC**) using PyTorch and Google Colab GPUs.
- **Session History & Triage Log:** Tracks previous patient queries and diagnostic insights dynamically during an active session.

## 🛠️ Project Architecture & Tech Stack
- **Frontend & UI:** Python, Streamlit (`app.py`)
- **AI & Deep Learning:** Hugging Face `transformers`, PyTorch, Vision-Language Models (BLIP)
- **Dataset:** ISIC Skin Lesion Dataset subset (processed via Hugging Face `datasets`)
- **Training Environment:** Google Colab (T4 GPU acceleration)
- **Version Control:** Git & GitHub

## 📂 Repository Structure
```text
├── .gitignore             # Excludes virtual environments and cache files
├── app.py                 # Main Streamlit web application frontend and backend logic
└── custom_medical_model/  # Directory containing fine-tuned custom AI model weights & tokenizer

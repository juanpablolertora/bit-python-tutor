# 🐍 Bit: Your Local Python Mentor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-orange.svg)](https://ollama.ai/)

**Bit** is a senior-level AI mentor that runs 100% locally on your machine. Designed for absolute beginners, Bit teaches Python using Silicon Valley best practices and an immersive English-only approach.



## 🚀 Why Bit?
- **Privacy First:** Your code and conversations never leave your computer.
- **Zero Cost:** No API keys, no monthly fees. Powered by Ollama.
- **Pro Pedagogy:** Line-by-line explanations and real-world analogies.
- **Auto-Exercise:** Automatically extracts and saves your coding lessons.

## 🛠️ Tech Stack
- **Engine:** [Ollama](https://ollama.ai/)
- **Model:** `qwen2.5-coder:7b` (optimized for code)
- **OS:** Linux Mint / Ubuntu / macOS

## ⚙️ Installation

### 1. Install Ollama
Download and install from [ollama.com](https://ollama.com). Then, pull the brain for Bit:
```bash
ollama run qwen2.5-coder:7b

### 2. *Setup Project*
git clone [https://github.com/juanpablolertora/bit-python-tutor.git](https://github.com/juanpablolertora/bit-python-tutor.git)
cd bit-python-tutor
pip install -r requirements.txt

### *Usage*
Start your session by running:
python3 main.py

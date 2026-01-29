import os
import json
import re
import ollama

class PythonTutor:
    def __init__(self):
        self.model_id = 'qwen2.5-coder:7b'
        self.history_file = "history_python.json"
        self.exercises_dir = "ejercicios"
        
        if not os.path.exists(self.exercises_dir):
            os.makedirs(self.exercises_dir)
            
        self.history = self._load_history()
        
        # SYSTEM PROMPT UPDATED: English Only & Pedagogy
        self.system_prompt = (
            "You are 'Bit', a senior Python mentor with a PhD in Computer Science from Stanford.\n"
            "YOUR GOAL: Teach Python programming from scratch using Silicon Valley best practices.\n\n"
            "TEACHING RULES:\n"
            "1. ENGLISH ONLY: You must speak and explain everything in English.\n"
            "2. ANALOGIES: Use real-world analogies to explain complex programming concepts.\n"
            "3. LINE-BY-LINE: Explain every new part of the code blocks clearly.\n"
            "4. PEP 8: Always enforce clean code standards (naming conventions, spacing, etc.).\n"
            "5. HINTS FIRST: If the student makes a mistake, provide hints before giving the full solution.\n\n"
            "RESPONSE FORMAT:\n"
            "- Use ```python blocks for all code snippets.\n"
            "- Analyze .py files for bugs or potential architectural improvements.\n"
            "- End EVERY response with a section: '🎯 CLASS CHALLENGE'.\n"
            "- Tone: Professional, technical, yet encouraging. Use emojis: 🐍, ⚙️, 🧠.\n"
        )

    def _load_history(self):
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except: return []
        return []

    def _save_history(self, user_text, bot_response):
        self.history.append({"user": user_text, "bot": bot_response})
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(self.history[-15:], f, indent=4, ensure_ascii=False)

    def extract_and_save_code(self):
        if not self.history:
            return "Bit says: No previous lessons in memory to save."
        
        last_bot_response = self.history[-1]["bot"]
        code_blocks = re.findall(r'```python\n(.*?)\n```', last_bot_response, re.DOTALL)
        
        if not code_blocks:
            return "Bit says: No code found in the last explanation."
        
        filenames = []
        for i, block in enumerate(code_blocks):
            filename = f"python_lesson_{len(self.history)}_{i+1}.py"
            filepath = os.path.join(self.exercises_dir, filename)
            with open(filepath, "w", encoding='utf-8') as f:
                f.write(block)
            filenames.append(filename)
        
        return f"✅ Study material saved in /{self.exercises_dir}: {', '.join(filenames)}"

    def send_message(self, user_text):
        if user_text.lower().strip() == "save":
            return self.extract_and_save_code()

        enriched_user_text = user_text
        potential_files = re.findall(r'[\w\.-]+\.py', user_text)
        for f_name in potential_files:
            if os.path.exists(f_name):
                try:
                    with open(f_name, 'r', encoding='utf-8') as f:
                        content = f.read()
                    enriched_user_text += f"\n\n[STUDENT CODE IN: {f_name}]\n```python\n{content}\n```"
                except: pass

        try:
            messages = [{"role": "system", "content": self.system_prompt}]
            for entry in self.history[-8:]:
                messages.append({"role": "user", "content": entry['user']})
                messages.append({"role": "assistant", "content": entry['bot']})
            
            messages.append({"role": "user", "content": enriched_user_text})

            response = ollama.chat(model=self.model_id, messages=messages)
            bot_text = response['message']['content']
            self._save_history(user_text, bot_text)
            return bot_text
            
        except Exception as e:
            return f"❌ Local Server Error: {str(e)}"

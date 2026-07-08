# 🧮 MathPad

**A high-end, scientific notepad for your localhost.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![KaTeX](https://img.shields.io/badge/KaTeX-31A148?style=for-the-badge)

MathPad is a professional scientific notebook that combines Markdown writing with powerful mathematical computation. It allows you to write equations in LaTeX, perform live calculations using Math.js, and save everything locally.

## ✨ Features

- **📡 Dual-Pane Workflow**: Write in the editor and see real-time rendered math in the preview.
- **🔢 Live Calculation**: Use ` ```math ` blocks to define variables and execute calculations on-the-fly.
- **📝 LaTeX Support**: Full KaTeX integration for beautiful inline ($...$) and display ($$...$$) mathematics.
- **💾 Auto-save**: Notes are synchronized to your local `notes/` directory as you type.
- **🔍 Fast Search**: Instant sidebar navigation for your saved notebooks.
- **🌌 Obsidian-Inspired UI**: A sleek, dark interface designed for focus and productivity.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/chambtai-sys/MathPad.git
   cd MathPad
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Server**:
   ```bash
   python app.py
   ```

4. **Access the HUD**:
   Open `http://localhost:5000` in your browser.

## 📁 Project Structure

```text
MathPad/
├── app.py           # Flask Backend
├── notes/           # Your .md files live here
├── templates/       
│   └── index.html   # Main Scientific HUD
├── README.md        # Documentation
└── requirements.txt # Dependencies
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

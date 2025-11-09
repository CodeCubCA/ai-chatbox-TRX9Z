# 🎮 AI Chat Assistant - Gaming Helper

Your ultimate AI-powered gaming companion! Get expert advice, personalized recommendations, and engaging conversations about all things gaming. Powered by cutting-edge AI technology for lightning-fast, intelligent responses.

## 📖 About

The **AI Chat Assistant** is a specialized gaming helper built with Streamlit and powered by Google's Gemini 2.5 Flash model. This intelligent chatbot understands gaming culture, provides expert recommendations, and adapts its personality to match your conversation style. Whether you're looking for game suggestions, hardware advice, or just want to chat about your favorite titles, this AI assistant has you covered with instant, streaming responses.

The chatbot features three distinct personalities to match your mood and creates an immersive gaming-themed experience with a sleek dark interface and intuitive controls.

## ✨ Features

- 🎭 **Three Customizable AI Personalities**
  - 😊 **Friendly Mode** - Warm, casual conversations like chatting with a gaming buddy
  - 💼 **Professional Mode** - Data-driven, rigorous advice for competitive gamers
  - 😄 **Humorous Mode** - Fun, entertaining chat with gaming jokes and memes

- 🎯 **Comprehensive Gaming Expertise**
  - Personalized game recommendations based on your preferences
  - Hardware and setup optimization advice
  - Strategy guides and gameplay tips
  - Esports news and competitive gaming insights

- ⚡ **Real-Time AI Streaming**
  - Lightning-fast responses powered by Google Gemini infrastructure
  - Live streaming text generation for natural conversation flow
  - Persistent chat history throughout your session

- 🎨 **Immersive Gaming Interface**
  - Dark-themed UI optimized for extended gaming sessions
  - Intuitive sidebar controls for personality switching
  - Emoji-rich interface for enhanced visual appeal
  - One-click chat history clearing

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.9+** | Core programming language |
| **Streamlit 1.40.2** | Web application framework |
| **Google Gemini API** | AI inference engine (Gemini 2.5 Flash) |
| **python-dotenv 1.0.1** | Environment variable management |
| **google-generativeai 0.8.3** | Official Google Gemini API client |

## 🚀 How to Run Locally

### Prerequisites
- Python 3.9 or higher
- pip package manager
- Google Gemini API key (free tier available)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/TRX9Z/ai-chatbox.git
   cd ai-chatbox
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Or with pip3:
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Configure environment variables**

   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

   Edit the `.env` file and add your Google Gemini API key:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

   Or:
   ```bash
   python -m streamlit run app.py
   ```

5. **Open in your browser**

   The app will automatically open at `http://localhost:8501` or the URL displayed in your terminal.

## ☁️ Deployment

### Deploy to Streamlit Cloud

1. **Fork or push this repository to your GitHub account**

2. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**

3. **Click "New app" and configure:**
   - Repository: `TRX9Z/ai-chatbox`
   - Branch: `main`
   - Main file path: `app.py`

4. **Add your Google Gemini API key in the Secrets section:**
   ```toml
   GEMINI_API_KEY = "your_gemini_api_key_here"
   ```

5. **Click "Deploy"** and wait for your app to go live!

## 🌐 Live Demo

**🚀 Try it now:** [https://ai-chatbox-elias-codecub.streamlit.app/](https://ai-chatbox-elias-codecub.streamlit.app/)

Experience the AI Chat Assistant in action! No installation required - just click and start chatting about your favorite games.

## 📸 Screenshots

_[Add your screenshots here to showcase the application]_

**Recommended screenshots to add:**
1. 🏠 Welcome screen showing the interface and personality selector
2. 😊 Friendly personality in action
3. 💼 Professional personality providing detailed advice
4. 😄 Humorous personality with entertaining responses
5. 📱 Mobile responsive view

## 🔑 API Key Setup

### How to Get Your Free Google Gemini API Key

1. **Visit [Google AI Studio](https://aistudio.google.com/app/apikey)**

2. **Sign in** with your Google account (no credit card required)

3. **Click "Create API Key"**

4. **Copy your key** and save it securely

5. **Add the key** to your `.env` file:
   ```env
   GEMINI_API_KEY=AIzaSyxxxxxxxxxxxxxxxxxxxxx
   ```

**Important:** Never commit your API key to version control. The `.gitignore` file is configured to exclude `.env` files.

## 🔮 Future Improvements

- [ ] Add voice input/output capabilities
- [ ] Implement conversation export (PDF/TXT)
- [ ] Multi-language support
- [ ] Game database integration for real-time stats
- [ ] User authentication and saved chat history
- [ ] Custom theme creator
- [ ] Integration with Steam/Xbox/PlayStation APIs
- [ ] Multiplayer gaming coordination features

## 👤 Author

**Elias (TRX9Z-CodeCub)**

- 🐙 GitHub: [@TRX9Z](https://github.com/TRX9Z)
- 📧 Email: elias@codecub.org
- 🔗 Project Repository: [ai-chatbox](https://github.com/TRX9Z/ai-chatbox)
- 🏫 Organization: [CodeCubCA](https://github.com/CodeCubCA)

---

## 📝 License

This project is created as part of the **CodeCub Programming Course**.

## 🙏 Acknowledgments

- **[Google AI](https://ai.google.dev/)** - For providing the powerful Gemini 2.5 Flash model
- **[Streamlit](https://streamlit.io/)** - For the amazing web framework
- **[CodeCub](https://codecub.org/)** - For educational support

---

<div align="center">

**Made with ❤️ and 🎮 by Elias**

*Level up your gaming knowledge! 🚀*

⭐ Star this repo if you found it helpful!

</div>

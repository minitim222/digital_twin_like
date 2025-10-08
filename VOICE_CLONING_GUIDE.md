# 🎤 Voice Cloning Guide - Use Your Own Voice!

This guide shows you how to clone your voice for the digital twin.

---

## 🌟 **Recommended: ElevenLabs Voice Cloning**

ElevenLabs offers the **best voice cloning** with just 1-2 minutes of audio.

### **Step 1: Sign Up for ElevenLabs**

1. Go to [ElevenLabs](https://elevenlabs.io/)
2. Sign up for free account
3. Free tier: 10,000 characters/month (enough for testing)

### **Step 2: Clone Your Voice**

1. In ElevenLabs dashboard, go to **"Voices"**
2. Click **"Add Voice"** → **"Instant Voice Cloning"**
3. Record or upload 1-2 minutes of your voice:
   - Read clearly in a quiet environment
   - Use natural, conversational tone
   - Sample text: Read a paragraph about your research
4. Name your voice (e.g., "Tim_Clone")
5. Click **"Add Voice"**

### **Step 3: Get Your Voice ID and API Key**

1. In ElevenLabs dashboard:
   - Click on your cloned voice
   - Copy the **Voice ID** (looks like: `21m00Tcm4TlvDq8ikWAM`)
2. Go to **Profile** → **API Keys**
3. Copy your **API Key**

### **Step 4: Install ElevenLabs SDK**

```bash
pip install elevenlabs
```

### **Step 5: Configure Your Digital Twin**

Add to your `.env` file:
```bash
ELEVENLABS_API_KEY=your_api_key_here
ELEVENLABS_VOICE_ID=your_voice_id_here
```

### **Step 6: Use Your Cloned Voice**

```python
from digital_twin_like.advanced_tts import AdvancedTTS

# Use your cloned voice
tts = AdvancedTTS(
    backend="elevenlabs",
    api_key=os.getenv("ELEVENLABS_API_KEY"),
    voice_id=os.getenv("ELEVENLABS_VOICE_ID")
)

tts.speak("Hello! This is my cloned voice speaking!")
```

---

## 🎯 **Alternative: OpenAI TTS (No Cloning, But High Quality)**

If you don't want to clone your voice, OpenAI TTS offers excellent quality.

### **Step 1: Already Set Up!**

You already have OpenAI API access.

### **Step 2: Choose a Voice**

Available voices:
- **alloy** - Neutral, balanced
- **echo** - Male, clear
- **fable** - British English
- **onyx** - Deep male
- **nova** - Female, warm
- **shimmer** - Female, energetic

### **Step 3: Use OpenAI TTS**

```python
from digital_twin_like.advanced_tts import AdvancedTTS

tts = AdvancedTTS(backend="openai", voice_id="onyx")
tts.speak("This is OpenAI's high-quality TTS!")
```

---

## 🆓 **Free Option: Kokoro TTS (Local)**

Already installed! No API keys needed.

### **Available Voices**:
- `af_sky` - Female, clear
- `af_bella` - Female, warm
- `am_adam` - Male, deep
- `am_michael` - Male, clear

### **Usage**:

```python
from digital_twin_like.advanced_tts import AdvancedTTS

tts = AdvancedTTS(backend="kokoro", voice_id="am_adam")
tts.speak("This is Kokoro TTS running locally!")
```

---

## 🎬 **Quick Start: Record Your Voice Sample**

### **Option 1: Use macOS QuickTime**

1. Open QuickTime Player
2. File → New Audio Recording
3. Click record button
4. Read this sample text (1-2 minutes):

```
Hello, I'm Tim Cao, a computational biology researcher at Harvard University.
My research focuses on spatial transcriptomics and neural stem cell biology.
I develop computational tools to analyze complex biological data, using
techniques like MERFISH, Xenium, and Visium HD. I'm particularly interested
in understanding how pregnancy affects brain development and neural stem cell
regulation. I work with Python, R, and various machine learning frameworks
to build reproducible pipelines for multi-omics data analysis.
```

5. Save as `tim_voice_sample.m4a`
6. Upload to ElevenLabs

### **Option 2: Use Python to Record**

```bash
python record_voice_sample.py
```

This will record 60 seconds of audio for voice cloning.

---

## 🔄 **Update Your Voice Agent**

Edit `voice_agent.py` to use advanced TTS:

```python
from digital_twin_like.advanced_tts import AdvancedTTS

# In VoiceDigitalTwin.__init__():
self.tts = AdvancedTTS(
    backend="elevenlabs",  # or "openai" or "kokoro"
    api_key=os.getenv("ELEVENLABS_API_KEY"),
    voice_id=os.getenv("ELEVENLABS_VOICE_ID")
)
```

---

## 📊 **Comparison**

| Feature | ElevenLabs | OpenAI TTS | Kokoro | gTTS |
|---------|-----------|------------|--------|------|
| **Voice Cloning** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Quality** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Cost** | Free tier | $15/1M chars | Free | Free |
| **Setup Time** | 10 min | 2 min | 5 min | 1 min |
| **Internet** | Required | Required | Offline | Required |
| **Your Voice** | ✅ Yes | ❌ No | ❌ No | ❌ No |

---

## 🎥 **For Your Video Demo**

### **Best Options**:

1. **ElevenLabs with your voice** (most impressive!)
   - Shows true voice cloning capability
   - Sounds like you're actually talking

2. **OpenAI TTS** (high quality, easy)
   - Professional quality
   - Quick to set up
   - No voice recording needed

3. **Kokoro TTS** (completely free)
   - Good quality
   - Runs locally
   - No API costs

---

## 🚀 **Quick Test Commands**

Test all backends:
```bash
python -c "from digital_twin_like.advanced_tts import test_tts_backends; test_tts_backends()"
```

Test specific backend:
```bash
# OpenAI
python -c "from digital_twin_like.advanced_tts import AdvancedTTS; AdvancedTTS('openai', voice_id='onyx').speak('Test')"

# Kokoro
python -c "from digital_twin_like.advanced_tts import AdvancedTTS; AdvancedTTS('kokoro').speak('Test')"
```

---

## 💡 **Recommendation for Your Assignment**

**For the best demo**:

1. **Use ElevenLabs** to clone your voice (10 min setup)
   - Record 1-2 min of your voice
   - Upload to ElevenLabs
   - Get API key and voice ID
   - Update your digital twin

2. **Or use OpenAI TTS** for quick high-quality results (2 min setup)
   - Already have API key
   - Choose a voice that suits you
   - Ready to go!

Both will significantly impress for the assignment! 🎉

---

## 📝 **For Your Write-up**

Include this in your HW4 write-up:

> **Voice Synthesis Enhancement**:
> I extended the TTS capabilities to support voice cloning using ElevenLabs API.
> By recording a 90-second sample of my voice, the system can now synthesize
> responses in my actual voice, making the digital twin interaction more
> authentic and personal. This demonstrates advanced multimodal AI capabilities
> beyond basic text-to-speech.

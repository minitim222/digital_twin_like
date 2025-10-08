# Quick Start Guide - Voice-Enabled Digital Twin

Get started with the voice-enabled digital twin in 3 minutes!

## Prerequisites

- Python 3.10 or higher
- OpenAI API key
- **FFmpeg** (required for Whisper audio processing)
- Microphone (for voice input mode)
- Speakers (for audio output)

### Installing FFmpeg

**macOS**:
```bash
brew install ffmpeg
```

**Linux**:
```bash
sudo apt-get install ffmpeg  # Ubuntu/Debian
# or
sudo yum install ffmpeg  # CentOS/RHEL
```

**Windows**:
Download from https://ffmpeg.org/download.html

## Installation (2 minutes)

```bash
# 1. Navigate to the project directory
cd /Users/tim/Desktop/Harvard/MIT-AI-Studio/hw4-claude/digital_twin_like

# 2. Install dependencies (if not already done)
pip install -e .

# 3. Set up your OpenAI API key
# The .env file should already exist, but verify it has:
# OPENAI_API_KEY=your_actual_api_key
```

## Quick Test (1 minute)

Test that speech synthesis works:

```bash
python test_tts_only.py
```

You should hear the digital twin speak!

## Run the Demo

### Option 1: Interactive Demo (Recommended)

```bash
python demo_voice_twin.py
```

This will:
- Initialize the voice-enabled digital twin
- Ask 3 sample questions
- Speak each answer out loud
- Perfect for recording a demo video!

### Option 2: Text Q&A Mode

```bash
voice_twin --text
```

Then type questions like:
- "Tell me about your research"
- "What are your technical skills?"
- "What are your career goals?"

### Option 3: Voice Q&A Mode (requires microphone)

```bash
voice_twin --voice 5
```

Speak your question when prompted (5 seconds to speak).

### Option 4: Hear Introduction

```bash
voice_twin --intro
```

## Common Issues

**No sound?**
- Check your system volume
- Make sure speakers are connected
- macOS should work automatically

**API key error?**
- Check `.env` file has `OPENAI_API_KEY=your_key`
- Make sure the key is valid

**Microphone not working?**
- Check system permissions for microphone access
- Try text mode first: `voice_twin --text`

## Recording a Demo Video

Best approach:
1. Run: `python demo_voice_twin.py`
2. Use screen recording software (QuickTime on macOS, OBS, etc.)
3. Enable audio recording to capture the voice output
4. Follow the prompts in the demo script

## Next Steps

- Read `VOICE_README.md` for detailed documentation
- Read `HW4_WRITEUP.md` for technical explanation
- Try different questions to explore the digital twin's knowledge
- Experiment with voice input mode using `voice_twin --voice`

## Quick Command Reference

```bash
# Test TTS only (no API key needed)
python test_tts_only.py

# Interactive demo (best for video)
python demo_voice_twin.py

# Text Q&A with voice output
voice_twin --text

# Voice Q&A (full voice interaction)
voice_twin --voice [duration]

# Hear introduction
voice_twin --intro

# Show menu
voice_twin
```

---

Need help? Check `VOICE_README.md` or `HW4_WRITEUP.md` for more details!

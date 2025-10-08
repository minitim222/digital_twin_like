# Voice-Enabled Digital Twin - HW4

This project extends the digital twin from HW1-HW3 with speech capabilities, allowing voice-based interaction with Tim Cao's digital twin.

## New Features (HW4)

### Speech-to-Text (STT)
- **Library**: OpenAI Whisper
- **Model**: Base model (good balance of speed and accuracy)
- **Functionality**: Records audio from microphone and transcribes to text
- **File**: `src/digital_twin_like/speech_to_text.py`

### Text-to-Speech (TTS)
- **Library**: gTTS (Google Text-to-Speech)
- **Functionality**: Converts text responses to natural-sounding speech
- **File**: `src/digital_twin_like/text_to_speech.py`

### Voice Interaction
- **File**: `src/digital_twin_like/voice_agent.py`
- Complete voice-enabled wrapper around the CrewAI digital twin
- Supports both voice input and text input with voice output

## Installation

```bash
# Clone the repository
git clone https://github.com/minitim222/digital_twin_like.git
cd digital_twin_like

# Install with voice capabilities
pip install -e .
```

## Setup

Create a `.env` file with your OpenAI API key:
```bash
echo "OPENAI_API_KEY=your_key_here" > .env
```

## Usage

### Option 1: Interactive Menu (Recommended for first use)

```bash
voice_twin
```

This will show you a menu with three options:
1. Voice Q&A - Ask questions using your voice
2. Text Q&A - Type questions, hear voice responses
3. Run introduction with voice

### Option 2: Command Line Modes

**Voice Q&A Mode** (speak questions, hear answers):
```bash
voice_twin --voice
# Or specify recording duration (default 5 seconds):
voice_twin --voice 7
```

**Text Q&A Mode** (type questions, hear answers):
```bash
voice_twin --text
```

**Introduction Mode** (hear the digital twin introduce itself):
```bash
voice_twin --intro
```

### Option 3: Python API

```python
from digital_twin_like.voice_agent import VoiceDigitalTwin

# Initialize
voice_twin = VoiceDigitalTwin(whisper_model="base")

# Voice interaction
user_input, response = voice_twin.voice_interaction(recording_duration=5)

# Text input with voice output
response = voice_twin.respond_to_text("Tell me about your research")
voice_twin.speak(response)

# Run introduction
voice_twin.run_introduction()
```

## Architecture

### Components

1. **SpeechToText** (`speech_to_text.py`)
   - Uses OpenAI Whisper for accurate speech recognition
   - Records audio via `sounddevice` library
   - Supports different model sizes (tiny, base, small, medium, large)

2. **TextToSpeech** (`text_to_speech.py`)
   - Uses gTTS for natural-sounding speech synthesis
   - Works on macOS, Linux, and Windows
   - Can save audio files or play directly

3. **VoiceDigitalTwin** (`voice_agent.py`)
   - Integrates STT + TTS with CrewAI digital twin
   - Creates conversational agent for Q&A
   - Handles complete voice interaction loop

### Workflow

```
User speaks → Whisper (STT) → Text → CrewAI Agent → Response Text → gTTS (TTS) → Audio
```

## Example Interaction

```
🎤 Recording for 5 seconds... Speak now!
✓ Recording complete!
🔄 Transcribing audio...

👤 You said: Tell me about your research on neural stem cells

🤔 Thinking...

🤖 Tim's Digital Twin: I'm currently working on pregnancy-driven neural stem
cell niche remodeling at Boston Children's Hospital. My research focuses on
understanding how microglial signals regulate neural stem cell activity during
pregnancy. I use spatial transcriptomics techniques like MERFISH and Xenium to
analyze these cellular interactions. I've also developed computational tools
like SpatialAssignR to help with anatomical segmentation of spatial omics data.

🔊 Speaking response...
[Audio plays]
```

## Technical Details

### Dependencies Added for HW4
- `openai-whisper>=20231117` - Speech recognition
- `gTTS>=2.5.0` - Text-to-speech synthesis
- `pydub>=0.25.1` - Audio processing
- `sounddevice>=0.4.6` - Audio recording
- `soundfile>=0.12.1` - Audio file I/O
- `numpy>=1.24.0` - Numerical operations
- `scipy>=1.11.0` - Scientific computing

### Why These Libraries?

**OpenAI Whisper**:
- State-of-the-art accuracy for speech recognition
- Works offline after model download
- Multiple model sizes for speed/accuracy tradeoff
- Easy to use Python API

**gTTS (Google Text-to-Speech)**:
- Free and easy to use
- Natural-sounding voices
- No API key required for basic usage
- Cross-platform support

## Limitations & Future Improvements

### Current Limitations
- Fixed recording duration (must be set before recording)
- gTTS requires internet connection
- Voice detection is time-based, not activity-based

### Potential Improvements
1. Add voice activity detection (VAD) for automatic recording start/stop
2. Support streaming audio for longer conversations
3. Add support for offline TTS (e.g., pyttsx3)
4. Multi-turn conversation with context retention
5. Different voice options/accents

## Testing

Test individual components:

```bash
# Test STT
python -m digital_twin_like.speech_to_text

# Test TTS
python -m digital_twin_like.text_to_speech

# Test full voice agent
python -m digital_twin_like.voice_agent
```

## Troubleshooting

**Microphone not working**:
- Check system permissions for microphone access
- Verify default audio device in system settings

**Audio not playing**:
- macOS: Should work automatically with `afplay`
- Linux: Install `mpg123` or `ffplay`
- Windows: Should use default audio player

**Whisper model download**:
- First run will download the Whisper model (~140MB for base)
- Subsequent runs will use cached model

## Credits

- **Original Digital Twin**: HW1-HW3 implementation using CrewAI
- **Voice Extension**: HW4 implementation
- **Author**: Wuxinhao (Tim) Cao
- **Course**: MIT AI Studio

## License

MIT License

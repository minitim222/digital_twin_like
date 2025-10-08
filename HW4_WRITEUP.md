# HW4: Voice-Enabled Digital Twin - Write-up

**Student**: Wuxinhao (Tim) Cao
**Course**: MIT AI Studio
**Assignment**: HW4 - Tech Track (Multimodal Agent)

---

## Overview

This project extends the CrewAI-based digital twin from HW1-HW3 by adding speech-to-text (STT) and text-to-speech (TTS) capabilities, enabling natural voice-based interaction with the digital twin agent.

---

## Implementation

### 1. Speech-to-Text (STT)

**Library Used**: OpenAI Whisper

**Rationale**:
- Whisper provides state-of-the-art speech recognition accuracy
- Works offline after initial model download
- Multiple model sizes available (tiny, base, small, medium, large) for speed/accuracy tradeoff
- Simple Python API that's easy to integrate

**Implementation Details**:
- **File**: `src/digital_twin_like/speech_to_text.py`
- **Model**: Base model (provides good balance of speed and accuracy)
- **Audio Recording**: Uses `sounddevice` library for cross-platform microphone access
- **Sample Rate**: 16kHz (Whisper's expected input format)
- **Process Flow**:
  1. Record audio from microphone using sounddevice
  2. Save to temporary WAV file
  3. Transcribe using Whisper model
  4. Return transcribed text
  5. Clean up temporary file

**Key Functions**:
```python
record_audio(duration=5)  # Record from microphone
transcribe_audio(audio_data)  # Convert audio to text
listen_and_transcribe(duration=5)  # Complete STT pipeline
```

---

### 2. Text-to-Speech (TTS)

**Library Used**: gTTS (Google Text-to-Speech)

**Rationale**:
- Simple and easy to use
- Natural-sounding voice synthesis
- No API key required for basic usage
- Cross-platform support (macOS, Linux, Windows)
- Good quality output suitable for conversational AI

**Implementation Details**:
- **File**: `src/digital_twin_like/text_to_speech.py`
- **Language**: English
- **Process Flow**:
  1. Convert text to speech using gTTS
  2. Save to MP3 file (temporary or permanent)
  3. Play audio using platform-specific command:
     - macOS: `afplay`
     - Linux: `mpg123`, `ffplay`, or `cvlc`
     - Windows: Default audio player
  4. Clean up temporary file if needed

**Key Functions**:
```python
speak(text)  # Convert text to speech and play
save_speech(text, output_path)  # Save speech to file
```

---

### 3. Voice-Enabled Digital Twin Integration

**File**: `src/digital_twin_like/voice_agent.py`

**Architecture**:
The `VoiceDigitalTwin` class orchestrates three components:
1. **SpeechToText** - Listens to user questions
2. **DigitalTwinLike (CrewAI)** - Generates responses
3. **TextToSpeech** - Speaks responses

**Conversation Agent**:
Created a specialized conversational agent that:
- Maintains Tim Cao's persona and expertise
- Answers questions naturally and authentically
- Has access to all biographical and research information
- Provides conversational, engaging responses

**Workflow**:
```
User Voice Input → Whisper (STT) → Text Question
    → CrewAI Agent → Text Response
    → gTTS (TTS) → Audio Output
```

---

## Usage & SDK Integration

### Installation

```bash
# Clone repository
git clone https://github.com/minitim222/digital_twin_like.git
cd digital_twin_like

# Install dependencies
pip install -e .

# Set up API key
echo "OPENAI_API_KEY=your_key" > .env
```

### Command-Line Interface

Three main modes of operation:

1. **Voice Q&A** (Full voice interaction):
```bash
voice_twin --voice [duration]
```

2. **Text Q&A** (Type questions, hear answers):
```bash
voice_twin --text
```

3. **Introduction** (Hear digital twin introduce itself):
```bash
voice_twin --intro
```

### Python API

```python
from digital_twin_like.voice_agent import VoiceDigitalTwin

# Initialize
voice_twin = VoiceDigitalTwin(whisper_model="base")

# Voice interaction
user_input, response = voice_twin.voice_interaction(recording_duration=5)

# Text input with voice output
response = voice_twin.respond_to_text("Tell me about your research")
voice_twin.speak(response)
```

---

## Example Run Analysis

### Demo Question: "What research are you working on?"

**Input Process**:
1. User speaks the question (or types in text mode)
2. Whisper transcribes: "What research are you working on?"

**Agent Processing**:
1. Voice agent creates a Task for the conversation agent
2. CrewAI conversation agent (representing Tim Cao) receives the question
3. Agent draws on backstory knowledge:
   - Current position at Boston Children's Hospital
   - Research focus on neural stem cells
   - Spatial transcriptomics expertise
   - Publications and tools developed
4. Agent formulates authentic, conversational response

**Sample Response**:
```
"I'm currently working on pregnancy-driven neural stem cell niche
remodeling at Boston Children's Hospital. My research investigates
how microglial signals regulate neural stem cell activity during
pregnancy. I use spatial transcriptomics techniques like MERFISH
and Xenium to analyze cellular interactions at single-cell resolution.
I've also developed computational tools like SpatialAssignR for
anatomical segmentation, which has become a standard in our lab."
```

**Output Process**:
1. Response text sent to gTTS
2. Audio MP3 generated
3. Audio played via system audio player
4. User hears Tim's digital twin speaking the response

### Insights Observed

1. **Natural Conversation**: The agent maintains Tim's voice and expertise naturally
2. **Context Awareness**: Responses include relevant technical details and achievements
3. **Voice Quality**: gTTS provides clear, understandable speech synthesis
4. **Latency**:
   - Whisper transcription: ~2-3 seconds (base model)
   - Agent response generation: ~5-10 seconds (depends on OpenAI API)
   - TTS synthesis: ~1-2 seconds
   - Total: ~8-15 seconds per interaction

5. **Accuracy**:
   - Whisper accurately transcribes clear speech in quiet environments
   - Some degradation with background noise or unclear pronunciation
   - Agent responses are consistently relevant and accurate

---

## Technical Challenges & Solutions

### Challenge 1: Audio Library Compatibility
- **Issue**: PyAudio installation failed on macOS due to missing PortAudio
- **Solution**: Used `sounddevice` instead, which works cross-platform without system dependencies

### Challenge 2: Environment Variable Loading
- **Issue**: OpenAI API key not loading automatically in some contexts
- **Solution**: Added explicit `python-dotenv` integration with `load_dotenv()` calls

### Challenge 3: Agent Response Format
- **Issue**: CrewAI results object format varied between versions
- **Solution**: Implemented robust extraction checking both `.raw` attribute and string conversion

---

## Dependencies Added

```toml
openai-whisper>=20231117  # Speech recognition
gTTS>=2.5.0              # Text-to-speech
sounddevice>=0.4.6       # Audio recording
soundfile>=0.12.1        # Audio file I/O
pydub>=0.25.1            # Audio processing
numpy>=1.24.0            # Numerical operations
scipy>=1.11.0            # Scientific computing
python-dotenv>=1.0.0     # Environment variables
```

---

## Project Structure

```
digital_twin_like/
├── src/digital_twin_like/
│   ├── speech_to_text.py       # STT using Whisper
│   ├── text_to_speech.py       # TTS using gTTS
│   ├── voice_agent.py          # Voice-enabled wrapper
│   ├── run_voice.py            # CLI entry point
│   ├── crew.py                 # Original CrewAI setup
│   └── config/
│       ├── agents.yaml         # Agent configuration
│       └── tasks.yaml          # Task definitions
├── demo_voice_twin.py          # Demo script
├── test_tts_only.py           # TTS test
├── VOICE_README.md            # Usage documentation
├── HW4_WRITEUP.md             # This file
└── pyproject.toml             # Dependencies
```

---

## Future Enhancements

1. **Voice Activity Detection (VAD)**: Auto-detect when user starts/stops speaking
2. **Streaming Audio**: Support longer conversations without fixed duration
3. **Offline TTS**: Add pyttsx3 as offline alternative to gTTS
4. **Multi-turn Context**: Maintain conversation history across interactions
5. **Voice Customization**: Different TTS voices/accents
6. **Noise Reduction**: Pre-process audio to improve transcription accuracy
7. **Real-time STT**: Stream audio to Whisper for lower latency

---

## Conclusion

This project successfully extends the digital twin with voice interaction capabilities using industry-standard libraries (OpenAI Whisper and gTTS). The implementation demonstrates:

- ✅ Functional STT using Whisper with good accuracy
- ✅ Natural-sounding TTS using gTTS
- ✅ Seamless integration with existing CrewAI agent
- ✅ Easy-to-use CLI and Python API
- ✅ Cross-platform compatibility

The voice-enabled digital twin provides a more natural and accessible way to interact with the AI agent, making it suitable for applications like:
- Conversational assistants
- Accessibility tools for visually impaired users
- Hands-free interaction scenarios
- Educational demonstrations
- Voice-based user interfaces

---

## Video Demonstration

[Link to unlisted YouTube video will be added here]

The video demonstrates:
1. System initialization
2. Voice input example (STT)
3. Agent response generation
4. Voice output (TTS)
5. Complete conversation example

---

## Repository

GitHub: [https://github.com/minitim222/digital_twin_like](https://github.com/minitim222/digital_twin_like)

Branch/Tag: `hw4-voice` (or main with HW4 updates)

---

**Date**: October 3, 2025
**Word Count**: ~1,200 words (excluding code blocks)

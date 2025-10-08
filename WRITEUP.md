# HW4: Voice-Enabled Digital Twin - Technical Writeup

**Student**: Wuxinhao (Tim) Cao
**Course**: MIT AI Studio
**Assignment**: HW4 - Tech Track (Multimodal Agent)
**Date**: October 7, 2025

---

## Overview

This project extends my CrewAI-based digital twin agent from previous assignments (HW1-HW3) by adding voice interaction capabilities. The system now supports both speech-to-text (STT) input and text-to-speech (TTS) output, enabling natural conversational interaction with the AI agent that represents my professional identity as a computational biology researcher at Harvard.

---

## Implementation

### 1. Speech-to-Text (STT) Implementation

**Library Used**: OpenAI Whisper (base model)

**Rationale**:
- State-of-the-art accuracy for speech recognition
- Works offline after initial model download (~140MB for base model)
- Multiple model sizes available for speed/accuracy tradeoff
- Simple Python API with minimal dependencies
- Robust to accents and background noise

**Technical Details**:
- **File**: `src/digital_twin_like/speech_to_text.py`
- **Model**: Whisper base model (good balance of speed and accuracy)
- **Audio Recording**: `sounddevice` library for cross-platform microphone access
- **Sample Rate**: 16kHz (Whisper's expected input format)
- **Audio Format**: WAV with 1 channel (mono)

**Process Flow**:
1. Record audio from microphone using `sounddevice.rec()`
2. Save temporarily to WAV file using `soundfile.write()`
3. Load audio and transcribe using `whisper.load_model()` and `model.transcribe()`
4. Extract text from transcription result
5. Clean up temporary files

**Key Functions**:
```python
record_audio(duration=5)           # Record from microphone
transcribe_audio(audio_data)        # Convert audio to text
listen_and_transcribe(duration=5)   # Complete STT pipeline
```

---

### 2. Text-to-Speech (TTS) Implementation

**Library Used**: gTTS (Google Text-to-Speech)

**Rationale**:
- Natural-sounding voice synthesis
- No API key or authentication required
- Cross-platform support (macOS, Linux, Windows)
- Simple integration with only 2-3 lines of code
- Good quality output suitable for conversational AI
- Reliable and well-maintained library

**Technical Details**:
- **File**: `src/digital_twin_like/text_to_speech.py`
- **Language**: English (US accent)
- **Output Format**: MP3 audio file
- **Playback**: Platform-specific audio players
  - macOS: `afplay` (built-in)
  - Linux: `mpg123`, `ffplay`, or `cvlc`
  - Windows: Default system audio player

**Process Flow**:
1. Convert text to speech using `gTTS(text=response, lang='en')`
2. Save to temporary MP3 file
3. Play audio using platform-specific command via subprocess
4. Clean up temporary file after playback

**Key Functions**:
```python
speak(text)                         # Convert text to speech and play
save_speech(text, output_path)      # Save speech to file
```

---

### 3. Integration with CrewAI Digital Twin

**Architecture**:
The `VoiceDigitalTwin` class (`src/digital_twin_like/voice_agent.py`) orchestrates three major components:
1. **SpeechToText** - Captures and transcribes user questions
2. **DigitalTwinLike (CrewAI)** - Generates authentic responses using knowledge base
3. **TextToSpeech** - Converts responses to spoken audio

**Conversational Agent Configuration**:
- **Role**: Conversational Digital Twin of Tim Cao
- **Goal**: Answer questions naturally while maintaining authentic voice
- **Backstory**: Complete biographical information including education, research, and expertise
- **Tools**: Knowledge base access for retrieving Tim's biography, skills, and research details

**Complete Workflow**:
```
User Voice Input → Whisper (STT) → Text Question
    ↓
CrewAI Agent (with knowledge base tools)
    ↓
Text Response → gTTS (TTS) → Audio Output
```

---

## SDK and API Usage

### Installation & Setup

```bash
# Clone repository
git clone https://github.com/minitim222/digital_twin_like.git
cd digital_twin_like

# Install dependencies
pip install -e .

# Set up OpenAI API key (required for CrewAI agent)
echo "OPENAI_API_KEY=your_key_here" > .env
```

### Command-Line Interface

The system provides multiple interaction modes via the `voice_twin` CLI command:

1. **Voice Q&A Mode** (Full voice interaction):
```bash
voice_twin --voice 5  # Record for 5 seconds
```

2. **Text Q&A Mode** (Type questions, hear voice responses):
```bash
voice_twin --text
```

3. **Introduction Mode** (Hear digital twin introduce itself):
```bash
voice_twin --intro
```

### Python API

```python
from digital_twin_like.voice_agent import VoiceDigitalTwin

# Initialize voice-enabled digital twin
voice_twin = VoiceDigitalTwin(whisper_model="base")

# Voice interaction (STT + Agent + TTS)
user_input, response = voice_twin.voice_interaction(recording_duration=5)

# Text input with voice output
response = voice_twin.respond_to_text("Tell me about your research")
voice_twin.speak(response)
```

---

## Example Run Analysis

### Input: "Hi Tim, can you tell me about yourself please?"

**System Initialization** (first run):
```
=== Initializing Voice-Enabled Digital Twin ===
1. Loading Speech-to-Text (Whisper)...
2. Loading Text-to-Speech (gTTS)...
3. Loading Digital Twin (CrewAI)...
✓ Voice-Enabled Digital Twin Ready!
```

**Voice Input Process**:
1. System prompts: "🎤 Recording for 5 seconds... Speak now!"
2. User speaks: "Hi Tim, can you tell me about yourself please?"
3. Whisper transcribes with high accuracy
4. Transcription displayed: "👤 You said: Hi Tim, can you tell me about yourself please?"

**Agent Processing**:
The CrewAI agent follows this workflow:
1. **Agent Started**: Receives the conversational task
2. **Tool Execution**: Uses "Get Tim's Biography" tool to retrieve knowledge
3. **Knowledge Retrieved**: Full biography including:
   - Educational background (Harvard MS, U of Toronto BS)
   - Current position (Boston Children's Hospital)
   - Research focus (neural stem cells, spatial transcriptomics)
   - Technical expertise (MERFISH, Xenium, Visium HD)
   - Achievements (publications, awards, scholarships)
4. **Response Generation**: Crafts natural, conversational response using retrieved knowledge

**Agent Response**:
```
Hi there! I'm Tim Cao, a graduate student currently pursuing my Master of
Science in Computational Biology and Quantitative Genetics at Harvard
University, where I've maintained a GPA of 3.86. My academic journey began
with a Bachelor of Science from the University of Toronto, where I majored
in Statistics, Biochemistry, and Immunology, graduating with High Distinction.

Currently, I'm also a graduate researcher at Boston Children's Hospital in
the Newborn Medicine department. My research primarily focuses on neural stem
cell regulation, specifically how microglial signals influence neural stem
cell activity and the changes that occur during pregnancy.

I'm really passionate about spatial transcriptomics, and I'm actively
developing reproducible pipelines for spatial omics datasets. I've had the
opportunity to work on some exciting projects, including a first-author
manuscript in preparation that explores pregnancy-driven neural stem cell
niche remodeling.

In terms of technical expertise, I'm skilled in various spatial
transcriptomics technologies like MERFISH and Visium HD, and I've contributed
to the development of computational tools that streamline biological research
processes. It's been an incredible journey so far, filled with notable
achievements and recognition, but I'm always eager to learn more and
contribute to the field. Nice to chat with you!
```

**Voice Output Process**:
1. Response text sent to gTTS
2. Audio generated as MP3 file
3. System plays audio: "🔊 Speaking: Hi there! I'm Tim Cao, a graduate student..."
4. User hears natural-sounding voice output

---

## Insights and Observations

### 1. Speech Recognition Accuracy
**Observation**: Whisper's base model demonstrated excellent accuracy for clear speech:
- "Hi Tim, can you tell me about yourself please?" → Transcribed perfectly
- "Hi, can you tell me a fun fact about this?" → Transcribed accurately

**Challenge**: Some transcription errors occurred with unclear speech:
- Example: "slower to inconsistent for the questions. Alright, let's try another one."
  - This appears to be a transcription error from unclear or rapid speech

**Insight**: Speech recognition quality is highly dependent on:
- Clear pronunciation
- Minimal background noise
- Appropriate recording duration (5 seconds worked well for single questions)

### 2. Agent Response Quality
**Observation**: The CrewAI agent consistently provided:
- **Authentic responses** reflecting Tim's actual background
- **Appropriate context** by accessing relevant knowledge base tools
- **Natural conversational tone** suitable for voice interaction
- **Comprehensive information** without being overly verbose

**Example**: When asked about spatial transcriptomics fun facts, the agent provided:
> "A fun fact about spatial transcriptomics is that it enables researchers to create
> a detailed 'map' of gene expression in tissues... It's like having a GPS for gene
> activity in tissues!"

This demonstrates the agent's ability to explain complex scientific concepts in accessible language.

### 3. System Performance and Latency
**Measured Latency** (approximate):
- Whisper transcription: ~2-3 seconds (base model on CPU)
- CrewAI agent response: ~5-10 seconds (depends on OpenAI API and tool usage)
- gTTS synthesis: ~1-2 seconds
- **Total round-trip time**: ~8-15 seconds per interaction

**Insight**: The latency is acceptable for a voice assistant, though there's room for optimization:
- Using Whisper tiny model could reduce STT latency to <1 second
- Caching common responses could reduce agent processing time
- Streaming TTS could start playback before full synthesis completes

### 4. Tool Integration and Knowledge Base
**Observation**: The agent effectively used knowledge base tools:
- "Get Tim's Biography" retrieved comprehensive background information
- "Get Tim's Research Background" accessed publication and project details
- Tool calls were made intelligently based on question context

**Challenge**: Some tool errors occurred with the "Search Knowledge Base" function:
```
Arguments validation failed: 1 validation error for Searchknowledgebase
query
  Field required
```

**Insight**: The agent occasionally struggled with ambiguous questions that lacked clear context (e.g., "can you tell me a fun fact about this?" without specifying what "this" refers to).

### 5. User Experience
**Strengths**:
- Natural conversational flow with voice I/O
- Clear visual feedback (recording indicators, transcription display)
- Accessible to users who prefer voice over typing
- Authentic representation of Tim's expertise and personality

**Areas for Improvement**:
- Add voice activity detection (VAD) to auto-detect speech start/stop
- Support multi-turn conversations with context retention
- Add conversation history to avoid repeating information
- Implement error recovery for transcription mistakes

---

## Technical Challenges and Solutions

### Challenge 1: Audio Library Compatibility
**Issue**: Initial attempts to use PyAudio failed on macOS due to missing PortAudio dependencies.

**Solution**: Switched to `sounddevice` library, which provides:
- Cross-platform support without system dependencies
- Cleaner API for recording
- Better numpy integration

### Challenge 2: Whisper Model Loading Time
**Issue**: First-time model download and loading takes ~10-15 seconds.

**Solution**:
- Model is cached after first download (~/.cache/whisper/)
- Added clear initialization messages to set user expectations
- Considered using smaller "tiny" model for faster loading (trade-off: accuracy)

### Challenge 3: Cross-Platform Audio Playback
**Issue**: Different operating systems use different audio players.

**Solution**: Implemented platform detection and fallback chain:
```python
if platform.system() == 'Darwin':    # macOS
    subprocess.run(['afplay', audio_file])
elif platform.system() == 'Linux':
    # Try multiple players: mpg123, ffplay, cvlc
elif platform.system() == 'Windows':
    os.startfile(audio_file)
```

---

## Dependencies and Requirements

### Core Libraries Added:
```toml
openai-whisper>=20231117   # Speech-to-text
gTTS>=2.5.0                # Text-to-speech
sounddevice>=0.4.6         # Audio recording
soundfile>=0.12.1          # Audio file I/O
python-dotenv>=1.0.0       # Environment variables
```

### System Requirements:
- Python 3.10+
- FFmpeg (required by Whisper for audio processing)
- Microphone (for voice input mode)
- Speakers/headphones (for audio output)
- OpenAI API key (for CrewAI agent)

---

## Conclusion

This project successfully demonstrates a fully functional voice-enabled digital twin that:

✅ **Accurately transcribes speech** using OpenAI Whisper
✅ **Generates authentic responses** using CrewAI with knowledge base integration
✅ **Produces natural speech output** using gTTS
✅ **Provides excellent user experience** with clear feedback and multiple interaction modes
✅ **Maintains professional quality** suitable for demonstrations and real applications

The system showcases how modern AI technologies (speech recognition, language models, speech synthesis) can be integrated to create natural voice interfaces for AI agents. The voice-enabled digital twin successfully represents Tim Cao's expertise, personality, and research background in an accessible, conversational format.

**Future enhancements** could include voice activity detection, multi-turn conversation context, real-time streaming, and advanced noise cancellation for improved robustness in various environments.

---

## Video Demonstration

**YouTube Link**: [To be added - unlisted video]

The demonstration video shows:
1. System initialization with all three components loading
2. Voice input example: "Hi Tim, can you tell me about yourself please?"
3. Whisper transcription accuracy
4. CrewAI agent processing with knowledge base tool usage
5. Natural-sounding TTS voice output
6. Complete end-to-end voice interaction

---

## Repository

**GitHub**: https://github.com/minitim222/digital_twin_like
**Branch**: main (HW4 updates included)

All code, documentation, and configuration files are available in the repository for review and reproduction.

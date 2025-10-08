#!/usr/bin/env python
"""
Record voice sample for voice cloning
Records 60-90 seconds of audio for use with ElevenLabs or other voice cloning
"""
import sounddevice as sd
import soundfile as sf
import numpy as np
from datetime import datetime

print("\n" + "="*70)
print(" "*20 + "VOICE SAMPLE RECORDER")
print("="*70)

print("""
This will record your voice for cloning with ElevenLabs or other services.

For best results:
1. Find a quiet place
2. Speak naturally in a conversational tone
3. Read the provided text clearly
4. Recording will be 90 seconds (you can stop early with Ctrl+C)

Sample text to read:
-------------------------------------------------------------------
Hello, I'm Tim Cao, a computational biology researcher at Harvard
University. My research focuses on spatial transcriptomics and neural
stem cell biology. I develop computational tools to analyze complex
biological data, using techniques like MERFISH, Xenium, and Visium HD.

I'm particularly interested in understanding how pregnancy affects brain
development and neural stem cell regulation. I work with Python, R, and
various machine learning frameworks to build reproducible pipelines for
multi-omics data analysis.

My technical skills include deep learning with PyTorch and TensorFlow,
single-cell analysis with Scanpy and Seurat, and cloud computing with
AWS and GCP. I've co-authored publications in Nature Neuroscience and
Nature Communications, focusing on computational approaches to
understanding biological systems.
-------------------------------------------------------------------

Read this text naturally, as if you're introducing yourself to someone.
""")

input("\nPress Enter when you're ready to start recording...")

# Recording parameters
duration = 90  # seconds
sample_rate = 44100  # CD quality

print(f"\n🎤 Recording for {duration} seconds... Start speaking now!")
print("(Press Ctrl+C to stop early)\n")

try:
    # Record audio
    audio = sd.rec(int(duration * sample_rate),
                  samplerate=sample_rate,
                  channels=1,
                  dtype=np.float32)
    sd.wait()
    print("\n✓ Recording complete!")

except KeyboardInterrupt:
    print("\n\n⏹️ Recording stopped early by user")
    sd.stop()
    # Get the actual recorded duration
    audio = audio[:sd.get_stream().write_available * sd.get_stream().channels]

# Save to file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"voice_sample_tim_{timestamp}.wav"

sf.write(filename, audio, sample_rate)

print(f"\n💾 Audio saved to: {filename}")
print(f"📊 Duration: {len(audio) / sample_rate:.1f} seconds")
print(f"📈 Sample rate: {sample_rate} Hz")

print("\n" + "="*70)
print("NEXT STEPS:")
print("="*70)
print("""
1. Go to https://elevenlabs.io/ and sign up
2. Navigate to "Voices" → "Add Voice" → "Instant Voice Cloning"
3. Upload the file: """ + filename + """
4. Name your voice (e.g., "Tim_Clone")
5. Get your Voice ID and API Key
6. Add to .env file:
   ELEVENLABS_API_KEY=your_api_key
   ELEVENLABS_VOICE_ID=your_voice_id

7. Use your cloned voice:
   from digital_twin_like.advanced_tts import AdvancedTTS
   tts = AdvancedTTS("elevenlabs", voice_id="your_voice_id")
   tts.speak("Hello from my cloned voice!")

See VOICE_CLONING_GUIDE.md for full instructions.
""")

print("\n✨ Voice sample ready for cloning! ✨\n")

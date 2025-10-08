#!/usr/bin/env python
"""
Demonstration script for HW4 - Voice-Enabled Digital Twin
This script demonstrates the voice capabilities added to the digital twin
"""
import os
os.chdir('/Users/tim/Desktop/Harvard/MIT-AI-Studio/hw4-claude/digital_twin_like')

from dotenv import load_dotenv
load_dotenv()

from digital_twin_like.voice_agent import VoiceDigitalTwin
from digital_twin_like.text_to_speech import TextToSpeech

print("\n" + "="*70)
print(" "*15 + "VOICE-ENABLED DIGITAL TWIN DEMO - HW4")
print("="*70)

print("""
This demo showcases the voice interaction capabilities added to Tim Cao's
digital twin for HW4. The system combines:

1. Speech-to-Text (STT) using OpenAI Whisper
2. Text-to-Speech (TTS) using gTTS
3. The CrewAI digital twin from HW1-HW3

For this demo, we'll use text input to demonstrate the system's capabilities,
but the full voice interaction is available via the voice_twin command.
""")

input("Press Enter to begin the demo...")

print("\n" + "="*70)
print("INITIALIZING VOICE-ENABLED DIGITAL TWIN")
print("="*70)

voice_twin = VoiceDigitalTwin(whisper_model="base")

print("\n✓ System ready!")

# Demo questions
demo_questions = [
    "Can you introduce yourself?",
    "What research are you working on?",
    "What technical skills do you have?"
]

print("\n" + "="*70)
print("DEMO: TEXT-TO-SPEECH Q&A")
print("="*70)
print("\nThe following questions will be answered by the digital twin")
print("with voice output:\n")

for i, question in enumerate(demo_questions, 1):
    print(f"\n{'-'*70}")
    print(f"Question {i}: {question}")
    print('-'*70)

    # Get response from digital twin
    print("🤔 Thinking...")
    response = voice_twin.respond_to_text(question)

    print(f"\n💬 Response:\n{response}\n")

    # Speak the response
    print("🔊 Speaking response (audio will play)...")
    voice_twin.speak(response)

    if i < len(demo_questions):
        input("\nPress Enter for next question...")

print("\n" + "="*70)
print("DEMO COMPLETE")
print("="*70)

print("""
✅ Successfully demonstrated:
   ✓ Text-to-Speech (TTS) synthesis
   ✓ Integration with CrewAI digital twin
   ✓ Natural conversational responses with voice output

📝 Additional capabilities available:
   • Full voice interaction: voice_twin --voice
   • Text Q&A mode: voice_twin --text
   • Introduction mode: voice_twin --intro

🎤 For voice input (STT), run: voice_twin --voice
   (This requires a microphone and allows speaking questions)

📹 This demo can be recorded for the assignment video submission.
""")

print("\n" + "="*70 + "\n")

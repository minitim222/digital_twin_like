#!/usr/bin/env python
"""
Test script for voice-enabled digital twin
Tests TTS functionality without requiring microphone input
"""
import os
os.chdir('/Users/tim/Desktop/Harvard/MIT-AI-Studio/hw4-claude/digital_twin_like')

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

print("\n" + "="*60)
print("TESTING VOICE-ENABLED DIGITAL TWIN")
print("="*60)

print("\n1. Testing Text-to-Speech...")
print("-" * 60)

from digital_twin_like.text_to_speech import TextToSpeech

tts = TextToSpeech()
test_text = "Hello! I am Tim's digital twin, a computational biology researcher at Harvard."
print(f"Speaking: {test_text}")
tts.speak(test_text)
print("✓ TTS test complete!")

print("\n2. Testing Digital Twin Response with Voice Output...")
print("-" * 60)

from digital_twin_like.voice_agent import VoiceDigitalTwin

print("\nInitializing voice-enabled digital twin...")
voice_twin = VoiceDigitalTwin(whisper_model="base")

print("\n✓ Voice system initialized!")

# Test text-based Q&A with voice output
test_question = "What are you currently researching?"
print(f"\nTest Question: {test_question}")

response = voice_twin.respond_to_text(test_question)
print(f"\nResponse: {response}")

print("\nSpeaking response...")
voice_twin.speak(response)

print("\n" + "="*60)
print("✓ ALL TESTS PASSED!")
print("="*60)

print("\n📝 Next Steps:")
print("1. Run 'voice_twin --text' for interactive text Q&A with voice output")
print("2. Run 'voice_twin --voice' for full voice interaction (requires microphone)")
print("3. Run 'voice_twin --intro' to hear the digital twin introduce itself")
print("\n")

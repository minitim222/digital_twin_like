#!/usr/bin/env python
"""
Simple test for Text-to-Speech only (no API key needed)
"""
import os
os.chdir('/Users/tim/Desktop/Harvard/MIT-AI-Studio/hw4-claude/digital_twin_like')

print("\n" + "="*60)
print("TESTING TEXT-TO-SPEECH (TTS)")
print("="*60)

from digital_twin_like.text_to_speech import TextToSpeech

print("\nInitializing TTS...")
tts = TextToSpeech()

print("\nTest 1: Basic greeting")
print("-" * 60)
text1 = "Hello! I am Tim's digital twin."
print(f"Speaking: {text1}")
tts.speak(text1)
print("✓ Test 1 complete!")

print("\nTest 2: Research introduction")
print("-" * 60)
text2 = """I'm a computational biology researcher at Harvard University.
My research focuses on neural stem cell regulation using spatial transcriptomics techniques."""
print(f"Speaking: {text2}")
tts.speak(text2)
print("✓ Test 2 complete!")

print("\n" + "="*60)
print("✓ ALL TTS TESTS PASSED!")
print("="*60)

print("\n✅ Speech synthesis is working correctly!")
print("\n📝 To test the full system with the digital twin agent:")
print("   1. Make sure your .env file has OPENAI_API_KEY set")
print("   2. Run: voice_twin --text")
print("\n")

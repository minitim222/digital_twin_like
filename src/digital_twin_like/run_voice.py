#!/usr/bin/env python
"""
Simple script to run voice-enabled digital twin
"""
import sys
from digital_twin_like.voice_agent import VoiceDigitalTwin


def main():
    """Main entry point for voice digital twin"""

    if len(sys.argv) > 1 and sys.argv[1] == "--intro":
        # Run introduction mode
        voice_twin = VoiceDigitalTwin(whisper_model="base")
        voice_twin.run_introduction()

    elif len(sys.argv) > 1 and sys.argv[1] == "--text":
        # Text Q&A mode
        voice_twin = VoiceDigitalTwin(whisper_model="base")
        print("\n💬 Text Q&A Mode - Type 'quit' to exit")

        while True:
            question = input("\n👤 Ask a question: ").strip()
            if question.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break

            if question:
                response = voice_twin.respond_to_text(question)
                print(f"\n🤖 Response: {response}")
                voice_twin.speak(response)

    elif len(sys.argv) > 1 and sys.argv[1] == "--voice":
        # Voice Q&A mode
        voice_twin = VoiceDigitalTwin(whisper_model="base")
        print("\n🎤 Voice Q&A Mode - Speak when prompted, Ctrl+C to exit")
        print("(Type 'quit' after speaking to exit, or just press Ctrl+C)\n")

        duration = 5
        if len(sys.argv) > 2:
            try:
                duration = int(sys.argv[2])
            except ValueError:
                pass

        try:
            while True:
                user_input, response = voice_twin.voice_interaction(recording_duration=duration)

                # Check if user said quit/exit
                if user_input and any(word in user_input.lower() for word in ['quit', 'exit', 'stop', 'goodbye']):
                    print("\nGoodbye!")
                    break

                # Auto-continue without prompting
        except KeyboardInterrupt:
            print("\n\nGoodbye!")

    else:
        # Default: show menu
        from digital_twin_like.voice_agent import run_voice_demo
        run_voice_demo()


if __name__ == "__main__":
    main()

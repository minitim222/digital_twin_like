"""
Text-to-speech module using gTTS (Google Text-to-Speech)
"""
from gtts import gTTS
import tempfile
import os
import subprocess
import platform


class TextToSpeech:
    """Handles text-to-speech conversion using gTTS"""

    def __init__(self, language='en', slow=False):
        """
        Initialize TTS settings

        Args:
            language: Language code (default 'en' for English)
            slow: Whether to speak slowly (default False)
        """
        self.language = language
        self.slow = slow

    def speak(self, text, save_to_file=None):
        """
        Convert text to speech and play it

        Args:
            text: Text to convert to speech
            save_to_file: Optional path to save audio file (otherwise uses temp file)
        """
        if not text or not text.strip():
            print("⚠️  No text to speak")
            return

        print(f"🔊 Speaking: {text[:100]}{'...' if len(text) > 100 else ''}")

        # Create speech
        tts = gTTS(text=text, lang=self.language, slow=self.slow)

        # Determine file path
        if save_to_file:
            audio_file = save_to_file
            delete_after = False
        else:
            # Create temporary file
            tmp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
            audio_file = tmp_file.name
            tmp_file.close()
            delete_after = True

        try:
            # Save audio to file
            tts.save(audio_file)

            # Play audio based on platform
            self._play_audio(audio_file)

        finally:
            # Clean up temporary file if needed
            if delete_after and os.path.exists(audio_file):
                os.remove(audio_file)

    def _play_audio(self, audio_file):
        """
        Play audio file using platform-specific command

        Args:
            audio_file: Path to audio file to play
        """
        system = platform.system()

        try:
            if system == "Darwin":  # macOS
                subprocess.run(["afplay", audio_file], check=True)
            elif system == "Linux":
                # Try multiple players
                for player in ["mpg123", "ffplay", "cvlc"]:
                    try:
                        subprocess.run([player, "-q", audio_file], check=True)
                        break
                    except FileNotFoundError:
                        continue
            elif system == "Windows":
                os.startfile(audio_file)
            else:
                print(f"⚠️  Cannot play audio on {system}")

        except Exception as e:
            print(f"⚠️  Error playing audio: {e}")

    def save_speech(self, text, output_path):
        """
        Convert text to speech and save to file without playing

        Args:
            text: Text to convert to speech
            output_path: Path where audio file should be saved
        """
        print(f"💾 Saving speech to: {output_path}")
        tts = gTTS(text=text, lang=self.language, slow=self.slow)
        tts.save(output_path)
        print("✓ Speech saved!")


# Example usage
if __name__ == "__main__":
    tts = TextToSpeech()

    print("\n=== Text-to-Speech Test ===")
    test_text = "Hello! I am Tim's digital twin. I'm a computational biology researcher at Harvard."
    tts.speak(test_text)

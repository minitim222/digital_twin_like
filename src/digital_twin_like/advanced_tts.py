"""
Advanced Text-to-Speech with multiple backend options:
1. gTTS (Google TTS) - Free, basic
2. OpenAI TTS - High quality, requires API key
3. ElevenLabs - Voice cloning, requires API key
4. Kokoro TTS - Local, high quality
"""
import os
import tempfile
import subprocess
import platform
from pathlib import Path


class AdvancedTTS:
    """Advanced TTS with multiple backend options"""

    def __init__(self, backend="gtts", api_key=None, voice_id=None):
        """
        Initialize Advanced TTS

        Args:
            backend: 'gtts', 'openai', 'elevenlabs', or 'kokoro'
            api_key: API key for OpenAI or ElevenLabs
            voice_id: Voice ID for ElevenLabs or model for others
        """
        self.backend = backend
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.voice_id = voice_id

        if backend == "kokoro":
            try:
                from kokoro_onnx import Kokoro
                self.kokoro = Kokoro("kokoro-v0_19.onnx", "voices.bin")
                print("✓ Kokoro TTS initialized")
            except Exception as e:
                print(f"⚠️ Kokoro TTS failed to initialize: {e}")
                print("Falling back to gTTS")
                self.backend = "gtts"

    def speak(self, text, save_to_file=None):
        """
        Convert text to speech using selected backend

        Args:
            text: Text to convert
            save_to_file: Optional path to save audio
        """
        if not text or not text.strip():
            print("⚠️ No text to speak")
            return

        print(f"🔊 Speaking with {self.backend}: {text[:100]}{'...' if len(text) > 100 else ''}")

        if self.backend == "gtts":
            self._speak_gtts(text, save_to_file)
        elif self.backend == "openai":
            self._speak_openai(text, save_to_file)
        elif self.backend == "elevenlabs":
            self._speak_elevenlabs(text, save_to_file)
        elif self.backend == "kokoro":
            self._speak_kokoro(text, save_to_file)

    def _speak_gtts(self, text, save_to_file=None):
        """Use Google TTS"""
        from gtts import gTTS

        if save_to_file:
            audio_file = save_to_file
            delete_after = False
        else:
            tmp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
            audio_file = tmp_file.name
            tmp_file.close()
            delete_after = True

        try:
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(audio_file)
            self._play_audio(audio_file)
        finally:
            if delete_after and os.path.exists(audio_file):
                os.remove(audio_file)

    def _speak_openai(self, text, save_to_file=None):
        """Use OpenAI TTS API"""
        try:
            from openai import OpenAI

            client = OpenAI(api_key=self.api_key)

            # Default to 'alloy' voice, or use specified voice
            voice = self.voice_id or "alloy"  # Options: alloy, echo, fable, onyx, nova, shimmer

            if save_to_file:
                audio_file = save_to_file
                delete_after = False
            else:
                tmp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
                audio_file = tmp_file.name
                tmp_file.close()
                delete_after = True

            try:
                response = client.audio.speech.create(
                    model="tts-1",  # or "tts-1-hd" for higher quality
                    voice=voice,
                    input=text
                )

                response.stream_to_file(audio_file)
                self._play_audio(audio_file)
            finally:
                if delete_after and os.path.exists(audio_file):
                    os.remove(audio_file)

        except Exception as e:
            print(f"⚠️ OpenAI TTS error: {e}")
            print("Falling back to gTTS")
            self._speak_gtts(text, save_to_file)

    def _speak_elevenlabs(self, text, save_to_file=None):
        """Use ElevenLabs TTS/Voice Cloning"""
        try:
            from elevenlabs import generate, play, set_api_key

            set_api_key(self.api_key)

            # Use specified voice_id or default voice
            voice_id = self.voice_id or "21m00Tcm4TlvDq8ikWAM"  # Default: Rachel voice

            audio = generate(
                text=text,
                voice=voice_id,
                model="eleven_monolingual_v1"
            )

            if save_to_file:
                with open(save_to_file, 'wb') as f:
                    f.write(audio)
                self._play_audio(save_to_file)
            else:
                # Play directly
                play(audio)

        except Exception as e:
            print(f"⚠️ ElevenLabs error: {e}")
            print("Falling back to gTTS")
            self._speak_gtts(text, save_to_file)

    def _speak_kokoro(self, text, save_to_file=None):
        """Use Kokoro TTS (local, high quality)"""
        try:
            if save_to_file:
                audio_file = save_to_file
                delete_after = False
            else:
                tmp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
                audio_file = tmp_file.name
                tmp_file.close()
                delete_after = True

            try:
                # Generate audio
                samples, sample_rate = self.kokoro.create(
                    text,
                    voice=self.voice_id or 'af_sky',  # Default voice
                    speed=1.0,
                    lang='en-us'
                )

                # Save to file
                import soundfile as sf
                sf.write(audio_file, samples, sample_rate)

                # Play
                self._play_audio(audio_file)
            finally:
                if delete_after and os.path.exists(audio_file):
                    os.remove(audio_file)

        except Exception as e:
            print(f"⚠️ Kokoro TTS error: {e}")
            print("Falling back to gTTS")
            self._speak_gtts(text, save_to_file)

    def _play_audio(self, audio_file):
        """Play audio file using platform-specific command"""
        system = platform.system()

        try:
            if system == "Darwin":  # macOS
                subprocess.run(["afplay", audio_file], check=True)
            elif system == "Linux":
                for player in ["mpg123", "ffplay", "cvlc"]:
                    try:
                        subprocess.run([player, "-q", audio_file], check=True)
                        break
                    except FileNotFoundError:
                        continue
            elif system == "Windows":
                os.startfile(audio_file)
        except Exception as e:
            print(f"⚠️ Error playing audio: {e}")


# Quick test function
def test_tts_backends():
    """Test different TTS backends"""
    test_text = "Hello! I am Tim's digital twin, a computational biology researcher at Harvard."

    print("\n" + "="*60)
    print("TESTING TTS BACKENDS")
    print("="*60)

    # Test gTTS (always available)
    print("\n1. Testing Google TTS (gTTS)...")
    tts_gtts = AdvancedTTS(backend="gtts")
    tts_gtts.speak(test_text)

    # Test Kokoro (if available)
    print("\n2. Testing Kokoro TTS...")
    tts_kokoro = AdvancedTTS(backend="kokoro")
    tts_kokoro.speak(test_text)

    # Test OpenAI (if API key available)
    if os.getenv("OPENAI_API_KEY"):
        print("\n3. Testing OpenAI TTS...")
        tts_openai = AdvancedTTS(backend="openai", voice_id="alloy")
        tts_openai.speak(test_text)

    print("\n" + "="*60)
    print("✓ TTS Backend Tests Complete!")
    print("="*60)


if __name__ == "__main__":
    test_tts_backends()

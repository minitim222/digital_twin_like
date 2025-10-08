"""
Speech-to-text module using OpenAI Whisper
"""
import whisper
import sounddevice as sd
import soundfile as sf
import numpy as np
import tempfile
import os


class SpeechToText:
    """Handles speech-to-text conversion using Whisper"""

    def __init__(self, model_size="base"):
        """
        Initialize Whisper model

        Args:
            model_size: Size of Whisper model (tiny, base, small, medium, large)
                       'base' provides good balance of speed and accuracy
        """
        print(f"Loading Whisper {model_size} model...")
        self.model = whisper.load_model(model_size)
        self.sample_rate = 16000  # Whisper expects 16kHz audio

    def record_audio(self, duration=5, sample_rate=16000):
        """
        Record audio from microphone

        Args:
            duration: Recording duration in seconds
            sample_rate: Sample rate for recording (default 16000 for Whisper)

        Returns:
            numpy array of audio samples
        """
        print(f"\n🎤 Recording for {duration} seconds... Speak now!")
        audio = sd.rec(int(duration * sample_rate),
                      samplerate=sample_rate,
                      channels=1,
                      dtype=np.float32)
        sd.wait()  # Wait until recording is finished
        print("✓ Recording complete!")
        return audio.flatten()

    def transcribe_audio(self, audio_data, sample_rate=16000):
        """
        Transcribe audio data to text using Whisper

        Args:
            audio_data: numpy array of audio samples
            sample_rate: Sample rate of the audio

        Returns:
            Transcribed text string
        """
        # Create temporary file for audio
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
            tmp_path = tmp_file.name

        try:
            # Save audio to temporary file
            sf.write(tmp_path, audio_data, sample_rate)

            # Transcribe using Whisper
            print("🔄 Transcribing audio...")
            result = self.model.transcribe(tmp_path, language="en")
            transcribed_text = result["text"].strip()

            return transcribed_text

        finally:
            # Clean up temporary file
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def listen_and_transcribe(self, duration=5):
        """
        Record audio from microphone and transcribe it

        Args:
            duration: Recording duration in seconds

        Returns:
            Transcribed text string
        """
        audio = self.record_audio(duration, self.sample_rate)
        text = self.transcribe_audio(audio, self.sample_rate)
        return text


# Example usage
if __name__ == "__main__":
    stt = SpeechToText(model_size="base")

    print("\n=== Speech-to-Text Test ===")
    text = stt.listen_and_transcribe(duration=5)
    print(f"\n📝 Transcribed text: {text}")

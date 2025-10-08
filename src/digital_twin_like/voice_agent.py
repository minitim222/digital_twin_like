"""
Voice-enabled digital twin agent
Combines speech-to-text and text-to-speech with the CrewAI digital twin
"""
from digital_twin_like.crew import DigitalTwinLike
from digital_twin_like.speech_to_text import SpeechToText
from digital_twin_like.text_to_speech import TextToSpeech
from crewai import Agent, Task, Crew, Process
import warnings
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Disable CrewAI execution trace prompts
os.environ["CREWAI_STORAGE_DIR"] = "/tmp/crewai"  # Use temp storage
os.environ["CREWAI_TELEMETRY_OPT_OUT"] = "true"  # Opt out of telemetry

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


class VoiceDigitalTwin:
    """Voice-enabled digital twin that can listen and speak"""

    def __init__(self, whisper_model="base"):
        """
        Initialize voice-enabled digital twin

        Args:
            whisper_model: Size of Whisper model for STT (tiny, base, small, medium, large)
        """
        print("\n=== Initializing Voice-Enabled Digital Twin ===")

        # Initialize speech components
        print("\n1. Loading Speech-to-Text (Whisper)...")
        self.stt = SpeechToText(model_size=whisper_model)

        print("\n2. Loading Text-to-Speech (gTTS)...")
        self.tts = TextToSpeech()

        print("\n3. Loading Digital Twin (CrewAI)...")
        self.digital_twin = DigitalTwinLike()

        # Import knowledge tools
        from digital_twin_like.tools.knowledge_tool import KNOWLEDGE_TOOLS

        # Create a conversational agent for Q&A
        self.conversation_agent = Agent(
            role="Conversational Digital Twin of Tim Cao",
            goal="Answer questions about Tim Cao authentically, representing his expertise and personality",
            backstory="""You are the digital representation of Wuxinhao (Tim) Cao, a graduate student and researcher
            at Harvard University specializing in computational biology and spatial transcriptomics.

            You have access to a comprehensive knowledge base through these tools:
            - "Get Tim's Biography" for educational background and achievements
            - "Get Tim's Technical Skills" for programming and technical capabilities
            - "Get Tim's Research Background" for research projects and publications
            - "Search Knowledge Base" to find specific information

            Use these tools to retrieve accurate information when answering questions. Keep responses conversational,
            informative, and authentic to Tim's voice. Answer questions naturally, as if Tim himself is speaking.""",
            verbose=True,
            allow_delegation=False,
            tools=KNOWLEDGE_TOOLS
        )

        print("\n✓ Voice-Enabled Digital Twin Ready!\n")

    def listen(self, duration=5):
        """
        Listen to user's voice input

        Args:
            duration: Recording duration in seconds

        Returns:
            Transcribed text
        """
        return self.stt.listen_and_transcribe(duration=duration)

    def respond_to_text(self, user_input):
        """
        Generate text response to user input using the digital twin

        Args:
            user_input: User's question or input text

        Returns:
            Digital twin's response text
        """
        # Create a task for responding to the user's input
        response_task = Task(
            description=f"Respond to this question or prompt conversationally: {user_input}",
            expected_output="A natural, conversational response that authentically represents Tim Cao",
            agent=self.conversation_agent
        )

        # Create a crew with just the conversation agent
        crew = Crew(
            agents=[self.conversation_agent],
            tasks=[response_task],
            process=Process.sequential,
            verbose=False,  # Less verbose for cleaner output
            memory=False,   # Disable memory to avoid prompts
            cache=False     # Disable cache for faster execution
        )

        # Get response
        result = crew.kickoff()

        # Extract text from result
        if hasattr(result, 'raw'):
            response_text = result.raw
        else:
            response_text = str(result)

        return response_text

    def speak(self, text):
        """
        Speak the given text

        Args:
            text: Text to speak
        """
        self.tts.speak(text)

    def voice_interaction(self, recording_duration=5):
        """
        Complete voice interaction: listen, process, and respond

        Args:
            recording_duration: Duration for recording user's voice in seconds

        Returns:
            Tuple of (user_input, response)
        """
        print("\n" + "="*60)
        print("🎤 VOICE INTERACTION MODE")
        print("="*60)

        # Listen to user
        user_input = self.listen(duration=recording_duration)
        print(f"\n👤 You said: {user_input}")

        # Generate response
        print("\n🤔 Thinking...")
        response = self.respond_to_text(user_input)
        print(f"\n🤖 Tim's Digital Twin: {response}")

        # Speak response
        print("\n🔊 Speaking response...")
        self.speak(response)

        print("\n" + "="*60 + "\n")

        return user_input, response

    def run_introduction(self):
        """
        Run the original introduction task from the digital twin
        with voice output
        """
        print("\n=== Running Introduction with Voice ===")

        # Run the original crew
        result = self.digital_twin.crew().kickoff(inputs={})

        # Extract and speak the result
        if hasattr(result, 'raw'):
            intro_text = result.raw
        else:
            intro_text = str(result)

        print(f"\n📝 Introduction Text:\n{intro_text}")
        print("\n🔊 Speaking introduction...")
        self.speak(intro_text)

        return intro_text


def run_voice_demo():
    """Demo function showing voice capabilities"""
    print("\n" + "="*60)
    print("🎤 VOICE-ENABLED DIGITAL TWIN DEMO")
    print("="*60)

    # Initialize voice-enabled digital twin
    voice_twin = VoiceDigitalTwin(whisper_model="base")

    print("\nChoose a mode:")
    print("1. Voice Q&A (ask questions with your voice)")
    print("2. Text Q&A (type questions, hear responses)")
    print("3. Run introduction with voice")

    choice = input("\nEnter choice (1/2/3): ").strip()

    if choice == "1":
        # Voice interaction mode
        print("\n📢 Voice Q&A Mode - Speak your question when prompted")
        recording_time = int(input("Recording duration in seconds (default 5): ").strip() or "5")
        voice_twin.voice_interaction(recording_duration=recording_time)

    elif choice == "2":
        # Text input with voice output
        print("\n💬 Text Q&A Mode")
        question = input("Ask a question: ").strip()
        if question:
            response = voice_twin.respond_to_text(question)
            print(f"\n🤖 Response: {response}")
            voice_twin.speak(response)

    elif choice == "3":
        # Introduction mode
        voice_twin.run_introduction()

    else:
        print("Invalid choice")


if __name__ == "__main__":
    run_voice_demo()

# 🤖 Tim's Digital Twin - CrewAI Agent with Voice Interaction

## 📋 Overview
This project creates a CrewAI agent that embodies my skills, personality, and research background as a computational biology graduate student at Harvard University.

## 🎤 **NEW in HW4: Voice Interaction!**
The digital twin now supports voice-based interaction:
- 🎙️ **Speech-to-Text**: Speak questions using OpenAI Whisper
- 🔊 **Text-to-Speech**: Hear responses using gTTS
- 💬 **Natural Conversation**: Voice-enabled Q&A with the digital twin

**Quick Start with Voice**:
```bash
# Text Q&A with voice output (easiest)
voice_twin --text

# Full voice interaction (requires microphone)
voice_twin --voice

# Hear the digital twin introduce itself
voice_twin --intro
```

📚 **Voice Documentation**: See [`QUICKSTART.md`](QUICKSTART.md) for voice setup or [`VOICE_README.md`](VOICE_README.md) for complete details.

## 🤝 AI Usage Disclosure
**Percentage of AI assistance in this project:**
- **Code Development**: ~25% - AI assisted with CrewAI framework guidance, debugging configuration issues, and code structure suggestions
- **Documentation**: ~40% - AI helped with README formatting, structure organization, and technical writing improvements
- **Agent Configuration**: ~15% - AI provided guidance on YAML structure and best practices for agent persona development
- **Problem Solving**: ~30% - AI assisted with troubleshooting Git issues, API authentication, and deployment guidance

The core agent persona, technical expertise, research background, and CV data are 100% authentic and human-generated. AI was used as a coding assistant and documentation tool, similar to how one might use Stack Overflow or technical documentation.

## 🧬 About the Agent
My digital twin represents me (Tim Cao) as a computational biology researcher specializing in:
- 🧠 Spatial transcriptomics and neural stem cell biology
- 🤖 Machine learning and deep learning applications in biology
- 🛠️ Development of computational tools for scientific research
- 🔬 Multi-omics data analysis and visualization

## ⚡ Agent Capabilities
The agent can:
- 👋 Introduce me professionally to academic and professional audiences
- 🔬 Explain my research on pregnancy-driven neural stem cell niche remodeling
- 💻 Describe my technical skills in Python, R, and spatial omics
- 🎯 Discuss my career goals in computational biology and neuroscience

## 🚀 Setup and Installation

### 📋 Prerequisites
- 🐍 Python 3.10+
- 🔑 OpenAI API key
- 🎬 FFmpeg (for voice features: `brew install ffmpeg` on macOS)

### 📦 Installation
```bash
# Clone the repository
git clone https://github.com/minitim222/digital_twin_like.git
cd digital_twin_like

# Install CrewAI
pip install crewai

# Set up environment variables
echo "OPENAI_API_KEY=your_key_here" > .env

# Install dependencies
crewai install

# Run the agent
crewai run
```

## 🎮 How to Use This Agent

### 🔄 Basic Usage
The agent is configured to run through multiple tasks sequentially when you execute `crewai run`. It will:

1. 👋 **Introduction Task**: Provide a professional self-introduction
2. 🔬 **Research Explanation**: Explain current research in accessible terms
3. 💪 **Skills Showcase**: Detail technical capabilities and tools developed
4. 🎯 **Career Goals**: Discuss future aspirations in computational biology

### ▶️ Running the Agent
```bash
# Standard execution (runs all tasks)
crewai run

# Alternative execution
python src/digital_twin_like/main.py
```

### ⏱️ Expected Runtime
- ⏲️ Total execution time: ~2-3 minutes
- 🕐 Each task takes 30-60 seconds depending on complexity
- 📊 Output is displayed in real-time with verbose logging

## 📄 Sample Output

### 🎤 Introduction Task Output
```
Hello everyone, I'm Tim Cao. I'm currently pursuing a Master of Science in Computational Biology and Quantitative Genetics at Harvard, where I'm building on a strong foundation in statistics, biochemistry, and immunology. I earned my B.Sc. (Honors) from the University of Toronto in Statistics, Biochemistry & Immunology with High Distinction, and I've been honored to be on the Dean's List for four consecutive years (2021–2024). This mix of quantitative training and wet-lab insight has shaped how I approach biology: as a problem at the intersection of data, theory, and experiment.

My research sits at the crossroads of spatial transcriptomics and neural stem cell biology. I'm a graduate researcher at Boston Children's Hospital in the Newborn Medicine division, where I study neural stem cell regulation and the microglial signals that modulate their activity. My work encompasses spatial technologies—MERFISH, Xenium, and Visium HD—and I'm developing computational pipelines for anatomical segmentation and cell annotation. I'm also pursuing a first-author manuscript on how pregnancy remodels the neural stem cell niche, a project that blends developmental biology with state-of-the-art spatial analytics.

On the technical front, I bring a broad toolkit for computational biology and machine learning: Python (PyTorch, TensorFlow, Scanpy), R (Seurat, Bioconductor), SQL, Bash; deep learning, CNNs, and transformers (BERT); multi-omics integration; and cloud/HPC workflows (AWS, GCP, SLURM, Docker, Snakemake). I'm especially focused on building reproducible pipelines for spatial omics datasets and developing methods for more accurate anatomical segmentation and cell annotation, with a particular emphasis on how microglial signals influence neural stem cell activity. My goal is to translate complex computational signals into biologically meaningful insights.

I've had the privilege to contribute to high-impact publications in Nature Neuroscience, Nature Communications, and Advanced Science, underscoring my ability to work across disciplines and collaborate effectively. I've been recognized with a first-place award at the UTSW Healthcare Case Competition in 2025 and over $30k in scholarships, reflecting both the rigor and the potential impact of my work. Beyond publications, I'm deeply committed to using computational methods to understand biological systems—from development and neural biology to spatial omics—always prioritizing reproducibility, efficiency, and clear communication. I'm excited to learn from and contribute to this class, applying robust, data-driven approaches to complex questions in neuroscience and beyond.
```

### ✨ Key Features of Output
- 🎯 **Authentic voice**: Reflects my actual speaking style and personality
- 🔬 **Technical accuracy**: Correctly describes my research and skills
- 💼 **Professional tone**: Appropriate for academic and professional settings
- 📚 **Comprehensive coverage**: Includes education, research, skills, and achievements
- 📖 **Engaging narrative**: Tells a coherent story about my background and goals

## ⚙️ Technical Implementation

### 🤖 Agent Configuration
- **Role**: Computational Biology Researcher and Data Science Graduate Student
- **Goal**: Authentically represent Tim Cao's expertise and background
- **Backstory**: Comprehensive background including education at University of Toronto and Harvard, research at Boston Children's Hospital, publications, and technical skills

### 📋 Key Tasks
1. 👋 **Introduction Task**: Professional self-introduction
2. 🔬 **Research Explanation**: Detailed explanation of spatial transcriptomics research
3. 💪 **Skills Showcase**: Technical abilities and tools developed
4. 🎯 **Career Goals**: Future aspirations in computational biology

### 📁 Project Structure
```
digital_twin_like/
├── src/
│   └── digital_twin_like/
│       ├── config/
│       │   ├── agents.yaml      # Agent configuration
│       │   └── tasks.yaml       # Task definitions
│       ├── crew.py              # Crew orchestration
│       └── main.py              # Execution entry point
├── .env                         # Environment variables (not in repo)
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## 📊 Assignment Requirements Met

### ✅ What Worked
- 🎉 Successfully installed CrewAI and set up project structure
- 👤 Configured agent with authentic personal background from CV
- 📋 Defined multiple tasks that showcase different aspects of expertise
- 🤖 Agent successfully executes and provides detailed, authentic responses
- 🔧 Created reproducible setup with proper configuration management

### ❌ What Didn't Work (Initially)
- 💳 Initial API quota limitations with OpenAI (resolved by setting up proper billing)
- 🏷️ Naming mismatches between configuration files (fixed through careful alignment)

### 🎓 What I Learned
- 🧠 How to structure CrewAI agents with personal knowledge and expertise
- 🔗 The importance of consistent naming across YAML configuration files
- 👤 How to create authentic agent personas using real CV data
- ⚡ The power of CrewAI's configuration-driven approach for rapid prototyping
- 🔐 Best practices for managing API keys and environment variables

## 🛠️ Troubleshooting

### ⚠️ Common Issues
1. 🔑 **API Key Error**: Ensure your OpenAI API key is set in `.env` file
2. 📦 **Module Not Found**: Run `crewai install` to install dependencies
3. 🚫 **Rate Limiting**: Check your OpenAI usage and billing status

### 📈 Performance Notes
- 💰 Each task execution requires API calls to OpenAI
- 📊 Verbose mode shows detailed execution logs
- 💵 Total cost per run is typically $0.05-0.10 depending on output length

## 🚀 Future Enhancements
- 🌐 Add web search capabilities for current research updates
- 📚 Integrate with academic databases for publication queries
- 📄 Add file processing tools for CV analysis
- 🧠 Implement memory for conversation context

## 🛠️ Technologies Used
- 🤖 **CrewAI**: Multi-agent orchestration framework
- 🧠 **OpenAI GPT**: Language model for agent responses
- 🐍 **Python**: Primary programming language
- 📋 **YAML**: Configuration management

## 📞 Contact
- 👤 **Name**: Wuxinhao (Tim) Cao
- 📧 **Email**: tim_cao@hsph.harvard.edu
- 🏛️ **Institution**: Harvard T.H. Chan School of Public Health
- 🎓 **Program**: MS in Computational Biology and Quantitative Genetics
# Knowledge Base System

## Overview

The digital twin now uses a **modular knowledge base** system instead of hardcoded information in the agent configuration. This makes it easier to update information and maintain the system.

## Architecture

### Knowledge Base Files

All personal background information is stored in structured markdown files in the `knowledge/` directory:

1. **`tim_bio.md`** - Biography
   - Personal information
   - Educational background
   - Current position
   - Notable achievements

2. **`tim_skills.md`** - Technical Skills
   - Programming languages (Python, R, SQL, Bash)
   - Machine learning expertise
   - Computational biology tools
   - Cloud & HPC experience

3. **`tim_research.md`** - Research Background
   - Current research projects
   - Publications
   - Research areas
   - Future directions

### Knowledge Tools

Four tools provide access to the knowledge base:

1. **Get Tim's Biography** - Retrieves biographical information
2. **Get Tim's Technical Skills** - Retrieves technical expertise
3. **Get Tim's Research Background** - Retrieves research info
4. **Search Knowledge Base** - Searches across all files

### Implementation

**Tool Definition:** `src/digital_twin_like/tools/knowledge_tool.py`
```python
@tool("Get Tim's Biography")
def get_biography() -> str:
    """Retrieves biographical information"""
    return load_knowledge_file("tim_bio.md")
```

**Agent Configuration:** `src/digital_twin_like/config/agents.yaml`
```yaml
digital_twin_tim:
  backstory: >
    You have access to a comprehensive knowledge base...
    Use these tools to retrieve accurate information:
    - "Get Tim's Biography"
    - "Get Tim's Technical Skills"
    - "Get Tim's Research Background"
    - "Search Knowledge Base"
```

**Crew Setup:** `src/digital_twin_like/crew.py`
```python
from digital_twin_like.tools.knowledge_tool import KNOWLEDGE_TOOLS

@agent
def digital_twin_tim(self) -> Agent:
    return Agent(
        config=self.agents_config['digital_twin_tim'],
        tools=KNOWLEDGE_TOOLS  # Knowledge base tools
    )
```

## Benefits

### 1. **Easy Updates**
Update information by editing markdown files - no code changes needed:
```bash
# Edit biography
vim knowledge/tim_bio.md

# No need to modify agents.yaml or crew.py!
```

### 2. **Modular & Maintainable**
- Separation of concerns: data vs. logic
- Clean agent configuration
- Reusable knowledge tools

### 3. **Scalable**
Easy to add new knowledge:
```bash
# Add new knowledge file
echo "# Tim's Publications..." > knowledge/tim_publications.md

# Create new tool
@tool("Get Publications")
def get_publications():
    return load_knowledge_file("tim_publications.md")
```

### 4. **Accurate Retrieval**
Agent uses tools to fetch current information instead of relying on potentially outdated backstory text.

## Usage

### Testing Knowledge Base

```bash
# Test knowledge tools directly
python test_knowledge_base.py
```

### Updating Information

1. **Edit knowledge files**:
   ```bash
   vim knowledge/tim_bio.md
   vim knowledge/tim_skills.md
   vim knowledge/tim_research.md
   ```

2. **Changes apply immediately** - no restart needed!

### Adding New Knowledge

1. **Create new markdown file**:
   ```bash
   echo "# New Topic" > knowledge/new_topic.md
   ```

2. **Add tool in `knowledge_tool.py`**:
   ```python
   @tool("Get New Topic")
   def get_new_topic() -> str:
       return load_knowledge_file("new_topic.md")

   # Add to KNOWLEDGE_TOOLS list
   KNOWLEDGE_TOOLS = [
       get_biography,
       get_skills,
       get_research,
       search_knowledge,
       get_new_topic  # New tool
   ]
   ```

3. **Tool available to agent automatically!**

## Agent Behavior

When asked a question, the agent:

1. **Recognizes** what information is needed
2. **Calls appropriate tool** (e.g., "Get Tim's Biography")
3. **Retrieves** information from knowledge base
4. **Formulates** natural response using the data

**Example:**
```
User: "What is your educational background?"

Agent thinks: Need biography information
Agent action: Calls "Get Tim's Biography"
Agent receives: Full biography from tim_bio.md
Agent responds: Natural answer based on retrieved data
```

## File Structure

```
digital_twin_like/
├── knowledge/
│   ├── tim_bio.md          # Biography
│   ├── tim_skills.md       # Technical skills
│   └── tim_research.md     # Research background
├── src/digital_twin_like/
│   ├── tools/
│   │   └── knowledge_tool.py  # Knowledge retrieval tools
│   ├── config/
│   │   └── agents.yaml        # Agent config (now minimal)
│   └── crew.py                # Crew with knowledge tools
└── test_knowledge_base.py     # Test script
```

## Advantages Over Hardcoded Backstory

### Before (Hardcoded):
```yaml
backstory: >
  Educational Background:
  - Harvard MS (GPA: 3.86)
  - UofT BS (GPA: 3.91)
  ...
  [40+ lines of static text]
```

**Problems:**
- ❌ Hard to update
- ❌ Mixed concerns (data + config)
- ❌ No dynamic retrieval
- ❌ Duplicate information

### After (Knowledge Base):
```yaml
backstory: >
  You have access to knowledge base tools.
  Use them to retrieve accurate information.
```

**Benefits:**
- ✅ Easy to update (edit .md files)
- ✅ Separation of concerns
- ✅ Dynamic retrieval
- ✅ Single source of truth

## Testing

The agent successfully uses knowledge tools:

```bash
$ python test_knowledge_base.py

✓ Knowledge base files loaded successfully
✓ Knowledge tools working correctly
✓ Agent has access to 4 knowledge tools
✓ Agent retrieves information correctly

Agent Tool Execution:
  Using Tool: Get Tim's Biography
  Tool Output: [Full biography retrieved]
  Final Answer: [Natural response based on knowledge]
```

## Future Enhancements

1. **Vector Search** - Semantic search across knowledge
2. **Knowledge Versioning** - Track changes over time
3. **Multi-format Support** - PDFs, CSVs, JSON
4. **Auto-indexing** - Automatically discover new files
5. **Knowledge Graph** - Relationships between concepts

---

**Summary**: The knowledge base system provides a clean, maintainable way to manage personal information with dynamic retrieval through specialized tools.

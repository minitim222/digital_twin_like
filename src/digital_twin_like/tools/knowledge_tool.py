"""
Knowledge base tool for accessing Tim's background information
"""
from crewai.tools import tool
import os
from pathlib import Path


def load_knowledge_file(filename):
    """Load content from knowledge base file"""
    knowledge_dir = Path(__file__).parent.parent.parent.parent / "knowledge"
    file_path = knowledge_dir / filename

    if file_path.exists():
        with open(file_path, 'r') as f:
            return f.read()
    return f"Knowledge file {filename} not found"


@tool("Get Tim's Biography")
def get_biography() -> str:
    """
    Retrieves Tim Cao's biographical information including education,
    current position, and notable achievements.

    Returns:
        str: Complete biography with educational background and achievements
    """
    return load_knowledge_file("tim_bio.md")


@tool("Get Tim's Technical Skills")
def get_skills() -> str:
    """
    Retrieves Tim Cao's technical skills and expertise including programming
    languages, machine learning capabilities, and computational biology tools.

    Returns:
        str: Detailed technical skills and capabilities
    """
    return load_knowledge_file("tim_skills.md")


@tool("Get Tim's Research Background")
def get_research() -> str:
    """
    Retrieves Tim Cao's research background, publications, and current
    research projects in spatial transcriptomics and neural stem cells.

    Returns:
        str: Research background and publications
    """
    return load_knowledge_file("tim_research.md")


@tool("Search Knowledge Base")
def search_knowledge(query: str) -> str:
    """
    Search across all knowledge base files for specific information.

    Args:
        query: The search query or topic to find information about

    Returns:
        str: Relevant information from the knowledge base
    """
    # Load all knowledge files
    bio = load_knowledge_file("tim_bio.md")
    skills = load_knowledge_file("tim_skills.md")
    research = load_knowledge_file("tim_research.md")

    # Simple search - return sections that contain the query (case-insensitive)
    results = []
    query_lower = query.lower()

    all_content = {
        "Biography": bio,
        "Skills": skills,
        "Research": research
    }

    for category, content in all_content.items():
        if query_lower in content.lower():
            # Extract relevant paragraphs
            lines = content.split('\n')
            relevant_lines = []
            for i, line in enumerate(lines):
                if query_lower in line.lower():
                    # Include context (previous and next lines)
                    start = max(0, i-2)
                    end = min(len(lines), i+3)
                    relevant_lines.extend(lines[start:end])

            if relevant_lines:
                results.append(f"\n## From {category}:\n" + '\n'.join(relevant_lines))

    if results:
        return '\n'.join(results)
    else:
        return f"No specific information found for: {query}. Try using the biography, skills, or research tools for general information."


# List of all knowledge tools
KNOWLEDGE_TOOLS = [
    get_biography,
    get_skills,
    get_research,
    search_knowledge
]

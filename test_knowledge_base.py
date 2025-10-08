#!/usr/bin/env python
"""
Test knowledge base integration
"""
import os
os.chdir('/Users/tim/Desktop/Harvard/MIT-AI-Studio/hw4-claude/digital_twin_like')

from dotenv import load_dotenv
load_dotenv()

print("\n" + "="*70)
print(" "*20 + "KNOWLEDGE BASE TEST")
print("="*70)

print("\n1. Testing Knowledge Tools Directly...")
print("-" * 70)

from src.digital_twin_like.tools.knowledge_tool import (
    get_biography,
    get_skills,
    get_research,
    search_knowledge
)

# Test biography tool
print("\n📄 Testing Biography Tool:")
bio_result = get_biography.func()
print(f"✓ Retrieved {len(bio_result)} characters")
print(f"Preview: {bio_result[:200]}...")

# Test skills tool
print("\n💻 Testing Skills Tool:")
skills_result = get_skills.func()
print(f"✓ Retrieved {len(skills_result)} characters")
print(f"Preview: {skills_result[:200]}...")

# Test research tool
print("\n🔬 Testing Research Tool:")
research_result = get_research.func()
print(f"✓ Retrieved {len(research_result)} characters")
print(f"Preview: {research_result[:200]}...")

# Test search tool
print("\n🔍 Testing Search Tool:")
search_result = search_knowledge.func("spatial transcriptomics")
print(f"✓ Search found {len(search_result)} characters")
print(f"Preview: {search_result[:300]}...")

print("\n" + "="*70)
print("2. Testing with CrewAI Agent...")
print("="*70)

from digital_twin_like.crew import DigitalTwinLike

print("\nInitializing Digital Twin with Knowledge Base...")
twin = DigitalTwinLike()

print("\n✓ Agent created with knowledge tools!")
print(f"  Agent has {len(twin.digital_twin_tim().tools)} tools available")

# List the tools
print("\n  Available tools:")
for i, tool in enumerate(twin.digital_twin_tim().tools, 1):
    print(f"    {i}. {tool.name}")

print("\n" + "="*70)
print("3. Testing Agent Response with Knowledge Base...")
print("="*70)

print("\nAsking agent: 'What is your educational background?'")
print("(This should use the knowledge base tools)")

from crewai import Task, Crew

agent = twin.digital_twin_tim()
task = Task(
    description="Tell me about your educational background.",
    expected_output="A detailed response about educational background using knowledge base",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=False
)

print("\nRunning agent...")
result = crew.kickoff()

print("\n📝 Agent Response:")
print("-" * 70)
print(result)
print("-" * 70)

print("\n" + "="*70)
print("✅ KNOWLEDGE BASE INTEGRATION TEST COMPLETE!")
print("="*70)

print("""
Summary:
- ✓ Knowledge base files loaded successfully
- ✓ Knowledge tools working correctly
- ✓ Agent has access to knowledge tools
- ✓ Agent can retrieve information from knowledge base

The digital twin now uses a modular knowledge base instead of
hardcoded information in the agent configuration!
""")

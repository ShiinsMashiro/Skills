---
name: disc-generator
description: This skill should be used when the user asks to "生成讨论课页面", "生成学习网页", "生成类似cs61a的页面", "生成练习页面", "create a discussion page", "create a practice page", or wants to generate an interactive learning webpage similar to CS61A discussion materials.
version: 1.0.0
---

# Discussion Page Generator (讨论课页面生成器)

This skill generates interactive learning webpages similar to CS61A discussion sections. When the user provides a learning topic, it will automatically generate a complete HTML page with:
- Structured chapter/section organization
- Concept explanations
- Programming exercises with editable code editors (Monaco Editor)
- Solutions with collapsible sections
- Learning objectives

## When This Skill Applies

This skill activates when the user wants to:
- Generate a study/practice webpage for a specific topic
- Create interactive coding exercises
- Build a discussion-style learning page
- Get an HTML page similar to cs61a.org/disc/ format

## Input Format

When invoking this skill, provide:
- **topic**: The learning topic (e.g., "Python Functions", "Recursion", "Stack Data Structure")
- **level** (optional): Difficulty level - beginner, intermediate, or advanced
- **num_exercises** (optional): Number of exercises to generate (default: 4-6)

The page structure follows this hybrid design:
- **Theory Section**: Similar to https://www.composingprograms.com/ - comprehensive explanations with examples
- **Practice Section**: Similar to https://cs61a.org/disc/sol-disc01/ - interactive exercises with code editors

Example invocation:
```
topic: "队列(Queue)"
level: "intermediate"
num_exercises: 5
```

## Output

The skill generates a complete, self-contained HTML file that includes:
1. **Header** - Topic title and navigation
2. **Learning Objectives** - What users will learn
3. **Concept Explanation** - Theory and background
4. **Exercises** - Multiple programming problems with:
   - Problem description
   - Editable Monaco Editor for user code
   - Collapsible solution
   - Test cases (doctests)
5. **Optional: Environment Diagrams** - For applicable topics like functions/recursion
6. **Footer** - Navigation and references

## HTML Features

The generated HTML includes:
- Monaco Editor integration for Python code editing
- Syntax highlighting
- Collapsible answer sections
- Responsive sidebar navigation
- Smooth scroll navigation
- Clean academic-style design

## Usage

Simply tell me what topic you want to learn, for example:
- "帮我生成一个学习'递归'的讨论课页面"
- "生成一个Python函数练习页面"
- "Create a discussion page for Stack data structure"

I will generate a complete HTML file that you can open in your browser to practice.

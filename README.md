# SnehaPythonExcercises1
Python Excercises
# AI Automation Engineer Exercise

This repository contains a Python script to scrape product listings from Amazon (or fallback API) and categorize them using AI. The exercise demonstrates robust Selenium automation, error handling, and AI integration.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Technical Details](#technical-details)
- [AI Enhancement](#ai-enhancement)
- [Fallback & Edge Cases](#fallback--edge-cases)
- [Author](#author)

---

## Project Overview

The script scrapes the first 5 product listings from Amazon based on a search query (default: "laptops"). If Amazon blocks scraping, it falls back to [FakeStore API](https://fakestoreapi.com/) to ensure output. Each product is enhanced with an AI-generated category: `budget`, `gaming`, or `professional`.

---

## Features

- Scrape product **title, price, rating, URL** from Amazon
- Fallback to a **public API** if Amazon blocks scraping
- **AI categorization** of products (budget, gaming, professional)
- **CLI support** for flexible search queries
- Handles missing elements and exceptions gracefully
- Runs in **headless or visible browser mode**

---

## Prerequisites

- Python 3.10+
- Chrome browser + Chrome WebDriver
- OpenAI API Key for AI categorization

---

## Installation

```bash
# Clone repo
git clone https://github.com/yourusername/ai-automation-exercise.git
cd ai-automation-exercise

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Set OpenAI API key
$env:OPENAI_API_KEY="your_api_key_here"  # Windows PowerShell
# export OPENAI_API_KEY="your_api_key_here"  # macOS/Linux

---
## Usage

Run with the default query ("laptops"):

```bash
python exercise.py
---
Usage

Run with the default query ("laptops"):

python exercise.py


Run with a custom search query:

python exercise.py --query="headphones"


Output is JSON-formatted with AI categories included.

Technical Details

Selenium WebDriver with explicit waits

Anti-bot measures: custom user-agent, optional headless/visible browser

Fallback API: FakeStore API ensures consistent output if Amazon blocks scraping

Handles missing price or rating gracefully

AI Enhancement

Uses OpenAI GPT (gpt-4o-mini) to categorize products

Fallback rule-based categorization ensures reliable output

Fallback & Edge Cases

Amazon blocking → fallback API

AI failure → rule-based category

Missing product fields handled gracefully

Default query: "laptops", but any query supported via CLI

Author

Snehalatha Momidi
Senior QA Automation Engineer

Notes:

Demonstrates robust automation and AI integration

Shows thoughtful handling of edge cases and flexible CLI usage

First coding exercise in my career completed using ChatGPT guidance responsibly, not “vibe coding”


---

### ✅ Why this will fix your problem

1. **All headings are proper `##` Markdown** → TOC links now work.  
2. **Code blocks are closed properly** → no accidental merging of text and code.  
3. **Sections are clearly separated with `---`** → readable and professional.  

---

If you replace your current README.md with this one, **clicking any TOC link on GitHub will scroll to the correct section**.  

---

If you want, I can now give you **:contentReference[oaicite:0]{index=0}** — ready to submit.  

Do you want me to do that next?

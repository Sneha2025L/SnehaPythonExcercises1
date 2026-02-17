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

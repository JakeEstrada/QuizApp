# QuizApp — Command Line Quiz with Leitner System

This is a command-line quiz application built in Python that helps users study any subject using customizable multiple-choice questions. The quiz follows the Leitner System to help reinforce learning: questions you get wrong appear more frequently, while questions you master appear less often or are removed completely.

## Features

- **Leitner System-Based Learning**: Reinforces weak topics through spaced repetition.
- **Progress Tracking**: Tracks your correct/wrong answers and shows your mastery percentage.
- **Flexible Input**: Supports both number keys (1-4) and letters (a-d) for answering.
- **Clear Feedback**: Immediate feedback is shown after each answer.
- **Customizable Question Source**: Add or modify your questions using either a `questions.py` or `questions.json` file.

## Getting Started

### Prerequisites

- Python 3.x
- A terminal (Linux, macOS, or Windows with WSL or PowerShell)

### Installation

Clone the repo and set up your environment:

```bash
git clone https://github.com/JakeEstrada/QuizApp.git
cd QuizApp
python3 -m venv venv
source venv/bin/activate     # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt


## Example output

Incorrect! The correct answer was b) Manipulation of SQL queries
Correct: 4 | Wrong: 1 | Progress: 4.44% mastery

What protocol is commonly used for network file transfers?
1) a) HTTP
2) b) FTP
3) c) SSH
4) d) IPX

Your answer (1-4, a-d), or '0' to exit:

## Example Customized Question file

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["a) Berlin", "b) Paris", "c) Rome", "d) Madrid"],
        "answer": "b"
    },
    ...
]


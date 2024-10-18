# Cyber Security Quiz Application

This is a command-line quiz application built in Python that helps users study cyber security topics and legal articles. The quiz follows the Leitner System to help users reinforce learning by prioritizing questions that need more practice. Once a user demonstrates mastery by answering correctly multiple times, the quiz stops showing those questions. The app keeps track of the user's progress, including the percentage of questions mastered and a tally of correct and incorrect answers. 

## Features

- **Leitner System-Based Learning**: Questions are asked more frequently if you answer them incorrectly and less frequently if you answer them correctly.
- **Progress Tracking**: Track your progress with a percentage of questions mastered.
- **Flexible Input**: Answer with either numeric (1-4) or letter (a-d) input.
- **Clear Feedback**: After each answer, the system clears the screen and shows whether you were right or wrong, along with the correct answer.
- **Customizable**: You can add or modify questions by editing a separate `questions.py` file.
- **Legal Articles Included**: The app includes questions based on various legal articles related to cybercrime.

## Getting Started

### Prerequisites

- Python 3.x
- An environment where you can run terminal commands (Linux, macOS, or WSL on Windows)

### Installation - **Clone the Repository**:

```bash
git clone https://github.com/your-username/cyber-security-quiz.git
cd cyber-security-quiz
```

### Set up your environment


```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Running the quiz 

Navigate to the file directoru that you cloned the repo to

```bash
python3 review.py
```


### Example (this is what it looks like in your terminal)

```
Correct: 5 | Wrong: 2

Which of the following is an offense related to 'Child Pornography' in cybercrime?
1) a) Offering or distributing child pornography
2) b) Unauthorized access to child data
3) c) Manipulating data to create false records
4) d) Disrupting child services through DDoS

Your answer (1-4, a-d), or '0' to exit: 1
Correct!

```


### Reusing the source code for the Future ! 

Hey, you dont need to just study these cyber 101 topics. It is easy to just create your own questions and definitions. 

```
questions = [
    {
        "question": "*** Put your question in here *** ?",
        "options": ["a) Answer1", "b) Answer2", 
                    "c) Answer3", "d) Answer4"],
        "answer": "a"  #or whichever is the correct answer
    },
    {
	"question": "*** Put your question in here *** ?",
        "options": ["a) Answer1", "b) Answer2", 
                    "c) Answer3", "d) Answer4"],
        "answer": "a"  #or whichever is the correct answer
    }]
```

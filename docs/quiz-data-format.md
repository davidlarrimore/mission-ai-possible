# Quiz Data Format - Documentation

## Overview

This is a simplified, focused quiz format for the Mission: AI Possible training program. The format is designed to be easy to work with while supporting the essential features needed for educational quizzes.

## File Structure

```
├── quiz_schema.json     # JSON Schema definition
├── week_1_quiz.json     # Example quiz data (Week 1)
└── README.md            # This file
```

## Data Structure

### Top Level

```json
{
  "title": "Fundamentals of AI",
  "week": 1,
  "overview": { ... },
  "questions": [ ... ]
}
```

### Overview Section

Contains the quiz description and learning context:

```json
{
  "overview": {
    "description": "What this quiz covers",
    "learningObjectives": [
      "What participants will learn",
      "Key concepts covered"
    ],
    "prerequisites": [
      "Required knowledge before taking quiz"
    ]
  }
}
```

### Question Structure

Each question has:
- **id**: Question number (1, 2, 3, etc.)
- **type**: Either "multiple-choice" or "true-false"
- **text**: The question text
- **options**: Array of possible answers
- **references**: Supporting materials specific to this question

```json
{
  "id": 1,
  "type": "multiple-choice",
  "text": "What is AI?",
  "options": [
    {
      "label": "A",
      "text": "Option text",
      "isCorrect": false
    },
    {
      "label": "B",
      "text": "Correct option",
      "isCorrect": true,
      "reasoning": "Why this is the correct answer"
    }
  ],
  "references": [
    {
      "title": "Reference Title",
      "url": "https://example.com",
      "description": "What this reference provides"
    }
  ]
}
```

### Option Structure

Each option includes:
- **label**: Display label (A, B, C, D for multiple choice; True/False for boolean)
- **text**: The option text
- **isCorrect**: Boolean indicating if this is the correct answer
- **reasoning**: (Only for correct answers) Explanation of why this is correct

**Important**: The `reasoning` field is only included for the correct answer. This explains why that option is the right choice.

### References

Each question can have specific reference materials:

```json
{
  "references": [
    {
      "title": "IBM Deep Blue History",
      "url": "https://www.ibm.com/history/deep-blue",
      "description": "Official IBM page documenting Deep Blue's development"
    }
  ]
}
```

References are curated resources that:
- Support the question's topic
- Provide authoritative information
- Help learners understand the concept better

## Question Types

### Multiple Choice
- 2-4 options labeled A, B, C, D
- Exactly one correct answer
- Reasoning provided for correct answer

### True/False
- Two options labeled "True" and "False"
- Boolean question format
- Reasoning provided for correct answer

## Usage Examples

### Loading Quiz Data

```javascript
// JavaScript/Node.js
const quiz = require('./week_1_quiz.json');
console.log(quiz.title);        // "Fundamentals of AI"
console.log(quiz.week);          // 1
console.log(quiz.questions.length); // 10
```

```python
# Python
import json

with open('week_1_quiz.json', 'r') as f:
    quiz = json.load(f)

print(quiz['title'])      # "Fundamentals of AI"
print(quiz['week'])       # 1
print(len(quiz['questions']))  # 10
```

### Accessing Question Data

```javascript
// Get first question
const question = quiz.questions[0];

console.log(question.text);     // Question text
console.log(question.type);     // "multiple-choice"

// Get correct answer
const correctOption = question.options.find(opt => opt.isCorrect);
console.log(correctOption.label);     // "D"
console.log(correctOption.reasoning); // Why it's correct
```

### Checking User Answers

```javascript
function checkAnswer(questionId, userAnswer) {
  const question = quiz.questions.find(q => q.id === questionId);
  const correct = question.options.find(opt => opt.isCorrect);
  
  return {
    correct: correct.label === userAnswer,
    explanation: correct.reasoning,
    references: question.references
  };
}

// Usage
const result = checkAnswer(2, "C");
console.log(result.correct);      // true/false
console.log(result.explanation);  // Reasoning for correct answer
```

### Displaying Questions in UI

```javascript
// Render a question
function renderQuestion(question) {
  return `
    <div class="question">
      <h3>Question ${question.id}</h3>
      <p>${question.text}</p>
      <div class="options">
        ${question.options.map(opt => `
          <label>
            <input type="radio" name="q${question.id}" value="${opt.label}">
            ${opt.label}. ${opt.text}
          </label>
        `).join('')}
      </div>
    </div>
  `;
}
```

## Best Practices

### Content Creation

1. **Clear Questions**: Write unambiguous questions that test one concept
2. **Quality Options**: Make incorrect options plausible but clearly wrong
3. **Helpful Reasoning**: Provide educational explanations, not just "it's correct"
4. **Relevant References**: Link to authoritative, helpful resources

### Technical Implementation

1. **Validate Structure**: Use the JSON schema to validate quiz files
2. **Secure Answers**: Don't send correct answers to client until after submission
3. **Track Progress**: Store user answers and calculate scores server-side
4. **Show References**: Display references after answering to encourage learning

### Question Writing Tips

**Good Question:**
```json
{
  "text": "Which system defeated Garry Kasparov in 1997?",
  "reasoning": "IBM Deep Blue defeated Kasparov in May 1997 in a six-game match, marking a significant milestone in AI history."
}
```

**Avoid:**
- Double negatives: "Which is NOT incorrect?"
- Trick questions: "Which is false about X? (Choose the true statement)"
- Ambiguous wording: "Some say that..."

## Validation

Validate your quiz data against the schema:

```bash
# Using ajv-cli
ajv validate -s quiz_schema.json -d week_1_quiz.json
```

```javascript
// Using JavaScript
const Ajv = require('ajv');
const ajv = new Ajv();

const schema = require('./quiz_schema.json');
const quiz = require('./week_1_quiz.json');

const valid = ajv.validate(schema, quiz);
if (!valid) {
  console.error(ajv.errors);
}
```

## Creating New Quizzes

1. Copy `week_1_quiz.json` as a template
2. Update the title and week number
3. Update overview section
4. Replace questions with your content
5. Research and add appropriate references for each question
6. Validate against the schema

### Template

```json
{
  "title": "Your Quiz Title",
  "week": 2,
  "overview": {
    "description": "What this quiz covers",
    "learningObjectives": [
      "Objective 1",
      "Objective 2"
    ],
    "prerequisites": [
      "Week 1 completion"
    ]
  },
  "questions": [
    {
      "id": 1,
      "type": "multiple-choice",
      "text": "Your question?",
      "options": [
        {
          "label": "A",
          "text": "First option",
          "isCorrect": false
        },
        {
          "label": "B",
          "text": "Correct option",
          "isCorrect": true,
          "reasoning": "Why this is correct"
        }
      ],
      "references": [
        {
          "title": "Reference",
          "url": "https://...",
          "description": "What this covers"
        }
      ]
    }
  ]
}
```

## Integration with Applications

### Basic Quiz Flow

1. Load quiz data
2. Display questions one at a time
3. Collect user answers
4. Calculate score
5. Show results with reasoning and references

### Scoring

```javascript
function calculateScore(quiz, userAnswers) {
  let correct = 0;
  
  quiz.questions.forEach(question => {
    const userAnswer = userAnswers[question.id];
    const correctOption = question.options.find(opt => opt.isCorrect);
    
    if (userAnswer === correctOption.label) {
      correct++;
    }
  });
  
  return {
    correct,
    total: quiz.questions.length,
    percentage: (correct / quiz.questions.length) * 100
  };
}
```

### Showing Results

```javascript
function showResults(quiz, userAnswers) {
  return quiz.questions.map(question => {
    const userAnswer = userAnswers[question.id];
    const correctOption = question.options.find(opt => opt.isCorrect);
    const isCorrect = userAnswer === correctOption.label;
    
    return {
      id: question.id,
      question: question.text,
      userAnswer,
      correct: isCorrect,
      correctAnswer: correctOption.label,
      explanation: correctOption.reasoning,
      references: question.references
    };
  });
}
```

## File Format

- **Encoding**: UTF-8
- **Format**: JSON
- **Indentation**: 2 spaces
- **Line Endings**: LF (Unix style)

## Version Control

When updating quizzes:
1. Keep question IDs stable
2. Document changes in commit messages
3. Version the content (Week 1 v1.0, v1.1, etc.)
4. Test thoroughly after changes

## Support

For questions or issues:
- Review this documentation
- Check the JSON schema for validation rules
- Examine the Week 1 quiz as an example

## License

Internal use for Amivero Mission: AI Possible training program.

---

**Version**: 1.0
**Last Updated**: December 2024
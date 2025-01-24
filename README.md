## Quiz Insights and Recommendations

This project is designed to analyze quiz performance data, generate actionable insights and recommendations, and define a learner's persona based on their performance. It leverages Python for data processing, visualization, and insights generation.

### Table of Contents

- [Project Overview](#Project-Overview)
- [Setup Instructions](#Setup-Instructions)
- [Approach Description](#Approach-Description)
- [Visualizations and Insights](#Visualizations-and-Insights)


### Project Overview

The Quiz Insights and Recommendations application analyzes a student's quiz submissions, compares them with historical data, and provides:

1. Insights into strengths and weaknesses.
2. Recommendations for improvement.
3. A persona definition based on current performance.
4. Visualizations for easy understanding of the results.

The app supports structured data inputs, processes performance by topics and difficulty levels, and outputs valuable recommendations to help students improve.

### Setup Instructions

Follow these steps to set up and run the project:

#### Prerequisites

Ensure you have Python 3.8 or higher installed along with the following libraries:

- matplotlib
- seaborn
- requests

#### Installation

1. Clone the repository:

```
git clone https://github.com/your-username/quiz-insights.git
cd quiz-insights
```

2. Install required dependencies:

```
pip install -r requirements.txt
```

3. Place the input files (current_quiz.json and quiz_submission.json) in the project directory.

#### Running the Application

Run the following command to start the app:

```
python app.py
```

### Approach Description

The project workflow is divided into the following key steps:

1. Data Ingestion
- Load the current quiz and submission data from JSON files.
- Fetch historical quiz data from an external API.
2. Performance Analysis
- Analyze topic-wise accuracy using historical and current quiz data.
- Measure overall accuracy and difficulty-level performance.
3. Generate Insights and Recommendations
- Identify weak topics and difficulty levels to suggest areas of focus.
- Provide recommendations for improvement based on accuracy.
4. Define Student Persona
- Classify the learner as a "Beginner," "Specialist," or "Consistent Performer."
- Highlight strong and weak topics for personalized feedback.
5. Visualization
- Create a bar chart showing topic-wise accuracy.
- Generate a pie chart to visualize the percentage of correct and incorrect answers.


### Visualizations and Insights

#### Key Visualizations

1. Topic-Wise Performance
2. Current Quiz Accuracy

#### Example Insights

1. "Focus on the following weak topics: Algebra, Trigonometry."
2. "Your overall accuracy is 68.5%. Keep improving!"

#### Example Recommendations

1. "Practice more questions on Geometry and Probability."
2. "Work on questions at the 'Hard' difficulty level to improve your performance."

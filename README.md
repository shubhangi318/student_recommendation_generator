# Student Quiz Performance Insights

## Overview
This project analyzes quiz performance data to generate insights, recommendations, and a student persona. It ingests quiz performance data from two sources:

- **current_quiz.json**: Contains the details of the quiz, including topics and question difficulty.
- **quiz_submission.json**: Contains student responses to the quiz.

Based on this data, the application analyzes the student's performance, provides personalized insights, generates recommendations, and visualizes the performance data. 

## Setup Instructions

### Prerequisites

Ensure you have Python 3.7+ installed. You'll also need to install the required dependencies listed in the `requirements.txt` file.

### Steps

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have the required input files:
   - `current_quiz.json`
   - `quiz_submission.json`

4. Run the application:

    ```bash
    python app.py
    ```

The app will process the data and display insights, recommendations, and the student persona, along with visualizations.

## Project Approach

### Data Ingestion
The project loads two data sources:
- `current_quiz.json`: Contains details about the quiz, including topics, questions, and difficulty levels.
- `quiz_submission.json`: Contains the student's responses to the quiz.

Additionally, historical data is fetched from an API (`https://api.jsonserve.com/XgAgFJ`) to analyze past performance.

### Data Analysis
The data is analyzed in several ways:
1. **Topic Performance**: Measures the student's accuracy for each topic based on historical data.
2. **Current Accuracy**: Compares the student's responses to the correct answers and calculates their overall accuracy.
3. **Difficulty Performance**: Analyzes performance by question difficulty and provides insights on areas that need improvement.

### Insights and Recommendations
Based on the performance data, the application generates:
- **Insights**: Identifies weak topics, areas of difficulty, and provides suggestions for improvement.
- **Recommendations**: Suggests practice topics, improvement strategies for weak areas, and focuses on specific difficulty levels.

### Persona Definition
The student's performance is used to categorize them into one of three personas:
- **The Consistent Performer**: High and consistent performance across topics.
- **The Specialist**: Strong performance in specific areas but weaker overall.
- **The Beginner**: Low overall performance, but potential for growth with practice.

### Visualizations
The application generates the following visualizations:
1. **Topic-wise Performance**: A bar chart visualizing the student's performance across different topics.
2. **Quiz Accuracy**: A pie chart showing the percentage of correct and incorrect answers.

### Creative Insights
The application also provides personalized feedback based on the student's persona, offering creative insights like:
- **The Consistent Performer**: Encouragement to continue performing well.
- **The Specialist**: Suggestions to broaden focus and work on weaker areas.
- **The Beginner**: Advice to practice consistently to improve.

## Key Visualizations

1. **Topic-wise Performance**
   - A bar chart shows the accuracy percentage for each quiz topic.
   
   ![Topic-wise Performance](topic_performance_chart.png)

2. **Quiz Accuracy**
   - A pie chart visualizes the overall accuracy, highlighting the percentage of correct and incorrect answers.
   
   ![Quiz Accuracy](accuracy_pie_chart.png)

## Insights Summary
The analysis generates several key insights:
- **Weak Topics**: Identifies topics where the student needs to improve.
- **Accuracy**: Provides the overall accuracy of the student, encouraging improvement.
- **Difficulty Levels**: Suggests which difficulty levels the student should focus on based on performance.

### Example Output
After running the application, you will see results like the following:

--- Insights ---

- Focus on the following weak topics: Algebra, Geometry.
- Your overall accuracy is 65.00%. Keep improving!
- Pay extra attention to questions with difficulty 'Hard', as your accuracy is only 55.00%.
  
--- Recommendations ---

- Practice more questions on: Algebra, Geometry.
- Aim to improve your overall accuracy, which is currently 65.00%. Start by revisiting incorrect answers.
- Work on questions at the 'Hard' difficulty level to improve your performance.
  
--- Persona --- 

- Persona: The Beginner Weak Topics: Algebra, Geometry

--- Creative Insights ---

- You are just starting out. Consistent practice will help you improve.
- Work on improving these weak topics: Algebra, Geometry.


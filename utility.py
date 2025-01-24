import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import json
import requests

# Data Ingestion
def load_json_file(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def fetch_historical_data(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"API Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Data Analysis
def analyze_performance(current_quiz, submission, historical_data):
    topic_accuracy = defaultdict(list)
    for record in historical_data:
        topic = record['quiz']['topic']
        accuracy = float(record['accuracy'].strip('%'))
        topic_accuracy[topic].append(accuracy)

    topic_performance = {k: sum(v) / len(v) for k, v in topic_accuracy.items()}

    correct_ids = {opt["id"] for q in current_quiz["quiz"]["questions"] for opt in q["options"] if opt["is_correct"]}
    submitted_responses = submission["response_map"]
    correct_responses = sum(1 for q_id, ans_id in submitted_responses.items() if ans_id in correct_ids)
    total_questions = current_quiz["quiz"]["questions_count"]
    current_accuracy = (correct_responses / total_questions) * 100

    difficulty_analysis = defaultdict(list)
    for question in current_quiz["quiz"]["questions"]:
        level = question.get("difficulty_level", "Unknown")
        is_correct = submitted_responses.get(str(question["id"])) in correct_ids
        difficulty_analysis[level].append(1 if is_correct else 0)

    difficulty_performance = {k: (sum(v) / len(v)) * 100 for k, v in difficulty_analysis.items()}

    return topic_performance, current_accuracy, difficulty_performance, correct_ids

# Generate Insights and Recommendations
def generate_insights(topic_performance, current_accuracy, difficulty_performance):
    insights = []

    weak_topics = [topic for topic, acc in topic_performance.items() if acc < 70]
    if weak_topics:
        insights.append(f"Focus on the following weak topics: {', '.join(weak_topics)}.")

    insights.append(f"Your overall accuracy is {current_accuracy:.2f}%. Keep improving!")

    for level, acc in difficulty_performance.items():
        if acc < 70:
            insights.append(f"Pay extra attention to questions with difficulty '{level}', as your accuracy is only {acc:.2f}%.")

    return insights

def generate_recommendations(topic_performance, current_accuracy, difficulty_performance):
    recommendations = []

    weak_topics = [topic for topic, acc in topic_performance.items() if acc < 70]
    if weak_topics:
        recommendations.append(f"Practice more questions on: {', '.join(weak_topics)}.")

    if current_accuracy < 75:
        recommendations.append(f"Aim to improve your overall accuracy, which is currently {current_accuracy:.2f}%. Start by revisiting incorrect answers.")

    for level, acc in difficulty_performance.items():
        if acc < 70:
            recommendations.append(f"Work on questions at the '{level}' difficulty level to improve your performance.")

    return recommendations

# Persona Definition
def define_student_persona(topic_performance, difficulty_performance, current_accuracy):
    if current_accuracy >= 80:
        persona = "The Consistent Performer"
    elif current_accuracy < 50:
        persona = "The Beginner"
    else:
        persona = "The Specialist"

    strong_topics = [topic for topic, acc in topic_performance.items() if acc >= 80]
    weak_topics = [topic for topic, acc in topic_performance.items() if acc < 50]

    strong_levels = [level for level, acc in difficulty_performance.items() if acc >= 80]
    weak_levels = [level for level, acc in difficulty_performance.items() if acc < 50]

    return {
        "persona": persona,
        "strong_topics": strong_topics,
        "weak_topics": weak_topics,
        "strong_levels": strong_levels,
        "weak_levels": weak_levels
    }

# Visualization
def create_visualizations(topic_performance, difficulty_performance, current_accuracy, submitted_responses, total_questions, correct_ids):
    topics = list(topic_performance.keys())
    accuracies = list(topic_performance.values())

    plt.figure(figsize=(10, 6))
    sns.barplot(x=topics, y=accuracies, palette="coolwarm")
    plt.title("Topic-wise Performance")
    plt.xlabel("Topics")
    plt.ylabel("Accuracy (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    correct_answers = sum(1 for q_id, ans_id in submitted_responses.items() if ans_id in correct_ids)
    incorrect_answers = total_questions - correct_answers
    accuracy_data = [correct_answers, incorrect_answers]

    plt.figure(figsize=(7, 7))
    plt.pie(accuracy_data, labels=["Correct", "Incorrect"], autopct="%1.1f%%", colors=["#4CAF50", "#FF5733"], startangle=90)
    plt.title(f"Current Quiz Accuracy: {current_accuracy:.2f}%")
    plt.axis("equal")
    plt.show()

# Creative Insights
def creative_insights(persona_summary):
    insights = []

    if persona_summary["persona"] == "The Consistent Performer":
        insights.append("You are a consistent high performer. Keep up the great work!")
    elif persona_summary["persona"] == "The Specialist":
        insights.append("You excel in specific areas. Expand your focus to become a more balanced learner.")
    elif persona_summary["persona"] == "The Beginner":
        insights.append("You are just starting out. Consistent practice will help you improve.")

    if persona_summary["strong_topics"]:
        insights.append(f"Your strongest topics are: {', '.join(persona_summary['strong_topics'])}.")
    if persona_summary["weak_topics"]:
        insights.append(f"Work on improving these weak topics: {', '.join(persona_summary['weak_topics'])}.")

    return insights

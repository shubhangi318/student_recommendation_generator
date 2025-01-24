from utility import (
    load_json_file,
    fetch_historical_data,
    analyze_performance,
    generate_insights,
    generate_recommendations,
    define_student_persona,
    create_visualizations,
    creative_insights,
)

def main():
    # Load data
    current_quiz = load_json_file("current_quiz.json")
    submission = load_json_file("quiz_submission.json")
    historical_data = fetch_historical_data("https://api.jsonserve.com/XgAgFJ")

    # Analyze data
    topic_performance, current_accuracy, difficulty_performance, correct_ids = analyze_performance(
        current_quiz, submission, historical_data
    )

    # Generate insights and recommendations
    insights = generate_insights(topic_performance, current_accuracy, difficulty_performance)
    recommendations = generate_recommendations(topic_performance, current_accuracy, difficulty_performance)

    # Define persona
    persona_summary = define_student_persona(topic_performance, difficulty_performance, current_accuracy)

    # Visualizations
    create_visualizations(topic_performance, difficulty_performance, current_accuracy, submission["response_map"], current_quiz["quiz"]["questions_count"], correct_ids)

    # Display results
    print("\n--- Insights ---")
    for insight in insights:
        print(f"- {insight}")

    print("\n--- Recommendations ---")
    for recommendation in recommendations:
        print(f"- {recommendation}")

    print("\n--- Persona ---")
    print(f"Persona: {persona_summary['persona']}")
    if persona_summary["strong_topics"]:
        print(f"Strong Topics: {', '.join(persona_summary['strong_topics'])}")
    if persona_summary["weak_topics"]:
        print(f"Weak Topics: {', '.join(persona_summary['weak_topics'])}")

    creative_labels = creative_insights(persona_summary)
    print("\n--- Creative Insights ---")
    for label in creative_labels:
        print(f"- {label}")

if __name__ == "__main__":
    main()

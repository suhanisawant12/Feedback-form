
import streamlit as st
import csv
import os
from datetime import datetime

st.set_page_config(
    page_title="College Campus Feedback",
    page_icon="🏫",
    layout="centered"
)

st.title("🏫 College Campus Feedback Form")
st.write(
    "Help us improve our campus! Share your experience "
    "and suggestions about college facilities."
)

st.info("Your feedback helps us make our campus better.")

with st.form("campus_feedback_form"):

    st.subheader("Student Information")

    name = st.text_input("Student Name")
    department = st.selectbox(
        "Department",
        ["Computer Science", "IT", "Electronics",
         "Mechanical", "Civil", "Electrical", "Other"]
    )
    year = st.selectbox(
        "Year of Study",
        ["First Year", "Second Year",
         "Third Year", "Fourth Year"]
    )

    st.divider()
    st.subheader("Rate Campus Facilities")

    facilities = [
        "Classrooms",
        "Laboratories",
        "Library",
        "Wi-Fi and Internet",
        "Canteen and Food Quality",
        "Drinking Water",
        "Washrooms and Cleanliness",
        "Sports and Playground",
        "Parking Facilities",
        "College Campus Cleanliness",
        "Seating and Common Areas",
        "Security and Safety",
        "College Transport",
        "Electricity and Fans",
        "Medical and First Aid"
    ]

    ratings = {}

    for facility in facilities:
        ratings[facility] = st.select_slider(
            facility,
            options=[
                "Poor",
                "Needs Improvement",
                "Average",
                "Good",
                "Excellent"
            ],
            value="Average",
            key=facility
        )

    st.divider()
    st.subheader("Overall Experience")

    overall_rating = st.slider(
        "Overall campus satisfaction (1 = Very Poor, 5 = Excellent)",
        min_value=1,
        max_value=5,
        value=3
    )

    best_facility = st.selectbox(
        "Which facility do you like the most?",
        facilities
    )

    improvement = st.multiselect(
        "Which facilities need improvement?",
        facilities
    )

    st.subheader("Suggestions")

    comments = st.text_area(
        "Your suggestions or complaints",
        placeholder="Tell us what should be improved..."
    )

    submitted = st.form_submit_button(
        "Submit Feedback",
        use_container_width=True
    )

if submitted:

    if not name.strip():
        st.error("Please enter your name.")

    else:
        file_name = "campus_feedback.csv"
        file_exists = os.path.exists(file_name)

        with open(
            file_name, "a", newline="", encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            if not file_exists or os.path.getsize(file_name) == 0:
                writer.writerow([
                    "Date and Time",
                    "Student Name",
                    "Department",
                    "Year",
                    "Facility Ratings",
                    "Overall Rating",
                    "Best Facility",
                    "Facilities to Improve",
                    "Suggestions"
                ])

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                name,
                department,
                year,
                "; ".join(
                    f"{facility}: {rating}"
                    for facility, rating in ratings.items()
                ),
                overall_rating,
                best_facility,
                "; ".join(improvement),
                comments
            ])

        st.success("Thank you! Your campus feedback has been recorded.")
        st.balloons()

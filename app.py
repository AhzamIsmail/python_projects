import streamlit as st
import random
from datetime import datetime

# Title of the app
st.title("🌱 Growth Mindset Tracker")

# Motivational Quotes
quotes = [
    
    "So be patient. Indeed, the promise of Allah is truth. – Quran (30:60)",
    "Verily, with hardship comes ease. – Quran (94:6)",
    "Allah does not burden a soul beyond that it can bear. – Quran (2:286)",
    "Indeed, Allah will not change the condition of a people until they change what is in themselves. – Quran (13:11)",
    "Do not lose hope, nor be sad. – Quran (3:139)",
    "If you are grateful, I will surely increase you [in favor]. – Quran (14:7)",
    "The strong believer is better and more beloved to Allah than the weak believer, while there is good in both. – Prophet Muhammad (ﷺ)",
    "Take benefit of five before five: Your youth before your old age, your health before your sickness, your wealth before your poverty, your free time before you are preoccupied, and your life before your death. – Prophet Muhammad (ﷺ)",
    "And whoever relies upon Allah – then He is sufficient for him. – Quran (65:3)",
    "The most beloved deeds to Allah are those that are consistent, even if they are small. – Prophet Muhammad (ﷺ)"
]

# Display a random quote
st.subheader("💡 Today's Motivational Quote")
st.write(random.choice(quotes))

# Daily Goal Setting
st.subheader("🎯 Set Your Daily Goal")
goal = st.text_input("What’s your growth mindset goal for today?")

if st.button("Save Goal"):
    if goal:
        with open("goals.txt", "a") as f:
            f.write(f"{datetime.today().strftime('%Y-%m-%d')}: {goal}\n")
        st.success("Goal saved! You’ve got this! 💪")
    else:
        st.warning("Please enter a goal.")

# Progress Tracker
st.subheader("📊 Your Progress")
try:
    with open("goals.txt", "r") as f:
        goals = f.readlines()
    if goals:
        st.write("Here are your saved goals:")
        for goal in goals:
            st.write(f"- {goal.strip()}")
    else:
        st.write("No goals saved yet. Start by setting a goal above!")
except FileNotFoundError:
    st.write("No goals saved yet. Start by setting a goal above!")

# Reflection Journal
st.subheader("📔 Daily Reflection")
reflection = st.text_area("How did you grow today? Write a short reflection:")

if st.button("Save Reflection"):
    if reflection:
        with open("reflections.txt", "a") as f:
            f.write(f"{datetime.today().strftime('%Y-%m-%d')}: {reflection}\n")
        st.success("Reflection saved! Great job reflecting on your growth. 🌟")
    else:
        st.warning("Please write a reflection.")
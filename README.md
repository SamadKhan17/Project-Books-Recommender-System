# Project-Recommender-System


This project builds a book recommendation system that suggests books to users based on their previous preferences and ratings. The system is implemented using machine learning techniques and is deployed via Streamlit.

#Project Overview

This project aims to develop a recommendation system that suggests books by identifying similar users based on their rating history. The model utilizes both explicit and implicit feedback to generate personalized recommendations. The dataset consists of anonymized user IDs, book details, and user ratings.

#Business Objective

The goal is to generate features from the dataset and recommend books to users by finding users with similar preferences, thereby improving the system's performance. The final model is deployed using Streamlit for easy accessibility and interaction.

#Dataset Details

The dataset consists of three main components:

Users: Contains anonymized user IDs along with demographic data (like location and age), though some fields may be null.

Books: Identified using ISBN numbers.

Ratings: Includes both explicit ratings (on a scale from 1 to 10) and implicit feedback (0 for no explicit rating).

#Model Building

The project involves the following steps:

Exploratory Data Analysis (EDA): Understand the dataset, handle missing values, and generate relevant features.
Model Training:

Collaborative Filtering (User-User): Uses cosine similarity to find users with similar rating patterns and provide recommendations based on similar users’ preferences.

Content-based Filtering: Recommends books with similar content to those the user has rated highly.

Model Evaluation: Performance metrics are used to assess accuracy and refine the model.

#Deployment

The system is deployed using Streamlit. It offers a user-friendly interface where users can input their preferences and receive personalized book recommendations in real-time.

#Acceptance Criteria

The model should deliver high-performance recommendations. The deployment should be user-friendly and efficient, using Streamlit.

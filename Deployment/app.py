import streamlit as st
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# Load the data
books = pd.read_csv('Books.csv')
ratings = pd.read_csv('Ratings.csv')
users = pd.read_csv('Users.csv')

# Filtering the data to include only users who have rated at least 50 books
user_counts = ratings['User-ID'].value_counts()
active_users = user_counts[user_counts >= 50].index
ratings = ratings[ratings['User-ID'].isin(active_users)]

# Similarly, filtering the data to include only books that have been rated at least 50 times
book_counts = ratings['ISBN'].value_counts()
popular_books = book_counts[book_counts >= 50].index
ratings = ratings[ratings['ISBN'].isin(popular_books)]

# Merge ratings with book titles using ISBN
ratings_with_name = ratings.merge(books, on='ISBN')

# Creating a sparse pivot table 
user_book_matrix = ratings_with_name.pivot_table(index='User-ID', columns='Book-Title', values='Book-Rating').fillna(0)
sparse_user_book_matrix = csr_matrix(user_book_matrix.values)

# Standardizing the data 
scaler = StandardScaler(with_mean=False)
sparse_user_book_matrix_standardized = scaler.fit_transform(sparse_user_book_matrix)

# Calculate the cosine similarity on sparse standardized matrix
similarity_scores = cosine_similarity(sparse_user_book_matrix_standardized)

def recommend(user_id, num_recommendations=5):
    if user_id not in user_book_matrix.index:
        return f"User ID {user_id} not found in the dataset."
    
    index = np.where(user_book_matrix.index == user_id)[0][0]
    similar_users = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
    
    recommended_books = []
    for user in similar_users:
        similar_user_id = user_book_matrix.index[user[0]]
        user_books = ratings_with_name[ratings_with_name['User-ID'] == similar_user_id]['Book-Title'].unique()
        
        for book in user_books:
            if book not in recommended_books:
                recommended_books.append(book)
                if len(recommended_books) >= num_recommendations:
                    break
        if len(recommended_books) >= num_recommendations:
            break
    
    return recommended_books

# Streamlit app Title
st.title('Book Recommendation System')

# Display available User IDs
active_user_ids = ratings['User-ID'].unique()
st.write("Available User IDs:")
st.write(active_user_ids)

# Take User ID as input
user_id = st.number_input('Enter User ID', min_value=int(active_user_ids.min()), max_value=int(active_user_ids.max()))

if st.button('Recommend'):
    recommendations = recommend(user_id)
    if isinstance(recommendations, list):
        st.write(f"Top {len(recommendations)} recommendations for User {user_id}:")
        for book in recommendations:
            # Display the book title and image
            book_info = books[books['Book-Title'] == book].iloc[0]
            st.image(book_info['Image-URL-M'], width=100, caption=book)
            st.write(f"Author: {book_info['Book-Author']}")
    else:
        st.write(recommendations)
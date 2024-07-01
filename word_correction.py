"""
A simple Word Correction App using Levenshtein Distance Algorithm.
"""

from levenshtein import *
import streamlit as st


def main():
    """
    Main UI function.
    """
    vocab = load_vocab("data/vocab.txt")
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input("Enter a word")

    if st.button("Correct"):
        all_distances = levenshtein_all_vocab(word, vocab)
        closest_word = next(iter(all_distances))
        st.write(f"Closest Word: {closest_word}")

        col1, col2 = st.columns(2)

        with col1:
            st.write("Vocabulary:")
            st.write({i: words for i, words in enumerate(vocab)})

        with col2:
            st.write("Levenshtein Distances:")
            st.write(all_distances)


if __name__ == "__main__":
    main()

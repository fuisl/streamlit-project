"""
Simple object detection using OpenCV
"""

from dnn import *
import numpy as np
from PIL import Image
import streamlit as st


def main():
    """
    Main function of the app
    """

    st.title("Object detection for Images")
    file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    if file is not None:
        st.image(file, caption="Uploaded Image")

        image = np.array(Image.open(file))
        detection = process_img(image)
        annotated_image = annotate_img(image, detection)
        st.image(annotated_image, caption="Processed Image")


if __name__ == "__main__":
    main()

import easyocr as ocr
import streamlit as st
from PIL import Image
import numpy as np

# Установка ширины страницы Streamlit
st.set_page_config(layout="wide")

# Заголовок приложения
st.title("Read Text from Photo")

# Загрузка модели OCR
@st.cache_data
def load_model():
    reader = ocr.Reader(['ru', 'en'], model_storage_directory='.')
    return reader

reader = load_model()

# Загрузка изображения
image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

if image is not None:
    input_image = Image.open(image)

    # Отображение изображения
    st.image(input_image)

    # Использование OCR для чтения текста
    with st.spinner("Loading..."):
        result = reader.readtext(np.array(input_image))
        result_text = "\n".join([text[1] for text in result])
        st.text(result_text)

    st.success("Text extraction completed")
else:
    st.write("Upload an Image")

# Добавление подписи
st.caption("Made with Streamlit")

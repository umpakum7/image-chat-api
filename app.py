import streamlit as st
import google.generativeai as gemini
from PIL import Image
gemini.configure(api_key="AIzaSyAQ0QcV7MFLZTMV7P5K0vxgk6E_bmP8Bb4")

def get_response(input, image):
    model = gemini.GenerativeModel("gemini-2.0-flash")
    if input != "":
        response = model.generate_content([input,image])
    else:
        input = "이미지 설명:"
        response = model.generate_content([input, image])
    return response.text

def main():
    st.title("Image AI Chatbot")
    st.write("이미지와 질무을 올려보세요")

    capture = st.radio("모드 선택", ("cam", "upload"))

    if capture == "cam":
        img = st.camera_input(label="", key = "cam")

        if img is not None:
            image = Image.open(img)
            st.image(image, caption="cam")
    else:
        upload = st.file_uploader("upload img", type=["jpg", "jpeg", "png"])
        if upload is not None:
            image = Image.open(upload)
            st.image(image, caption="upload")

    input = st.text_input("input prompt:", key = "input")
    submit = st.button("Response******")

    if submit:
        response = get_response(input,image)
        st.subheader("Response")
        st.write(response)

if __name__ == "__main__":
    main()

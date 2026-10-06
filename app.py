import streamlit as st
from PIL import Image
from transformers import pipeline

st.title("🩺 Multimodal Healthcare Assistant")
st.write("Upload a medical image and type your symptoms below!")

# 1. Create a file uploader for pictures
uploaded_file = st.file_uploader("Choose a medical image...", type=["jpg", "jpeg", "png"])

# 2. Create a text box for symptoms
user_symptoms = st.text_input("Describe your symptoms:", "e.g., Rash appeared 3 days ago and feels itchy.")

# 3. Always show the button so you can see it right away!
if st.button("Generate Preliminary Report"):
    if uploaded_file is not None:
        with st.spinner("AI is analyzing your image and symptoms... (Downloading model on first run)"):
            # Open and display the uploaded image on the website
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Medical Scan", use_container_width=True)
            
            # Load the updated image-text pipeline from Hugging Face
            captioner = pipeline("image-text-to-text", model="Salesforce/blip-image-captioning-base")
            
            # Generate description from the image
            ai_analysis = captioner(image)[0]['generated_text']
            
            # Show the final report on the screen
            st.success("Analysis Complete!")
            st.subheader("Preliminary Health Report")
            st.write(f"**Image Observations:** {ai_analysis}")
            st.write(f"**Patient Symptoms:** {user_symptoms}")
    else:
        st.warning("Please upload a medical image first before generating the report!")
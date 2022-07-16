import streamlit as st
from PIL import Image
from clf import predict
import time
st.set_option('deprecation.showfileUploaderEncoding', False)

st.title("VisualFeast Simple Image Classification App")
st.write("")
st.write("")
option = st.selectbox(
     'Choose the model you want to use?',
     ('resnet50', 'resnet101', 'densenet121','shufflenet_v2_x0_5','mobilenet_v2'))
file_up = st.file_uploader("Upload an image", type="jpg")

if file_up is not None:
    image = Image.open(file_up)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Just a second...")
    labels,fps = predict(file_up,option)

    # print out the top 5 prediction labels with scores
    st.success('successful prediction')
    for i in labels:
        st.write("Prediction (index, name)", i[0], ",   Score: ", i[1])

    # print(t2-t1)
    # st.write(float(t2-t1))
    st.write("")
    st.metric("","FPS:   "+str(fps))
from datetime import time
import time
import pandas as pd
import streamlit as  st
st.title('startup Dashboard')
st.header("i Am Learing the streamlit app")
st.subheader("Streamlit app")

st.markdown("""
            ### Top Movie Name:
            - Heropanti
                - jony liver
            - Muder
            - Bahubali
            - kaho na pyar he
            """)
st.code(
    """
    def foo(input)
        return input**2
    x=foo(input)
    """
)
st.latex('x^2+y^2+3=0')
df=pd.DataFrame({
    'name':['yash','pawan','jay'],
    'age':[22,22,22],
    'marks':[40,52,60]
})
st.dataframe(df)
st.image('yash.jpg')
st.sidebar.title("Yash Marathe")
col1,col2=st.columns(2)
with col1:
    st.image('yash.jpg')
with col2:
    st.image('yash.jpg')
st.error("you are doing the Wrong")
st.success("well done you have done write")
st.info("you are doing the Wrong")
st.warning("you are doing the Wrong")

bar=st.progress(0)
for i in range(100):
    bar.progress(i+1)
name=st.text_input("enter your name")
age=st.text_input("enter your age")
gender=st.text_input("enter your gender")
st.text(name)
st.text(age)
st.text(gender)
st.button("click button")

Email=st.text_input("Enter your Email")
Password=st.text_input("Enter your Password")

btn=st.button("Login Please")
if btn:
    if Email=='yashmarathe58@gmail.com' and Password=='1234':
        st.success("You are logged in Successfully")
    else:
        st.error("You are not logged in Successfully")
import pandas as pd
import streamlit as st
file=st.file_uploader("Upload csv File")
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())

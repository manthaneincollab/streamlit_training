import streamlit as st 
import pandas as pd
import numpy as np
import altair as alt

st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")

st.title('this is my title')

st.header('this is a simple header')
st.header('this is with divider', divider="red")

st.subheader('this is a simple subheader')
st.subheader('this is with subheader with divider', divider="red")


st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
st.divider()

st.caption("This is a string that explains something above.")

df = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
c = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write("this is an object" , c)
st.caption("A caption with _italics_ :blue[colors] and emojis :sunglasses:")
 
st.divider()

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

st.divider()
def get_user_name():
    return 'John'

# ------------------------------------------------
# Want people to see this part of the code...

def get_punctuation():
    return '!!!'

greeting = "Hi there, "
user_name = get_user_name()
punctuation = get_punctuation()

st.write(greeting, user_name, punctuation)

# ...up to here
# ------------------------------------------------

foo = 'bar'
st.write('Done!')

st.divider()

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
st.divider()
st.text("This is text\n[and more text](that's not a Markdown link).")
st.divider()
st.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)
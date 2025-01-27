import streamlit as st

import time


st.success('This is a success message!', icon="✅")

st.info('This is a purely informational message', icon="ℹ️")

st.info('This is a purely informational message', icon="ℹ️")

st.error('This is an error', icon="🚨")

e = RuntimeError("This is an exception of type RuntimeError")
st.exception(e)


progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()

st.button("Rerun")


with st.spinner('Wait for it...'):
    time.sleep(5)
st.success("Done!")

if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')


st.balloons()

st.snow()



import streamlit as st
import pandas as pd
import numpy as np
from vega_datasets import data


st.write('areachart')

chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=["col1", "col2", "col3"]
)

st.area_chart(
    chart_data,
    x="col1",
    y=["col2", "col3"],
    color=["#FF0000", "#0000FF"],  # Optional
)

st.divider()
st.write('areachart-stack')

source = data.unemployment_across_industries()

st.area_chart(source, x="date", y="count", color="series", stack="center")


st.divider()
st.write('bar_chart')

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)

st.divider()
st.write('bar_chart')

chart_data = pd.DataFrame(
    {
        "col1": list(range(20)),
        "col2": np.random.randn(20),
        "col3": np.random.randn(20),
    }
)

st.bar_chart(
    chart_data,
    x="col1",
    y=["col2", "col3"],
    color=["#FF0000", "#0000FF"],  # Optional
)

st.divider()
st.write('bar_charthorizontal')


source = data.barley()

st.bar_chart(source, x="variety", y="yield", color="site", horizontal=True)

st.divider()
st.write('bar_chart_not_stacked')


source = data.barley()

st.bar_chart(source, x="year", y="yield", color="site", stack=False)

st.divider()
st.write('line_chart')

chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=["col1", "col2", "col3"]
)

st.line_chart(
    chart_data,
    x="col1",
    y=["col2", "col3"],
    color=["#FF0000", "#0000FF"],  # Optional
)

st.divider()
st.write('map')

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)
st.map(df)

st.divider()
st.write('map')
df = pd.DataFrame(
    {
        "col1": np.random.randn(1000) / 50 + 37.76,
        "col2": np.random.randn(1000) / 50 + -122.4,
        "col3": np.random.randn(1000) * 100,
        "col4": np.random.rand(1000, 4).tolist(),
    }
)

st.map(df, latitude="col1", longitude="col2", size="col3", color="col4")

st.divider()
st.write('scatter_chart')

chart_data = pd.DataFrame(
    np.random.randn(20, 4), columns=["col1", "col2", "col3", "col4"]
)

st.scatter_chart(
    chart_data,
    x="col1",
    y=["col2", "col3"],
    size="col4",
    color=["#FF0000", "#0000FF"],  # Optional
)


st.divider()
st.write('scatter_chart')
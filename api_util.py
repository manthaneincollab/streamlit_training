from streamlit_extras.altex import   line_chart
import streamlit as st 
import pandas as pd
import numpy as np

def example_bottom():
    from streamlit_extras.bottom_container import bottom
    st.write("This is the main container")

    with bottom():
        st.write("This is the bottom container")
        st.text_input("This is a text input in the bottom container")



def example_1():
    from annotated_text import annotated_text

    annotated_text(
        "This ",
        ("is", "verb", "#8ef"),
        " some ",
        ("annotated", "adj", "#faa"),
        ("text", "noun", "#afa"),
        " for those of ",
        ("you", "pronoun", "#fea"),
        " who ",
        ("like", "verb", "#8ef"),
        " this sort of ",
        ("thing", "noun", "#afa"),
    )
 
def example_multi_line():
    chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=["col1", "col2", "col3"]
    )

    line_chart(
        data=chart_data,
        x="col1",
        y="col2",
        color="col3",
        title="A beautiful multi line chart",
    )
 
def example_button_sel():
    from streamlit_extras.button_selector import button_selector
    month_list = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    selected_index = button_selector(
        month_list,
        index=0,
        spec=4,
        key="button_selector_example_month_selector",
        label="Month Selector",
    )
    st.write(f"Selected month: {month_list[selected_index]}")

def example1echo_expander():
    from streamlit_extras.echo_expander import echo_expander
    with echo_expander():
        import streamlit as st

        st.markdown(
            """
            This component is a combination of `st.echo` and `st.expander`.
            The code inside the `with echo_expander()` block will be executed,
            and the code can be shown/hidden behind an expander
            """
        )

def example_grid():
    from streamlit_extras.grid import grid

    random_df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    my_grid = grid(2, [2, 4, 1], 1, 4, vertical_align="bottom")

    # Row 1:
    my_grid.dataframe(random_df, use_container_width=True)
    my_grid.line_chart(random_df, use_container_width=True)
    # Row 2:
    my_grid.selectbox("Select Country", ["Germany", "Italy", "Japan", "USA"])
    my_grid.text_input("Your name")
    my_grid.button("Send", use_container_width=True)
    # Row 3:
    my_grid.text_area("Your message")
    # Row 4:
    my_grid.button("Example 1", use_container_width=True)
    my_grid.button("Example 2", use_container_width=True)
    my_grid.button("Example 3", use_container_width=True)
    my_grid.button("Example 4", use_container_width=True)
    # Row 5 (uses the spec from row 1):
    with my_grid.expander("Show Filters", expanded=True):
        st.slider("Filter by Age", 0, 100, 50)
        st.slider("Filter by Height", 0.0, 2.0, 1.0)
        st.slider("Filter by Weight", 0.0, 100.0, 50.0)
    my_grid.dataframe(random_df, use_container_width=True)
def example_metric():
    from streamlit_extras.metric_cards import style_metric_cards
    col1, col2, col3 = st.columns(3)

    col1.metric(label="Gain", value=5000, delta=1000)
    col2.metric(label="Loss", value=5000, delta=-1000)
    col3.metric(label="No Change", value=5000, delta=0)

    style_metric_cards()

def examplerw():
    from streamlit_extras.row import row
    random_df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    row1 = row(2, vertical_align="center")
    row1.dataframe(random_df, use_container_width=True)
    row1.line_chart(random_df, use_container_width=True)

    row2 = row([2, 4, 1], vertical_align="bottom")

    row2.selectbox("Select Country", ["Germany", "Italy", "Japan", "USA"])
    row2.text_input("Your name")
    row2.button("Send", use_container_width=True)

def examplestoggle():
    from streamlit_extras.stoggle import stoggle
    stoggle(
        "Click me!",
        """🥷 Surprise! Here's some additional content""",
    )

def want_to_contribute():
    from streamlit_extras.switch_page_button import switch_page
    want_to_contribute = st.button("I want to contribute!")
    if want_to_contribute:
        switch_page("api_data")

def exampletagger_component():
    from streamlit_extras.tags import tagger_component
    tagger_component("Here is a feature request", ["p2", "🚩triaged", "backlog"])
    tagger_component(
        "Here are colored tags",
        ["turtle", "rabbit", "lion"],
        color_name=["blue", "orange", "lightblue"],
    )
    tagger_component(
        "Annotate the feature",
        ["hallucination"],
        color_name=["blue"],
    )
def exampletoggle():
    from streamlit_extras import st_toggle_switch

    st.write("## Toggle Switch")
    st_toggle_switch(
        label="Enable Setting?",
        key="switch_1",
        default_value=False,
        label_after=False,
        inactive_color="#D3D3D3",  # optional
        active_color="#11567f",  # optional
        track_color="#29B5E8",  # optional
    )

exampletoggle()
exampletagger_component()

want_to_contribute()

examplestoggle()
examplerw()
example_metric()
example_grid()
example1echo_expander()
example_multi_line()
example_1()
example_button_sel()
example_bottom()

import streamlit as st
import numpy as np
from scipy import stats
from scipy.stats import t
from statistics import stdev

st.set_page_config(page_title="Two Sample T-Test App", layout="centered")

st.title("📊 Two Sample T-Test Calculator")

st.write("Enter sample values separated by commas.")

# User Input
sample1 = st.text_input("Enter Sample 1 values", "10,12,14,15,18")
sample2 = st.text_input("Enter Sample 2 values", "8,9,11,13,10")

alternative = st.selectbox(
    "Select Alternative Hypothesis",
    ["two-sided", "left", "right"]
)

if st.button("Run Test"):

    try:
        # Convert input to lists
        a = list(map(float, sample1.split(",")))
        b = list(map(float, sample2.split(",")))

        n1 = len(a)
        n2 = len(b)

        xbar1 = np.mean(a)
        xbar2 = np.mean(b)

        sd1 = stdev(a)
        sd2 = stdev(b)

        alpha = 0.05 / 2
        df = n1 + n2 - 2

        se = np.sqrt((sd1**2)/n1 + (sd2**2)/n2)

        tcal = ((xbar1 - xbar2) - 0) / se

        # P-value calculation
        if alternative == "two-sided":
            p_value = 2 * (1 - t.cdf(abs(tcal), df))
        elif alternative == "left":
            p_value = t.cdf(tcal, df)
        elif alternative == "right":
            p_value = 1 - t.cdf(tcal, df)

        st.subheader("Results")

        st.write("Sample 1 Mean:", round(xbar1, 4))
        st.write("Sample 2 Mean:", round(xbar2, 4))
        st.write("t-statistic:", round(tcal, 4))
        st.write("Degrees of Freedom:", df)
        st.write("p-value:", round(p_value, 6))

        if p_value < 0.05:
            st.success("Reject the Null Hypothesis ✅")
        else:
            st.warning("Fail to Reject the Null Hypothesis ❌")

    except:
        st.error("Please enter valid numeric values separated by commas.")
import streamlit as st
import pandas as pd
import plotly.express as px

from router.recommend import recommend_algorithms
from router.analyzer import analyze_dataset

st.set_page_config(
    page_title="Meta Learning Router",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Meta-Learning ML Strategy Router")

st.markdown("""
Analyze any dataset and extract important machine learning characteristics.
""")

uploaded_file = st.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

    except Exception as e:
        st.error(f"CSV Error: {e}")
        st.stop()

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Shape")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    target_column = st.selectbox(
        "Select Target Column",
        df.columns
    )

    if st.button("Analyze Dataset"):

        result = analyze_dataset(
            df,
            target_column
        )

        st.subheader("Dataset Statistics")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Rows",
            result["rows"]
        )

        col2.metric(
            "Columns",
            result["cols"]
        )

        col3.metric(
            "Missing %",
            result["missing_percent"]
        )

        col4, col5, col6 = st.columns(3)

        col4.metric(
            "Numeric Features",
            result["numeric"]
        )

        col5.metric(
            "Categorical Features",
            result["categorical"]
        )

        col6.metric(
            "Target Type",
            result["target_type"]
        )

        # Missing values table
        st.subheader("Missing Values")

        missing_table = pd.DataFrame({
            "Column": df.columns,
            "Missing Values": df.isnull().sum().values
        })

        st.dataframe(missing_table)

        # Datatypes
        st.subheader("Column Data Types")

        dtype_df = pd.DataFrame({
            "Column": df.columns,
            "Datatype": df.dtypes.astype(str)
        })

        st.dataframe(dtype_df)

        # Missing chart
        st.subheader("Missing Value Chart")

        fig = px.bar(
            missing_table,
            x="Column",
            y="Missing Values",
            title="Missing Values Per Column"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # Feature distribution
        st.subheader("Feature Distribution")

        numeric_cols = df.select_dtypes(
            include=["int64", "float64"]
        ).columns

        if len(numeric_cols) > 0:

            selected_col = st.selectbox(
                "Choose Numeric Column",
                numeric_cols
            )

            hist = px.histogram(
                df,
                x=selected_col,
                title=f"Distribution of {selected_col}"
            )

            st.plotly_chart(
                hist,
                use_container_width=True
            )

        st.success(
            "Dataset Analysis Complete!"
        )

             # =================================================
        # STEP 2: AI RECOMMENDATION ENGINE
        # =================================================

        st.markdown("---")

        st.header(
            "🤖 Step 2: AI Recommendation Engine"
        )

        try:

            ranking = recommend_algorithms(
                result["rows"],
                result["cols"],
                result["missing_percent"],
                result["numeric"],
                result["categorical"]
            )

            recommended = ranking[0][0]

            st.success(
                f"🏆 Recommended Algorithm: {recommended}"
            )

            # ============================================
            # WHY THIS RECOMMENDATION
            # ============================================

            st.subheader(
                "🧠 Why This Recommendation?"
            )

            if recommended == "Random Forest":

                st.info(
                    f"""
                    • Dataset contains {result['cols']} features.

                    • Random Forest handles large feature spaces effectively.

                    • It captures complex feature interactions.

                    • Ensemble learning helps reduce overfitting.

                    • Similar datasets in the training history achieved strong results using Random Forest.
                    """
                )

            elif recommended == "SVM":

                st.info(
                    f"""
                    • Dataset contains {result['rows']} rows and {result['cols']} features.

                    • SVM performs well on classification tasks with clear boundaries.

                    • Effective for small and medium-sized datasets.

                    • Works efficiently in high-dimensional feature spaces.

                    • Similar benchmark datasets favored SVM.
                    """
                )

            elif recommended == "Logistic Regression":

                st.info(
                    f"""
                    • Dataset appears relatively simple in structure.

                    • Logistic Regression is fast and interpretable.

                    • Performs well when relationships are mostly linear.

                    • Similar datasets achieved good results using Logistic Regression.
                    """
                )

            elif recommended == "Decision Tree":

                st.info(
                    f"""
                    • Dataset patterns can be represented as decision rules.

                    • Easy to understand and visualize.

                    • Works with both numerical and categorical features.

                    • Similar datasets performed well with Decision Trees.
                    """
                )

            elif recommended == "KNN":

                st.info(
                    f"""
                    • Dataset size is suitable for neighbor-based learning.

                    • Similar records are likely to belong to similar classes.

                    • Effective for local pattern recognition.

                    • Similar benchmark datasets favored KNN.
                    """
                )

            # ============================================
            # ANALYSIS SUMMARY
            # ============================================

            st.markdown("---")

            st.header(
                "📋 Analysis Summary"
            )

            summary_df = pd.DataFrame({
                "Metric": [
                    "Rows",
                    "Columns",
                    "Missing %",
                    "Numeric Features",
                    "Categorical Features",
                    "Target Type"
                ],
                "Value": [
                    result["rows"],
                    result["cols"],
                    result["missing_percent"],
                    result["numeric"],
                    result["categorical"],
                    result["target_type"]
                ]
            })

            st.dataframe(
                summary_df,
                use_container_width=True
            )

            # ============================================
            # CONFIDENCE SCORES
            # ============================================

            st.header(
                "📊 Confidence Scores"
            )

            ranking_df = pd.DataFrame(
                ranking,
                columns=[
                    "Algorithm",
                    "Confidence"
                ]
            )

            ranking_df["Confidence"] = (
                ranking_df["Confidence"] * 100
            ).round(2)

            st.dataframe(
                ranking_df,
                use_container_width=True
            )

            st.info(
                f"""
                The Meta-Learning Router analyzed the dataset characteristics and
                compared them with patterns learned from previously benchmarked datasets.

                Based on those learned patterns, {recommended} received the highest
                confidence score and is predicted to be the most suitable algorithm
                for this dataset.
                """
            )

            chart = px.bar(
                ranking_df,
                x="Algorithm",
                y="Confidence",
                title="Recommendation Confidence (%)"
            )

            st.plotly_chart(
                chart,
                use_container_width=True
            )

        except Exception as e:

            st.error(
                f"Recommendation Error: {e}"
            )
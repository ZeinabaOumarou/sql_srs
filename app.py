import duckdb as db
import streamlit as st


con = db.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# solution_df = db.sql(answer_str).df()

with (st.sidebar):
    theme = st.selectbox(
        "What would you like to review",
        ("cross_joins", "GroupBY", "window_functions"),
        index=None,
        placeholder="Select a theme",
    )
    st.write("You selected:", theme)
    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme ='{theme}'").df()
    #  .sort_values("Last_reviewed").reset_index()
    st.write(exercise)


st.header("Entrez votre code :")
query = st.text_area(label="Votre code SQL ici", key="user_input")

if query:
    result = con.execute(query).df()
    st.dataframe(result)

#     try:
#         result = result[solution_df.columns]
#         st.dataframe(result.compare(solution_df))
#     except KeyError as e:
#         st.write("Some columns are missing")
#
#     n_lines_difference = result.shape[0] - solution_df.shape[0]
#     if n_lines_difference != 0:
#         st.write(
#             f"result has a {n_lines_difference} lines difference with the solution_df"
#         )
#
#
tab1, tab2 = st.tabs(["Tables", "solution_df"])

with tab1:
    exercise_tables = exercise.loc[0, "tables"]
    for table in exercise_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f" SELECT * FROM {table}").df()
        st.dataframe(df_table)
        # st.write("table: food_items")
        # st.dataframe(food_items)
        # st.write("table: expected")
        # st.dataframe(solution_df)

with tab2:
    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()
    st.write(answer)

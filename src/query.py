from src.plotting import plot_system, plot_route

def query_route(ridership_df):
    user_input = input("Imput route number or 'All': ")

    if user_input.lower() == "all":
        df = ridership_df.groupby("date")["avg_riders"].sum().reset_index()
        plot_system(df)
    else:
        df = ridership_df[
            (ridership_df["route"].astype(str) == user_input) |
            (ridership_df["route_full_name"].str.contains(user_input, case=False, na=False))
        ]
        if df.empty:
            print("The route is DNE")
        else:
            plot_route(df, user_input)

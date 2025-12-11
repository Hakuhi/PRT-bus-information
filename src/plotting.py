import matplotlib.pyplot as plt

def plot_system(df):
    plt.figure(figsize=(14, 5))
    plt.plot(df["date"], df["avg_riders"], label="System Total Avg Riders")
    plt.title("System Total Monthly Ridership")
    plt.xlabel("Month")
    plt.ylabel("Avg Riders")
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_route(df, route):
    plt.figure(figsize=(14, 5))
    plt.plot(df["date"], df["avg_riders"], label=f"Route {route}")
    plt.title(f"Monthly Ridership: Route {route}")
    plt.xlabel("Month")
    plt.ylabel("Avg Riders")
    plt.grid(True)
    plt.legend()
    plt.show()

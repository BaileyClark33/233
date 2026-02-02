import pandas as pd

path = "https://georgiadoing.github.io/CSC233-W26/Data/"
csv_file = "state_example.csv"
filename = path + csv_file

state_df = pd.read_csv(filename)
print(state_df)

new = pd.Series(
    [12, 2, 4, 1, 1], index=["California", "New York", "Texas", "Florida", "Illinois"]
)

state_df["density"] = state_df["population"] / state_df["area"]


def createDF(cols, inds):
    data = {c: [str(c) + str(i) for i in inds] for c in cols}
    return pd.DataFrame(data, inds)

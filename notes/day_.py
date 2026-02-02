import pandas as pd


def createDF(cols, inds):
    data = {c: [str(c) + str(i) for i in inds] for c in cols}
    return pd.DataFrame(data, inds)


df2 = createDF(["AB"], [3, 4])

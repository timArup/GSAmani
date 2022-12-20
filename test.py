import pandas as pd 

df = pd.DataFrame({"element index":[6], "max_Fx":[800.2]})


# if 5 in df["element index"].values:
#     print("hi")
# if 6 in df["element index"].values:
#     print("hi")
print(df[df["element index"]==5])
print(df[df["element index"]==6])
print(df.index[df["element index"]==5].tolist())
print(df.index[df["element index"]==6].tolist())

print(df)
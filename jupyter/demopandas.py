import os
import pandas

# df1 = pandas.DataFrame([[2, 4, 6], [3, 5, 7]])
# print(df1.mean())
# print(df1.mean().mean())

print(os.listdir())
df1 = pandas.read_csv("supermarkets.csv")
df2 = pandas.read_json("supermarkets.json")
df3 = pandas.read_excel("supermarkets.xlsx", sheet_name=0)
df4 = pandas.read_csv("supermarkets-commas.txt") # sep="," by default (seperator)
df5 = pandas.read_csv("supermarkets-semi-colons.txt", sep=";") 
df6 = pandas.read_csv("data.txt", header=None) # source file does not have a header
print(df1)
print(df2)
print(df3)
print(df4)
print(df5)
print(df6)
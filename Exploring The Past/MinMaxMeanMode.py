import statistics
import pandas as pd
my_list = list(range(51))

print(min(my_list)) # 0
print(max(my_list)) # 50
print(statistics.mean(my_list)) # 25.0
print(statistics.median(my_list)) # 25

pandaDF = pd.DataFrame(my_list)
print(pandaDF.skew())
print(pandaDF.var())
print(pandaDF.kurt())




import pandas

fp = "C:\\Users\\JobiW\\Desktop\\Design, Search,Optimization\\Joe_Kasia\\50Lap_6.csv"
lapTimes = pandas.read_csv(fp, header=None)
print(round(sum(lapTimes.transpose().loc[13])/60,3))
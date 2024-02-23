import pandas as pd

# load and split according to timepoints
data = pd.read_csv("./Data/OldVersions/FEATURES NORM TO V3 FINAL.csv")
dataTemp = data.copy()
label = 1- (dataTemp.drop_duplicates(subset="sampleID").drop(["population","reagent","stimulation","time","feature"],axis =1).sort_values("sampleID")["group"] == "placebo")
data = data.drop(["group"],axis=1)
dataV4a = data[data["time"] == 'V4a'].drop('time',axis = 1)
dataV4b = data[data["time"] == 'V4b'].drop('time',axis = 1)
dataV5 = data[data["time"] == 'V5'].drop('time',axis = 1)

# Pivot data
dataV4aPivoted = pd.pivot(dataV4a,index = ["sampleID"],columns=["population","reagent","stimulation"],values=["feature"])
dataV4aPivoted.columns = [f'{i}_{j}_{k}'  for _,i,j,k in dataV4aPivoted.columns]
dataV4bPivoted = pd.pivot(dataV4b,index = ["sampleID"],columns=["population","reagent","stimulation"],values=["feature"])
dataV4bPivoted.columns = [f'{i}_{j}_{k}'  for _,i,j,k in dataV4bPivoted.columns]
dataV5Pivoted = pd.pivot(dataV5,index = ["sampleID"],columns=["population","reagent","stimulation"],values=["feature"])
dataV5Pivoted.columns = [f'{i}_{j}_{k}'  for _,i,j,k in dataV5Pivoted.columns]
label.index = dataV4bPivoted.index

# save
dataV4aPivoted.to_csv("./Data/Alkahest-V4a.csv")
dataV4bPivoted.to_csv("./Data/Alkahest-V4b.csv")
dataV5Pivoted.to_csv("./Data/Alkahest-V5.csv")
label.to_csv("./Data/AlkahestLabel.csv")
# ...
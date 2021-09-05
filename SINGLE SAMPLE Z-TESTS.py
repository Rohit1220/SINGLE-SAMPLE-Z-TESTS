import pandas as pd, statistics as stt, plotly.figure_factory as pff, random , plotly.graph_objects as pgo

df = pd.read_csv("data.csv")
print (df)

data = df["InternetUsers"].tolist()
print(data)

data1 = df["Population"].tolist()
print(data1)

data2 = df["Per capita"].tolist()
print(data2)

Standard_Devition = stt.stdev(data)
print(Standard_Devition)

Standard_Devition_1 = stt.stdev(data1)
print(Standard_Devition_1)

Standard_Devition_2 = stt.stdev(data2)
print(Standard_Devition_2)

mean = stt.mean(data)
print(mean)

mean1 = stt.mean(data1)
print(mean1)

mean2 = stt.mean(data2)
print(mean2)

fig = pff.create_distplot([data],["InternetUsers"],show_hist=False)
fig.show()

fig1 = pff.create_distplot([data1],["Population"],show_hist=False)
fig1.show()

def random_mean(counter):
    dataset = []
    print(dataset)
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data)-1)
        print(random)
        value = data[randomIndex]
        print(value)
        dataset.append(value)
        print(dataset)
    mean = stt.mean(dataset)
    return mean

meanLIST=[]

for i in range(0,1000):
        setofmean = random_mean(100)
        print(setofmean)
        meanLIST.append(setofmean)
        print(meanLIST)
        
stdDevofMeanList = stt.stdev(meanLIST)
print(stdDevofMeanList)

meanofSamples = stt.mean(meanLIST)
print(meanofSamples)

first_std_dev_start  = mean -stdDevofMeanList
print(first_std_dev_start)
first_std_dev_end  = mean  + stdDevofMeanList
print(first_std_dev_end)
first_std_deviation = first_std_dev_end-first_std_dev_start
print(first_std_deviation)

second_std_dev_start  = mean -2 * stdDevofMeanList
print(second_std_dev_start)
second_std_dev_end  = mean + 2 * stdDevofMeanList
print(second_std_dev_end)
second_std_deviation = second_std_dev_end-second_std_dev_start
print(second_std_deviation)

third_std_dev_start  = mean - 3 * stdDevofMeanList
print(third_std_dev_start)
third_std_dev_end  = mean + 3 * stdDevofMeanList
print(third_std_dev_end)
third_std_deviation = third_std_dev_end-third_std_dev_start
print(third_std_deviation)
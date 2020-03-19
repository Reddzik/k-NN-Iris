from math import sqrt
import csv

def readFromFile(path):
    context= list()
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            context.append(line)
    return context

def result_column_to_int(data):
    result_types= set([row[-1] for row in data])
    result_to_int_map= dict()
    for i , value in enumerate(result_types):
        result_to_int_map[value] = i
        print("{} is {}".format(i, value))
    for row in data:
        row[-1] = result_to_int_map[row[-1]]
    return result_to_int_map


def string_into_floats(data,column):
    for singleRow in data:
        singleRow[column] = float(singleRow[column])

def find_minmax_of_each_column(data):
    min_and_max= []
    for i in range(len(data[0])):
        values = [rows[i] for rows in data]
        min_and_max.append([min(values), max(values)])
    return  min_and_max

def findDistance(row1, row2):
    distance = 0.0
    for i in range(len(row1) - 1):
        distance += (row1[i]-row2[i])**2
    euclideanDistance = sqrt(distance)
    return euclideanDistance

def getNeighbors(trainData, testRow, k):
    distances = []
    neighbors = []
    for row in trainData:
        distance = findDistance(testRow, row)
        distances.append((distance,row))
    distances.sort(key=lambda x: x[0])
    for i in range(k):
        neighbors.append(distances[i][1])
    return neighbors

def predict(trainData, testRow, k):
    neighbors = getNeighbors(trainData,testRow, k)
    resultColumn = [row[-1] for row in neighbors]
    # prediction = max(resultColumn, key=resultColumn.count)
    prediction = max(set(resultColumn), key=resultColumn.count)
    return prediction


def prepare_data(trainData):
    for column in range(len(trainData[1])):
        if column == len(trainData[1]) - 1: break
        string_into_floats(trainData, column)

    result_column_to_int(trainData)
    return trainData;

def add_your_own_row(trainData,row, k):
    label = predict(trainData, row, k)
    print("Prediction is {}".format(int(label)))

# trainData = readFromFile("D:/NAI/KNN/dane/iris.data");

# for column in range(len(trainData[1])):
#     if column == len(trainData[1]) - 1: break
#     string_into_floats(trainData, column)
# print(set([row[-1] for row in trainData]))
# print(trainData[0][0])
# # print(find_minmax_of_each_column(trainData))
# # print(result_column_to_int(trainData))
# # print(trainData)

# result_column_to_int(trainData)
# row= [6.3,3.4,5.6,2.4]
# label = predict(trainData,row,3)



# print("Prediction is {}".format(int(label)))

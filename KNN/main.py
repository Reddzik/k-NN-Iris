import knn
numbers_of_data=4
trainData = knn.readFromFile("D:/NAI/KNN/dane/iris.data");
my_row=[]
print("Podaj dane: ")
for i in range(numbers_of_data):
    print("Podaj {} liczbe".format(i+1))
    my_row.append(float(input()))

knn.prepare_data(trainData)
print("===================================")
knn.add_your_own_row(trainData,my_row,3)

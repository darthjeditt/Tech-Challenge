import json

#Global Variable
jsonFile = open('data.json')
data = json.load(jsonFile)
orderList = [x for x in data["orders"]]
orderIdList = [str(x["orderId"]) for x in orderList]

def main():
    '''Initiate the script'''

    print(orderIdList)
    print('Please select which orders you would like to run, example input: 1122, 1123, 1124')
    orderRunQuestion = input()
    selectedId = list(orderRunQuestion.split(', '))
    
    if selectedId is not None and any(x in selectedId for x in orderIdList):
        processOrders(selectedId)
    else:
        print('No orders are to be run, thank you for using NOMSS order run tool.')

def processOrders():
    pass

def reOrders():
    pass


if __name__ == '__main__':
    main()
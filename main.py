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
    '''Bulk of the order processing work'''

    #processOrders variables
    productList = [x for x in data["products"]]
    allItemsList = [x["items"] for x in orderList]
    unfulfilledIdList = []
    productInfo1 = []
    productInfo2 = []
    productInfo3 = []
    productQuant1 = 0
    productQuant2 = 0
    productQuant3 = 0
    orderStatus = ''

    #Assigning each product quantity to a variable
    for info in productList:
        productId = str(info["productId"])
        for id in productId:
            if '1' in id:
                productInfo1 = info
                productQuant1 = int(productInfo1["quantityOnHand"])
            elif '2' in id:
                productInfo2 = info
                productQuant2 = int(productInfo2["quantityOnHand"])
            else:
                productInfo3 = info
                productQuant3 = int(productInfo3["quantityOnHand"])

def reOrders():
    pass


if __name__ == '__main__':
    main()
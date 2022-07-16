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

def processOrders(selectedId: list[str]):
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
    
    #Begin processing the order(s)
    print(f'Running through your orders {selectedId}')   
    for orderId in selectedId:  
        for itemInfo in orderList:
            if orderId in str(itemInfo["orderId"]):
                orderStatus = str(itemInfo["status"])
                for items in allItemsList:
                    itemsId = [str(id["orderId"]) for id in items]
                    if orderId in [x for x in itemsId]:
                        for item in items:
                            itemList = str(item["productId"])
                            itemQuant = int(item["quantity"])
                            for itemId in itemList:
                                if '1' == itemId:                                    
                                    if int(productQuant1) < itemQuant:
                                        orderStatus = 'Unfulfilled'
                                        orderStatus 
                                        reOrders()
                                        if orderId not in [x for x in unfulfilledIdList]: 
                                            unfulfilledIdList.append(orderId)
                                    else:
                                        productQuant1 = str(int(productQuant1) - int(itemQuant))
                                elif '2' == itemId:
                                    if int(productQuant2) < itemQuant:
                                        orderStatus = 'Unfulfilled'
                                        orderStatus 
                                        reOrders()
                                        if orderId not in [x for x in unfulfilledIdList]:
                                            unfulfilledIdList.append(orderId)
                                    else:
                                        productQuant2 = str(int(productQuant2) - int(itemQuant))
                                elif '3' == itemId:
                                    if int(productQuant3) < itemQuant:
                                        orderStatus = 'Unfulfilled'
                                        orderStatus
                                        reOrders()
                                        if orderId not in [x for x in unfulfilledIdList]: 
                                            unfulfilledIdList.append(orderId)
                                    else:
                                        productQuant3 = str(int(productQuant3) - int(itemQuant))

    if unfulfilledIdList != []:
        print(f'Some orders have been unfulfilled and are being re-stocked, These orders are: {unfulfilledIdList}\nThank you for using NOMSS order run tool.')

    else:
        print('All orders have been fulfilled, Thank you for using NOMSS order run tool.')

def reOrders():
    pass


if __name__ == '__main__':
    main()
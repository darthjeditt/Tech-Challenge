import json

#Global Variable
jsonFile = open('data.json')
data = json.load(jsonFile)


class OrderItem:
    '''Setup for data variables'''
    orderList = [orders for orders in data["orders"]]
    orderIdList = [str(orderIds["orderId"]) for orderIds in orderList]
    productList = [products for products in data["products"]]

    def singleItem(itemList = []) -> list:
        orderList = [orders for orders in data["orders"]]
        allItemsList = [items["items"] for items in orderList]
        itemsList = []
        for item in allItemsList:
            itemId = [str(y["orderId"]) for y in item]
            for selectedId in itemList:
                if selectedId in itemId:
                    itemsList.extend(item)
        return itemsList


def main():
    '''Initiate the script'''

    print(OrderItem.orderIdList)

    print('Please select which orders you would like to run, example input: 1122, 1123, 1124')
    orderRunQuestion = input()
    selectedId = list(orderRunQuestion.split(', '))
    if selectedId is not None and all(x in OrderItem.orderIdList for x in selectedId):
        processOrders(selectedId)
    else:
        print('No orders are to be run, thank you for using NOMSS order run tool.')


def processOrders(selectedId = []):
    '''Bulk of the order processing work'''

    #processOrders variables
    unfulfilledIdList = []

    #Assigning each product quantity to a variable
    productQuant1 = next((x["quantityOnHand"] for x in OrderItem.productList if x["productId"] == 1), None)
    productQuant2 = next((x["quantityOnHand"] for x in OrderItem.productList if x["productId"] == 2), None)
    productQuant3 = next((x["quantityOnHand"] for x in OrderItem.productList if x["productId"] == 3), None)
    orderQuant1 = next((x["quantity"] for x in OrderItem.singleItem(selectedId) if x["productId"] == 1), None)
    orderQuant2 = next((x["quantity"] for x in OrderItem.singleItem(selectedId) if x["productId"] == 2), None)
    orderQuant3 = next((x["quantity"] for x in OrderItem.singleItem(selectedId) if x["productId"] == 3), None)

    #Begin processing the order(s)
    print(f'Running through your orders {selectedId}')   

    for i in range(len(OrderItem.singleItem(selectedId))):
        singleOrderId = OrderItem.singleItem(selectedId)[i]["orderId"]
        orderStatus = next((x["status"] for x in OrderItem.orderList if x["orderId"] == singleOrderId), None)
        if OrderItem.singleItem(selectedId)[i]["productId"] == 1:
            if productQuant1 < orderQuant1:
                orderStatus = 'Unfulfilled'
                orderStatus
                reOrders()
                if singleOrderId not in [x for x in unfulfilledIdList]: 
                    unfulfilledIdList.append(singleOrderId)
            else:
                productQuant1 -= orderQuant1
        elif OrderItem.singleItem(selectedId)[i]["productId"] == 2:
            if productQuant2 < orderQuant2:
                orderStatus = 'Unfulfilled'
                orderStatus
                reOrders()
                if singleOrderId not in [x for x in unfulfilledIdList]: 
                    unfulfilledIdList.append(singleOrderId)
            else:
                productQuant2 -= orderQuant2
        elif OrderItem.singleItem(selectedId)[i]["productId"] == 3:
            if productQuant3 < orderQuant3:
                orderStatus = 'Unfulfilled'
                orderStatus
                reOrders()
                if singleOrderId not in [x for x in unfulfilledIdList]: 
                    unfulfilledIdList.append(singleOrderId)
            else:
                productQuant3 -= orderQuant3

    if unfulfilledIdList != []:
        print(f'Some orders have been unfulfilled and are being re-stocked, These orders are: {unfulfilledIdList}\nThank you for using NOMSS order run tool.')
    else:
        print('All orders have been fulfilled, Thank you for using NOMSS order run tool.')


def reOrders():
    '''Redordering process'''
    pass


if __name__ == '__main__':
    main()
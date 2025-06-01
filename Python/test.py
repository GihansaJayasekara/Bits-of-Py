# Importing datetime
import datetime

# Creating necessary lists
customersList = []
ordersList = []

# Checking the inputted date is correct
def isValidDate(date):
    if '-' not in date or date.count('-') != 2:
        return False
    year, month, day = date[:4], date[5:7], date[8:]
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False
    year, month, day = int(year), int(month), int(day)
    if year < 1 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    elif month in [4, 6, 9, 11] and day > 30:
        return False
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    return True

# CREATING BODY OF CHOICE 1(Registering a NEW customer)
def registerCustomer():
    print("              ================")
    print("               ABC Supermarket ")
    print("              ================")
    print("        **Register a new customer**")
    print("                                    ")

    # Getting Customer ID
    customerId = ""
    while not (customerId[:1] == 'C' and len(customerId) == 4 and customerId[1:].isdigit()):
        customerId = input("Customer ID (C followed by 3 digits, e.g., C123): ")
        if not (customerId[:1] == 'C' and len(customerId) == 4 and customerId[1:].isdigit()):
            print("-Invalid Customer ID. Please enter an ID that starts with 'C' followed by 3 digits.-")
    
    # Checking if customer ID already exists
    customerExists = False
    for cust in customersList:
        if cust['customerId'] == customerId:
            customerExists = True
            break
    
    if customerExists:
        print("-This Customer has already registered. No need to register again.-")
        return

    # Getting Customer's Name
    customerName = ""
    while len(customerName) > 20 or len(customerName) == 0:
        customerName = input("Customer's Name ( maximum of 20 characters): ")
        if len(customerName) > 20:
            print("-Invalid Customer Name. Please enter a name with a maximum of 20 characters.-")
            
    # Getting Customer's Birth date
    birthDate = ""
    while not isValidDate(birthDate):
        birthDate = input("Birth Date (YYYY-MM-DD): ")
        if not isValidDate(birthDate):
            print("-Invalid Birth Date. Please enter the date in YYYY-MM-DD format.-")
    
    # Getting Customer's Telephone number  
    telephone = ""
    while len(telephone) != 10 or not telephone.isdigit():
        telephone = input("Telephone Number (String, 10 characters): ")
        if len(telephone) != 10 or not telephone.isdigit():
            print("-Invalid Telephone Number. Please enter a 10-digit number.-")
            
    # Getting Customer's Address
    customerAddress = ""
    while len(customerAddress) == 0:
        customerAddress = input("Address: ")
        if len(customerAddress) == 0:
            print("-Invalid Address. Please enter a non-empty address.-")
            
    # Saving the given data of the customer
    save = ""
    while save not in ['yes', 'no']:
        save = input("Do you want to save the details (Please enter Yes/No)? ").lower()
        if save == 'yes':
            customersList.append({
                'customerId': customerId,
                'customerName': customerName,
                'birthDate': birthDate,
                'telephone': telephone,
                'customerAddress': customerAddress
            })
            print("-Customer registered successfully.-")
        elif save == 'no':
            print("-Customer details not saved.-")
        else:
            print("-Invalid input!- ")

# Making branch code list
branchCodes = [
    ['B001', 'Colombo'],
    ['B002', 'Nugegoda'],
    ['B003', 'Piliyandala'],
    ['B004', 'Gampaha']
]

# Function to get branch location based on branch code
def getBranchLocation(branchCode):
    for code, location in branchCodes:
        if code == branchCode:
            return location
    return None

# CREATING BODY OF CHOICE 2 (Placing an order)
def placeOrder():
    print("              ===============")
    print("              ABC Supermarket")
    print("              ===============")
    print("          **Place a customer order**")
    print("                                       ")
    
    # Getting Customer's ID
    customerId = ""
    while not (customerId[:1] == 'C' and len(customerId) == 4 and customerId[1:].isdigit()):
        customerId = input("Customer ID (C followed by 3 digits, e.g., C123): ")
        if not (customerId[:1] == 'C' and len(customerId) == 4 and customerId[1:].isdigit()):
            print("-Invalid Customer ID. Please enter an ID that starts with 'C' followed by 3 digits.-")

    # Check if customer ID already exists
    customerExists = False
    for cust in customersList:
        if cust['customerId'] == customerId:
            customerExists = True
            break
    
    if not customerExists:
        print("-This Customer is not registered. Please register before placing an order.-")
        return
    
    # Check if customer has already placed an order
    customerOrders = [order for order in ordersList if order['customerId'] == customerId]
    if customerOrders:
        print("-This customer has already placed an order. Only one order is allowed.-")
        return

    # Getting Order ID
    orderId = ""
    while True:
        orderId = input("Order ID (OD followed by 2 digits, e.g., OD12): ")
        if not (orderId[:2] == 'OD' and len(orderId) == 4 and orderId[2:].isdigit()):
            print("-Invalid Order ID. Please enter an ID that starts with 'OD' followed by 2 digits.-")
        else:
            # Check if the order ID already exists
            orderExists = False
            for ord in ordersList:
                if ord['orderId'] == orderId:
                    orderExists = True
                    break
            if orderExists:
                print("-This Order ID is already used. Please try a different Order ID.-")
            else:
                break

    # Getting Branch Code
    branchCode = ""
    while not getBranchLocation(branchCode):
        branchCode = input("Branch Codes- B001(Colombo), B002(Nugegoda), B003(Piliyandala), B004(Gampaha): ")
        if not getBranchLocation(branchCode):
            print("-Invalid Branch Code. Please enter one of the following: B001(Colombo), B002(Nugegoda), B003(Piliyandala), B004(Gampaha).-")
    branchLocation = getBranchLocation(branchCode)

    # Getting the date which order place
    orderDate = ""
    while not isValidDate(orderDate):
        orderDate = input("Date (YYYY-MM-DD): ")
        if not isValidDate(orderDate):
            print("-Invalid Date. Please enter the date in YYYY-MM-DD format.-")
    
    # Items in the order
    orderItems = []
    totalOrderAmount = 0
    # Initializing total order amount
    while len(orderItems) < 3:
        itemName = input("Item Name: ")
        quantity = ""
        while not quantity.isdigit():
            quantity = input("Quantity: ")
            if not quantity.isdigit():
                print("-Invalid Quantity. Please enter a numeric value.-")
        
        unitPrice = ""
        while True:
            unitPrice = input("Unit Price: ")
            parts = unitPrice.split('.')
            if parts[0].isdigit() and (len(parts) == 1 or (len(parts) == 2 and parts[1].isdigit())):
                break
            else:
                print("-Invalid Unit Price. Please enter a numeric value.-")
        
        totalAmount = float(quantity) * float(unitPrice)
        totalOrderAmount += totalAmount
        # Calculating total order amount
        orderItems.append({
            'itemName': itemName,
            'quantity': quantity,
            'unitPrice': unitPrice,
            'totalAmount': totalAmount
        })
        
        # Display total amount for the item
        print(f"Total Amount for {itemName}: {totalAmount:.2f}")
        
        if len(orderItems) < 3:
            moreItems = input("Do you want to add more items to the same order (Yes/No)? ").lower()
            if moreItems != 'yes':
                break
    
    # Display total order amount
    print(f"Total Order Amount: {totalOrderAmount:.2f}")
    
    # Confirming the order
    placeOrderConfirmation = ""
    while placeOrderConfirmation not in ['yes', 'no']:
        placeOrderConfirmation = input("Do you want to place the order (Yes/No)? ").lower()
        if placeOrderConfirmation == 'yes':
            ordersList.append({
                'customerId': customerId,
                'orderId': orderId,
                'branchCode': branchCode,
                'branchLocation': branchLocation,
                'orderDate': orderDate,
                'orderItems': orderItems,
                'totalOrderAmount': totalOrderAmount # Saving total order amount
                })
            print("-Order placed successfully.-")
        elif placeOrderConfirmation == 'no':
            print("-Order not placed.-")

# CREATING BODY OF CHOICE 3 (Viewing daily sales amount of a given branch)
def viewDailySales():
    print("              ===============")
    print("              ABC Supermarket")
    print("              ===============")
    print("                             ")
    print("    **View daily sales amount of a given branch**")
    print("                                                  ")
    
    # Getting Branch Code
    branchCode = ""
    while not getBranchLocation(branchCode):
        branchCode = input("Branch Codes- B001(Colombo), B002(Nugegoda), B003(Piliyandala), B004(Gampaha): ")
        if not getBranchLocation(branchCode):
            print("-Invalid Branch Code. Please enter one of the following: B001(Colombo), B002(Nugegoda), B003(Piliyandala), B004(Gampaha).-")
    
    # Getting Date
    salesDate = ""
    while not isValidDate(salesDate):
        salesDate = input("Date (YYYY-MM-DD): ")
        if not isValidDate(salesDate):
            print("-Invalid Date. Please enter the date in YYYY-MM-DD format-.")
    
    # Calculating daily sales of the given date
    dailySales = sum(order['totalOrderAmount'] for order in ordersList if order['branchCode'] == branchCode and order['orderDate'] == salesDate)
    print(f"Daily Sales Amount: {dailySales:.2f}")
    viewAnother = input("Do you want to view another date (Yes/No)? ").lower()
    if viewAnother == 'yes':
        viewDailySales()

# CREATING BODY OF CHOICE 4 (Displaying customer details of a given customer)
def displayCustomerDetails():
    print("              ===============")
    print("             ABC Supermarket")
    print("              ================")
    print("    **Display customer details of a given customer**")
    print("                               ")
    customerId = input("Customer ID (C followed by 3 digits, e.g., C123): ")
    customer = None
    for cust in customersList:
        if cust['customerId'] == customerId:
            customer = cust
            break
    if customer:
        print(f"Customer ID: {customer['customerId']}")
        print(f"Customer Name: {customer['customerName']}")
        print(f"Birth Date: {customer['birthDate']}")
        print(f"Telephone Number: {customer['telephone']}")
        print(f"Address: {customer['customerAddress']}")
    else:
        print("-This Customer has not registered early.-")
    
    viewAnother = input("Do you want to display another customer details (Yes/No)? ").lower()
    if viewAnother == 'yes':
        displayCustomerDetails()

# CREATING BODY OF CHOICE 5 (Display order details of a customer)
def displayOrderDetails():
    print("              ===============")
    print("              ABC Supermarket")
    print("              ===============")
    print("                             ")
    customerId = input("Customer ID (C followed by 3 digits, e.g., C123): ")
    order = None
    for ord in ordersList:
        if ord['customerId'] == customerId:
            order = ord
            break
    if order:  
        print("     **Display order details of a customer**")
        print("                                             ")
        print(f"Customer ID: {order['customerId']}")
        print(f"Order ID: {order['orderId']}")
        print(f"Branch Code: {order['branchCode']}")
        print(f"Branch Location: {order['branchLocation']}")
        print(f"Date: {order['orderDate']}")
        for item in order['orderItems']:
            print(f"Item Name: {item['itemName']}")
            print(f"Quantity: {item['quantity']}")
            print(f"Unit Price: {item['unitPrice']}")
            print(f"Total Amount: {item['totalAmount']}")
        print(f"Total Order Amount: {order['totalOrderAmount']:.2f}")
    else:
        print("-Order not found.-")
    
    viewAnother = input("Do you want to view another order details (Yes/No)? ").lower()
    if viewAnother == 'yes':
        displayOrderDetails()

#MAIN LOOP
continueProgram = True
while continueProgram:
    
    # Displaying main menu options
    print("              =================")
    print("              ABC Supermarket ")
    print("              =================")
    print("               **Main Menu**")
    print("                             ")
    print("1) Register a new customer")
    print("2) Place a customer order")
    print("3) View daily sales amount of a given branch")
    print("4) Display customer details of a given customer")
    print("5) Display order details of a customer")
    print("6) Exit")
    choice = input("Your Choice: ")
    
    # Accessing given choices and calling corresponding functions
    if choice == '1':
        registerCustomer()
    elif choice == '2':
        placeOrder()
    elif choice == '3':
        viewDailySales()
    elif choice == '4':
        displayCustomerDetails()
    elif choice == '5':
        displayOrderDetails()
    elif choice == '6':
        print("~~~Thank you. Have a nice day~~~")
        continueProgram = False
    else:
        print("-Invalid choice. Please try again.-")

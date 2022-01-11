---
id: zcZawKL2UTiZT6UMVCYPL
title: Ownership
desc: ''
updated: 1641924099620
created: 1641923936088
---
# Fulfillment Proccess


### Subtitutions:

- Ezra runs Python script with list of parts unable to fulfil to due inv issues
- Jeff goes through and checks for any applicables SKUS that can be subbed
    -  Hand off on Monday, aiming for Wednesday completion


### Reallocation:
- Frank runs F_Reallocate_DC EOD to check ahead for any orders that need to have stock reallocated from and older order
- Frank runs F_Grainger_Reallocate (Amz/Grn) 10 Days ~ 2 times a week to look ahead for any orders that can have stock reallocated from orders no longer in lead time

- The above two also encompass finding SKUS that are set to the wrong location.
This means that when going through reallocations, many other orders are found with the one in lead time that are all not going to ship out due to line item locations being incorrect.

### Manipulations:

- Frank runs F_GraingerDC_FindIF_CompleteQTYCommit ADJUSTMENT to check for Grainger DC orders that need to have their commit status changed to Available QTY.

- Frank monitors two reports very similar to the reallocation block, they are instead looking for any blanks preffered bins on those orders and flagging them to get ahead of the shipping teams encountering blanks bins.

### Fulfillment:

- Shipping managers (probably Anna and Mel) monitor the reminders to try and keep the numbers as low as possible.

    - They are printing work out from NetSuite reminders and using access to mass print.
    1. Grainger DC In Shipment Window
    2. Grainger Drop Ship in Shipment Window
    3. Grainger_Amaz_Past Due
    <br>
    
    ``` These above reports are the core grainger shipping que```

    4. Backlog w/ Inv - Access Template

    ``` This is to print out work for all other customers ```
    - They should also be monitoring the Priority Requests Google Sheet to identify the NDA requests that Tony inputs. (Also Sales Requests go on this sheet)
    


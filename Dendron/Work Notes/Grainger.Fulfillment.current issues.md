---
id: RMSrDypoNxgP0RcGgBcuZ
title: Current issues
desc: ''
updated: 1642101986454
created: 1639680513899
---

##### Need a saved search to find how many products dont have a bin under the item : Bin Number field

- This should find any items that wont return their bin in other key searched we are building

- The Bin should still be able to be pulled from Inventory Detail : Bin Number


### Search for partial intime with 0 backlog
#### GraingerDropShip_0 Backlog (Partials in lead time)
    - Orders in lead time
    - were previously a partial fulfillment
    - can now be shipped in leadtime for the remaining qty
    
### Wrong Location Sales 0 Committed
#### F_Wrong_LOC_0_Commit
    - Adjust one of the current reallocation reports
    - need to be able to find past and future orders that meet this 

### How to identify the orders that need to xfer warehouse to committ complete quantity


### Saved Search for Orders that need a Transfer Order to fulfill
- Criteria
    - Find sales where qty committed are 0
    - Pull in total QTY available
    - More things i cant think of yet

## Build Network Days on DC report

ROUND(((To_Char({today}-{shipdate})))-((((TRUNC({today},'D'))-	(TRUNC({shipdate},'D')))/7)*2) -  (CASE WHEN TO_CHAR({shipdate},'DY')='SUN' 	THEN 1 ELSE 0 END) -  (CASE WHEN TO_CHAR({today},'DY')='SAT' THEN 1 ELSE 0 END),2)
















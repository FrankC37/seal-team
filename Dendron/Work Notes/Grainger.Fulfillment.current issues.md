---
id: RMSrDypoNxgP0RcGgBcuZ
title: Current issues
desc: ''
updated: 1643134247172
created: 1639680513899
---


    
### Wrong Location Sales 0 Committed
#### F_Wrong_LOC_0_Commit
    - Adjust one of the current reallocation reports
    - need to be able to find past and future orders that meet this 

### How to identify the orders that need to xfer warehouse to committ complete quantity


## Build Network Days on DC report

ROUND(((To_Char({today}-{shipdate})))-((((TRUNC({today},'D'))-	(TRUNC({shipdate},'D')))/7)*2) -  (CASE WHEN TO_CHAR({shipdate},'DY')='SUN' 	THEN 1 ELSE 0 END) -  (CASE WHEN TO_CHAR({today},'DY')='SAT' THEN 1 ELSE 0 END),2)


## Finding List of Items and their SO Default Location


## Moe asked about a way to track finishing 
- Similar to the fulfillment 
    - Work Order Completion - Track by this?

    
















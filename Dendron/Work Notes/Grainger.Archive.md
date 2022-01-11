---
id: KUOZnTexFknkBSNxscbj0
title: Archive
desc: ''
updated: 1641323847896
created: 1641323786604
---
**Things that need to be captured in DC report**
1. Amount of shipments that are in +/- 2 day window that have gone out
<br/> ```F_GraingerDC_Shipped_KPI```
<br/> This will show what has already shipped and was due today

2. Items in +/- 2 day window that can be shipped 
        (Already done in [[Grainger.Fulfillment.Saved Searches##Grainger DC Searches]]) 
        ```F_GraingerDC_InShipmentWindow_KPI```
        <br/> This will show what can ship
3.  Total Shipments Due for the shipment window (+/- 2 Days)
    <br/> In theory this should work for future dates. Service Rate _may_ be wonky however if trying to look ahead.
    <br/> ```F_GraingerDC_TotalShip_KPI```
    <br/> This will show the DC Total for the day/range in the KPI
    
4. Breakdown the Failures into Fulfillment, No Stock and possibly Manufacturing (In Netsuite)
    -   If items committed = 0, Is Parent, Is Pass Through (No inv)
    -   If {quantity}-{quantitycommitted} = 0 (Fulfillment Delay)
    - How to find the production delays ?
        - Item : RM Master Units for BOM (Custom) = BOM QTY for 1 Build
        - Limitation is not being able to pull in Parent QTY 
# Double Check DC KPI Numbers
 - Make a no inv counter for DC (KPI)
 - Make a search for what orders need to be switched to Available for DC
    -    Search Created, waiting on a call from Wen


**Shipped By Shipping Station Dash**

Does not appear to be working as expected, Today seems inflated and yesterday is never a correct reflection of what we saw the previous day.
    - Syed reached out to gary on this (12.17)

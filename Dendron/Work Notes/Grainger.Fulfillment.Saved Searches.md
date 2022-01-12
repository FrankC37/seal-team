---
id: tJOWWTj25zw3zjQ8hUR65
title: Saved Searches
desc: ''
updated: 1642024958911
created: 1639753337247
---
## Description of Grainger Saved Searches

### Overall Grainger Look 
<br />

- **F_GraingerALL_AllDueToday**
    - All Grainger Shipments Due today (Includes Branch and DC)
    with no respect for inventory
    
- **F_GraingerALL_ShippedToday**
    - All Grainger Shipments that went out that are due to ship today (Includes Branch and DC)

- **F_GraingerALL_w/InvDueToday**
    - All Grainger Shipments that are due today and have inventory to ship out (Includes DC and Branch)

-**GraingerDropShip_InShipmentWindow**
    - All Grainger Drop Ship, that can be fulfilled and meet lead times
    - 5 days ahead is the window

   
### These are Grainger searches being used for KPIs and Daily Service Rate Tracking
<br />

- **F_GraingerMetrics_AllDueToday**
    - All Drop Shipments Due Today 

- **F_GraingerMetrics_AllDueToday(COUNT)**
    - Same as above but this only returns a count for KPI purposes

- **F_GraingerMetrics_DueToday(Shipped)**
    - All Shipments that are due today, and have shipped

- **F_GraingerMetrics_DueToday(Shipped)(COUNT)**
    - Same as above, only returns a count
- **F_GraingerMetrics_w/InvDueToday**
    - All shipments that have inv full committed and can ship

- **F_GraingerMetrics_w/InvDueToday(COUNT)**
    - Same as above, only returns a count


### Grainger DC Searches

<br />

- **GraingerDC_InShipmentWindow**
    - All DC Shipments that have any qty committed that are still within lead time (- 2 Days), (Used by Shipping Team)

- **F_GraingerMetrics_DC**
    - Place holder currently for duping (Has Grainger DC Address match cases)

- **F_GraingerDC_Shipped_KPI**
    - This will show what has already shipped and was due today
- **F_GraingerDC_InShipmentWindow_KPI**
    - This will show what we can ship
- **F_GraingerDC_TotalShip_KPI**
    - This will show the DC total for the day/Range in the KPI
- **F_GraingerMetricsDS(No Inv)KPI**
    - Returns a count of Drop Ship Line items that are Pass Through or Parents that have nothing committed (No Inv)
- **F_GraingerMetrics_DC(No Inv)KPI**
    -   Same as above but for DC orders
    -   Sums the QTY value to get unit total
        - Will sum units on order to calculate rate



### One Offs

- **F_Grainger_Amaz/Acrylics**
    - Finds orders the Amazon placed through Grainger for Acrylic Sheets. This send out an email to Me(Frank) when new records show up that need to be expedited.

- **Child Lookup (Sales Orders)**
    - Pulls in all sales orders, Let the user put in a Parent and pull all the children with open sales orders 
    -   Built for Jeffs Remnant work

-**F_EAU_CALC**
    - Using this to calculate EAU based on actual order quantity

-**Pref Bin v Inv Detail**
    - Building for Jeff
    - Goal is to pull in pref bin and inv detail
        - having issues pulling in QOH for specific inv detail bin
    
-**F_GraingerDC_FindIF_CompleteQTYCommit ADJUSTMENT**
    - Used for daily updates of commit status on DC orders

-**Transfer Lookahead**
    - Created to try and find orders that need to transfer warehouses
    - Currently works at a way to find orders that need line item location swapped



```Deleted```
<br/>


~~F_GraingerMetrics_DC_Due&ShippedbyToday~~
~~F_GraingerMetrics_DC_Due&ShippedbyToday(Count)~~<br/>
~~F_GraingerMetrics_DC_DueToday~~<br/>
~~F_GraingerMetrics_DC_DueToday(Count)~~<br/>
~~F_GraingerMetrics_DC_DueToday_w/Inv~~<br/>
~~F_GraingerMetrics_DC_DueToday_w/Inv(Count)~~

Replaced By:
[[Grainger DC Searches|Grainger.Fulfillment.Saved Searches#grainger-dc-searches]]

 
    

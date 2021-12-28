---
id: DRZs4VtQYLcEUa5lF9ZOR
title: Substitutions
desc: ''
updated: 1640634329317
created: 1640632843999
---

Goals:
1.  Need to be able to take one SKU and see all of its children 



Inputs:
1. Inventory Report (On Hand)
2. Sales Report (Filtered for Grainger)
3. Item Name (User Input)

Logic:
1.  Input Item (SKU)
    - Return L,W
    - Return Parent L,W,Thickness

2.  Input SKU, Find Every SKU that that has that parent
    - Sort by largest to smalled BOM

    SKU| W | L |  Thickness | QoH | B.O | ROPS | BIN 

3.  Input SKU
    1.   Find all SOs with SKU

SO# | ITEM | QTY on SO | ORDER DATE | SHIP DATE 





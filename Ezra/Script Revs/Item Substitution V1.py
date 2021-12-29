# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 09:39:27 2021

@author: Syed Haque
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 2021

@author: Syed Haque
"""
import pandas as pd

inv=pd.read_excel('C:/Users/Syed Haque/Desktop/PY-sub proj/EZProductionInvSearchResults.xlsx')
#inv.info()
sales=pd.read_excel('C:/Users/Syed Haque/Desktop/PY-sub proj/EZ_Backlog_by_Product.xlsx')
#sales.info()

sku= input("Enter SKU: ")

child_info=inv[inv['Item']==sku] #creating a new dataframe and pulling in matching sku data from inv file
#child_info.info()

inv_children=inv[inv['RM Master Parent']==child_info.iat[0,4] ]#creating a new dataframe with matching rm parents from the inv file
                                                       # the number 12 refers to the column position, needs to updated if inv files is changed
#print(inv_children)

child_info_stack=child_info[['Item','RM Length','RM Width']] #creating a new data set by pulling out specified field of the sku in question we like to look at on top - output 0

inv_children=inv_children[['Item','On Hand','On Order','Committed','Preferred Stock Level','Reorder Point','Reorder Multiple','RM Master Parent','BOM','RM Thickness','RM Length','RM Width','Bin Number','Product Class','Machine Assignment']] #output 1

sales_match=pd.merge(left=child_info, right=sales,how='left',left_on='Item', right_on='Product SKU') #pulling in sales againt the children, has duplicates

sales_match=sales_match[['Product SKU','Document Number','Date','Qty on Backorder','Qty on Order','Qty Available','Requested Ship Date']] #dropping excess columns/redefining the data set, output 2

children_sales_grouped=pd.concat([inv_children, sales_match], axis= 1) #chilren sku with related sales pulled in their own columns, takes care of duplicates as they get their own column and by doing sales_match I only captured the relevant ones

#print(children_sales_grouped)

result_wip = children_sales_grouped.sort_values(by='BOM',ascending=False) # organizing by bom

result= pd.concat([child_info_stack, result_wip], axis= 1)# adding the sku in quesiton info to our over all results

#result.to_excel(r'C:\Users\Syed Haque\Desktop\PY-sub proj\"sku".xlsx',index=False) #exporting to excel file with defined name

df= r"C:/Users/Syed Haque/Desktop/PY-sub proj/"
 
result.to_excel(df + sku + ".xlsx",index= False)

print("File Ready") #decorations
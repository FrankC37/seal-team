import pandas as pd
from tqdm import tqdm
from datetime import datetime
import os

inv=pd.read_excel('C:/Users/fconiglio/git/seal-team/Ezra/EZProductionInvSearchResults728.xlsx')
sales=pd.read_excel('C:/Users/fconiglio/git/seal-team/Ezra/EZSalesDetailsResults160.xlsx')

# Date Conversions
sales["Date"] = pd.to_datetime(sales["Date"])
sales["Date"] = sales["Date"].dt.strftime('%m/%d/%Y')
sales["Requested Ship Date"] = pd.to_datetime(sales["Requested Ship Date"])
sales["Requested Ship Date"] = sales["Requested Ship Date"].dt.strftime('%m/%d/%Y')
#Output File
df= r"C:/Users/fconiglio/git/seal-team/Ezra/output/"

#Taking user input for Multiple SKUS, must be Comma Seperated
user_input = input("Enter SKU: ")
#Splitting the input into a list delimited by commas per item
skus = user_input.split(",")

#Loop to run through all SKUs in list, using TQDM for progress bar
for sku in tqdm(skus):
    #creating a new dataframe and pulling in matching sku data from inv file
    child_info=inv[inv['Item']==sku] 
    
    #creating a new dataframe with matching rm parents from the inv file
    # the number 4 refers to the column position, needs to updated if inv files is changed
    inv_children=inv[inv['RM Master Parent']==child_info.iat[0,4] ]
    
    #creating a new data set by pulling out specified field of the sku in question we like to look at on top - output 0
    child_info_stack=child_info[['Item','RM Length','RM Width']] 

    #output 1
    inv_children=inv_children[['Item','RM Thickness','RM Length','RM Width','On Hand','Back Ordered','Committed','Preferred Stock Level','Reorder Point','Reorder Multiple','RM Master Parent','BOM','Bin Number']] 

    #pulling in sales againt the children, has duplicates
    sales_match=pd.merge(left=child_info, right=sales,how='left',left_on='Item', right_on='Product SKU') 

    #dropping excess columns/redefining the data set, output 2
    sales_match=sales_match[['Product SKU','Document Number','Date','Quantity','Qty Available','Requested Ship Date']] 

    
    #testing if this works, dropping indexing off the dataframe
    children_sales_grouped=pd.concat([inv_children.reset_index(drop=True), sales_match], axis= 1) 
    
    # organizing by bom
    result_wip = children_sales_grouped.sort_values(by='BOM',ascending=False) 
    
    #adding the sku in quesiton info to our over all results
    result= pd.concat([child_info_stack.reset_index(drop=True), result_wip.reset_index(drop=True)], axis= 1)

    #printing each SKU into its own Excel document to the hardcoded path
    result.to_excel(df + sku + ".xlsx",index= False)
    #declaring path to file we just output
    #opening file in excel , uncomment these if you want auto open :)
    #file = df+sku+'.xlsx'
    #os.startfile(file)
print("File(s) Ready") #decorations
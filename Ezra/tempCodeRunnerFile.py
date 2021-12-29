
<<<<<<< HEAD
    sales_match=sales_match[['Product SKU','Document Number','Date','Qty on Backorder','Qty on Order','Qty Available','Requested Ship Date']] #dropping excess columns/redefining the data set, output 2

    #children_sales_grouped=pd.concat([inv_children, sales_match], axis= 1) #chilren sku with related sales pulled in their own columns, takes care of duplicates as they get their own column and by doing sales_match I only captured the relevant ones
    
    children_sales_grouped=pd.concat([inv_children.reset_index(drop=True), sales_match], axis= 1) 
    #testing if this works, dropping indexing off the dataframe
=======
    # the number 12 refers to the column position, needs to updated if inv files is changed
>>>>>>> b427148a9ba46dcf4e2188b9342accaa27e27d7f

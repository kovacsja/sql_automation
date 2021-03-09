SELECT 
    pinv.ProductID, 
    pr.Name as ProductName, 
    pinv.LocationID, 
    l.Name as LocationName,
    SUM([Quantity]) as SumOfQuantity
FROM [Production].[ProductInventory] pinv
    INNER JOIN Production.Product pr on pr.ProductID = pinv.ProductID
    INNER JOIN Production.[Location] l on l.LocationID = pinv.LocationID
GROUP BY 
    pinv.ProductID, pinv.LocationID, pr.Name, l.Name
      
      
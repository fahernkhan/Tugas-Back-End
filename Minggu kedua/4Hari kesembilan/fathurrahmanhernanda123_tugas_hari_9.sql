SELECT 
    o.orderNumber ,
    o.orderDate ,
    c.customerName ,
    c.city ,
    c.country ,
    od.quantityOrdered ,
    p.productName 
FROM
    orders o
    JOIN customers c ON o.customerNumber = c.customerNumber
    JOIN orderdetails od ON o.orderNumber = od.orderNumber
    JOIN products p ON od.productCode = p.productCode
WHERE
    p.productName = '1992 Ferrari 360 Spider red'
    AND o.orderDate >= '2004-08-01'
    AND o.orderDate <= '2004-12-01';
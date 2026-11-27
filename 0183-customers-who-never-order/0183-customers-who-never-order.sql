select customers.name as Customers from customers 
where customers.id not in(
    select c.id from Customers c inner join 
    Orders o on c.id = o.customerId
);

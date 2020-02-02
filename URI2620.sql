select cus.name, ord.id

from customers cus

inner join orders ord
on cus.id = ord.id_customers

Where ord.orders_date >= '2016-01-01' and ord.orders_date <= '2016-06-30'
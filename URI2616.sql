select cus.id, cus.name

from customers cus

left join locations loc
on cus.id = loc.id_customers

where loc.id_customers is null
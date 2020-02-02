select cus.name

from customers cus

inner join legal_person leg
on cus.id = leg.id_customers
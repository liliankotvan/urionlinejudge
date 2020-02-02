select cus.name, ren.rentals_date
from customers cus

inner join rentals ren
    on cus.id = ren.id_customers

where ren.rentals_date >= '2016-09-01'
and ren.rentals_date <= '2016-09-30'
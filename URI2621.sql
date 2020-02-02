select prod.name

from providers prov

inner join products prod
on prov.id = prod.id_providers

where prod.amount between 10 and 20 and prov.name like 'P%'
select cat.name, sum(prod.amount)
from products prod
inner join categories cat
on prod.id_categories = cat.id
group by cat.name
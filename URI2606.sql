select

    prod.id, 
    prod.name

from products prod

inner join categories cat
        on prod.id_categories = cat.id

where cat.name like 'super%'

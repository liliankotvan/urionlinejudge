select mov.id, mov.name
from movies mov

inner join prices pri
    on mov.id_prices = pri.id

where pri.value < '2.00'
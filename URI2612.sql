select mov.id, mov.name
from movies mov

inner join genres gen
    on mov.id_genres = gen.id
inner join movies_actors mova
    on mov.id = mova.id_movies
inner join actors act
    on act.id = mova.id_actors

where act.name in ('Marcelo Silva', 'Miguel Silva') 
and gen.description = 'Action'

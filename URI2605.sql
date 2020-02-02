/**
 * Escreva a sua solução aqui
 * Code your solution here
 * Escriba su solución aquí
 */
SELECT 
prod.name, prov.name
FROM products prod
inner JOIN providers prov
ON prod.id_providers = prov.id
WHERE prod.id_categories = 6
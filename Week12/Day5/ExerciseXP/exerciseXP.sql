--Exercise 1

SELECT * FROM public.items
ORDER BY item_price ASC

SELECT * FROM public.items WHERE (item_price >= 80)
ORDER BY item_price DESC

SELECT first_name, last_name From customers
ORDER BY first_name ASC LIMIT 3

SELECT last_name From customers
ORDER BY last_name DESC

--Exercise 2

SELECT * FROM customer

SELECT CONCAT_WS(' ',first_name, last_name) AS full_name FROM customer

SELECT DISTINCT create_date FROM customer

SELECT * FROM customer ORDER BY first_name DESC

SELECT film_id, title, description, release_year, rental_rate from film
ORDER BY rental_rate ASC

SELECT address, phone FROM customer INNER JOIN address ON customer.address_id=address.address_id
WHERE (district='Texas')

SELECT * FROM film WHERE (film_id=150 OR film_id=15)

SELECT film_id, title, description, length, rental_rate FROM film WHERE (title='Harry Potter')

SELECT film_id, title, description, length, rental_rate FROM film WHERE (title LIKE 'Ha%')

SELECT * FROM film ORDER BY rental_rate DESC LIMIT 10

SELECT * FROM film LEFT JOIN inventory ON film.film_id=inventory.film_id
WHERE inventory_id IS null

SELECT * FROM city INNER JOIN country ON city.country_id=country.country_id


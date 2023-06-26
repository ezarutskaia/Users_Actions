# Статистика по городам, сколько-откуда
SELECT city, COUNT(*) qty
FROM Users
GROUP BY city
ORDER BY qty DESC
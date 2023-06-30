# Статистика по городам, сколько-откуда
SELECT city, COUNT(*) qty
FROM Users
GROUP BY city
ORDER BY qty DESC

# Найти ботов в таблице Actions
WITH X AS
(SELECT USER, (maxi-mini) diff
FROM
(SELECT USER, TIME_TO_SEC(MIN(TIME)) 'mini', TIME_TO_SEC(MAX(TIME)) 'maxi'
FROM Actions
GROUP BY USER) Y)

SELECT USER, diff
FROM X
WHERE diff<5
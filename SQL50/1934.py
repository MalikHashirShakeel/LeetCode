# # Write your MySQL query statement below
# WITH ConfirmationCounts AS (
#     SELECT 
#         user_id,
#         COUNT(*) AS total_requests,
#         SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) AS confirmed_requests
#     FROM Confirmations
#     GROUP BY user_id
# )
# SELECT 
#     s.user_id,
#     COALESCE(ROUND(c.confirmed_requests / NULLIF(c.total_requests, 0), 2), 0) AS confirmation_rate
# FROM Signups s
# LEFT JOIN ConfirmationCounts c ON s.user_id = c.user_id
# ORDER BY s.user_id;

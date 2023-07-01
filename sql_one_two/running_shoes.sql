USE running_shoes;

SELECT 
	w.ID,
	w.title,
    w.price AS price_running_warehouse,
    r.price AS price_runrepeat,
    ROUND(ABS(w.price - r.price), 2) AS difference_dollars$,
    e.highest_similarity AS Similarity_percentage 
FROM webpage2_warehouse w
JOIN webpage1_runrepeat r
	ON 	w.ID = r.ID
JOIN equal_titles e
	ON e.ID = w.ID; 
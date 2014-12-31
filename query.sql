SELECT siteid from rainfall WHERE ST_DWithin(geom, ST_GeomFromText('POINT(120.221341 22.997255)', 4326), 1);

SELECT siteid, SUM(rainfall10min) from rainfall group by siteid HAVING sum(rainfall10min) > 0;

SELECT siteid, sum(rainfall10min) from rainfall group by siteid ORDER BY sum(rainfall10min) DESC LIMIT 1;

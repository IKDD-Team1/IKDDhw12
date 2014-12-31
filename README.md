Postgresql and PostGIS
========

## Requirement

(1) Install the Postgresql and PostGIS.

(2) Index the geometry(type GEOMETRY) attributes(column).

(3) Create your own database and table (no constraint on name), and write one or more program for inserting the “10 minutes rainfall" datas (csv files).

(4) Query:

1. Find “siteid" and SUM of the cumulative "rainfall10min" which the SUM value are more than zero.

2. Following the previous, find “siteid” and MAX of SUM of the cumulative “rainfall10min”.

3. Find all “siteid” within 10 km (about 0.1 in geometry distance) of NCKU location (22.997255, 120.221341).


## Dataset

+ Data Source: [click me] (http://opendata.epa.gov.tw/Data/Contents/RainTenMin/)
+ Download Dataset: [click me] (https://drive.google.com/file/d/0ByntzdeiRxfVN1V2YlFWSGVKcVE/view?usp=sharing)

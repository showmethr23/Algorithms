/*
    Weather Observation Station 2
*/

select round(sum(lat_n), 2), round(sum(long_w), 2) from station;
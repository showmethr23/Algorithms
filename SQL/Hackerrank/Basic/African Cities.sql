/*
    African Cities
*/

select city.name
from city 
left join country
on city.countrycode = country.code
where country.continent = "Africa";
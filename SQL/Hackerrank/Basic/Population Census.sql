/*
    Population Census
*/

select sum(city.population)
from city
left join country
on city.countrycode = country.code
where country.continent = "Asia";
select *
  from [E911Test].[dbo].[Export_Roads]
  order by OBJECTID DESC

select top 13 *
  from [E911Test].[dbo].[Export_Roads]
  WHERE (street like 'AIRPORT RD%' AND RLO = 2301) OR street like 'HWY%' or street like '%AVE'
  order by OBJECTID, street

select OBJECTID, count(OBJECTID) AS HMM
  from [E911Test].[dbo].[Export_Roads]
  group by OBJECTID
  having (count(OBJECTID) > 1)
  ORDER BY HMM
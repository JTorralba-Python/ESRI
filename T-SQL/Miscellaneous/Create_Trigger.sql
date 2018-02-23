declare @SQL as varchar(max)
/*set @SQL = 'select * from ' + @Add_Table*/
set @SQL = 'create trigger dbo.roadsegments_insert
	on A26
	for insert as
begin
	set nocount on;
	update A26
		set RoadSegmentID = GlobalID
		where ObjectID in (select ObjectID from inserted) and RoadSegmentID is null
end
'

/*print @SQL*/
exec (@SQL)
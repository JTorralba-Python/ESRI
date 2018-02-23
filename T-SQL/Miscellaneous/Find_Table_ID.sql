use E911Test

declare @registration_id as integer
declare @roadsegments as varchar(6)
declare @segmentnames as varchar(6)
declare @roadsegmentresponses as varchar(8)
declare @externalkeys as varchar(8)

set @registration_id = (select registration_id from sde.sde_table_registry where lower(table_name) like 'roadsegments')
set @roadsegments = 'A' + CONVERT(VARCHAR(6),(@registration_id))

set @registration_id = (select registration_id from sde.sde_table_registry where lower(table_name) like 'segmentnames')
set @segmentnames = 'A' + CONVERT(VARCHAR(6),(@registration_id))

set @registration_id = (select registration_id from sde.sde_table_registry where lower(table_name) like 'roadsegmentresponses')
set @roadsegmentresponses = 'A' + CONVERT(VARCHAR(6),(@registration_id))

set @registration_id = (select registration_id from sde.sde_table_registry where lower(table_name) like 'externalkeys')
set @externalkeys = 'A' + CONVERT(VARCHAR(6),(@registration_id))

print 'roadsegments = ' + @roadsegments
print 'segmentnames = ' + @segmentnames
print 'roadsegmentresponses = ' + @roadsegmentresponses
print 'externalkeys = ' + @externalkeys
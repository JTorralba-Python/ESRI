create trigger dbo.roadsegments_insert
	on A26
	for insert as
begin
	set nocount on;

	declare @globalid as uniqueidentifier
	declare @objectid as integer

	declare @sde_state_id as bigint
	select @sde_state_id = inserted.sde_state_id from inserted

	declare @roadsegmentid as uniqueidentifier
	select @roadsegmentid = inserted.roadsegmentid from inserted
	select @globalid = inserted.globalid from inserted

	/*if (@roadsegmentid is null or @roadsegmentid = @globalid)*/
	if @roadsegmentid is null
	begin

		set @roadsegmentid = @globalid
		update A26 set roadsegmentid = @roadsegmentid where objectid in (select objectid from inserted)

		exec sde.next_rowid 'dbo', 'segmentnames', @objectid OUTPUT
		set @globalid = NEWID()
		insert into A14 (roadsegmentid, sde_state_id, objectid, globalid) values (@roadsegmentid, @sde_state_id, @objectid , @globalid)

		declare @segmentnameid as uniqueidentifier
		set @segmentnameid = (select segmentnameid from A14 where roadsegmentid = @roadsegmentid and objectid = @objectid)

		exec sde.next_rowid 'dbo', 'roadsegmentresponses', @objectid OUTPUT
		set @globalid = NEWID()
		insert into A7 (roadsegmentid, sde_state_id, objectid, globalid) values (@roadsegmentid, @sde_state_id, @objectid , @globalid)

		declare @roadsegmentresponseid as uniqueidentifier
		set @roadsegmentresponseid = (select roadsegmentresponseid from A7 where roadsegmentid = @roadsegmentid and objectid = @objectid)

		exec sde.next_rowid 'dbo', 'externalkeys', @objectid OUTPUT
		set @globalid = NEWID()
		insert into A9 (roadsegmentid, sde_state_id, objectid, globalid, segmentnameid, roadsegmentresponseid) values (@roadsegmentid, @sde_state_id, @objectid , @globalid, @segmentnameid, @roadsegmentresponseid)

	end
end


create trigger dbo.segmentnames_insert
	on A14
	for insert as
begin
	set nocount on;
	update A14
		set SegmentNameID = GlobalID
		where ObjectID in (select ObjectID from inserted) and SegmentNameID is null
end


create trigger dbo.roadsegmentresponses_insert
	on A7
	for insert as
begin
	set nocount on;
	update A7
		set RoadSegmentResponseID = GlobalID
		where ObjectID in (select ObjectID from inserted) and RoadSegmentResponseID is null
end
create trigger dbo.Instead_Of
	on dbo.A26
	instead of insert as
begin
	set nocount on;
    declare @GlobalID uniqueidentifier
	declare @TestSegmentID uniqueidentifier
    select @GlobalID = inserted.GlobalID from inserted
	select @TestSegmentID = inserted.TestSegmentID from inserted

	if @TestSegmentID is NULL
	begin
		set @TestSegmentID = @GlobalID
	end

    insert into dbo.A26 (OBJECTID, TestSegmentID, created_date, created_user, last_edited_date, last_edited_user, SHAPE, GlobalID, SDE_STATE_ID) select inserted.OBJECTID, @TestSegmentID, inserted.created_date, inserted.created_user, inserted.last_edited_date, inserted.last_edited_user, inserted.SHAPE, inserted.GlobalID, inserted.SDE_STATE_ID from inserted

end
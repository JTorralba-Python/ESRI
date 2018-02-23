create function Point(@Line geometry, @Direction char)
returns geometry
as
begin
    declare @Point geometry
	if @Direction = 'S'
        set @Point = @Line.STStartPoint()
	else
		set @Point = @Line.STEndPoint()
	return (@Point)
end


create function Point_X (@Point geometry)
returns float
as
begin
	return (@Point.STX)
end


create function Point_Y (@Point geometry)
returns float
as
begin
	return (@Point.STY)
end


if object_id('Alt_Pre') is not null
   drop function dbo.Alt_Pre

create function Alt_Pre(@PrefixCode nvarchar(5), @GroupCode nvarchar(5))
returns nvarchar(10)
as
begin
	declare @Alt_Pre as nvarchar(10)
	set @Alt_Pre = (SELECT Alias FROM dbo.RoadNamePrefixAliases_evw WHERE PrefixCode = @PrefixCode and GroupCode = @GroupCode)
	return isnull(@Alt_Pre, @PrefixCode)
end


if object_id('Alt_Suf') is not null
   drop function dbo.Alt_Suf

create function Alt_Suf(@SuffixCode nvarchar(5), @GroupCode nvarchar(5))
returns nvarchar(10)
as
begin
	declare @Alt_Suf as nvarchar(10)
	set @Alt_Suf = (SELECT Alias FROM dbo.RoadNameSuffixAliases_evw WHERE SuffixCode = @SuffixCode and GroupCode = @GroupCode)
	return isnull(@Alt_Suf, @SuffixCode)
end


if object_id('Law_Response') is not null
   drop function dbo.Law_Response

create function Law_Response(@LawAreaID uniqueidentifier, @PSAP smallint)
returns nvarchar(30)
as
begin
	return (ISNULL((select Name from dbo.LawResponseAliases_evw where LawResponseAliasID in (SELECT LawResponseAliasID FROM dbo.LawResponseAreas_LawResponseAliases_evw WHERE LawResponseAreaID = @LawAreaID) and PSAP = @PSAP), ''))
end


if object_id('Fire_Response') is not null
   drop function dbo.Fire_Response

create function Fire_Response(@FireAreaID uniqueidentifier, @PSAP smallint)
returns nvarchar(30)
as
begin
	return (ISNULL((select Name from dbo.FireResponseAliases_evw where FireResponseAliasID in (SELECT FireResponseAliasID FROM dbo.FireResponseAreas_FireResponseAliases_evw WHERE FireResponseAreaID = @FireAreaID) and PSAP = @PSAP), ''))
end
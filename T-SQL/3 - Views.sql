USE [E911Test]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE VIEW [dbo].[Export_Roads]
AS
SELECT        dbo.RoadSegments_evw.OBJECTID, dbo.RoadSegments_evw.Shape, dbo.ExternalKeys_evw.ExternalKey AS ARCID, dbo.SegmentNames_evw.RoadNumber AS RDNAME, 
                         dbo.RoadSegments_evw.SegmentClass AS CLASS, dbo.RoadSegments_evw.OneWay, dbo.RoadSegments_evw.FromAddressLeft AS LLO, dbo.RoadSegments_evw.ToAddressLeft AS LHI, 
                         dbo.RoadSegments_evw.FromAddressRight AS RLO, dbo.RoadSegments_evw.ToAddressRight AS RHI, RTRIM(LTRIM(RTRIM(dbo.SegmentNames_evw.PrefixDescriptor) + ' ') 
                         + LTRIM(RTRIM(dbo.SegmentNames_evw.RoadName) + ' ') + LTRIM(RTRIM(dbo.SegmentNames_evw.SuffixDescriptor) + ' ')) AS STREET, dbo.RoadSegments_evw.ESNLeft AS LESN, 
                         dbo.RoadSegments_evw.ESNRight AS RESN, CITIES_L.CityName AS LTWN, CITIES_R.CityName AS RTWN, dbo.RoadSegments_evw.ZipLeft AS LZIP, dbo.RoadSegments_evw.ZipRight AS RZIP, 
                         dbo.RoadSegments_evw.Comments AS COM, dbo.RoadNames_evw.PrefixDirection AS PD, dbo.RoadNames_evw.PrefixCode AS PT, dbo.RoadNames_evw.SuffixDirection AS SD, 
                         dbo.RoadNames_evw.SuffixCode AS ST, dbo.RoadNames_evw.Name AS SN, dbo.RoadSegments_evw.ZFrom AS F_ELEV, dbo.RoadSegments_evw.ZTo AS T_ELEV, CITIES_L.CityCode AS LCITY, 
                         CITIES_R.CityCode AS RCITY, COUNTIES_L.CountyNumber AS LCOUNT, COUNTIES_R.CountyNumber AS RCOUNT, dbo.RoadSegments_evw.SegmentType AS SEGTYPE, dbo.RoadSegments_evw.EType, 
                         'CO' AS LSTATE, 'CO' AS RSTATE, RTRIM(LTRIM(RTRIM(dbo.SegmentNames_evw.PrefixDescriptor) + ' ') + LTRIM(RTRIM(dbo.RoadNames_evw.PrefixDirection) + ' ') 
                         + LTRIM(RTRIM(dbo.Alt_Pre(dbo.RoadNames_evw.PrefixCode, N'CSPD')) + ' ') + LTRIM(RTRIM(dbo.RoadNames_evw.Name) + ' ') + LTRIM(RTRIM(dbo.Alt_Suf(dbo.RoadNames_evw.SuffixCode, N'CSPD')) + ' ') 
                         + LTRIM(RTRIM(dbo.RoadNames_evw.SuffixDirection) + ' ') + LTRIM(RTRIM(dbo.SegmentNames_evw.SuffixDescriptor) + ' ')) AS PDFD_CAD, LTRIM(RTRIM(dbo.Alt_Suf(dbo.RoadNames_evw.SuffixCode, N'CSPD')) 
                         + ' ') AS PDFDST, LTRIM(RTRIM(dbo.Alt_Pre(dbo.RoadNames_evw.PrefixCode, N'CSPD')) + ' ') AS PDFDPT, 'R' AS LPARITY, 'R' AS RPARITY, '' AS IGNRALEFT, '' AS IGNRARIGHT, 
                         dbo.ExternalKeys_evw.ExternalKey AS EXTERNALST, dbo.RoadSegments_evw.SpeedLimit, dbo.Point_Y(dbo.Point(dbo.RoadSegments_evw.Shape, 'S')) AS FROM_LAT, 
                         dbo.Point_X(dbo.Point(dbo.RoadSegments_evw.Shape, 'S')) AS FROM_LONG, dbo.Point_Y(dbo.Point(dbo.RoadSegments_evw.Shape, 'E')) AS TO_LAT, dbo.Point_X(dbo.Point(dbo.RoadSegments_evw.Shape, 'E')) 
                         AS TO_LONG, dbo.Fire_Response(dbo.RoadSegmentResponses_evw.FireAreaIDLeft, 4) AS LRESP1, dbo.Fire_Response(dbo.RoadSegmentResponses_evw.FireAreaIDRight, 4) AS RRESP1, 
                         dbo.Law_Response(dbo.RoadSegmentResponses_evw.LawAreaIDLeft, 4) AS RESPONSEL1, dbo.Law_Response(dbo.RoadSegmentResponses_evw.LawAreaIDRight, 4) AS RESPONSER1
FROM            dbo.RoadNames_evw RIGHT OUTER JOIN
                         dbo.SegmentNames_evw ON dbo.RoadNames_evw.FullName = dbo.SegmentNames_evw.RoadName RIGHT OUTER JOIN
                         dbo.ExternalKeys_evw RIGHT OUTER JOIN
                         dbo.RoadSegments_evw LEFT OUTER JOIN
                         dbo.Counties_evw AS COUNTIES_R RIGHT OUTER JOIN
                         dbo.Cities_evw AS CITIES_R ON COUNTIES_R.CountyID = CITIES_R.CountyID ON dbo.RoadSegments_evw.CityIDRight = CITIES_R.CityID LEFT OUTER JOIN
                         dbo.Counties_evw AS COUNTIES_L RIGHT OUTER JOIN
                         dbo.Cities_evw AS CITIES_L ON COUNTIES_L.CountyID = CITIES_L.CountyID ON dbo.RoadSegments_evw.CityIDLeft = CITIES_L.CityID ON 
                         dbo.ExternalKeys_evw.RoadSegmentID = dbo.RoadSegments_evw.RoadSegmentID LEFT OUTER JOIN
                         dbo.RoadSegmentResponses_evw ON dbo.RoadSegments_evw.RoadSegmentID = dbo.RoadSegmentResponses_evw.RoadSegmentID ON 
                         dbo.SegmentNames_evw.RoadSegmentID = dbo.RoadSegments_evw.RoadSegmentID
GO
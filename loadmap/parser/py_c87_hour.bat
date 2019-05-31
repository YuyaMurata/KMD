set FILE_NAME=%1
echo FILE_NAME=%FILE_NAME%
set SCALE=h
rem output file delete
del %FILE_NAME%_output_hour.csv
rem date
.\parser\log_extract %FILE_NAME% %FILE_NAME%_output_hour.csv -start 0 -length 4 -graphType date
rem smr
.\parser\log_extract %FILE_NAME% %FILE_NAME%_output_hour.csv -start 1628 -length 4 -graphType count -graphName numOfSample -graphNameSub smr -scale %SCALE%
rem engine
.\parser\log_extract %FILE_NAME% %FILE_NAME%_output_hour.csv -start 1024 -length 480 -graphType 2dim -graphName 実エンジン回転VSエンジントルク -graphNameSub tgt↓Di→ -threshData_x 10,20,30,35,40,45,50,55,60 -threshData_y 1100,1300,1500,1700,1800,1900,2000,2100,2200,2300,2400  -scale %SCALE%
rem work
.\parser\log_extract %FILE_NAME% %FILE_NAME%_output_hour.csv -start 1632 -length 60 -graphType count -graphName 作業機操作状況 -threshData_x BOOM,ARM,BUCKET,SWING,TRAVEL,SERVICE,NEUTRAL,DECEL,HOIST,DOWN,DIGGING,BREAKER,Nothing,Hi,SWING_ONLY -scale %SCALE%
rem pump_max
.\parser\log_extract %FILE_NAME% %FILE_NAME%_output_hour.csv -start 1504 -length 36 -graphType 1dim -graphName ポンプ圧(MAX) -graphNameSub MAX -threshData_x 50,100,150,200,250,300,340,365 -scale %SCALE%
rem pump_f
.\parser\log_extract %FILE_NAME% %FILE_NAME%_output_hour.csv -start 1544 -length 36 -graphType 1dim -graphName ポンプ圧(F) -graphNameSub F -threshData_x 50,100,150,200,250,300,340,365 -scale %SCALE%
rem pump_r
.\parser\log_extract %FILE_NAME% %FILE_NAME%_output_hour.csv -start 1584 -length 36 -graphType 1dim -graphName ポンプ圧(R) -graphNameSub R -threshData_x 50,100,150,200,250,300,340,365 -scale %SCALE%
rem work_mode
.\parser\log_extract %FILE_NAME% %FILE_NAME%_output_hour.csv -start 1728 -length 16 -graphType count -graphName 作業モード選択状況 -threshData_x P,E,L,B -scale %SCALE%
rem temperature
.\parser\log_extract %FILE_NAME% %FILE_NAME%_output_hour.csv -start 1760 -length 256 -graphType 2dim -graphName エンジン水温VS作動油温 -graphNameSub cool↓hyd→ -threshData_x 0,20,60,80,100,105,120 -threshData_y 50,75,85,95,100,105,120 -scale %SCALE%
rem starter
.\parser\log_extract %FILE_NAME% %FILE_NAME%_output_hour.csv -start 1696 -length 4 -graphType count -graphName starterUseTimes -scale c
rem volume_f
.\parser\log_extract %FILE_NAME% %FILE_NAME%_output_hour.csv -start 2108 -length 128 -graphType 2dim -graphName ポンプ斜板(F) -graphNameSub press↓volme→ -threshData_x 29,43,57,71,85,99,113 -threshData_y 100,200,300 -scale %SCALE%
rem volume_r
.\parser\log_extract %FILE_NAME% %FILE_NAME%_output_hour.csv -start 2236 -length 128 -graphType 2dim -graphName ポンプ斜板(R) -graphNameSub press↓volme→ -threshData_x 29,43,57,71,85,99,113 -threshData_y 100,200,300 -scale %SCALE%
rem variable_matching
.\parser\log_extract %FILE_NAME% %FILE_NAME%_output_hour.csv -start 2364 -length 40 -graphType 1dim -graphName 可変マッチング -threshData_x 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9 -scale %SCALE%

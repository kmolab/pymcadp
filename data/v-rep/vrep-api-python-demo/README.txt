V-Rep API python binding demo
=============================

File:

* static/ - css
* templates/ - html 
* app.py - Flask web-application
* vrep_linefollower.py - simple V-REP python API wrapper for LineFollower

Copy in this folder following files from V-REP:

* remoteApi.so (from V-REP_PRO_EDU_V3_2_2_64_Linux/programming/remoteApiBindings/lib/lib/64Bit)
* vrep.py (from V-REP_PRO_EDU_V3_2_2_64_Linux/programming/remoteApiBindings/python/python)
* vrepConst.py (from V-REP_PRO_EDU_V3_2_2_64_Linux/programming/remoteApiBindings/python/python)

Start:

0. Files `remoteApi.so`, `vrep.py`, `vrepConst.py` have to be copied in this folder
1. Start V-REP
2. Place `LineFollower` model to scene
3. Remove all Lua program from `LineFollower`
4. Start Flesk web-application `python app.py`
5. Open browser at `http://localhost:5000`
6. Start V-REP simulation
7. Click on control buttons at web-page to controler LineFollower at V-REP scene






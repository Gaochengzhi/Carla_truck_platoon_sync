# Carla_Truck_Platoon
A full stack Platoon framework for Semi-trailer Truck in Carla Simulation

Pakaged version of carla with semi-trailer vehicle is released at google drive: 
https://drive.google.com/file/d/1TNenSlMxyTfZH50XkhW2_fQShRyXXgSt/view?usp=sharing

![](./assets/front.jpg)

## Quick start
first download the pakaged version of carla in the link above

then start the carla in one terminal
```
cd LinuxNoEditor
./CarlaUE4.sh -quality-level=High  

```

try to run the first demo

```
pip install -r requirements.txt
cd src
python3.8 setup.py build_ext --inplace
python3.8 main.py --log console --debug platoon   
```

### how to change the car-following mode?


in the /Carla_Truck_Platoon_sync/src/plan/carFollowingModel.py

change the class
```
line:129 class PATH_CACC:
```

then rerun the code

### Evaluation
```
cd Carla_Truck_Platoon_sync/tool
python3.8 process_trajectories.py
```

then you can get picture in the /res

### bug
There may be generate different waypoints due to different version of python boost libaray,
you first should 
```
cd /src/cache/sp_points
python3.8 plot.py
```

then choose the right start and end points in platoon.yml 



import time
import traci
import random
def adjust_platoon():
	v_ids=traci.vehicle.getIDList()
	for i,v_id in enumerate(v_ids):
		traci.vehicle.setSpeed(v_id,15)
		traci.vehicle.changeLane(v_id,0,duration="1.0")
		if i>0:
			lead=v_ids[i-1]
	
def v2v():
	v_ids=traci.vehicle.getIDList()
	for i,v_id in enumerate(v_ids):
		if i>0:
			lead=v_ids[i-1]
			lead_speed=traci.vehicle.getSpeed(lead)
			traci.vehicle.setParameter(v_id,"leader_speed",lead_speed)
def adj_speed():
	v_ids=traci.vehicle.getIDList()
	for i,v_id in enumerate(v_ids):
		if i>0:
			leader_speed=float(traci.vehicle.getParameter(v_id,"leader_speed"))
			tar=leader_speed-1
			traci.vehicle.setSpeed(v_id,tar)
def run_simulation(num_steps):
	for step in range(num_steps):
		traci.simulationStep()
		v2v()
		adj_speed()
def close_simulation():
	traci.close()
traci.start(["sumo-gui","-c","sample.sumocfg"])
try: 

	run_simulation(200)
	adjust_platoon()
finally:
	close_simulation()
	

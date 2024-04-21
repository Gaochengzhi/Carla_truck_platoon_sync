from agent.truck_vehicle_agent import TruckVehicleAgent
import time
import copy


class Platoon():
    def __init__(self, config, client, world):
        self.config = config
        self.plt_list = []
        self.world = world
        self.client = client
        self.spawn_platoon_agents(config)

    def spawn_platoon_agents(self, config):
        for i, start_end in enumerate(zip(config["spawn_list"], config["target_list"])):
            plt_member_config = copy.deepcopy(config)
            plt_member_config["name"] = f"p_{i}"
            plt_member_config["topology"] = {
                "index": i,
                "len": len(config["spawn_list"]),
                "LV": 0 if i > 0 else -1,
                "FV": i-1 if i > 0 else -1,
                "RV": i+1 if i+1 < len(config["spawn_list"]) else -1
            }
            plt_member_config["port"] = int(config["base_port"]+i)
            plt_member_config["start_point"] = start_end[0]
            plt_member_config["end_point"] = start_end[1]

            v= TruckVehicleAgent(plt_member_config, self.client, self.world)
            self.plt_list.append(v)

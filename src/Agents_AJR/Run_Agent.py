"""Custom Agent"""

from pysc2.agents import base_agent
from pysc2.env import sc2_env, run_loop
from pysc2.lib import actions, features, units
from absl import app
import random
import numpy as np

class RawAgent(base_agent.BaseAgent):
    def __init__(self):
        super(RawAgent, self).__init__()
        self.base_top_left = None

    def get_my_units_by_type(self, obs, unit_type):
        return [unit for unit in obs.observation.raw_units if unit.unit_type == unit_type and unit.alliance == features.PlayerRelative.SELF]

    def get_my_completed_units_by_type(self, obs, unit_type):
        return [unit for unit in obs.observation.raw_units if unit.unit_type == unit_type and unit.build_progress == 100 and unit.alliance == features.PlayerRelative.SELF]
    
    def get_distances(self, obs, units, xy):
        units_xy = [(unit.x, unit.y) for unit in units]
        return np.linalg.norm(np.array(units_xy) - np.array(xy), axis=1)

    def step(self, obs):
        super(RawAgent, self).step(obs)

        if obs.first():
            command_center = self.get_my_units_by_type(obs, units.Terran.CommandCenter)[0]
            self.base_top_left = (command_center.x < 32)

        depots = self.get_my_units_by_type(obs, units.Terran.SupplyDepot)
        completed_depots = self.get_my_completed_units_by_type(obs, units.Terran.SupplyDepot)
    
        barracks = self.get_my_units_by_type(obs, units.Terran.Barracks)
        completed_barracks = self.get_my_completed_units_by_type(obs, units.Terran.Barracks)
        
        free_supply = (obs.observation.player.food_cap - obs.observation.player.food_used)

        marines = self.get_my_units_by_type(obs, units.Terran.Marine)
        
        if len(depots) == 0 and obs.observation.player.minerals >= 100:
            scvs = self.get_my_units_by_type(obs, units.Terran.SCV)
            if len(scvs) > 0:
                SupplyDepot_xy = (22, 20) if self.base_top_left else (35, 42)
                distances = self.get_distances(obs, scvs, SupplyDepot_xy)
                SCV = scvs[np.argmin(distances)]
                return actions.RAW_FUNCTIONS.Build_SupplyDepot_pt("now", SCV.tag, SupplyDepot_xy)
        
        if (len(completed_depots) > 0 and len(barracks) == 0 and obs.observation.player.minerals >= 150):
            scvs = self.get_my_units_by_type(obs, units.Terran.SCV)
            if len(scvs) > 0:
                Barracks_xy = (22, 24) if self.base_top_left else (35, 45)
                distances = self.get_distances(obs, scvs, Barracks_xy)
                SCV = scvs[np.argmin(distances)]
                return actions.RAW_FUNCTIONS.Build_Barracks_pt("now", SCV.tag, Barracks_xy)
        
        if (len(completed_barracks) > 0 and obs.observation.player.minerals >= 100 and free_supply >= 2):
            Barracks = barracks[0]
            if Barracks.order_length < 5:
                return actions.RAW_FUNCTIONS.Train_Marine_quick("now", Barracks.tag)
        
        if free_supply < 2 and len(marines) > 0:
            attack_xy = (38, 44) if self.base_top_left else (19, 23)
            distances = self.get_distances(obs, marines, attack_xy)
            Marine = marines[np.argmax(distances)]
            x_offset = random.randint(-4, 4)
            y_offset = random.randint(-4, 4)
            return actions.RAW_FUNCTIONS.Attack_pt("now", Marine.tag, (attack_xy[0] + x_offset, attack_xy[1] + y_offset))
        return actions.RAW_FUNCTIONS.no_op()

    
def main(unused_argv):
    agent = RawAgent()
    try:
        while True:
            with sc2_env.SC2Env(
                map_name = "Simple64",
                players = [sc2_env.Agent(sc2_env.Race.terran), sc2_env.Bot(sc2_env.Race.protoss, sc2_env.Difficulty.very_easy)],
                agent_interface_format = features.AgentInterfaceFormat(action_space=actions.ActionSpace.RAW, use_raw_units=True, raw_resolution=64),
            ) as env:
                run_loop.run_loop([agent], env)
    except KeyboardInterrupt:
        pass
if __name__ == "__main__":
    app.run(main)
  
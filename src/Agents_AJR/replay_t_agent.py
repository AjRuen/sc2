"""Custom Agent for Training on Terran Pro Replays"""

from pysc2.agents import base_agent
from pysc2.env import sc2_env
from pysc2.lib import actions, features, units
from absl import app
import random

class Replay_T_Agent(base_agent.BaseAgent):

  def __init__(self):
    super(Replay_T_Agent, self).__init__()

  def step(self, obs):
    super(Replay_T_Agent, self).step(obs)
    
    # Get and return a random action (for debugging purposes)
    function_id = numpy.random.choice(obs.observation.available_actions)
    args = [[numpy.random.randint(0, size) for size in arg.sizes]
            for arg in self.action_spec.functions[function_id].args]

    return actions.FunctionCall(function_id, args)
  
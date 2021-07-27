"""Custom Agent"""

from pysc2.agents import base_agent
from pysc2.env import sc2_env
from pysc2.lib import actions, features, units
from absl import app
import random

class AJRAgent(base_agent.BaseAgent):

  def __init__(self):
    super(AJRAgent, self).__init__()
    print("THIS AGENT WAS INITIALIZED")

  def step(self, obs):
    super(AJRAgent, self).step(obs)
    # print observations :)
    print("PRINTING OBS MAYBE?:", obs)
    
    # Get and return a random action (for debugging purposes)
    function_id = numpy.random.choice(obs.observation.available_actions)
    args = [[numpy.random.randint(0, size) for size in arg.sizes]
            for arg in self.action_spec.functions[function_id].args]
    
    print("PREANG:", function_id, args)
    print("ANGRY:", actions.FunctionCall(function_id, args))
    return actions.FunctionCall(function_id, args)
  
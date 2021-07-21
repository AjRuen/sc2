"""Custom Agent"""

from pysc2.agents import base_agent
from pysc2.env import sc2_env
from pysc2.lib import actions, features, units
from absl import app
import random

class AJRAgent(object):

  def __init__(self):
    super(AJRAgent, self).__init__()

  def step(self, obs):
    super(AJRAgent, self).step(obs)
    
    return actions.FunctionCall(actions.FUNCTIONS.no_op.id, [])

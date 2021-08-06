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
    
    # Return no_op until agent can be trained using replays
    return actions.FunctionCall(actions.FUNCTIONS.no_op.id, [])
  
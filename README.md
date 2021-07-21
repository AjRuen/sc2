# sc2
# Links
+ [pysc2](https://github.com/deepmind/pysc2)
+ [Blizzard sc2client](https://github.com/Blizzard/s2client-proto#downloads)

## Syncing Agents to pysc2
The contents of your agents directory within the `src` directory should be copied to the `pysc2/agents/`
 folder in your local copy of the `pysc` package.
You might even consider creating a symbolic link (using my local agents folder as an example and beginning with `src` 
 as the working directory):
```bash
ln -s $(realpath Agents_AJR) /path/to/pysc2/agents/AJR
```

To run an agent, follow the instructions on the pysc2 repo. Normally this would look something like:
```shell
$ python -m pysc2.bin.agent --map CollectMineralShards --agent pysc2.agents.scripted_agent.CollectMineralShards
```
This can also be done for agents within linked folders. Again, using my folder as the example:
```shell
$ python -m pysc2.bin.agent --map Simple64 --agent pysc2.agents.AJR.random_agent.RandomAgent
```
# Links
+ [pysc2](https://github.com/deepmind/pysc2)
+ [Blizzard sc2client](https://github.com/Blizzard/s2client-proto#downloads)

# Setup
## Installation of Python Packages
Follow instructions on the pysc2 repo, this should also install any additional necessary packages.
Follow instructions on the Blizzard sc2client repo.
Any setup instructions given here will be for a linux OS however, there shouldn't be too many differences if using Windows.

## Syncing Agents to pysc2
The contents of your agents directory within the `src` directory should be copied to the `pysc2/agents/`
 folder in your local copy of the `pysc` package.
Alternatively, you might even consider creating a symbolic link (using my local agents folder as an example and beginning with `src` 
 as the working directory):
```bash
ln -s $(realpath Agents_AJR) /path/to/pysc2/agents/AJR
```

# Running Agents
To run an agent, follow the instructions on the pysc2 repo. Normally this would look something like:
```shell
$ python -m pysc2.bin.agent --map CollectMineralShards --agent pysc2.agents.scripted_agent.CollectMineralShards
```
This can also be done for agents within linked folders. Again, using my folder as the example:
```shell
$ python -m pysc2.bin.agent --map Simple64 --agent pysc2.agents.AJR.random_agent.RandomAgent
```

## Running agents through script
You might consider putting the run command into a script for ease of use, especially in cases where you have a lot of 
 arguments in the command. For example, if wanted to specify that my agent will always be Terran and play against a 
 very easy bot I could use:
```shell
$ echo "python -m pysc2.bin.agent --map Simple64 --agent pysc2.agents.AJR.random_agent.RandomAgent --agent_race terran --difficulty very_easy" > script-name.sh
```
This copies the command into a script in the working directory. Next, make the script executable using:
```shell
$ chmod +x script-name.sh
```
And then I can run:
```shell
$ ./script-name.sh
```

# Coding Conventions Courtesy of Tyler
## Branches
When developing we must be sure to not lose track of or lose sight of our work.
Thus, we will be using the following branches
+ main
  + Code from development is merged here. This code will be the latest stable 
work.  
+ development
  + Code from feature branches is merged here. This code will be the latest and
(hopefully) greatest.
+ <feature_branch>
  + There will be several of these branches, named after what "feature" is 
  being attempted. They may link to several issues. The "feature" in question
  may also be a "bug".

## Github Issues
We need to keep our work organized and our plans transparent. Github issues 
should thus be created not only for real "issues" like bugs, but also ideas and
plans.
For the moment we are simply planning on having several free floating issues 
that will link to each other when appropriate.
If deemed beneficial we may shift to projects.
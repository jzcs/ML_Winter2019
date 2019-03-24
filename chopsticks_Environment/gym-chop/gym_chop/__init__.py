from gym.envs.registration import register

register(
    id='chop-v0',
    entry_point='gym_chop.envs:ChopStick',
)

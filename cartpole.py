# Import the gym library
import gymnasium as gym
# Import the time module
import time

# Create a CartPole environment with human rendering
env = gym.make("CartPole-v1", render_mode="human")

# Reset the environment to its initial state
env.reset()

# Render the environment to display it on screen
env.render()

# Print the observation space, which is continuous
print(env.observation_space)

# Print the action space
print(env.action_space)

# Reset the environment again
env.reset()

# Define the number of episodes and timesteps per episode
n_episodes = 50
n_timesteps = 50

# Loop through each episode
for i in range(n_episodes):
    Return = 0  # Initialize the return for this episode
    
    # Loop through each timestep in the episode
    for t in range(n_timesteps):
        env.render()  # Render the environment to display it
        
        # Choose a random action from the action space
        rnd_action = env.action_space.sample()
        
        # Take a step in the environment with the random action
        next_state, reward, done, infor, prob = env.step(rnd_action)
        
        # Update the cumulative return for this episode
        Return = Return + reward
        
        # Check if the episode is done, and if so, reset the environment
        if done:
            env.reset()
            break
        
        # Print episode information every 10 episodes
        if i % 10 == 0:
            print("Episode : {}, Return : {}".format(i+1, Return))

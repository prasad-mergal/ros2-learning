# ROS2 Learning Projects

Hands-on ROS2 (Jazzy) projects built while learning robotics fundamentals, running on Ubuntu 24.04 via WSL2.

## Packages

### my_package
A custom ROS2 Python node (`square_drawer`) that publishes velocity commands to `/turtle1/cmd_vel` in Turtlesim, making the turtle draw a square autonomously — no manual keyboard control.

**Concepts covered:** ROS2 nodes, publishers, the `geometry_msgs/Twist` message type, workspace/package structure with `colcon`.

### first_package
Early practice package covering basic publisher/subscriber patterns.

## Setup
```bash
cd ~/workspace
colcon build
source install/setup.bash
```

## Run the square-drawer
```bash
# Terminal 1
ros2 run turtlesim turtlesim_node

# Terminal 2
ros2 run my_package my_node
```

## What I'm learning next
- Using pose feedback (`/turtle1/pose`) instead of timing-based movement
- ROS2 parameters (polygon-drawer project)
- Gazebo simulation with a real robot model

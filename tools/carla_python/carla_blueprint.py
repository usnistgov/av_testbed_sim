#!/usr/bin/env python3

import time
import math
import random
import carla


if __name__ == '__main__':

    actors = []

    try:
        # ------------------------------------------------
        # Client and world
        # ------------------------------------------------
        # Connect to the client and retrieve the world object
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)
        # world = client.load_world("Town03")
        world = client.get_world()
        spectator = world.get_spectator()
        actors.append(spectator)

        # ------------------------------------------------
        # NPC vehicles
        # ------------------------------------------------
        # # Get the blueprint library and filter for the vehicle blueprints
        vehicle_blueprints = world.get_blueprint_library().filter('*vehicle*')

        # # Get the map's spawn points
        spawn_points = world.get_map().get_spawn_points()

        # Spawn 10 vehicles randomly distributed throughout the map
        # for each spawn point, we choose a random vehicle from the blueprint library
        for _ in range(5):
            world.try_spawn_actor(random.choice(vehicle_blueprints), random.choice(spawn_points))

        for vehicle in world.get_actors().filter('*vehicle*'):
            vehicle.set_autopilot(True)

        # ------------------------------------------------
        # Ego vehicle
        # ------------------------------------------------
        # Get the map's spawn points
        spawn_points = world.get_map().get_spawn_points()
        ego_bp = world.get_blueprint_library().find('vehicle.lincoln.mkz_2020')
        ego_bp.set_attribute('role_name', 'hero')
        ego_vehicle = world.spawn_actor(ego_bp, random.choice(spawn_points))
        ego_vehicle.set_autopilot(True)
        actors.append(ego_vehicle)

        # ------------------------------------------------
        # Add sensors to the ego vehicle
        # ------------------------------------------------
        # Create a transform to place the camera on top of the vehicle
        camera_init_trans = carla.Transform(carla.Location(z=1.5))
        # We create the camera through a blueprint that defines its properties
        camera_bp = world.get_blueprint_library().find('sensor.camera.rgb')
        # We spawn the camera and attach it to our ego vehicle
        camera = world.spawn_actor(camera_bp, camera_init_trans, attach_to=ego_vehicle)

        # ------------------------------------------------
        # Spectator
        # ------------------------------------------------

        # while True:
        #     # set the spectator to follow the ego vehicle
        #     spectator = world.get_spectator()
        #     transform = ego_vehicle.get_transform()
        #     spectator.set_transform(carla.Transform(transform.location + carla.Location(z=15),
        #                                             carla.Rotation(yaw=90, pitch=-90)))

    finally:
        print('Destroying actors')
        for actor in actors:
            actor.destroy()
        print('Done.')

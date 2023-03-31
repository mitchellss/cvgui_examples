from datetime import datetime
from random import randrange
import cvgui
import numpy as np
from haptic_glove import HapticGlove

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_FPS = 60


def main() -> None:

    # Specify input as a webcam and computer vision model as blazepose
    frame_input: cvgui.FrameInput = cvgui.Webcam(device_num=0, fps=30)
    cv_model: cvgui.CVModel = cvgui.BlazePose()

    # Create a pose generator based on a webcam + blazepose
    pose_input: cvgui.PoseGenerator = cvgui.ComputerVisionPose(
        frame_input=frame_input, model=cv_model)

    # Specify GUI to be pygame
    ui: cvgui.UserInterface = cvgui.PyGameUI(
        width=WINDOW_WIDTH, height=WINDOW_HEIGHT, fps=WINDOW_FPS)

    # Create activity
    activity = cvgui.Activity(pose_input=pose_input, frontend=ui)

    """
    haptic_glove = HapticGlove("172.16.1.2", 8888)
    try:
        haptic_glove.connect()
    except Exception as e:  # noqa
        print("Connecting to the glove failed. Make sure you are on "
              "the right network and the glove's light is green before "
              f"attempting to connect. \nThe error was: \n{e}\n")
        raise e
    """

    # Create a new scene
    scene_1 = cvgui.Scene()
    activity.add_scene(scene_1)

    # Create a new button
    button_1: cvgui.Button = cvgui.button(gui=ui,
                                          pos=(WINDOW_WIDTH//2,
                                               WINDOW_HEIGHT//2),
                                          activation_distance=50,
                                          color=(255, 0, 0, 255),
                                          radius=50)
    hand_bubble_1: cvgui.TrackingBubble = cvgui.tracking_bubble(
        gui=ui,
        radius=40,
        target=cv_model.LEFT_HAND,
        color=(255, 0, 0, 255))

    times = [datetime.now(), datetime.now()]

    def callback() -> None:
        # Move the button to a random position that is at least 300 pixels away
        min_distance = 300
        old_pos = button_1.pos
        new_pos = (randrange(600, 1000, 20), randrange(200, 600, 20))
        while abs(old_pos[0] - new_pos[0]) < min_distance \
                and abs(old_pos[1] - new_pos[1]) < min_distance:
            new_pos = (randrange(600, 1000, 20), randrange(200, 600, 20))
        button_1.pos = new_pos

        times[1] = datetime.now()
        print(times[1]-times[0])
        times[0] = datetime.now()

    def frame_callback() -> None:
        current_pos = np.array(
            [0, skeleton.skeleton_points[cv_model.LEFT_HAND][0],
             skeleton.skeleton_points[cv_model.LEFT_HAND][1]]
        )
        target_pos = np.array([0, button_1.pos[0], button_1.pos[1]])

        """
        haptic_glove.send_pull_feedback(current_pos, target_pos)
        """

    # Set the button to be clicked using the user's left hand
    button_1.targets = [cv_model.LEFT_HAND]

    # Link the callback function to the button
    button_1.callback = callback

    # Create a skeleton to display pose points
    skeleton: cvgui.Skeleton = cvgui.skeleton(
        gui=ui, pos=(800, 600), scale=cv_model.DEFAULT_SCALE)

    # Add the skeleton and button to the scene
    scene_1.add_component(button_1)
    scene_1.add_component(hand_bubble_1)
    scene_1.add_component(skeleton)

    scene_1.frame_callback = frame_callback

    # Start activity
    activity.run()


# This name == main line is required for windows multiprocessing
if __name__ == "__main__":
    main()

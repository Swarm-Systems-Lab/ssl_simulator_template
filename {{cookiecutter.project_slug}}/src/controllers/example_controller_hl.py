__all__ = ["ExampleControllerHL"]

import numpy as np
from ssl_simulator import Controller

class ExampleControllerHL(Controller):
    def __init__(self, context, low_level_ctrl_key, omega = np.pi/10):
        super().__init__(context)

        # Controller settings
        self.low_level_ctrl_key = low_level_ctrl_key
        self.omega = omega

        # Controller variables
        self.dummy_cmd = None

        # ---------------------------        
        # Controller variables to be tracked by logger
        self.tracked_vars = {
            "cmd": lambda: self.dummy_cmd,
        }

        self.tracked_settings = {
            "omega": self.omega,
        }
        # ---------------------------

    def compute_control(self, time, dt):
        omega = np.pi/10
        self.dummy_cmd = np.array([np.cos(time*omega), np.sin(time*omega)])
        self.context.call_interface(self.low_level_ctrl_key, "_example_interface", self.dummy_cmd)
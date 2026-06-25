__all__ = ["ExampleController"]

import numpy as np
from ssl_simulator import Controller


class ExampleController(Controller):
    def __init__(self, context, kw=1):
        super().__init__(context)

        # Controller settings
        self.kw = kw

        # Controller variables
        self.dummy_cmd = np.ones((1, 2))
        self.ctrl_u = None

        # ---------------------------
        # Controller output variables
        self.control_vars = {
            "u": lambda: self.ctrl_u,
        }

        # Controller variables to be tracked by logger
        self.tracked_vars = {
            "cmd": lambda: self.dummy_cmd,
        }

        self.tracked_settings = {
            "kw": self.kw,
        }
        # ---------------------------

        # Controller interface for other controller to interact with it
        self.register_interface(self._example_interface)

    def _example_interface(self, cmd):
        self.dummy_cmd = cmd

    def compute_control(self, time, dt):
        #state = self.context.get_robot_state()
        #state["p"]
        self.ctrl_u = self.kw * self.dummy_cmd

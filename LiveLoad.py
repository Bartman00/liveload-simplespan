'''
Live load definition
'''

class LiveLoad():

    # Change this to a dictionary with current values as keys
    # and values = types.
    valid_keys = [
        "name",
        "agency",
        "axle_load",
        "axle_spacing",
        "distributed_load",
        "distributed_shear_concentrated",
        "distributed_moment_concentrated",
        "truck_distributed_interaction",
        "impact",
        "impact_behavior",
        "children_live_loads"
    ]
    def __init__(self, **kwargs):

        for k, v in kwargs.items():

            # Check if a valid key
            if k not in self.valid_keys:
                raise ValueError(f"{k} is an invalid input. Valid keys include {self.valid_keys}")

            # Check if input is the correct type

            # Assign to this object
            setattr(self, k, v)


if __name__ == '__main__':
    print("Is running")
    live_load = LiveLoad(name='MyTruck', axle_load=[])
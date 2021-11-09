"""Support for Eufy switches."""
import lakeside

from homeassistant.components.switch import SwitchEntity


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up Eufy switches."""
    if discovery_info is None:
        return
    add_entities([EufySwitch(discovery_info)], True)


class EufySwitch(SwitchEntity):
    """Representation of a Eufy switch."""

    def __init__(self, device):
        """Initialize the light."""

        self._state = None
        self._name = device["name"]
        self._address = device["address"]
        self._code = device["code"]
        self._type = device["type"]
        self._switch = lakeside.switch(self._address, self._code, self._type)
        self._switch.connect()

    def update(self):
        """Synchronise state from the switch."""
        self._switch.update()
        self._state = self._switch.power

    @property
    def unique_id(self):
        """Return the ID of this light."""
        return self._address

    @property
    def name(self):
        """Return the name of the device if any."""
        return self._name

    @property
    def is_on(self):
        """Return true if device is on."""
        return self._state

    def turn_on(self, **kwargs):
        """Turn the specified switch on."""
        try:
            self._switch.set_state(True)
        except BrokenPipeError:
            self._switch.connect()
            self._switch.set_state(power=True)

    def turn_off(self, **kwargs):
        """Turn the specified switch off."""
        try:
            self._switch.set_state(False)
        except BrokenPipeError:
            self._switch.connect()
            self._switch.set_state(False)

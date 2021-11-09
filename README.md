# HA-Eufy-Integration
Fixed version of the Eufy Light/Switch integration for Home Assistant, originally written by @Frenck

Tested on HassOS

This is a near direct clone of https://github.com/home-assistant/core/tree/dev/homeassistant/components/eufy, but with manifest.json modified to include the requirements for Lakeside to work. You might not need setuptools in there but I left it in anyway just in case.

This is a workaround for people experiencing this issue: https://github.com/home-assistant/core/issues/33605 until such a time as an official fix is coded.

To install:
* Make a new directory in your <config_dir>/custom_components folder called 'eufy'
* Download the contents of this repo to that folder
* Restart Home Assistant

You do not need to modify your configuration.yaml.

Custom components with the same name as built-in components take precedence by default.

If you're a HA dev and you're reading this, my changes to manifest.json should solve the problem everyone's having. Please fix this issue in the official build.

Use at your own risk. I am by no means a programmer at all, I just read somewhere that this should fix it.

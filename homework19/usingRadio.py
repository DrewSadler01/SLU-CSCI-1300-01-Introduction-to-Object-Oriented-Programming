# Line 2: constructor must be named "__init__" not "init"
# Line 10:  _station is not defined, so it's supposed to be self._station and not _station
# Line 12: "_ind" is not a part of "Radio", so it's supposed to be _presets[ind] and not _presets[self._ind]
# Line 13: Indentation of this line wasn't far enough, not matching the rest of the class
# Line 17: No use of colon at the end of the block, so a new one cannot be started
# Line 20: Indentation of the body doesn't match other body indentations, but doesn't really matter

from Radio import Radio

radio=Radio()
radio.togglePower()
radio.setPreset(2)
radio.gotoPreset(1)
radio.increaseVolume()
radio.decreaseVolume()
radio.increaseStation()
radio.decreaseStation()
print("Everything is working good!")

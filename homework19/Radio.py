class Radio:
    def __init__(self):             
        self._powerOn = False
        self._volume = 5
        self._station = 90.7
        self._presets = [ 90.7, 92.3, 94.7, 98.1, 105.7, 107.7 ]  
    def togglePower(self):
        self._powerOn = not self._powerOn      
    def setPreset(self, ind):
        self._presets[ind] = self._station  
    def gotoPreset(self, ind):
        self._station = self._presets[ind] 
    def increaseVolume(self):                       
        self._volume = self._volume + 1
    def decreaseVolume(self):
        self._volume = self._volume - 1    
    def increaseStation(self):              
        self._station = self._station + .2
    def decreaseStation(self):
        self._station = self._station - .2

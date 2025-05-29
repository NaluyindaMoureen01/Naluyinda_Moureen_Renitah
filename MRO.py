#Method Resolution Order 
#Real life scenario
class Device:
    def __init__(self, name):
        self.name = name

    def power_on(self):
        print(f"{self.name} is powering on.")

    def power_off(self):
        print(f"{self.name} is powering off.")

    def status(self):
        print(f"{self.name} is generally working perfectly.")

class Speaker(Device):
    def __init__(self, name, volume=50):
        super().__init__(name)
        self.volume = volume

    def play_audio(self, song):
        print(f"{self.name} playing '{song}' at volume {self.volume}.")

    def status(self): # Overrides Device's status
      print(f"{self.name} are ready for audio playback.")
    
class Display(Device):
    def __init__(self, name, brightness=80):
        super().__init__(name)
        self.brightness = brightness

    def show_content(self, content):
        print(f"{self.name} displaying: '{content}' with brightness {self.brightness}%.")

    def status(self): # Overrides Device's status
        print(f"{self.name} is ready to show content.")

class SmartHub(Speaker, Display): # Inherits from both Speaker and Display
    def __init__(self, name):
        # MRO determines the order of calling super().__init__()
        # Speaker's __init__ will be called first,
        super().__init__(name)
        Speaker.__init__(self, name) # Call Speaker's init 
        Display.__init__(self, name) # Call Display's init 

    def send_notifications(self, message):
        print(f"{self.name} sending notification: {message}")

# The MRO of SmartHub
print(f"MRO of SmartHub: {SmartHub.__mro__}\n")

# Create objects
device = Device("Generic Gadget")
speaker = Speaker("Soundbars")
display = Display("Smart Screen")
smart_hub = SmartHub("Central Hub")

device.status()
speaker.status()
display.status()
smart_hub.status() # Which status method will be called?

print("\n--- Using SmartHub ---\n")

smart_hub.play_audio("Morning Playlist")
smart_hub.show_content("Weather Forecast")
smart_hub.send_notifications("New email received!")
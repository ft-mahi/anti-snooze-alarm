# main.py
import datetime
import time
from pygame import mixer
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

from config import ALARM_TIME, SECRET_KEY

def force_max_windows_volume():
    """Forces Windows Master Volume to 100% and unmutes it."""
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMute(0, None)                         # Unmute Windows
        volume.SetMasterVolumeLevelScalar(1.0, None)    # Force 100% Volume
    except Exception as e:
        pass # Ignore errors if audio drivers momentarily glitch

def run_text_alarm():
    print(f"⏰ Text-input Alarm Active. Armed for {ALARM_TIME}...")
    
    mixer.init()
    
    # Ensure you have a loud 'alarm.mp3' file inside this exact folder!
    try:
        mixer.music.load("alarm.mp3") 
    except:
        print("⚠️ Warning: 'alarm.mp3' not found in this folder. Script will run silently.")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        
        if current_time == ALARM_TIME:
            print("\n🚨🚨🚨 WAKE UP!!! 🚨🚨🚨")
            
            try:
                mixer.music.play(-1) # Loop audio indefinitely
            except:
                pass
            
            # Lock the user in a loop until they type the exact string
            while True:
                # Force volume to max right before asking for input
                force_max_windows_volume()
                
                # Prompt the user in the terminal
                user_input = input(f"Type '{SECRET_KEY}' to turn off the alarm: ")
                
                # Strip spaces and normalize to prevent minor typing typos from driving you crazy
                if user_input.strip() == SECRET_KEY:
                    print("\n✅ Correct! Alarm deactivated. Good morning.")
                    mixer.music.stop()
                    return # Exit the script entirely
                else:
                    print("❌ Wrong phrase! Try again.")
                    # Keep looping, volume will stay locked at 100%
        
        # Sleep for 5 seconds between checking the system clock
        time.sleep(5)

if __name__ == "__main__":
    run_text_alarm()
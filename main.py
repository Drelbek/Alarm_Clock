import time
import datetime
import pygame
import os

def set_alarm(alarm_time, sound_file):
    try:
        if not os.path.exists(sound_file):
            print("Error: Sound file does not exist.")
            return

        print(f"Alarm set for {alarm_time}")
        
        is_running = True
        while is_running:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Current Time: {current_time}", end="\r")  # Update time without clearing the screen

            if current_time == alarm_time:
                print("\nWake up! 😫😫")
                pygame.mixer.init()
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()

                print("Press Ctrl+C to stop the alarm.")
                try:
                    while True:
                        time.sleep(1)  # Keep the program running until the alarm finishes
                        if not pygame.mixer.music.get_busy():
                            break
                except KeyboardInterrupt:
                    pygame.mixer.music.stop()
                    print("\nAlarm stopped.")

                is_running = False
            
            time.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("\nExiting alarm clock.")

if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    sound_file = input("Enter the path to the sound file: ")
    set_alarm(alarm_time, sound_file)
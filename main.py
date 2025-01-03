import time
import datetime
import pygame
import os

def set_alarm(alarm_time):
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Alarm set for {alarm_time}")
    sound_file = "D:/Python/Alarm_Clock/Going_Home.mp3"

    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        

        if current_time == alarm_time:
            print("Wake up 😫😫")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False
        
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
#  Copyright 2016 Felix Koeth <fe.koeth@gmx.de>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
import time
import re
import configparser
import os
import pathlib

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

#Function loads soundfile and returns pygame.mixer object
def load_sound(filename_soundfile:str) -> pygame.mixer.Sound:

        sound_countdown = pygame.mixer.Sound(filename_soundfile)

        try:
                sound_countdown = pygame.mixer.Sound(filename_soundfile)

                return sound_countdown

        except:

                raise FileNotFoundError("Error, could not load " + filename_soundfile)

#Input mixer object. Plays object and waits until finished
def playwait(sound_mixer:pygame.mixer.Sound) -> bool:

        try:
                sound_mixer.play()
                time.sleep(sound_mixer.get_length())
        except:
                return False

        return True


def load_default_sounds(list_of_sounds:list[pathlib.Path],sound_vol:float = 100.0) -> list[list[pygame.mixer.Sound],list[float]]:

                sounds_list = [load_sound(i) for i in list_of_sounds]
                sounds_list_len = []

                for i in range(len(sounds_list)):

                        sounds_list_len.append(sounds_list[i].get_length())

                        sounds_list[i].set_volume(sound_vol/100.0)

                return [sounds_list,sounds_list_len]

def sleep_and_play(time_total:int,sound:pygame.mixer.Sound,sound_length:float) -> bool:

        time.sleep(time_total-sound_length)

        playwait(sound)

        return True

def main(args):

        configfile = "config.ini"

        if "-c" in args:
                configfile = args[args.index("-c")+1]

        config = configparser.ConfigParser()
        config.read(configfile)

        if "-s" in args:
                program_string = args[args.index("-s")+1]
        else:
                program_string = config["Default"]["pattern"]

        soundfolder = pathlib.Path(config["Default"]["Soundfolder"])
        pygame.init()
        sound_vol = 100

        keys = [i for i in config["Sounds"].keys()]
        folders = [soundfolder/config["Sounds"][i] for i in keys]

        sounds_list,sounds_list_len  = load_default_sounds(folders,sound_vol)

        sound_dict =  dict(zip(keys,sounds_list))
        length_dict = dict(zip(keys,sounds_list_len))

        times = []
        sounds = []
        partitions = program_string.split(";")

        for partition in partitions:

                partition = partition.split(":")
                num_repeat = int(partition[0])
                time_set = partition[1].split(",")

                times_x = [int(re.findall(r'\d+',x)[0]) for x in time_set]
                sounds_x = [x[-1] for x in time_set]

                times = times + num_repeat*times_x
                sounds = sounds + num_repeat*sounds_x

        print(f"Hi, this will take about {int(round(sum(times)/60,0))} Minutes. Have fun ;-)")

        for i in range(len(times)):
                sleep_and_play(times[i],sound_dict[sounds[i]],length_dict[sounds[i]])

        return 0

if __name__ == '__main__':
        import sys
        sys.exit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#
#  Copyright 2019 Josh <robotkid450@gmail.com>
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

import vs_control as vs
import sys
import argparse


scalerSources = ['CV', 'YC', 'YPrPb', 'VGA', 'HDMI']
scalerResolutions = ['Native', 'VGA', 'SVGA', 'XVGA', 'SXGA', 'UXGA', '480I', '480P', '720P60', '1080I60', '1080P60', 'WXGA', 'WSXGA', 'WUXGA', 'XGA+']
scalerModes = ['FULL', 'OVERSCAN', 'UNDERSCAN', 'LETTERBOX', 'PANSCAN', 'FOLLOW']



parser = argparse.ArgumentParser(description='Control tv one task 658 scaler via RS-232')
parser.add_argument('-d', '--device', help="Serial port that is connected to scaler.", required=True)
subparsers = parser.add_subparsers()
parserInput = subparsers.add_parser("source", help="Select which input the scaler should use.")
parserInput.add_argument("Video_source", help="The video source used by the scaler  WIP: List all inputs", choices=scalerSources)
parserResolution = subparsers.add_parser("resolution", help="Set the resolution the scaler outputs.")
parserResolution.add_argument("Video_resolution", help="Set output resolution of scaler.", choices=scalerResolutions)
parserScaling = subparsers.add_parser("scaling", help="Set scaling mode used.")
parserScaling.add_argument("scaling_mode", help="Sets scaling mode.", choices=scalerModes)

args = parser.parse_args()
#print(args)

vargs = vars(args)

device = vargs['device']
del vargs['device']

for x in vargs:
    command = x
    data = vargs[x]

#print(device)
#print(command)
#print(data)


sc = vs.scaler_connection(device)
sc._connect()

if command == 'Video_source':
    sc.setSource(data)
    
if command == 'Video_resolution':
    sc.setOutput(data)

if command == 'scaling_mode':
    sc.setSize(data)

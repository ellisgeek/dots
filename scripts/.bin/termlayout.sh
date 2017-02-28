#!/bin/sh
i3-msg workspace 2:TERM
i3-msg exec urxvt
i3-msg split h
i3-msg exec urxvt
i3-msg split v
i3-msg exec urxvt

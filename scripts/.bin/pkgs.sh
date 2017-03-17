#/bin/bash

pkgs=$(pacman -Qq)
pkgsfile=manjaro-xfce-16.10.3-stable-x86_64-pkgs.txt # File containting the default packages included in the build (get from SourceForge)

#make the magic happen (show only only packages that are not part of the vanilla install.
diff -U $(wc -l < $pkgs) $pkgs $(sed 's/ .*$//' < $pkgsfile) | grep '^-' | sed 's/^-//g' > packages-manjaro-xfce.txt
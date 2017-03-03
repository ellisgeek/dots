mkdir ~/.userdirs.old
for dir in Downloads Templates Public Documents Music Pictures Videos
    if test -d ~/$dir
        mv ~/$dir ~/.userdirs.old/$dir
    end
    ln -s /media/fixed/media/Home/$dir ~/$dir
end

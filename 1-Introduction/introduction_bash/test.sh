LISTE="alice sasha olive"

for USER in $LISTE
do
    while ! id $USER
    do
        sleep 1
    done
    sleep 1
done
sleep 1

cd /
tar -pxjf /tmp/home.tar.bz2

for USER in $LISTE
do
    cp /home/packer/.bashrc /home/$USER/
    echo . /etc/profile >> /home/$USER/.bashrc
    cp /home/packer/.profile /home/$USER/
    chown -R $USER:$USER /home/$USER
done

su - sasha
PS1='\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]$(pwd)\[\033[00m\]\$ '
clear

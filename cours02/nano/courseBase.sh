#!/bin/bash

MYUSER=sasha
MYMDP=sasha
MYGROUP=sasha

#création de l'utilisateur
useradd -s /bin/bash -G root -m -U $MYUSER
# Ajout au groupe
usermod -aG $MYGROUP $MYUSER
# attribution du mdp
echo -e '$MYMDP\n$MYMDP' | passwd $MYUSER
# config du profile
cp /home/packer/.bashrc /home/$MYUSER/
echo . /etc/profile >> /home/$MYUSER/.bashrc
cp /home/packer/.profile /home/$MYUSER/
# transfert des droits
chown -R $MYUSER:$MYUSER /home/$MYUSER

# fin de la config
echo 'done' > /tmp/.fini

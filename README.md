# calculus_transistor
Calculateur de paramètres statiques et dynamiques pour des montages à transistor.

Ce programme permet, pour 4 types de montage, de calculer les paramètres statique et dynamique. Les montages sont : 
- Emetteur commun NON dégénéré. 
- Emetteur commun dégénéré.
- Collecteur commun. 
- Base commune.
Les paramètres calculer sont : 
- Source de Thevenin *Vth*
- Résistance équivalente de Thevenin *Rth*
- Le courant de polarisation *Icq*
- La tension de polarisation *Vceq*
- La transconductance *Gm*
- La résistance de base *rb*
- La résistance de collecteur *r0*
- La résistance d'entrée du montage *ZE*
- La résistance de sortie du montage *ZS*
- Le gain intrinséque *AV*
- Le gain composite *GV*

Le programme permet également de tracer la de charge dynamique et la droite de charge statique. 

Les montages sont décomposés par bloc. Ils se trouvent dans le dossier ***/montages_transistor.***
Vous pouvez vous en servir comme librairie pour vos projets.

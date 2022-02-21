# calculus_transistor
[![image](https://img.shields.io/badge/python-v.3-blue)](https://python.org)
[![image](https://img.shields.io/badge/qt--gui-v.5-brightgreen)](https://www.qt.io/)

Ce programme permet, pour 4 types de montages, de calculer les paramètres statiques et dynamiques. Il est également de tracer la droite de charge dynamique et la droite de charge statique. 

**Les montages sont :**
- Emetteur commun NON dégénéré. 
- Emetteur commun dégénéré.
- Collecteur commun. 
- Base commune.

Les montages sont décomposés par bloc. Ils se trouvent dans le dossier ***/montages_transistor.*** Vous pouvez vous en servir comme librairie pour vos projets.

**Les paramètres calculés sont :**
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

**Choix du montage:**

![image](https://user-images.githubusercontent.com/62595480/154943085-da01faf8-13f0-4c98-b24b-df6b3f9765a4.png)

**Paramètrage du montage chois, affichage des caractéristiques statiques et dynamique:**

![image](https://user-images.githubusercontent.com/62595480/154943445-3e754aa6-2bc2-4a7c-80f6-1ba1e3f6c67a.png)

**Droite de charge statique et dynamique:**

![image](https://user-images.githubusercontent.com/62595480/154943542-bafd5fa9-acde-4734-874b-0649e8d70d64.png)



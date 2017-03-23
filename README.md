# Projet-Baxter
Projet M2 Rodeco / IARF - Université Paul Sabatier - Toulouse

*!!! Ce README regroupe le minimum d'informations. Pour plus de détails lire le manuel utilisateur fourni dans les fichiers. !!!

Projet réalisé par Marianne DATTAS, Mouna TAKHERIST, Victor DAVID, Benjamin HULAUD et Sébastien PIEDADE.
Si vous avez des questions vous pouvez nous contacter aux adresses suivantes :

      bhulaud@gmail.com


Le but de ce projet est de créer une aplication d'interaction homme-robot multimodale pour le robot BAXTER de Rethink Robotics.
Cette application est intégré sous ROS. Cette application à pour but de faire jouer au robot BACTER un role de Barman, donc de comprendre une commande, interagir avec un client et servir une boisson.

Il est possible d'utiliser ces programmes pour un autre robot possédant des caractéristiques similaires avec peu de modifications.

Ce projet est regroupe un travail autour de 3 domaines de la robotique : L'interaction vocale, la vision par ordinateur et la commande de robots.

****** INSTALLATION *****

Vou trouverez ci-joint un certain nombre de codes. Il suffit de copier/coller le contenu du dossier 'src' dans le dossier 'src' de votre répertoire principal ROS. Le fichiers 'baxter.sh', 'init.sh' 'start.sh' et 'start_rangement.sh' sont à copier directement à la racine de ce dossier ROS.
ATTENTION : L'application nécessite l'installation d'un certain nombre de librairies. Vous trouverez le détail dans le manuel utilisateur.

****** INITIALISATION *******

Dans un terminal, se placer dans votre dossier ROS puis executer :
  
   ./baxter.sh    puis ./init.sh
   
ATTENTION : Il faut egalement intaller le robot dans un certain environnement pour effectuer la demo. Les détails sont dans le manuel utilisateur.

****** LANCEMENT *******

Si vous souhaitez lancer le programme de service de boisson il faut se placer dans le terminal dans le dossier 'src', puis lancer le script 'start.sh'. Une fois lancé, l'utilisateur doit se mettre face au robot afin que la camera frontale le detecte et que l'interaction commence.

Si vous souhaitez lancer le programme de rangement des boissons, la procedure est la même mais il faut lancer 'start_rangement.sh'.

ATTENTION ; Pour chaque script, il faut initialiser l'environnement d'une certaine façon. Le détail est dans la manuel utilisateur.

*** !!! Le détail du role de chaque fichier et nottement chaque fontion sont détaillés dans le manuel utilisateur !! ***


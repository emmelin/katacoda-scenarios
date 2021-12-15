
# De l'intérêt de mettre un `/` à la fin des noms de répertoires

ATTENTION :

La commande `mv john.snow chateau` peut avoir plusieurs comportements différents :

* Si `chateau` n'existe pas, la commande renommera `john.snow` en `chateau`
* Si `chateau` est un dossier, cette commande déplacera  `john.snow` dans le dossier `chateau/`.
* Si `chateau` est un fichier, cette commande renommera `john.snow` en `chateau`. En clair, tu auras perdu le contenu de `chateau` !

Ainsi, pour ne pas prendre de risque, mets toujours un `/` à la fin des noms de répertoire.

Essaie :
* Crée un dossier `dossier_txt` dans ton home. Puis déplaces-y tous les fichiers texte qui sont dans le dossier `Exo2`
* Peux-tu, en une seule commande, déplacer le fichier `colorful_animal_bird_twitter_animal...` dans ton home et le renommer en `oizo.png` ?
* Crée un dossier `images` dans ton home et déplaces y le fichier `oizo.png` que tu viens de déplacer/renommer.
* Déplaces dans le dossier `images` tous les fichiers texte qui sont dans le dossier `Exo2`. Peux_tu le faire en une seule ligne de commande ?

Fait d'autres tests ! Vérifie à chaque fois que le résultat est bien le résultat attendu.


```{quizdown} 
  ##  Que fait `mv truc.txt machin/` ? 
  - [x] il génère une erreur car le dossier machin/ n'existe pas.
  - [ ] il crée un dossier machin/ et y déplace le fichier truc.txt.
  - [ ] il renomme le fichier truc.txt en machin
  - [ ] il crée une copie du fichier truc.txt qu'il nomme machin
```

```{quizdown} 
  ##  Que fait `mv chose.txt machin` ? 
  - [ ] il génère une erreur car le dossier machin/ n'existe pas.
  - [ ] il crée un dossier machin/ et y déplace le fichier chose.txt.
  - [x] il renomme le fichier chose.txt en machin
  - [ ] il crée une copie du fichier chose.txt qu'il nomme machin

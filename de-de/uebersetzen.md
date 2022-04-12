# Beim Übersetzen mithelfen

Ich unterstütze Leute, die *Minecraft* in ihrer Sprache benutzen und möchte dies auch in meinem Modpack fördern. Allerdings ist dies ein Modpack, also wenn du mithelfen willst, kannst du die einzelnen Mods übersetzen.

### Mod Menu Helper (Mod-Menü-Helfer) übersetzen

*Fabulously Optimized* beinhaltet ein Ressourcenpaket namens "Mod Menu Helper" das kurz beschreibt, welche Mods was macht. Standardmäßig ist es in englisch, aber ich bin offen, neue Übersetzungen hinzuzufügen. Folge also gerne diesem Tutorial:

1. Nachdem du FO gestartet hast, gehe zum Ressourcenpakete-Menü und klicke *Open Pack Folder*
2. Extrahiere *Mod Menu Helper.zip* in einen beliebigen Ordner, dann gehe in diesen Ordner → `assets` → `minecraft` → `lang`
3. Öffne die Datei `en_us.json` und kopiere ihren Inhalt
4. Erstelle eine neue Datei in dem Dateinamensformat `locale_code.json`, z.B. `et_ee.json` oder `de_de.json`. Schaue in [diese Tabelle](https://minecraft.fandom.com/wiki/Language#Languages) und suche den `in-game` Code, den du brauchst.
5. Füge den Text von Schritt 3 hier ein und übersetze die Angaben rechts **nach** dem Doppelpunkt:

```
"coolmod.config.title": "Example Text",
```
**↓** Kann übersetzt werden zu **↓**
```
"coolmod.config.title": "Beispieltext",
```

1. Halte dich kurz und knapp.
   * Ändere keine Farbcodes (§), den Stift-Emoji 🖉 oder "newlines" (Zeilenumbrüche, `\n`)
2. Teste deine Übersetzungen im Spiel, indem du auf `Options...` → `Resource Packs...`, die "Mod Menu Helper.zip" deaktivierst und stattdessen "Mod Menu Helper" aktivierst und danach in das `Mods`-Menü schaust.
   * Die Zeilen **müssen** bei einem maximierten Vollbildschirm-Fenster bei der *Full HD*-Auflösung (1920×1080) mit der Standardschrift (oder der Unicode Schrift, falls deine Sprache sie automatisch nutzt) vollständig sichtbar sein.
   * Du kannst `F3+J` nutzen, um die Sprachdateien neuzuladen.
3. Falls du mit deiner Übersetzung zufrieden bist, kopiere den Inhalt deiner Datei.
4. [Klick hier](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/Mod%20Menu%20Helper/assets/modmenu/lang/), dann `Add file` → `Create new file`. Du brauchst dafür ein GitHub-Konto.
5. Dies wird das Projekt "forken" und es wird sich ein neues Dateifenster öffnen. Nenne die Datei in dem Dateiformat von dem vorherigen Tutorial oben bei Schritt 4 und füge den kopierten Inhalt mit deiner neuen **Übersetzung** ein.
> **Tipp:** Du kannst auch einfach über `Add File` → `Create new file` eine Datei hochladen 
6. `Commit`e die Datei und eröffne einen `Pull Request`. Wenn deine Übersetzung perfekt in die Zeilen passt, dann werde ich sie sicherlich akzeptieren.
7. Danke für einen Beitrag! Die Übersetzung wird wahrscheinlich in der nächsten Version des Modpacks veröffentlicht. 

### Mods übersetzen

1. [Schau dir die Liste der Mods an](https://github.com/Madis0/fabulously-optimized#included-mods)
2. Finde auf jeder Website den entsprechenden `Issues` oder `Source` Link, siehe die Leiste oben.
3. Schau auf der GitHub-Projektseite, ob eine Übersetzungsplattform angegeben ist. Wenn das der Fall ist, besuche sie und fahre dort fort.
4. Falls nicht, ließ hier weiter: gehe zun `Code`-Tab der GitHub-Seite und öffne die Ordner `src` → `main` → `resources` → `assets` → `(Mod Name)` → `lang` → `en_us.json`
5. Öffne die Datei und kopiere ihren ganzen Inhalt.
6. Gehe zurück zum `lang` Ordner, klicke `Add file` → `Create new file`
7. Dies wird das Projekt "forken" und es wird sich ein neues Dateifenster öffnen. Schaue in [diese Tabelle](https://minecraft.fandom.com/wiki/Language#Languages) und suche den `in-game` Code, den du brauchst. Nenne entsprechend des Sprachcodes die neue Datei, z.B. `de_de.json` und füge den kopierten Inhalt mit deiner neuen **Übersetzung** ein.
8. `Commit`e die Datei und eröffne einen `Pull Request`. Wenn du Glück hast, schaut sich der Programmierer der Mod deine Übersetzung an und fügt sie in die Mod ein! 
9. Bei der nächsten Version von *Fabulously Optimized* sollte die Übersetzung auch erscheinen (falls die Übersetzung vom Programmierer der Mod in die Mod eingefügt wurde).

#### Wichtige Mods, die übersetzt werden sollten 

Liste der Mods, die die am meisten angesehenen Strings (Zeichenketten, "Texte") im Modpack haben.
Klicke den Namen der Bot an, um zu der entsprechenden Sprachdatei bzw. Übersetzungsplattform zu gelangen.

1. [Sodium Extra](https://github.com/FlashyReese/sodium-extra-fabric/blob/1.17.x/dev/src/main/resources/assets/sodium-extra/lang/en\_us.json)
2. [~~Sodium~~](https://github.com/CaffeineMC/sodium-fabric/issues/44) (derzeit unterbrochen)
3. [Iris Shaders](https://github.com/IrisShaders/Iris/blob/trunk/src/main/resources/assets/iris/lang/en\_us.json)
4. [Mod Menu](https://hosted.weblate.org/engage/fabric-modmenu/)
5. [LambdaBetterGrass](https://github.com/LambdAurora/LambdaBetterGrass/blob/1.18/src/main/resources/assets/lambdabettergrass/lang/en\_us.json)
6. [LambDynamicLights](https://github.com/LambdAurora/LambDynamicLights/blob/1.18/src/main/resources/assets/lambdynlights/lang/en\_us.json)
7. [Zoomify](https://github.com/isXander/Zoomify/blob/1.18/src/main/resources/assets/zoomify/lang/en\_us.json)
8. [SpruceUI](https://github.com/LambdAurora/SpruceUI/blob/1.18/src/main/resources/assets/spruceui/lang/en\_us.json) (mehr Texte werden in LambdaBetterGrass und LambDynamicLights genutzt)
9. [Fabric Capes](https://github.com/CaelTheColher/Capes/blob/master/src/main/resources/assets/capes/lang/en\_us.json)
10. [Continuity](https://github.com/PepperCode1/Continuity/blob/main/src/main/resources/assets/continuity/lang/en\_us.json)
11. [CIT Resewn](https://github.com/SHsuperCM/CITResewn/blob/main/src/main/resources/assets/citresewn/lang/en\_us.json)
12. [Colormatic](https://github.com/kvverti/colormatic/blob/master/src/main/resources/assets/colormatic/lang/en\_us.json)
13. [CEM](https://github.com/dorianpb/cem/blob/1.18/src/main/resources/assets/cem/lang/en\_us.json)
14. [Not Enough Crashes](https://github.com/natanfudge/Not-Enough-Crashes/blob/1.18/common/src/main/resources/assets/notenoughcrashes/lang/en\_us.json)
15. [Cloth Config](https://crowdin.com/project/cloth-config) (Texte in manchen Einstellungsmenüs)
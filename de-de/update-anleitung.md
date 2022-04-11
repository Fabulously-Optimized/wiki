# So hältst du das Modpack immer aktuell!

### *Curseforge Launcher*

Falls du nichts an den Mods geändert hast:

1. Wähle *Minecraft* in der Übersicht oder Seitenleiste
2. Gehe auf `My Modpacks`, rechtsklicke `Fabulously Optimized`, und drücke auf `⇄ Change Version`
   * Siehst du diesen Knopf nicht? Dann folge bitte den Schritten weiter unten.
3. Wähle die neuste Version, dann `Continue`.
4. Das Modpack sollte sich nun updaten.
5. Nach dem Update kannst du das Modpack starten und schauen, ob sich die Versionsnummer unten rechts geändert hat.

Falls du manche Mods hinzugefügt oder entfernt hast:

1. Wähle *Minecraft* in der Übersicht oder Seitenleiste
2. Gehe auf `My Modpacks`, klicke `Fabulously Optimized`
3. Gehe auf die Menüpunkte `⫶`
4. Öffne die `Profile Options`
5. Wähle "Allow content management for this profile" ab. Du kannst diesen Haken **nach** dem Update sehr gerne auch wieder aktivieren.
6. Klicke `Continue`
7. Öffne wieder die Menüpunkte `⫶`
8. Dann `⇄ Change Version`
9. Wähle die allerneuste Version aus und drücke `Continue`.
10. Das Modpack sollte sich nun updaten.
11. Nach dem Update kannst du das Modpack starten und schauen, ob sich die Versionsnummer unten rechts geändert hat.

### *MultiMC*

1.17 benötigt Java 16 oder höher, 1.18 hingegen Java 17 oder höher. [Offizielle Homepage](https://www.oracle.com/java/technologies/downloads/), [Adoptium](https://adoptium.net/download)

1. Gehe zu [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files)
2. Drücke `Download` bei der neusten **MultiMC**-Version
   * Siehst du nicht die *MultiMC*-Version? Klicke auf den Titel der Curseforge-Version und scrolle runter, dort sollte die *MultiMC*-Variante sichtbar sein.
   * Falls du gar keine oder nur eine Mod in der *.zip* siehst, hast du die falsche Version heruntergeladen.
3. Schiebe das ZIP-Archiv per drag & drop in das *MultiMC*-Fenster
4. Drücke auf das neue Profil, dann auf `Minecraft Folder`
5. Drücke auf das Profil mit der vorherigen Version, und da auch auf `Minecraft Folder`
6. Um deine alten Daten zu behalten, kopiere folgende wichtige Ordner und Dateien in die neue Version:
   * `saves` für diene Einzelspieler-Welten
   * `resourcepacks`, falls du Ressourcenpakete benutzt (kopiere NICHT *Mod Menu Helper*!)
   * `screenshots` für deine Screenshots
   * `servers.dat` für deine Mehrspieler-Server
   * `options.txt`, wenn du deine Spieleinstellungen behalten möchtest
7. Schließe die Ordner und starte die neuste Version
8. Wenn alles gut funktioniert, kannst du die alte Version löschen.

### *MultiMC* (mit automatischen Aktualisierungen)

1.17 benötigt Java 16 oder höher, 1.18 hingegen Java 17 oder höher. [Offizielle Homepage](https://www.oracle.com/java/technologies/downloads/), [Adoptium](https://adoptium.net/download)

In den meisten fällen genügt:

1. Einfach deine vorhandene Instanz starten. Wenn das Modpack aktualisiert wird, dann kann man einen Fortschrittsbalken erkennen
2. Schaue unten rechts, ob die neue Version des Modpacks angezeigt wird.

Um den *Fabric Loader* zu aktualisieren (falls du einen Fehler wie "mod X needs fabric-loader x.y.z" bekommst):

1. Öffne die Instanz
2. Klicke `Edit Instance`
3. Wähle in der Liste `Minecraft`, dann rechts `Fabric Loader` und `Remove`
4. Drücke `Install Fabric`, dann `OK`
5. Schließe das Fenster wieder mit `Close`. Nun sollte das Problem behoben sein.

Wenn eine neue *Minecraft* Version veröffentlicht wurde oder wenn du den *Fabric Loader* nicht aktualisieren kannst:

1. Gehe zur [Readme vom *FO GitHub*-Repository](https://github.com/Fabulously-Optimized/fabulously-optimized#downloads), dann "Alternative downloads"
2. Wähle die von dir benötigte Version im `MultiMC (auto-update)` 
3. Schiebe das ZIP-Archiv per drag & drop in das *MultiMC*-Fenster
4. Drücke auf das neue Profil, dann auf `Minecraft Folder`
5. Drücke auf das Profil mit der vorherigen Version, und da auch auf `Minecraft Folder`
6. Um deine alten Daten zu behalten, kopiere folgende wichtige Ordner und Dateien in die neue Version:
   * `saves` für diene Einzelspieler-Welten
   * `resourcepacks`, falls du Ressourcenpakete benutzt (kopiere NICHT *Mod Menu Helper*!)
   * `screenshots` für deine Screenshots
   * `servers.dat` für deine Mehrspieler-Server
   * `options.txt`, wenn du deine Spieleinstellungen behalten möchtest
7. Schließe die Ordner und starte die neuste Version
8. Wenn alles gut funktioniert, kannst du die alte Version löschen.

### *GDLauncher*

1. Rechtsklicke die *Fabulously Optimized*-Instanz
2. Wähle `🔧 Manage`
3. Gehe auf `Modpack` (rechts)
4. Klicke auf `Select a version` und wähle die neuste Version ganz oben
5. Drücke `Switch Version`
6. Das Modpack sollte sich nun updaten.
7. Nach dem Update kannst du das Modpack starten und schauen, ob sich die Versionsnummer unten rechts geändert hat.

### *Minecraft Launcher* (vanilla)

Aktuell kann man die Instanz nur aktualisieren, indem man sie neu installiert.

1. Installiere den [Fabric Loader](https://fabricmc.net/use/) **Version 0.13.3**
2. Öffne den *Minecraft Launcher*, klicke `Installations` und dann auf das Ordnersymbol 📂 bei der *Fabric*-Installation
3. Geh zu [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files) auf *Curseforge*
4. Klick auf `Download` bei das neusten **MultiMC Version** des Packs
   * Siehst du nicht die *MultiMC*-Version? Klicke auf den Titel der Curseforge-Version und scrolle runter, dort sollte die *MultiMC*-Variante sichtbar sein.
   * Falls du gar keine oder nur eine Mod in der *.zip* siehst, hast du die falsche Version heruntergeladen.
5. Öffne die zip-Datei, gehe zu *Fabulously Optimized x.x.x_* → *.minecraft*
6. Kopiere alle Ordner des *.minecraft* Ordners des Zip-Archivs zu deinem *.minecraft*-Ordner. Falls gefragt, erlaube das Ersetzen der Dateien und Ordner.
7. Wenn du auch die [FO Standard-Einstellungen](geaenderte-optionen.md) aktivieren willst, dann lösche die `options.txt`-Datei (Achtung - deine Einstellungen werden zurückgesetzt)
8. Starte das soeben installierte *Fabric* Profil
9. Falls du nun im Hauptmenü des Spiels unten rechts die neue Version des Modpacks angezeigt wird, dann hat's funktioniert!

### Einstellungen zurücksetzen

Da das Modpack `YOSBR` benutzt, werden sich deine Spieleinstellungen nicht zurücksetzen, nachdem du das Modpack aktualisiert [(auch wenn das manchmal so im *Changelog* steht)](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/CHANGELOG.md).

Dies ist eigentlich was Gutes, da du deine Einstellungen somit nicht immer neu konfigurieren musst. Allerdings solltest du sie hin und wieder mal zurücksetzen, um sicherzustellen, dass die neusten Funktionen verwendet werden können.

So geht's:

> Bitte schließe vorher das Spiel!

1. Öffne den Modpack Ordner.
   * *Curseforge Launcher*: rechtsklicke das Modpack → `Open Folder`
   * *MultiMC*: rechtsklicke die Instanz → `Minecraft Folder`
   * *GDLauncher*: rechtsklicke die Instanz → `Open Folder`
   * Vanilla launcher: wechsle zum `Installations`-Tab → beweg den Mauszeiger über die Instanz → klick das Ordnersymbol `📁`
2. Lösche die `options.txt` wenn du [die vorkonfigurierten Einstellungen des Modpacks](geaenderte-optionen.md) bevorzugst.
3. Öffne den Ordner `config` und lösche folgendes:
   * Den Ordner `fabric`
   * Die Datei `config.json5` im Ordner `slightguimodifications`
   * Alles andere in diesem Ordner **außer**:
     * Die Datei `citresewn.json`
     * Die Datei `fabric_loader_dependencies.json`
     * Der Ordner `yosbr`
4. Starte das Spiel. Nun sollten alle Änderungen aktiv sein.
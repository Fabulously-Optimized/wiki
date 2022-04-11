# Mods deaktivieren

Magst du manche Mods nicht oder hast du Probleme mit ihnen? Dann kannst du die Mod deaktivieren. Für Probleme mit Ressourcenpaketen, [schau bitte hier vorbei](ressourcenpaket-probleme.md).

Hinweise:

* Du kannst Mods auch komplett entfernen, allerdings wird es dann etwas dauern, sie wieder [hinzuzufügen](mods-hinzufuegen.md), außer du merkst dir die Namen auf.
* Bitte sei vorsichtig und deaktiviere und lösche nicht Mods mit "API" im Namen, wenn du nicht genau weißt, mit welchen Mods sie zusammenhängen. "API"-Mods werden von anderen Mods benötigt.

### Über das Menü

1. Gehe zum Options-Menüpunkt `Mods`
2. Scrolle zur Mod runter, die du deaktivieren willst, und schau dir die dritte Reihe mit dem Stiftsymbol ✏️ an:
   * Wenn der Stift blau ist und "Toggle mod" daneben steht, drücke den Knopf ![](https://i.ibb.co/j35cBtn/image.png) und finde die Einstellung, die die Mod deaktiviert.
   * Wenn der Stift blau ist und der Text was anderes aussagt, drücke den Knopf ![](https://i.ibb.co/j35cBtn/image.png) und schau nach, ob du die entsprechende Funktion der Mod, die stört deaktivieren kannst.
   * Wenn der Stift grau ist und kein Knopf angezeigt wird, dann schaue bei denen Launcher-spezifischen Methoden unten nach
    * Falls bei keinen Mods ein blauer Stift sichtbar ist, hast du wahrscheinlich aus Versehen das *Mod Menu Helper* Ressourcenpaket deaktiviert oder gelöscht. In diesem Fall:
    1. Drücke `Done` → `Options...` → `Resource Packs...` → `⏵` auf "Mod Menu Helper.zip" → `Done` → folge wieder den Schritten ab Schritt 1. 

### Curseforge Launcher

1. Öffne den *Curseforge Launcher*
2. Gehe zu `My Modpacks` und klicke auf *Fabulously Optimized*
3. Wähle im Dreipunktemenü `Profile Options`
4. Setze einen Haken für "Allow content management for this profile" und klicke `Done`
5. Finde die entsprechende Mod, die du deaktivieren willst und wähle sie ab.

**Hinweis: du musst "Allow content management for this profile" aktivieren, um das Modpack zu bearbeiten!**

### GDLauncher

1. Öffne *GDLauncher*
2. Rechtsklicke *Fabulously Optimized* und wähle `Manage`
3. Wähle `Mods`
4. Finde die entsprechende Mod, die du deaktivieren willst und wähle sie ab.

### MultiMC

1. Öffne *MultiMC*
2. Klicke auf die entsprechende Instanz, z.B. *Fabulously Optimized*, dann `Edit Instance`
3. Gehe zu `Loader mods`
4. Finde die entsprechende Mod, die du deaktivieren willst und wähle sie ab.

### MultiMC (auto-update)

Leider geht das hier nicht so einfach, da bei jedem Update alle Dateien neu heruntergeladen werden. Es gibt allerdings einen Umweg für GNU/Linux (und möglicherweise auch macOS), [siehe hier](multimc-auto-updates.md#Mods-vom-Auto-Update-ausschließen).

### Minecraft Launcher (vanilla)

1. Öffne den *Minecraft Launcher*, klicke auf `Installations`
2. Klicke das dem Modpack (möglicherweise *Fabric* genannt) entsprechende Ordnersymbol
3. Wähle `mods`
4. Benenne die Mod-Datei "modname.jar" zu "modname.jar-old" um (natürlich ist das nur ein Beispiel, nur der Text nach dem **`.`** ist relevant)
   * Siehst du nur die Modnamen, nicht aber `.jar` am Ende? [So kann man Dateinamenserweiterungen auf Windows aktivieren.](https://www.thewindowsclub.com/show-file-extensions-in-windows)
   * Wenn du die Mod später wieder aktivieren willst, benenne ihre Datei einfach von "modname.jar-old" zurück zu "modname.jar" um.
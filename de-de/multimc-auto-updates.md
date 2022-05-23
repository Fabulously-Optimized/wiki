# Automatische Aktualisierungen für MultiMC

Hier ist ein kurzes FAQ was Aktualisierungen für MultiMC angeht.
### Wie funktioniert es?

Es ist eigentlich ein ganz normales *MultiMC* Modpack welches [*packwiz*](https://github.com/comp500/packwiz) beim Start öffnet, ein Programm, welches sich um die automatischen Updates kümmert. *Packwiz* schaut einfach in die `pack.toml` Datei, welche Mods wie aktualisiert werden sollten.

### Wie installiere ich es?

Siehe [hier](einrichtung.md#multimc-auto-update)

### Wie aktualisiert es sich?

Es wird bei jedem Start eine Anfrage an einen Server gesendet, um nachzuschauen, ob es neue Versionen gibt. Du brauchst allerdings zwingend eine Internetverbindung, damit die Überprüfung gestartet werden kann. Keine Sorge, du kannst die Fehlermeldung auch ignorieren und die Überprüfung überspringen.

Wenn neue Updates erkannt wurden, installieren sie sich von alleine. Wenn nicht, wird einfach sofort das Spiel gestartet.

Eine häufiger Irrtum ist, dass sich auch andere Mods (die nicht von *Fabulously Optimized* in das Modpack getan wurden) automatisch aktualisieren. Dies ist nicht der Fall. Nur die von *Fabulously Optimized* aktivierten Mods werden aktualisiert.

### Wieso wird die *MultiMC Auto-Update* Variante nicht auf CurseForge veröffentlicht?

* Um die Variante in der Dateiliste sichtbar zu halten, müsste ich sie jedes Mal neu hochladen, wenn ich das Paket aktualisiere, was oft unnötig ist.
* Es kann sein, dass dadurch nicht [die Mod-Entwickler unterstützt werden](https://support.curseforge.com/en/support/solutions/articles/9000197898-rewards-program-terms-of-service#1.-Description-of-Rewards-Program), was ich schade finde, deswegen mag ich es lieber, wenn es nur ein paar Leute benutzten, die sich damit auskennen.
* Das ganze ist ein Stück weit experimentell und es kann zu Fehlern kommen. Da sind meine "normalen" Varianten für CurseForge und MultiMC (ohne auto-updates) viel stabiler.

### Aber warum gibt es diese Variante überhaupt?

* *MultiMC* hat eine solche Funktionalität noch nicht, siehe [*GitHub Issue* #2640](https://github.com/MultiMC/MultiMC5/issues/2640) und [*GitHub Issue* #3037](https://github.com/MultiMC/MultiMC5/issues/3057)
* Der Entwickler von *MultiMC* plant sowieso ein auto-update System, was ich auf jeden Fall für *Fabulously Optimized* haben ,möchte
* Außerdem wurde mir ein solches System schon vorgeschlagen, und derjenige, der es Vorgeschlagen hat, hat auch gesagt, dass er es nervig findet, ständig neue Instanzen zu erstellen. 
### Was wenn eine neue Version von *Minecraft* rauskommt?

Dann muss das ganze noch einmal heruntergeladen und installiert werden. Hier genügt es nicht, einfach das Spiel zu starten.

### Mods vom Auto-Update ausschließen

Hierzu gibt es keinen offiziellen Weg, aber eine [Abhilfe von *Remty5*](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/81) für *GNU/Linux*, wahrscheinlich auch *MacOS*, **nicht aber Windows**.

Die Abhilfe ist ziemlich kompliziert und nicht für Anfänger geeignet. Dennoch, hier ist sie:

* Als erstes musst du die Skripte installieren. Öffne deinen Dateimanager und wähle den Ordner, in dem du die Skripte installieren willst (z.B. direkt da, wo deine Instanz gespeichert ist). Dann rechtsklicke den Ordner und klicke `Open Terminal`. Auf *macOS* kann [dieses](https://www.petenetlive.com/KB/Article/0001060) Tutorial helfen, wie man das Terminal in einem Ordner öffnet.

![Screenshot](https://user-images.githubusercontent.com/77157639/156615703-f113293c-e821-4c94-a891-2fccd0ff8848.png)

Jetzt einfach die folgenden Befehle kopieren und im Terminal starten (für GNU/Linux gedacht):

> Du musst dafür `curl` möglicherweise erst installieren: `sudo apt install curl`.

`curl -Os https://gist.githubusercontent.com/Remty5/1b8a8d7c842dda56dacebf6db8c10961/raw/c0149c39ef4be375d013fa254b71899fb4bd6105/post-exit.sh && curl -Os https://gist.githubusercontent.com/Remty5/1b8a8d7c842dda56dacebf6db8c10961/raw/c0149c39ef4be375d013fa254b71899fb4bd6105/pre-launch.sh`

Wenn alles gut funktioniert hat, sollten nun alle Skripte erfolgreich installiert sein!

Jetzt sind nur noch 4 Schritte notwendig:

1. Aktualisiere die Überprüfungscodes ("Checksums").
2. Wähle die Mods aus, die du ignorieren willst
3. Aktualisiere die `pack.toml`-Datei
4. Bringe sie in *MultiMC* zum laufen:

Und so geht's:

*   Führe diesen Befehl im Terminal aus:

    `cd .minecraft && md5sum packwiz.json`

    Dies wird sowas wie "`101c3431ead01d42ffbc80fecdccf903` - packwiz.json" ausgeben. Kopiere **nur** diesen Code.

*   Öffne danach die `pre-launch.sh` mit einem Texteditor deiner Wahl und ändere die 12. Zeile um, die so ähnlich aussieht wie:

    `checksum=101c3431ead01d42ffbc80fecdccf903`. Ersetze diesen Code (nach `checksum=`) mit dem Code von vorher.

    **WICHTIG:** Du must dies nach jedem Update machen, sowas wird das Spiel abstürzen!

*   Gehe nun zu Zeile 20.

    Hier kannst du alle Mods angeben, die du von deinem `mods` Ordner ignorieren willst. Füge sie in der Reihenfolge wie im Skript ein. Füge nach jedem Mod-Namen ein `\` hinzu, außer bei der letzten Mod, sonst wird es nicht funktionieren.

* Immer wenn eine neue *Minecraft* Version veröffentlicht wird,muss die `pack.toml` wieder aktualisiert werden. Am Ende von Zeile 5 gibt es einen Link, in dem irgendwo eine Minecraft Version drinstehen sollte (z.B. 1.18.2). Du musst also bei jeder neuen Minecraft-Version die Nummer ändern, da sonst [dieser Fehler](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/258) auftritt.
  
* Fast geschafft! Die ganzen Skripte müssen von *MultiMC* nur noch gestartet werden, und so geht's:
  1. Öffne *MultiMC*, rechtsklicke deine auto-update Instanz und wähle "Edit Instance"
  2. Gehe in die Einstellungen und klicke "Custom Commands". Aktiviere sie
  3. Nun musst du bei "Pre-launch command" `/path/to/pre-launch.sh` und dem "Post-exit command" `/path/to/post-exit.sh` einsetzen (wobei `/path/to/` immer der Speicherort der beiden Skripte ist - ändere ihn also um, sodass es passt)

![Screenshot](https://user-images.githubusercontent.com/77157639/157910323-02015782-7c9d-4a1c-a735-b5f0b75b79df.png)

Falls du Probleme hast, kannst du im [Discord Server](https://discord.gg/yxaXtaQqdB) fragen. Dieses Tutorial wurde von *RaptaG* gemacht.

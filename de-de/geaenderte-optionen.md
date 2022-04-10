# Geänderte Spieloptionen

*Fabulously Optimized* ändert manche Standard-Optionen von *Minecraft*, um dein Spielerlebnis zu verbessern.

Weil das Modpack *YOSBR* ("Your Options Shall Be Respected", "Deine Einstellungen sollten respektiert werden") nutzt, werden mögliche Einstellungen in der `options.txt` oder `config`-Ordner statt den Standardeinstellungen von *Fabulously Optimized* genommen.

Das heißt, dass du das Modpack immer updaten kannst, ohne deine Einstellungen zu verlieren!

### Einstellungen

| Einstellung                 | Beschreibung                                                                                                                                                                                                                                                        | Vanilla  | Modpack | Grund für die Änderung                                                                                                                                                         |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| autoJump                    | Springt automatisch springen, wenn man sich einem 1-Block hohem Block nähert.                                                                                                                                                                                       | an       | aus     | Im normalen Spiel (Vanilla) ist es für die meisten eher ein Hindernis als eine nützliche Funktion, weshalb viele diese Einstellung deaktivieren.                               |
| snooperEnabled              | Aktiviert den [Snooper](https://minecraft.fandom.com/wiki/Snooper), ein Hardwareanalyse-Programm. Die Einstellung wurde bereits in 1.13 entfernt, ist allerdings heute noch in den Spieleoptionen vorhanden (und ist standardmäßig auf "an" aus irgendeinem Grund). | an       | aus     | Nur für den Fall; um Privatsphäre ein Stück weit zu verbessern. In 1.18+ erzwingt [TieFix](https://www.curseforge.com/minecraft/mc-mods/tiefix) diese Einstellung tatsächlich. |
| darkMojangStudiosBackground | Macht den Startbildschirm schwarz-weiß                                                                                                                                                                                                                              | aus      | an      | Weniger störend und ähnelt auch der Bedrock Edition                                                                                                                            |
| gamma                       | Helligkeit                                                                                                                                                                                                                                                          | 0.0      | 0.5     | Bessere Sicht im Dunkeln, +50% heller als der Standard, und um es für die 1.18 mit großen Höhlen zu optimieren                                                                 |
| simulationDistance          | Redstone und Mod-Spawn Distanz                                                                                                                                                                                                                                      | 12       | 6       | Bessere Leistung, ganz egal, welche Render-Distanz zu eingestellt hast.                                                                                                        |
| guiScale                    | Menügröße                                                                                                                                                                                                                                                           | 0        | 3       | 3 ist für alle Bildschirmgrößen passend, 0 (Auto) hingegen kann viel zu groß und unübersichtlich bei großen Bildschirmen aussehen.                                             |
| maxFps                      | Die maximale Bildwiederholungsrate                                                                                                                                                                                                                                  | 120      | 260     | 260 ist "unbegrenzt", dies wurde eingestellt um das Spielerlebnis für diejenigen, die VSync (bei schnellen Computern/Monitoren) ausstellen, zu optimieren.                     |
| resourcePacks               | Die Standard-Ressourcenpakete                                                                                                                                                                                                                                       | \[]      | ¹       | Um die Mods zu optimieren und das Spielerlebnis zu vereinfachen.                                                                                                               |
| tutorialStep                | Der Schritt der des [Spiele-Tutorials](https://minecraft.fandom.com/de/wiki/Anleitungs-Hinweise)                                                                                                                                                                    | bewegung | aus    | Ich nehme an, dass wenn du weißt, wie man ein Modpack installiert, du dir schon im Klaren bist, wie man das Spiel spielt.                                                      |
| skipMultiplayerWarning      | Ob die [Mehrspieler-Warnung](https://minecraft.fandom.com/wiki/Multiplayer?file=Multiplayer_disclaimer.png) übersprungen werden soll                                                                                                                                | aus      | an      | Ich nehme an, dass du schon weißt, dass Mehrspieler-Netzwerke nicht von Mojang oder Microsoft sind.                                                                            |
| joinedFirstServer           | Ob der Hinweis für das [Fenster für soziale Interaktionen](https://minecraft.fandom.com/wiki/Social_Interactions_screen) angezeigt werden soll                                                                                                                      | aus      | an      | Ich erwarte, dass du schon weißt, dass man das Fenster mit `P` öffnen kann.                                                                                                    |

¹ `["vanilla","Fabric Mods","lambdabettergrass/default","continuity/default","continuity/glass_pane_culling_fix","cullleaves/smartleaves","file/Mod Menu Helper.zip"]`

### Tastenkombinationen

| Option                            | Beschreibung                                                         | Standard | Modpack | Grund für die Änderung                                                  |
| --------------------------------- | ------------------------------------------------------------------- | ------- | ------- | ----------------------------------------------------------------------- |
| Vanilla: Schnellleiste speichern    | Speichert deine Schnellleiste wenn diese Taste und eine Nummerntaste gedrückt werden             | c       | keine    | Diese Taste wird üblicherweise für Zoom verwendet                                    |
| Zoomify/WI Zoom: Zoom             | Zoomt (ähnlich wie mit einem Fernglas) an das Spiel heran                                 | v       | c       | C ist üblicher für Zoom und wird auch bei OptiFine verwendet                                    |
| Zoomify: GUI                      | Öffnet die Zoomify Mod-Einstellungen                                      | F8      | keine    | Wird von den meisten wahrscheinlich sowieso nicht genutzt                                             |
| AntiGhost: Zeige Geisterblöcke ("verbuggte" Blöcke) an | Fordert vom Spiel ein Neuladen der Blöcke an, um das Problem, in einem Block "gefangen" zu sein, zu beheben. | g       | keine    | Versehentliches gedrückt halten kann Probleme verursachen, benutze **/ghost** stattdessen! |
| Iris: Shader neu laden              | Lädt die aktuellen Shader neu                                         | r       | keine    | Wird von den meisten wahrscheinlich sowieso nicht genutzt                                             |
| Iris: Shader-Auswahlfenster | Öffnet ein Fenster zum Auswählen eines Shaders                                   | o       | keine    | Wird von den meisten wahrscheinlich sowieso nicht genutzt                                             |
| Iris: Shader an- oder ausstellen              | Stellt die Shader an oder aus                                         | k       | keine    | Wird von den meisten wahrscheinlich sowieso nicht genutzt                                             |

Die geänderten Einstellungen können bei folgendem Pfad im GitHub-Repository gefunden werden: [.../yosbr/1.18.1/config](https://github.com/Madis0/fabulously-optimized/tree/main/Packwiz/1.18.1/config).

Siehe auch: [Minecraft Wiki: options.txt](https://minecraft.fandom.com/de/wiki/Options.txt) und [GitHub-Issue Nr. 30](https://github.com/Madis0/fabulously-optimized/issues/30)

### Behobene Fehler

Seit FO 3.3.0 beheben manche Mods Spielfehler ("Bugs").
Allerdings wird, [ähnlich wie bei den Mod-Richtlinien](prinzipien.md), Fabulously Optimized nicht "einfach nur irgendwelche" Fehler beheben - sie müssen ca. 70%+ der Spielerschaft betreffen.

| Mojang Fehler                                            | Beschreibung                                                                | Gelöst von                                                      |
| ----------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [MC-121772](https://bugs.mojang.com/browse/MC-121772) | Man kann auf MacOS nicht scrollen, während SHIFT gedrückt wird                                  | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify) |
| [MC-122477](https://bugs.mojang.com/browse/MC-122477) | Wenn man den Chat auf GNU/Linux öffnen will, schreibt man versehentlich "t" | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify) |
| [MC-140646](https://bugs.mojang.com/browse/MC-140646) | Textfelder scrollen nicht, wenn man Text mit SHIFT auswählt                   | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify) |
| [MC-145929](https://bugs.mojang.com/browse/MC-145929) | Titeltexte können manchmal ohne Hintergrund schwer lesbar sein    | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify) |
| [MC-148149](https://bugs.mojang.com/browse/MC-148149) | Das Spiel stürzt auf GNU/Linux ab, wenn Links angeklickt werden                                        | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify) |
| [MC-162253](https://bugs.mojang.com/browse/MC-162253) | Lag-Probleme wenn Chunk-Ränder betreten werden                              | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify) |
| [MC-199467](https://bugs.mojang.com/browse/MC-199467) | Manche Animationen hören nach gewisser Zeit auf | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify) |
| [MC-235035](https://bugs.mojang.com/browse/MC-235035) | Wenn man in einer benutzerdefinierten Dimension schläft, während "natural" ausgestellt ist, stürzt das Spiel ab    | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify) |
| [MC-237493](https://bugs.mojang.com/browse/MC-237493) | Telemetrie kann nicht ausgestellt werden                                               | [TieFix](https://www.curseforge.com/minecraft/mc-mods/tiefix) |
| [MC-249059](https://bugs.mojang.com/browse/MC-249059) | Ladefenster für die Landschaft schließt sich nicht bevor 2 Sekunden vergangen sind           | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify) |

Falls du mehr Fehlerbehebungen für das Spiel aktivieren möchtest, schau dir gerne die folgenden Listen für [Debugify](https://github.com/W-OVERFLOW/Debugify/blob/1.18/PATCHED.md#unpatched-in-vanilla) und [TieFix](https://github.com/j-tai/TieFix#bugs-fixed) an.

#### Eine Fehlerbehebung anfordern

Willst du, dass ein Fehler in Fabulously Optimized behoben wird? Folge diesen Schritten:

1. Finde den eigentlichen Fehler [in Mojangs offizieller Fehlersuche](https://bugs.mojang.com/projects/MC/issues?filter=allopenissues)
2. Frage ihn an oder überprüfe seinen Status auf [Debugifys Fehlerübersicht](https://github.com/W-OVERFLOW/Debugify/issues)
3. Sobald der Fehler in Debugify hinzugefügt wurde (oder dies geplant ist), kannst du [eine Anfrage zur Ändern der Einstellungen von FO](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/new?assignees=\&labels=option\&template=setting-request.yml) senden
4. Describe the bug, mention the mod that fixes it and why it is important to 70-80% of users
5. If accepted, expect the fix to be enabled in the next version of FO :)

### Mods konfigurieren

Das Modpack ist bereits so vorkonfiguriert, um das bestmögliche Spielerlebnis zu bieten. 

Falls du allerdings etwas ändern möchtest, kannst du das z.B. bei `Options...` → `Video Settings...` tun. Falls du einen sehr schnellen Computer und Monitor hast, kannst du dort `vSync` deaktivieren.

Für andere Dinge wie dynamische Lichter, Grass-Verbesserungen und Zoom:

1. Klicke auf `Mods`
2. Ließ die Beschreibung, um zu wissen, was welche Mods tun
3. Falls ein blauer Stift zu sehen ist, dann kannst du die Mod konfigurieren, indem du den dafür vorgesehenen Knopf drückst: ![](https://i.ibb.co/j35cBtn/image.png)
 * Falls bei keinen Mods ein blauer Stift sichtbar ist, hast du wahrscheinlich aus Versehen das *Mod Menu Helper* Ressourcenpaket deaktiviert oder gelöscht. In diesem Fall:
 1. Drücke `Done` → `Options...` → `Resource Packs...` → `⏵` auf "Mod Menu Helper.zip" → `Done` → folge wieder den Schritten ab Schritt 1. 

Falls du eine Mod allerdings komplett deaktivieren willst, [schau gerne hier vorbei](mods-deaktivieren.md).

Wenn du noch weitere Fragen zu den Mods hast, [schreibe uns gerne auf Discord!](https://discord.gg/yxaXtaQqdB)

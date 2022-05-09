# Probleme mit Ressourcenpaketen

*Fabulously Optimized* unterstützt [einige Funktionen von OptiFine](verzichte-auf-optifine.md), darunter auch Extras für Ressourcenpakete. Allerdings kann es hierbei auch Probleme geben. Dieses Tutorial zeigt dir, wie du sie löst!

Bitte [stelle sicher, dass du die neuste Version von *Fabulously Optimized* nutzt](update-anleitung.md), bevor du versuchst, die Probleme zu beheben.

### Falsche Dateipfade

Siehst du diese Fehlermeldung bei einem Ressourcenpaket?

![Contains broken paths](https://i.ibb.co/26cMtqr/Screenshot-20211116-191457.png)

Das heißt, dass der Ersteller des Ressourcenpakets Sonderzeichen in Ordner- oder Dateinamen hat.

Falls dies der Fall ist, wird das Modpack versuchen diese zu überschreiben. Das kann allerdings zu eine menge Fehler führen(Blöcke mit den falschen Farben oder unsichtbare Blöcke, Probleme mit der Beleuchtung, kaputte Texturen...).

Deswegen solltest du den Ersteller des Ressourcenpakets bitten, nur folgende Zeichen in Datei- und Ordnernamen zu verwenden: `a-z`, `0-9` und `._-`.

### Unsichtbare Blöcke

Dieses Problem kann auftreten, wenn das Ressourcenpaket falsche Pfade verwendet und versucht, die Modelle von Blöcken wie z.B. Truhen zu verändern.

**Enhanced Block Entities**

*Enhanced Block Entities* ist eine Mod in *Fabulously Optimized*, welche das Rendering von Böcken optimiert. Allerdings werden manche Optimierungen von deinem Ressourcenpaket nicht unterstützt.

So kannst du das Problem lösen:

1. Öffne im Spielmenü `Mods`
2. Suche nach "Enhanced Block Entities" und drücke das Einstellungssymbol ![](https://i.ibb.co/j35cBtn/image.png)
3. Stelle alle Blöcke auf "aus", die Probleme verursachen. Meistens genügt nur `Enhanced Chests`.
4. Drücke `Done`

**FastChest & Better Beds**

Manche Versionen von *Fabulously Optimized* haben diese Mods, welche zu Problemen führen können. Folge jeweils den Schritten:

*FastChest*

1. Öffne im Spielmenü `Mods`
2. Suche nach "FastChest" und drücke das Einstellungssymbol ![](https://i.ibb.co/j35cBtn/image.png)
3. Stelle die Mod aus und drücke `Done`.

*Better Beds*

1. Schließe das Spiel
2. [Entferne die Mod](mods-deaktivieren.md)
3. Starte das Spiel und schaue, ob das Problem nun behoben ist.

### Leuchtende Texturen

Wird schon bald unterstützt, siehe [Continuity#7](https://github.com/PepperCode1/Continuity/issues/7). Wenn du aber einfach nur leuchtende Erze usw. haben möchtest, [installiere ruhig die Shader](shader-installieren.md) namens [Complementary](https://www.curseforge.com/minecraft/customization/complementary-shaders) oder [Prismarine](https://www.curseforge.com/minecraft/customization/prismarine-shader).

### Custom Skymap (benutzerdefinierter Himmel)

Wird aktuell nicht für Ressourcenpakete unterstützt, siehe [issue #72](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/72) für mehr Info. Du kannst auch [Shader verwenden](shader-installieren.md), beispielsweise ändert [BSL](https://bitslablab.com/bslshaders/) die Wolken und [AstraLex](https://www.curseforge.com/minecraft/customization/astralex-shader-bsl-edit) sogar auch den Himmel.

Weitere Shader die das Aussehen des Himmels verändern:

* AstraLex
* Continuum
* Prismarine
* ProjectLUMA
* RedHat
* Sildur's Vibrant
* Skylec
* SkyLEX
* Triliton

Danke an *JulienRaptor01* für diese Liste!

### Custom Entity Models (benutzerdefinierte Modelle für Entitäten)

Dies wird nur teilweise unterstützt. Hier eine [Liste, **was** unterstützt wird](https://github.com/dorianpb/cem#differences).

Wenn dein Modell eigentlich unterstützt wird, aber es nicht richtig angezeigt werden kann, probiere folgendes:

1. Öffne im Spielmenü `Mods`
2. Suche nach "Custom Entity Models", und klicke den Einstellungsknopf (oben rechts über `Issues`)
3. Setze "Use model creation fix?" auf `No`
4. Drücke `Save & Quit` und `Done`
5. Trete einer Welt bei, halte `F3` (und `Fn` auf einigen Laptops) gedrückt und drücke `T`
6. Nun wird alles neu geladen.
7. Wenn es allerdings immer noch nicht funktioniert, setzte die Einstellung von vorhin auf `Yes` und warte bis *CEM* das Problem behebt.

Siehe auch: [cem#9](https://github.com/dorianpb/cem/issues/9)


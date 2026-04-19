# Resetting options

Because the pack is using Config Manager or YOSBR, your vanilla options and most of the mod ones will not change when you upgrade. This is made so that you can upgrade without having to reconfigure your options all the time. 

However, at some point you may still want to do that in order to get the latest changes.

{% tabs %}
{% tab title="Modpack version 10.3.2 and newer" %}

1. Launch the game
2. Go to `Mods` -> `Config Manager` -> `🎛️`
3. If you want to _apply latest changes_ but keep configs for added mods, select `Update modpack's configs`. If you want to _delete all configs_ and start fresh, select `Reset modpack's configs`.
4. Close the game and start it again. See if it works.
5. If you got an error (especially on alpha or beta versions) or need to send logs to support, close the game and start again.

{% endtab %}

{% tab title="Modpack version 10.3.1 and older" %}

1. Open the modpack folder
   * CurseForge App: right click on the modpack tile → `Open Folder`
   * Modrinth App: right click on the modpack tile → `📂 Open folder`
   * Prism Launcher: right click on the instance → `Folder` → `.minecraft`
   * MultiMC: right click on the instance → `Minecraft Folder`
   * Minecraft Launcher: click `Installations` → hover on the instance → click `📁`
2. Delete the `config` folder
   * If you prefer, also delete `options.txt` which stores vanilla options
3. Download [your version of FO again from Modrinth](https://modrinth.com/modpack/fabulously-optimized/versions)
4. Rename the file to `pack.zip`
5. Open the file you renamed, go to `overrides`
6. Copy/extract the folder `configs` out to the modpack folder you previously opened
   * You may delete the `pack.zip` after you're done
7. Launch the game. Modpack's defaults are now applied!

{% endtab %}
{% endtabs %}
# Minecraft Launcher

{% tabs %}
{% tab title="Installer" %}

{% hint style="info" %}
If you have an existing version of the installer, in most cases you do not need to redownload.
{% endhint %}

{% tabs %}
{% tab title="Windows" %}

1. Download and install [Minecraft Launcher](https://www.minecraft.net/en-us/download)
2. Download [Fabulously Optimized Installer](https://download.fo/vanilla)
3. Open the .exe file, click `More info` and then `Run anyway`.
4. Select preferred modpack version and install
5. Run Minecraft Launcher. You'll see the new installation, click PLAY.

{% endtab %}

{% tab title="macOS 15 and later" %}

1. Download and install [Minecraft Launcher](https://www.minecraft.net/en-us/download)
2. Download [Fabulously Optimized Installer](https://download.fo/vanilla)
3. Open the downloaded .dmg file
4. Double-click the "Fabulously Optimized Installer". You will get a warning, press `Done`.
5. On your menubar, press Apple logo, then `System Settings`, then click `Privacy & Security` in the sidebar
6. Scroll down on the right view, you should see the button `Open anyway`
7. Enter your password or fingerprint. The installer should open.
8. Future launches of the same installer version open the installer directly on double-click.
9. Select preferred modpack version and install
10. Run Minecraft Launcher. You'll see the new installation, click PLAY.

{% endtab %}

{% tab title="macOS 14 and older" %}

1. Download and install [Minecraft Launcher](https://www.minecraft.net/en-us/download)
2. Download [Fabulously Optimized Installer](https://download.fo/vanilla)
3. Open the downloaded .dmg file
4. Right click the "Fabulously Optimized Installer" and click `Open`
5. Click `Open` again when asked in a prompt. The installer should open.
6. Future launches of the same installer version open the installer directly on double-click.
7. Select preferred modpack version and install
8. Run Minecraft Launcher. You'll see the new installation, click PLAY.

{% endtab %}

{% tab title="Linux" %}

1. Download and install [Minecraft Launcher](https://www.minecraft.net/en-us/download)
2. Download [Fabulously Optimized Installer](https://download.fo/vanilla)
3. Open the .appimage file and click `Run once` when prompted.
   * If it doesn't open directly, right click, find `Properties` and add a checkmark to an option `Allow executing this file`
4. Select preferred modpack version and install
5. Run Minecraft Launcher. You'll see the new installation, click PLAY.

{% endtab %}
{% endtabs %}

{% hint style="info" %}
You may now see a new file _paigaldaja_meta.json_ next to the installer. This is a configuration file that ensures smoother upgrades and remembers some of your install settings.
{% endhint %}

{% endtab %}

{% tab title="Manual install" %}
{% tabs %}
{% tab title="4.11.0 (MC 1.19.4) and newer" %}

1. Download and install [Fabric Loader](https://fabricmc.net/use/) **version 0.18.4**
   * Remember that the _installer version_ doesn't matter, what matters is the _loader version_ that appears when you run the installer.
2. Open Minecraft Launcher, click `Installations`, then click 📂 on the Fabric installation
3. [Open this site](https://download.fo/vanilla), then click the ⬇️ button
   * Optional: Select the version you want by selecting it on the dropdown before you click ⬇️.
      * Do not select an older version, this could corrupt your worlds and settings!
      * Do not update to an alpha or beta from a release version, [create it to a separate instance](https://help.minecraft.net/hc/en-us/articles/23431114561037-Create-a-New-Minecraft-Java-Installation-to-Troubleshoot-Launcher-Crashes) for testing.
   * If you got a prompt for popup windows or multiple downloads, please accept it - technical limitation.
4. Open the zip file and copy **all folders** to your _.minecraft_ folder
   * If asked - replace the files.
5. Recommended: delete current `options.txt` to get [modpack's default settings](changed-options.md)
    * Your vanilla options like selected resource packs, language, keybinds will be reset but you can reapply them later.
6. Launch the installed Fabric profile
7. If you now see "Fabulously Optimized" in the right bottom corner, you're done!

{% endtab %}

{% tab title="4.6.1 (MC 1.19.3) and older" %}

1. Download and install [Fabric Loader](https://fabricmc.net/use/)
    * Minecraft 1.19-1.19.3: Fabric Loader **0.14.24** and [Java 17](https://download.fo/java17)
    * Minecraft 1.17-1.18.2: Fabric Loader **0.14.12** and [Java 17](https://download.fo/java17)
    * Minecraft 1.16.5: Fabric Loader **0.13.3** and [Java 8](https://download.fo/java8)
    * Remember that the _installer version_ doesn't matter, what matters is the _loader version_ that appears when you run the installer.
2. Open Minecraft Launcher, click `Installations`, then click 📂 on the Fabric installation
3. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files?showAlphaFiles=show) on CurseForge
4. Click the version you need, then click "Additional files"
    * Never downgrade an instance, this could corrupt your worlds and settings!
    * It is not advised to upgrade release → alpha or release → beta, make a separate instance for testing.
    * Updating alpha → beta or beta → release is recommended as long as the Minecraft version matches.
5. Click `⋮` → `Download file` on the latest **MultiMC version**
    * If you see less than 10 mods in the zip, you downloaded the wrong version.  
6. Open the zip file, go to _Fabulously Optimized x.x.x_ > _minecraft_
7. Open the zip file and copy **all folders** from zip's _minecraft_ folder to your _.minecraft_ folder
    * If asked - replace the files.
8. Recommended: delete current `options.txt` to get [modpack's default settings](changed-options.md)
    * Your vanilla options like selected resource packs, language, keybinds will be reset but you can reapply them later.
9. Launch the installed Fabric profile
10. If you now see "Fabulously Optimized" in the right bottom corner, you're done!

{% endtab %}
{% endtabs %}
{% endtab %}
{% endtabs %}

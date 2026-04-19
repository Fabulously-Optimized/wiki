# Minecraft Launcher

{% tabs %}
{% tab title="Installer" %}

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
8. Select preferred modpack version and install
9. Run Minecraft Launcher. You'll see the new installation, click PLAY.

{% endtab %}

{% tab title="macOS 14 and older" %}

1. Download and install [Minecraft Launcher](https://www.minecraft.net/en-us/download)
2. Download [Fabulously Optimized Installer](https://download.fo/vanilla)
3. Open the downloaded .dmg file
4. Right click the "Fabulously Optimized Installer" and click `Open`
5. Click `Open` again when asked in a prompt. The installer should open.
6. Select preferred modpack version and install
7. Run Minecraft Launcher. You'll see the new installation, click PLAY.

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
Legacy versions of the modpack are not available on the installer. [Read more](../version-support.md#installer)
{% endhint %}

{% endtab %}

{% tab title="Manual install" %}
{% tabs %}
{% tab title="Modern versions" %}

{% hint style="info" %}
For macOS or Linux [you need Java](https://download.fo/java) to run the Fabric Installer.
{% endhint %}

1. Download and install [Minecraft Launcher](https://www.minecraft.net/en-us/download)
2. Download and install [Fabric Loader](https://fabricmc.net/use/) **version 0.19.2**
   * Remember that the _installer version_ doesn't matter, what matters is the _loader version_ that appears when you run the installer.
3. Open Minecraft Launcher, click `Installations`, then click 📂 on the Fabric installation
4. [Open this site](https://download.fo/vanilla), then click the ⬇️ button
   * Optional: Select the version you want by selecting it on the dropdown before you click ⬇️.
   * If you got a prompt for popup windows or multiple downloads, please accept it - technical limitation.
5. Open the zip file and copy **all folders** to your _.minecraft_ folder
   * If asked - replace the files.
6. Recommended: delete `options.txt` to get [modpack default settings](../changed-options.md)
    * Your vanilla options like selected resource packs, language, keybinds will be reset but you can reapply them later.
    * If you choose not to do this, please at least enable bundled resource packs manually.
7. Launch the installed Fabric profile
8. If you now see "Fabulously Optimized" in the right bottom corner, you're done!

{% endtab %}

{% tab title="FO 4.6.1 (MC 1.19.3) and older" %}

1. Download and install [Minecraft Launcher](https://www.minecraft.net/en-us/download)
2. Download and install [Fabric Loader](https://fabricmc.net/use/) and Java:

{% tabs %}
{% tab title="Minecraft 1.19-1.19.3" %}
Fabric Loader **0.14.24** and [Java 17](https://download.fo/java17)
{% endtab %}
{% tab title="Minecraft 1.17-1.18.2" %}
Fabric Loader **0.14.12** and [Java 17](https://download.fo/java17)
{% endtab %}
{% tab title="Minecraft 1.16.5" %}
Fabric Loader **0.13.3** and [Java 8](https://download.fo/java8)
{% endtab %}
{% endtabs %}

   * Remember that the _installer version_ doesn't matter, what matters is the _loader version_ that appears when you run the installer.
3. Open Minecraft Launcher, click `Installations`, then click 📂 on the Fabric installation
4. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files?showAlphaFiles=show) on CurseForge
5. Click the version you need, then click "Additional files"
6. Click `⋮` → `Download file` on the latest **MultiMC version**
   * If you see less than 10 mods in the zip, you downloaded the wrong version.  
7. Open the zip file, go to _Fabulously Optimized x.x.x_ > _minecraft_
8. Open the zip file and copy **all folders** from zip's _minecraft_ folder to your _.minecraft_ folder
   * If asked - replace the files.
9. Recommended: delete `options.txt` to get [modpack default settings](../changed-options.md)
   * Your vanilla options like selected resource packs, language, keybinds will be reset but you can reapply them later.
   * If you choose not to do this, please at least enable bundled resource packs manually.
10. Launch the installed Fabric profile
11. If you now see "Fabulously Optimized" in the right bottom corner, you're done!

{% endtab %}
{% endtabs %}
{% endtab %}
{% endtabs %}

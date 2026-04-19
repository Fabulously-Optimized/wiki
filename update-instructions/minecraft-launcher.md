# Minecraft Launcher

{% tabs %}
{% tab title="Installer" %}

{% tabs %}
{% tab title="Windows" %}

1. Download [Fabulously Optimized Installer](https://download.fo/vanilla)
   * If you already have the installer, launch it and skip to step 3.
2. Open the .exe file, click `More info` and then `Run anyway`.
3. Select preferred modpack version and install
4. Run Minecraft Launcher. You'll see the new installation, click PLAY.

{% endtab %}

{% tab title="macOS 15 and later" %}

1. Download [Fabulously Optimized Installer](https://download.fo/vanilla)
   * If you already have the installer, launch it and skip to step 7.
2. Open the downloaded .dmg file
3. Double-click the "Fabulously Optimized Installer". You will get a warning, press `Done`.
4. On your menubar, press Apple logo, then `System Settings`, then click `Privacy & Security` in the sidebar
5. Scroll down on the right view, you should see the button `Open anyway`
6. Enter your password or fingerprint. The installer should open.
7. Select preferred modpack version and install
8. Run Minecraft Launcher. You'll see the new installation, click PLAY.

{% endtab %}

{% tab title="macOS 14 and older" %}

1. Download [Fabulously Optimized Installer](https://download.fo/vanilla)
   * If you already have the installer, launch it and skip to step 5.
2. Open the downloaded .dmg file
3. Right click the "Fabulously Optimized Installer" and click `Open`
4. Click `Open` again when asked in a prompt. The installer should open.
5. Select preferred modpack version and install
6. Run Minecraft Launcher. You'll see the new installation, click PLAY.

{% endtab %}

{% tab title="Linux" %}

1. Download [Fabulously Optimized Installer](https://download.fo/vanilla)
   * If you already have the installer, launch it and skip to step 3.
2. Open the .appimage file and click `Run once` when prompted.
   * If it doesn't open directly, right click, find `Properties` and add a checkmark to an option `Allow executing this file`
3. Select preferred modpack version and install
4. Run Minecraft Launcher. You'll see the new installation, click PLAY.

{% endtab %}
{% endtabs %}

{% hint style="info" %}
You may now see a new file _paigaldaja_meta.json_ next to the installer. This is a configuration file that ensures smoother upgrades and remembers some of your install settings.
{% endhint %}

{% endtab %}

{% tab title="Manual install" %}
{% tabs %}
{% tab title="4.11.0 (MC 1.19.4) and newer" %}

1. Download and install [Fabric Loader](https://fabricmc.net/use/) **version 0.19.2**
   * Remember that the _installer version_ doesn't matter, what matters is the _loader version_ that appears when you run the installer.
2. Open Minecraft Launcher, click `Installations`, then click 📂 on the Fabric installation
3. [Open this site](https://download.fo/vanilla), then click the ⬇️ button
   * Optional: Select the version you want by selecting it on the dropdown before you click ⬇️.
   * If you got a prompt for popup windows or multiple downloads, please accept it - technical limitation.
4. Open the zip file and copy **all folders** to your _.minecraft_ folder
   * If asked - replace the files.
5. Launch the installed Fabric profile
6. If you now see "Fabulously Optimized" in the right bottom corner, you're done!

{% endtab %}

{% tab title="4.6.1 (MC 1.19.3) and older" %}

1. Download and install [Fabric Loader](https://fabricmc.net/use/) and Java:

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
2. Open Minecraft Launcher, click `Installations`, then click 📂 on the Fabric installation
3. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files?showAlphaFiles=show) on CurseForge
4. Click the version you need, then click "Additional files"
5. Click `⋮` → `Download file` on the latest **MultiMC version**
    * If you see less than 10 mods in the zip, you downloaded the wrong version.  
6. Open the zip file, go to _Fabulously Optimized x.x.x_ > _minecraft_
7. Open the zip file and copy **all folders** from zip's _minecraft_ folder to your _.minecraft_ folder
    * If asked - replace the files.
8. Launch the installed Fabric profile
9. If you now see "Fabulously Optimized" in the right bottom corner, you're done!

{% endtab %}
{% endtabs %}
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Never update to an older version, this could corrupt your worlds and settings!

Never update to an alpha or beta from a release version, [install a separate instance](https://help.minecraft.net/hc/en-us/articles/23431114561037-Create-a-New-Minecraft-Java-Installation-to-Troubleshoot-Launcher-Crashes) for testing.
{% endhint %}
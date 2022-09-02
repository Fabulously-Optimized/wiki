# Install instructions

**Prefer video tutorials instead of text?** [**Click here!**](https://github.com/Fabulously-Optimized/fabulously-optimized#reviews)

### [CurseForge Launcher](https://download.curseforge.com)

1. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files)
2. Click `Install` on the topmost CurseForge version
3. Accept the prompt (if asked), download should start

#### Or with the launcher already open:

1. Select _Minecraft_ from the grid or sidebar
2. Search "Fabulously Optimized"
3. Click `Install`

### [MultiMC](https://multimc.org)

You need [Java 17 or higher](https://www.oracle.com/java/technologies/downloads/) to play the game.

1. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files)
2. Click `Download` on the latest **MultiMC version**
   * Don't see the MultiMC version? Click the title of the CurseForge version you need and scroll down, you'll find the MultiMC variant there.
      * Alternatively, look for it in the sidebar, under "server packs". Don't worry, these are not server packs, just marked as such for findability.
   * If you don't see any mods inside the zip or only see one, you downloaded the wrong version.
3. Drag the ZIP-archive to MultiMC window, and hit OK in the window that pops up.

### [MultiMC](https://multimc.org) (auto-update)

You need [Java 17 or higher](https://www.oracle.com/java/technologies/downloads/) to play the game.

1. Go to [readme](https://github.com/Fabulously-Optimized/fabulously-optimized#downloads), click "Alternative downloads"
2. Click the version number you need in the MultiMC (auto-update) section
3. Drag the ZIP-archive to MultiMC window, and hit OK in the window that pops up.
4. Double-click that version you just created to download and launch the modpack
   * If you get asked to download a specific jar, it means I am not allowed to bundle it and you must add it manually:
      1. Copy its url to your browser
      2. Click `Cancel Launch`
      3. Click Download on the mod
      4. On MultiMC, right click on the instance -> View Mods
      5. Drag the downloaded mod into the mod list
      6. Click `Launch`

### [GDLauncher](https://gdevs.io)

1. Click ➕ on bottom left corner
2. Select `CurseForge` tab
3. Search for "Fabulously Optimized"
4. Click `Download Latest`
5. Click ➡️ on the bottom right

### [PolyMC](https://polymc.org/)

1.17 needs Java 16+, 1.18 needs Java 17+. [Get Java](https://polymc.org/wiki/getting-started/installing-java/)

1. Click `Add Instance`.
2. Select `Modrinth` tab from the left
3. Select "Fabulously Optimized"
4. Click `OK`
5. The modpack will now install.

### [Minecraft Launcher](https://www.minecraft.net/en-us/download) (vanilla)

For macOS or Linux [you need Java](https://www.oracle.com/java/technologies/downloads/) to run the Fabric Installer.

1. Download and install [Fabric Loader](https://fabricmc.net/use/) **version 0.14.9**
   * Older versions of the modpack - 1.12.3 and 2.7.3 need Fabric Loader 0.13.3.
   * Remember that the _installer version_ doesn't matter, what matters is the _loader version_ that appears when you run the installer.
2. Open Minecraft Launcher, click `Installations` and then click 📂 on the Fabric installation
3. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files) on CurseForge
4. Click `Download` on the latest **MultiMC version** of the pack
   * Don't see the MultiMC version? Click the title of the CurseForge version you need and scroll down, you'll find the MultiMC variant there.
      * Alternatively, look for it in the sidebar, under "server packs". Don't worry, these are not server packs, just marked as such for findability.
   * If you don't see any mods inside the zip or only see one, you downloaded the wrong version.
5. Open the zip file, go to _Fabulously Optimized x.x.x_ > _.minecraft_
6. Copy **all folders** from zip's .minecraft folder to your .minecraft folder; if asked - replace the files
7. If you want [FO default settings](changed-options.md) as well, delete `options.txt` (your vanilla options will be reset)
8. Launch the installed Fabric profile
9. If you now see "Fabulously Optimized" in the right bottom corner, you're done!

A simple installer for vanilla launcher [is coming soon](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/110)!

### Modrinth Launcher

I plan to support it, but it doesn't exist yet. For now see [PolyMC](#polymc) for a different launcher that also downloads from Modrinth.

### Other launchers

Technically you can install it in _some_ other launchers that support CurseForge modpacks or in _any_ launcher by following the vanilla instructions. However, I do not give support for them.

### Servers

Any server is supported, no installation is necessary. Still, it is highly recommended to protect your users from chat reports on 1.19.1+ - see [server setup](server-setup.md) for more info.

### Quilt

There have been questions regarding whether Fabulously Optimized can be installed with [Quilt](https://quiltmc.org). The answer is: probably, while Fabric mods are still supported in it, but this modpack's maintainer does not provide support for that. [(You can ask in Quilt's Discord, though.)](https://discord.quiltmc.org/)

If there becomes a need, Fabulously Optimized will move to Quilt overall and then it will be fully supported. Read more on [issue #257](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/257).

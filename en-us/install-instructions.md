# Install instructions

## Supported

### [CurseForge Launcher](https://download.curseforge.com/#download-options)

1. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files)
2. Click `Install` on the topmost CurseForge version
3. Accept the prompt (if asked), download should start
4. To run the modpack, hover on the modpack icon and click `Play`
5. Once the Minecraft Launcher has opened, click `Play` again

#### Or with the launcher already open:

1. Select _Minecraft_ from the grid or sidebar
2. Search "Fabulously Optimized"
3. Click `Install`
4. To run the modpack, hover on the modpack icon and click `Play`
5. Once the Minecraft Launcher has opened, click `Play` again

### [MultiMC](https://multimc.org)

You need [Java 17 or higher](https://adoptium.net/) to play the game.

1. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files)
2. Click `Download` on the latest **MultiMC version**
   * Click the title of the CurseForge version you need and scroll down, you'll find the MultiMC variant there.
      * Alternatively, look for it in the sidebar, under "server packs". Don't worry, these are not server packs, just marked as such for findability.
   * If you don't see any mods inside the zip or only see one, you downloaded the wrong version.   
3. Drag the ZIP-archive to MultiMC window, and hit OK in the window that pops up.
4. To run the modpack, double click the Fabulously Optimized icon

### [MultiMC](https://multimc.org) (auto-update)

You need [Java 17 or higher](https://adoptium.net/) to play the game.

1. Go to [readme](https://github.com/Fabulously-Optimized/fabulously-optimized#downloads), click "Alternative downloads"
2. Click the version number you need in the MultiMC (auto-update) section
3. Drag the ZIP-archive to MultiMC window, and hit OK in the window that pops up.
4. Double-click that version you just created to download and launch the modpack

<details>
  <summary>Need to download some mods manually?</summary>

  If you get asked to download a specific jar, it means I am not allowed to bundle it and you must add it manually:

  1. Copy and paste the given address to your browser
  2. Click `Cancel Launch`
  3. Click `Download` on the mod
  4. On MultiMC, click on the instance, then click `View Mods`
  5. Drag the downloaded mod into the mod list
  6. Click `Launch`

</details>

### [Prism Launcher](https://prismlauncher.org/)

You need [Java 17 or higher](https://prismlauncher.org/wiki/getting-started/installing-java/) to play the game.

1. Click `Add Instance`.
2. Select `Modrinth` tab from the left
3. Select "Fabulously Optimized"
4. Click `OK`
5. The modpack will now install.
6. Once installed, double-click the icon to play.

### [GDLauncher](https://gdlauncher.com/)

1. Click ➕ on bottom left corner
2. Select `CurseForge` tab
3. Search for "Fabulously Optimized"
4. Click `Download Latest`
5. Click ➡️ on the bottom right
6. To run the modpack, click the Fabulously Optimized icon

### [Minecraft Launcher](https://www.minecraft.net/en-us/download) (vanilla)

For macOS or Linux [you need Java](https://adoptium.net/) to run the Fabric Installer.

1. Download and install [Fabric Loader](https://fabricmc.net/use/) **version 0.14.11**
   * Older versions of the modpack - 1.12.3 and 2.7.3 need Fabric Loader 0.13.3.
   * Remember that the _installer version_ doesn't matter, what matters is the _loader version_ that appears when you run the installer.
2. Open Minecraft Launcher, click `Installations` and then click 📂 on the Fabric installation
3. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files) on CurseForge
4. Click `Download` on the latest **MultiMC version** of the pack
   * Click the title of the CurseForge version you need and scroll down, you'll find the MultiMC variant there.
      * Alternatively, look for it in the sidebar, under "server packs". Don't worry, these are not server packs, just marked as such for findability.
   * If you don't see any mods inside the zip or only see one, you downloaded the wrong version.
5. Open the zip file, go to _Fabulously Optimized x.x.x_ > _.minecraft_
6. Copy **all folders** from zip's .minecraft folder to your .minecraft folder; if asked - replace the files
7. If you want [FO default settings](changed-options.md) as well, delete `options.txt` (your vanilla options will be reset)
8. Launch the installed Fabric profile
9. If you now see "Fabulously Optimized" in the right bottom corner, you're done!

A simple installer for vanilla launcher [is coming soon](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/110)!

## Not supported

### Modrinth Launcher

Fabulously Optimized is [available on Modrinth](https://modrinth.com/modpack/fabulously-optimized), but an official launcher doesn't exist yet. When it gets released, it will be supported.
For now see [Prism Launcher](#prism-launcher) for a different launcher that also downloads from Modrinth.

### Pojav Launcher

Pojav Launcher is not yet supported due to drawbacks (long installation process, high energy usage, performance may not be better etc), but is being considered.

### ATLauncher

ATLauncher is currently not supported simply because the interface is confusing and complex. There have been discussions with its developer to improve this and it may be considered in the future.

### PolyMC

**[PolyMC is considered unsafe](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/496) and you should uninstall it immediately!**

To migrate to Prism Launcher (a safe fork of PolyMC), follow these instructions:

1. Uninstall PolyMC
2. Install [Prism Launcher](https://prismlauncher.org/)
3. Go to one of these directories according to your operating system:
   - Portable (Windows / Linux): `PolyMC/instances`
   - Windows: `%APPDATA%/PolyMC/instances`
   - macOS: `~/Library/Application Support/PolyMC/instances`
   - Linux: `~/.local/share/PolyMC/instances`
4. Select all the files and folders in the instances folder, right click on one of them and select `Copy`
5. Open Prism Launcher, click `Folders`, then `View Instance Folder`
6. Once your instance folder has opened, right click anywhere and select `Paste`
7. Close Prism Launcher and reopen it, your instances should be there
8. Sign in to your accounts, configure Prism Launcher to your preferences
9. If needed, [update](update-instructions.md#prism-launcher) or [install](install-instructions.md#prism-launcher) the modpack again
10. To run the modpack, double click the Fabulously Optimized icon

### Cracked launchers

Any launchers that let you run the game without having purchased it first are not supported.

There is a legitimate way to obtain Minecraft for cheaper: [get a giftcode from a trusted reseller!](https://punktid.com/minecraft-gift-code) Sign up with [this referral link for additional 10% off](https://punktid.com/?ref=robotkoer).
After that, pick any supported launcher from this page and enjoy the game! 

### Other launchers

Technically you can install it in _some_ other launchers that support CurseForge or Modrinth modpacks or in _any_ launcher by following the vanilla instructions. However, please do not ask for support if you use an unsupported launcher.

## Servers

Any server is supported, no installation is necessary. Still, it is highly recommended to protect your users from chat reports on 1.19.1+, see [server setup](server-setup.md) for more info.

## Quilt

There have been questions regarding whether Fabulously Optimized can be installed with [Quilt](https://quiltmc.org). The answer is: probably, while Fabric mods are still supported in it, but this modpack's maintainer does not provide support for that. [(You can ask in Quilt's Discord, though.)](https://discord.quiltmc.org/)

If there becomes a need, Fabulously Optimized will move to Quilt overall and then it will be fully supported. Read more on [issue #257](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/257).

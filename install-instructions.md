# Install instructions

Here are the instructions to install Fabulously Optimized to various launchers.

Can't use Minecraft 1.17 and higher? [Follow this tutorial](https://gist.github.com/Kichura/9fa44010d8ed9e5733d258292e327001) and then retry.

## Supported

### [CurseForge Launcher](https://download.curseforge.com/#download-options)

1. Go to [the listing page](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/) on CurseForge
2. Click `Install`
3. Accept the prompt (if asked), download should start in the launcher
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

1. Click `Add Instance`
2. Select `Modrinth` tab from the left
3. Select "Fabulously Optimized"
4. Click `OK`
5. The modpack will now install.
6. Once installed, double-click the icon to play.

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

1. Click `Add Instance`
2. Select `Modrinth` tab from the left
3. Select "Fabulously Optimized"
4. Click `OK`
5. The modpack will now install.
6. Once installed, double-click the icon to play.

### [Steam Deck](https://www.steamdeck.com/)

1. With Steam Deck turned on, hold down `⏻` (power) and tap `Switch to Desktop`.
2. From the taskbar, select 👜 "Discover".
3. Tap the searchbar on the top left corner, then press ❎ to open the on-screen keyboard.
4. Search for "Prism Launcher" and tap `Install` on the first result.
5. Launch it and go through its initial setup process, then close it.
6. Open Steam app, select `Games` → `Add a Non-Steam Game to My Library...` → select Prism Launcher → `ADD SELECTED PROGRAMS`.
7. Close Steam and launch `Return to Gaming Mode`.
8. Launch Prism Launcher from your game library.
9. Tap `Add Instance`
10. Select `Modrinth` tab from the left
11. Select "Fabulously Optimized"
12. Click `OK`
13. The modpack will now install.
14. Once installed, double-tap the icon and wait.
15. Tap `Options...` → `Controls...` → `🎮`
16. Set `Mode: Controller`, then `Done` → `Done` → `Done`
17. The game is now set up and you can just launch it from your game library from now on. 
18. Bonus: if you want a better icon in your game library, [follow these instructions](https://prismlauncher.org/download/steam-deck/#setting-up-artwork).

P.S. If you get Deck-specific issues, try asking on [r/SteamDeck](https://www.reddit.com/r/steamdeck) as FO moderators may not have one.

### [GDLauncher](https://gdlauncher.com/)

1. Click ➕ on bottom left corner
2. Select `CurseForge` tab
3. Search for "Fabulously Optimized"
4. Click `Download Latest`
5. Click ➡️ on the bottom right
6. To run the modpack, click the Fabulously Optimized icon

### [Minecraft Launcher](https://www.minecraft.net/en-us/download) (vanilla)

#### Windows

1. Open the [releases page](https://github.com/Fabulously-Optimized/vanilla-installer/releases/latest) and download the file with the `.exe` extension. (Example: `Vanilla Installer-GUI v0.1.0.exe`)
2. If it asks you where to save your file, select your Downloads folder (`%USERPROFILE%\Downloads`)
3. Navigate to the Downloads folder and double-click the file you just downloaded.
   * If you see a Microsoft Defender SmartScreen prompt, click `More info`, then `Run Anyway`.
4. Select the Minecraft version and directory, and click `Install`.
5. You're all done!

#### macOS

TODO

#### Linux

1. Install Python 3.8 or higher (3.11 recommended) from your package manager using one of the following examples: 
   - Ubuntu: `sudo apt install python3`
   - Arch Linux: `sudo pacman -S python3`
   - Fedora: `sudo dnf install python3` 

2. Run `pip3 install vanilla-installer[gui]`.
3. Then you can run `vanilla-installer-gui` to launch the program. If you have issues, try `python3 -m vanilla_installer gui`.

## Not supported

### Modrinth Launcher

Fabulously Optimized is [available on Modrinth](https://modrinth.com/modpack/fabulously-optimized), but an official launcher doesn't exist yet. When it gets released, it will be supported.
For now see [Prism Launcher](#prism-launcher) for a different launcher that also downloads from Modrinth.

### Pojav Launcher

Pojav Launcher is not yet supported due to drawbacks (long installation process, high energy usage, performance may not be better etc), but is being considered.

### ATLauncher

ATLauncher is currently not supported simply because the interface is confusing and complex. There have been discussions with its developer to improve this and it may be considered in the future.

### PolyMC

**[PolyMC is not safe](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/496) and you should uninstall it immediately!**

To migrate to Prism Launcher (a safe fork of PolyMC), follow these instructions:

1. Uninstall PolyMC
2. Install [Prism Launcher](https://prismlauncher.org/)
3. Launch it and pay attention to the prompt you get:
    1. > It looks like you used PolyMC before. Do you want to migrate your data to the new location of Prism Launcher?
         * Click `Yes` and the migration will complete.
    2. > It looks like you used PolyMC on Windows before. Do you want to migrate your data to the new location of Prism Launcher?
         * Click `Yes` and the migration will complete.
    3. > Old data from PolyMC was found, but you already have existing data for Prism Launcher. Sadly you will need to migrate yourself. Do you want to be reminded of the pending data migration next time you start Prism Launcher?
        * Click `No` and follow manual migration instructions below.
4. If needed, [update](update-instructions.md#prism-launcher) or [install](install-instructions.md#prism-launcher) the modpack again
5. To run the modpack, double click the Fabulously Optimized icon

<details>
  <summary>Manual migration</summary>

  1. Close Prism Launcher
  2. Go to one of these directories according to your operating system:
      - Portable (Windows/Linux): `PolyMC/instances`
      - Windows: `%APPDATA%/PolyMC/instances`
      - macOS: `~/Library/Application Support/PolyMC/instances`
      - Linux: `~/.local/share/PolyMC/instances`
  2. Select all the files and folders in the instances folder, right click on one of them and select `Copy`
  3. Open Prism Launcher, click `Folders`, then `View Instance Folder`
  4. Once your instance folder has opened, right click anywhere and select `Paste`
  5. Close Prism Launcher and reopen it, your instances should be there
  6. Sign in to your accounts, configure Prism Launcher to your preferences

</details>

### Cracked launchers

Any launchers that let you run the game without having purchased it first are not supported.

There is a legitimate way to obtain Minecraft for cheaper: [get a giftcode from a trusted reseller!](https://punktid.com/minecraft-java-bedrock) Sign up with [this referral link for additional 10% off](https://punktid.com/?ref=robotkoer).
After that, pick any supported launcher from this page and enjoy the game! 

### Other launchers

Technically you can install it in _some_ other launchers that support CurseForge or Modrinth modpacks or in _any_ launcher by following the vanilla instructions. However, please do not ask for support if you use an unsupported launcher.

### Other modpacks

Some users have experienced interest in using FO with other, content-focused modpacks. 

While it is theoretically possible, this is **not advised**:

* mods may have conflicts
* neither FO or the other modpack will be able to support you

Instead, we recommend you to use FO with [other mods added by you](adding-more-mods.md).

### Game clients

Fabulously Optimized is not compatible with any "game clients", including "hacked clients" and "PvP clients". [Use normal mods instead!](adding-more-mods.md)

### Bedrock Edition

Fabulously Optimized is not compatible with Bedrock Edition.

## Servers

Any server is supported, no installation is necessary. See [server setup](server-setup.md) for tips.

## Quilt

Fabulously Optimized is currently based on Fabric, not Quilt. It _may_ run on [Quilt](https://quiltmc.org), but it has not been tested and is not currently supported to ensure all mods work reliably. If you use it, do not ask for support in FO's Discord, but rather [Quilt's Discord](https://discord.quiltmc.org/).

If there becomes a need, Fabulously Optimized will move to Quilt overall and then it will be fully supported. Read more on [issue #257](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/257).

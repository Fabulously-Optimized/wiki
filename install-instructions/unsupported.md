---
hidden: true
---

## Unsupported launchers and install methods

### GDLauncher

Due to technical limits and issues, GDLauncher Legacy is no longer supported and GDLauncher Carbon not yet supported. It is recommended to use Prism Launcher instead:

1. [Install and run Prism Launcher](https://prismlauncher.org/)
2. Click `Add Instance`
3. Select `Modrinth` tab from the left
4. Select "Fabulously Optimized"
5. Click `OK`
6. The modpack will now install.
7. Once installed, click the `Folder` button on the left.
8. Open GDLauncher
9. Right click on your previously used instance → `Open Folder`
10. Copy the important files and folders over:
   * `saves` - your local worlds
   * `resourcepacks` - if you added any (it is not needed to copy [the modpack defaults](changed-options.md#resource-packs))
   * `shaders` - if you use any
   * `screenshots` - screenshots you've taken with F2 or F9
   * `servers.dat` - your multiplayer servers
   * `options.txt` - if you want to keep your vanilla option and all hotkey changes
11. Launch the instance on Prism and confirm everything is correct
12. Uninstall GDLauncher

### ATLauncher

_Not to be confused with [TLauncher](#tlauncher)._

ATLauncher is currently not supported simply because the interface is confusing and complex. There have been discussions with its developer to improve this and it may be considered in the future.

### Angel Aura Amethyst

Angel Aura Amethyst and its predecessor Pojav Launcher are not supported because they allow piracy and do not support Sodium, among some other issues.

### PolyMC

**[PolyMC is compromised](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/496) and you should uninstall it immediately!**

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

### TLauncher

_Not to be confused with [ATLauncher](#atlauncher)._

[TLauncher is malware](https://www.youtube.com/watch?v=SBTH9n6lz9o), so it will never be supported by Fabulously Optimized.
It is highly recommended to [reset your entire computer](https://www.howtogeek.com/202590/stop-trying-to-clean-your-infected-computer-just-nuke-it-and-reinstall-windows/), then come back to this page and follow install instructions for any supported launcher.

### Cracked launchers

Any launchers that let you run the game without having purchased it first are not supported.

There is a legitimate way to obtain Minecraft for cheaper: [get a giftcode from a trusted reseller](https://download.fo/minecraft).
After that, pick any supported launcher from this page and enjoy the game! 

### Other launchers

Technically you can install it in other launchers that support CurseForge or Modrinth modpacks or in any launcher by following the vanilla instructions. However, please do not ask for support if you use an unsupported launcher.

### Other mod loaders

The modpack only supports Fabric Loader.

### Other modpacks

Some users have experienced interest in using FO with other, content-focused modpacks. 

While it is theoretically possible, this is **not advised**:

* mods may have conflicts
* neither FO or the other modpack will be able to support you

Instead, we recommend you to use FO with [other mods added by you](adding-more-mods.md).

If you'd still like to do it on your responsibility, just install the other modpack first and then copy modpack's files on top [(see vanilla instructions)](install-instructions.md#minecraft-launcher-vanilla).

### Game clients

Fabulously Optimized is not compatible with any "game clients", including "hacked clients" and "PvP clients". [It is also itself not one.](principles.md#why-is-fabulously-optimized-not-a-client)

Instead, it is suggested to use this modpack and [add individual features as mods](adding-more-mods.md) that you might be missing from said clients. Here is a list for:
- [Lunar Client](https://alternatives.microcontrollers.dev/latest/lunar/#17-visuals)
- [Feather Client](https://alternatives.microcontrollers.dev/latest/feather/#visuals)
- [Badlion Client](https://alternatives.microcontrollers.dev/latest/badlion/#17-visuals)
- [Essential Mod](https://alternatives.microcontrollers.dev/latest/essential/#pictures)
   - Considered a "client" due to the amount of different things it does, which can also have incompatibilities.
   - World hosting [already exists in this modpack](disclaimers.md)

_Note: these lists are managed by contributors outside this wiki. There can be mods that are already in this modpack or are incompatible with it._

### Bedrock Edition

Fabulously Optimized is not compatible with Bedrock Edition [or mobile devices in general](install-instructions.md#angel-aura-amethyst). You may be interested in the [VDX resource pack](https://www.curseforge.com/minecraft-bedrock/addons/vdx-legacy-desktop-ui) just to achieve a Java-like look, however.
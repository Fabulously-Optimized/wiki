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

Or with the launcher already open:

1. Select _Minecraft_ from the grid or sidebar
2. Search "Fabulously Optimized"
3. Click `Install`
4. To run the modpack, hover on the modpack icon and click `Play`
5. Once the Minecraft Launcher has opened, click `Play` again

### [Prism Launcher](https://prismlauncher.org/)

You need [Java 17 or higher](https://prismlauncher.org/wiki/getting-started/installing-java/) to play the game.

1. Click `Add Instance`
2. Select `Modrinth` tab from the left
3. Select "Fabulously Optimized"
4. Click `OK`
5. The modpack will now install.
6. Once installed, double-click the icon to play.

### [Steam Deck](https://www.steamdeck.com/) + Prism Launcher

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

### [Minecraft Launcher](https://www.minecraft.net/en-us/download) (vanilla)

For macOS or Linux [you need Java](https://adoptium.net/) to run the Fabric Installer.

1. Download and install [Fabric Loader](https://fabricmc.net/use/) **version 0.14.19**
   * Older versions of the modpack - 1.12.3, 2.7.3 and 3.14.1 require the use of Fabric Loader 0.14.12 instead.
   * Remember that the _installer version_ doesn't matter, what matters is the _loader version_ that appears when you run the installer.
2. **For 4.8.0 and up**: Download [Sodium](https://modrinth.com/mod/sodium/version/mc1.19.4-0.4.10)
3. Open Minecraft Launcher, click `Installations`, then click 📂 on the Fabric installation
4. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files) on CurseForge
5. Click the topmost version, scroll down to "Additional files" section
6. Click `⋮` → `Download file` on the latest **MultiMC version**
   * If you don't see any mods inside the zip or only see one, you downloaded the wrong version.  
7. Open the zip file, go to _Fabulously Optimized x.x.x_ > _.minecraft_
8. Copy **all folders** from zip's .minecraft folder to your .minecraft folder; if asked - replace the files
9. **For 4.8.0 and up**: Copy downloaded Sodium JAR to _mods_ folder
10. It is highly recommended to delete `options.txt` as well to get [FO default settings](changed-options.md)
    * Your vanilla options like selected resource packs, language, keybinds will be reset but you can reapply them later.
    * If you choose not to do this, it is recommended to at least enable bundled resource packs manually.
11. Launch the installed Fabric profile
12. If you now see "Fabulously Optimized" in the right bottom corner, you're done!

A simple installer for vanilla launcher [is coming soon](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/110)!

### [Pojav Launcher](https://github.com/PojavLauncherTeam/PojavLauncher) (Android)

Fabulously Optimized can indeed be run on a mobile device! Be aware:

* This process has a lot of steps which you must follow carefully.
* The tutorial is made for Android devices - phones and tablets. iOS devices _could_ work, but that requires jailbreak or sideloading an alternative store, the steps are probably more complicated.
* Your device must be "mid-range" or "high-end" if you want decent FPS. 6+ GB RAM recommended.
* Pojav Launcher supports Android 5 and up, but these instructions were tested on Android 13.
* Your device will likely heat and consume a lot of battery as you play. It is _not_ as device-optimized as Bedrock Edition.
* Attempts have been made to improve performance, but depending on your device you may need to adjust video settings.
* In the worst case, you may not get it running at all. Try again after Pojav Launcher updates.

<details><summary><a href="https://play.google.com/store/apps/details?id=com.mojang.minecraftpe">I don't agree and just want to play Minecraft</a></summary></details>

<details>
  <summary>I agree and would like to see the instructions</summary>

1. [Download Pojav Launcher](https://play.google.com/store/apps/details?id=net.kdt.pojavlaunch)
   * Do not fall into scam websites and apps. The only official site for it is https://github.com/PojavLauncherTeam/PojavLauncher
2. [Download Files](https://play.google.com/store/apps/details?id=com.marc.files)
   * This is a shortcut to your system's file manager. Other file managers may need root to follow these instructions.
3. [Download Fabric installer](https://fabricmc.net/use/installer/) (Universal/.JAR)
4. [Download CurseForge GUI installer](https://github.com/Madis0/CurseForge-GUI/releases/download/2e9023f/CurseForge-GUI-1.0-SNAPSHOT.jar)
5. Download Fabulously Optimized patches for Pojav Launcher: [1.19.4](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/Fabulously-Optimized/fabulously-optimized/tree/pojav/PojavLauncher/1.19.4)
   * This optimizes the modpack for mobile users.
6. Run Pojav Launcher
7. Tap `Add account` → `Microsoft account` and sign in
8. Tap `(Default) - Unknown` → `Create new profile` → `SAVE`
9. Tap `Play`. Wait for it to fully load to the title screen, then exit the game.
    * If you get a RAM warning ("The current amount of..."), tap `OK` for now. It usually means you just need to close background apps for better performance.
    * If you get a black screen: quit the game, go back to Pojav → `🎛️` → `Video and renderer` → `Renderer` → (choose any) → ⬅️ → ⬅️ → try playing again
10. Launch Pojav again, tap `Install .jar` → select `fabric-installer-x.x.x.jar`. You'll see the Fabric installer with some logs.
11. Tap `❌` to close the logs, then `Install` → `OK` → `⛝`
12. Tap `Install .jar` → select `CurseForge-GUI-1.0-SNAPSHOT.jar`. You'll see a different kind of installer with some logs.
13. Tap `❌` to close the logs, then `Install modpack` → `KEYBOARD`
14. Enter the following code, according to the version you prefer. The keyboard may cover your screen, but try to get it right regardless.
    * **Latest for 1.19.4**: enter `396246`.
    * **3.14.1 for 1.18.2**: enter `396246_3983420`.
    * **2.7.3 for 1.17.1**: enter `396246_3667614`.
    * **1.12.3 for 1.16.5**: enter `396246_3667608`.
15. Press Enter on the keyboard and wait for the install to complete. Once installed, press `OK` → `⛝`
    * If you failed to enter the correct code, just close and try again from step 12.
16. Close Pojav and open Files.
17. Tap `☰` → `Downloads` → `(Minecraft version).zip` or `DownGit.zip` → `(Minecraft version)`
18. Hold down on `config` folder and tap on both items, then tap `⋮` → `Extract to...`
19. Tap `☰` → `PojavLauncher` → `curseforge-cli` → `modpack` → `fabulously-optimized_396246` → `EXTRACT`
20. Tap `☰` → `PojavLauncher` → `curseforge-cli` → `modpack` → `fabulously-optimized_396246` → `config (2)`
21. Hold on any file and select the other one
21. Tap `⋮` → `Move to...` → `☰` → `PojavLauncher` → `curseforge-cli` → `modpack` → `fabulously-optimized_396246` → `config`
22. Press `fabulously-optimized_396246` on the "address bar"
23. Hold down on `config (2)` → tap `🗑️` → `OK`
24. Launch Pojav, tap `New - Latest Release` → `Fabulously Optimized - ...` → `Play`.
25. Fabulously Optimized should now be running! 

</details>


## Not supported

### GDLauncher

Due to technical limits and issues, GDLauncher is no longer supported. It is recommended to migrate to Prism Launcher:

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
    * `saves` for your local worlds
    * `resourcepacks`, if you use any (do not copy old versions of FO-bundled packs though)
    * `screenshots`
    * `servers.dat` for your multiplayer servers
    * `options.txt`, if you want to keep your vanilla option changes
11. Launch the instance on Prism and confirm everything is correct
12. Uninstall GDLauncher

[GDLauncher Carbon](https://gdlauncher.com/en/blog/curseforge-partnership-announcement/) may be supported in the future.

### Modrinth Launcher

Fabulously Optimized is [available on Modrinth](https://modrinth.com/modpack/fabulously-optimized), but an official launcher doesn't exist yet. When it gets released, it will be supported.
For now see [Prism Launcher](#prism-launcher) for a different launcher that also downloads from Modrinth.

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

Fabulously Optimized is not compatible with Bedrock Edition. See [Pojav Launcher](#pojav-launcher-android) for an alternative.

## Servers

Any server is supported, no installation is necessary. See [server setup](server-setup.md) for tips.

## Quilt

Fabulously Optimized is currently based on Fabric, not Quilt. It _may_ run on [Quilt](https://quiltmc.org), but it has not been tested and is not currently supported to ensure all mods work reliably. If you use it, do not ask for support in FO's Discord, but rather [Quilt's Discord](https://discord.quiltmc.org/).

If there becomes a need, Fabulously Optimized will move to Quilt overall and then it will be fully supported. Read more on [issue #257](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/257).

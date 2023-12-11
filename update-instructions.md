# Update instructions

### Disclaimers

- As with any update, *things may break*. Probably not due to the modpack itself, but maybe your launcher, your custom mods or your hard drive. If worried, make backups.
- Upgrades from stable to unstable (alpha, beta) versions are **never** supported (make a separate instance!), while updates from unstable versions to stable ones are.
- Any kind of instance downgrading is **never** supported. Make a separate old instance or use something like [ViaFabricPlus](https://modrinth.com/mod/viafabricplus) if your server hasn't updated yet.
- If you follow these instructions properly, all custom mods and most mod settings you have will persist (except those that need to change). If you want, you can [reset your settings](#resetting-settings) to get the latest changes.

### CurseForge App

If you haven't changed the mods:

1. Select _Minecraft_ from the grid or sidebar
2. On My Modpacks, right click _Fabulously Optimized_, then `⇄ Change Version`
   * Don't see that option? Follow the other instructions below.
3. Select the topmost version, then `Continue`.
4. Modpack will now update.
5. Run it and check the version difference in the bottom right corner.

If you added or removed some mods:

1. Select _Minecraft_ from the grid or sidebar
2. On My Modpacks, click _Fabulously Optimized_
3. Click `⫶`→ `Profile Options`
4. Uncheck "Allow content management for this profile". You can re-enable content management after the update.
5. Click `Continue`
6. Click `⫶` → `⇄ Change Version`.
7. Select the topmost version, then `Continue`.
8. Modpack will now update.
9. Run it and check the version difference in the bottom right corner.

### Modrinth App

1. Select existing FO instance
2. Click `🔄 Update modpack` on top right
3. Select latest version and click `⇆`

### Prism Launcher

1. Select existing FO instance
2. Click `Edit` on the sidebar
3. Select `Modrinth` on the tab list
4. Click `Update pack`
5. Once the name prompt comes up, click `Yes`

### MultiMC

1. Click `Add Instance`
2. Select `Modrinth` tab from the left
3. Select "Fabulously Optimized"
4. Click `OK`
5. The modpack will now install.
6. Click that version you just created, then `Minecraft Folder`
7. Click the previous version, then `Minecraft Folder`
8. Copy the important files and folders over:
   * `saves` for your local worlds
   * `resourcepacks`, if you use any (do not copy old versions of FO-bundled packs though)
   * `screenshots`
   * `servers.dat` for your multiplayer servers
   * `options.txt`, if you want to keep your vanilla option changes
   * Ignore the `Copy all 3 folders!` file, that's for vanilla launcher users 
9. Close the folders and run the new version
10. If everything looks right, delete the old version

### MultiMC (auto-update)

In most cases:

1. Run the existing version, wait for the progress bar to fill up
   * If you get a popup "This modpack uses new versions of the following...", just click `Update`.
2. Check the version difference in the bottom right corner.

If there is a new Minecraft version:

1. Go to [readme](https://github.com/Fabulously-Optimized/fabulously-optimized#downloads), click "Alternative downloads"
2. Click the version number you need in the MultiMC (auto-update) section
3. Drag the ZIP-archive to MultiMC window
4. Click that version, then `Minecraft Folder`
5. Click the previous version, then `Minecraft Folder`
6. Copy the important files and folders over:
   * `saves` for your local worlds
   * `resourcepacks`, if you use any (do not copy the _Mod Menu Helper_ though)
   * `screenshots`
   * `servers.dat` for your multiplayer servers
   * `options.txt`, if you want to keep your vanilla option changes
   * Ignore the `Copy all 3 folders!` file, that's for vanilla launcher users 
7. Close the folders and run the new version
8. If everything looks right, delete the old version

<details>
  <summary>Got asked to download a mod manually?</summary>

  If you get asked to download a specific jar, it means I am not allowed to bundle it and you must add it manually:

  1. Copy and paste the given address to your browser
  2. Click `Cancel Launch`
  3. Click `Download` on the mod
  4. On MultiMC, click on the instance, then click `View Mods`
  5. Drag the downloaded mod into the mod list
  6. Click `Launch`

</details>

### Minecraft Launcher (vanilla)

Currently the only way to update is to "reinstall" the pack. Consider installing a different launcher for a smoother upgrade experience.

1. Download and install [Fabric Loader](https://fabricmc.net/use/) **version 0.15.0**
   * Remember that the _installer version_ doesn't matter, what matters is the _loader version_ that appears when you run the installer.
2. Open Minecraft Launcher, click `Installations`, then click 📂 on the Fabric installation
3. [Open this site](https://download.fo/vanilla) and click on the version you want
   * If you got a prompt for popup windows or multiple downloads, please accept it - technical limitation.
4. Open the zip file and copy **all folders** [(why?)](vanilla-launcher-faq.md#so-i-just-copy-the-mods-right) to your _.minecraft_ folder
   * If asked - replace the files.
5. Recommended: delete `options.txt` to get [FO default settings](changed-options.md)
    * Your vanilla options like selected resource packs, language, keybinds will be reset but you can reapply them later.
    * If you choose not to do this, please at least enable bundled resource packs manually.
6. Launch the installed Fabric profile
7. If you now see "Fabulously Optimized" in the right bottom corner, you're done!

<details>
  <summary>Legacy instructions - Minecraft 1.19.3 and older</summary>

  1. Download and install [Fabric Loader](https://fabricmc.net/use/)
     * Minecraft 1.19-1.19.3: Fabric Loader **0.14.24**
     * Minecraft 1.16.5-1.18.2: Fabric Loader **0.14.12**
     * Remember that the _installer version_ doesn't matter, what matters is the _loader version_ that appears when you run the installer.
  2. Open Minecraft Launcher, click `Installations`, then click 📂 on the Fabric installation
  3. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files?showAlphaFiles=show) on CurseForge
  4. Click the topmost version, scroll down to "Additional files" section
  5. Click `⋮` → `Download file` on the latest **MultiMC version**
     * If you see less than 10 mods in the zip, you downloaded the wrong version.  
  6. Open the zip file, go to _Fabulously Optimized x.x.x_ > _minecraft_
  7. Open the zip file and copy **all folders** [(why?)](vanilla-launcher-faq.md#so-i-just-copy-the-mods-right) from zip's _minecraft_ folder to your _.minecraft_ folder
     * If asked - replace the files.
  8. Recommended: delete `options.txt` to get [FO default settings](changed-options.md)
     * Your vanilla options like selected resource packs, language, keybinds will be reset but you can reapply them later.
     * If you choose not to do this, please at least enable bundled resource packs manually.
  9. Launch the installed Fabric profile
  10. If you now see "Fabulously Optimized" in the right bottom corner, you're done!

</details>

### GDLauncher

No longer supported. [Please migrate to Prism Launcher.](install-instructions.md#gdlauncher)

### Updating mods

* If you are using a supported version of Fabulously Optimized and you haven't added any extra mods, **do not update any mods manually**, just update the modpack instead.
   * If you did add extra mods, **update those individually** after you've ensured you're on latest version of Fabulously Optimized.
   * Updating mods that are in FO may cause unexpected issues which FO releases would prevent, so manual updates only make your own life harder.
* If you are using an unsupported (legacy) version of Fabulously Optimized, **you may carefully update the mods**.
   * Keep in mind that we haven't tested those updates, so you may run into issues and need to revert back to previous versions.
* Some launchers have options to update all mods at once. **Do not use this feature** for reasons listed above.
    * Even for legacy versions of FO, updating everything at once like that may cause problems like mod loader mismatch, Minecraft version mismatch, mod platform variances (more recent version on one platform vs another) and so on.
    * It is always safer to update each mod individually so that you can see the update was successful and valid for your MC version/mod loader.
* If you did any of the things above and are having issues, simply update Fabulously Optimized again, even if you have the same version.

### Resetting options

Because the pack is using YOSBR, your vanilla options and most of the mod ones will not change when you upgrade, [despite what is stated in the changelog](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/CHANGELOG.md). This is made so that you can upgrade without having to reconfigure your options all the time. 

However, at some point you may still want to do that in order to get the latest changes. So:

1. Open the modpack folder
   * CurseForge Launcher: right click on the modpack tile → `Open Folder`
   * Prism Launcher: right click on the instance → `Folder` → `.minecraft`
   * MultiMC: right click on the instance → `Minecraft Folder`
   * Vanilla launcher: go to `Installations` tab → hover on the instance → click `📁`
2. Delete the `config` folder
   * If you prefer, also delete `options.txt` which stores vanilla options
3. Download [your version of FO again from Modrinth](https://modrinth.com/modpack/fabulously-optimized/versions)
4. Rename the file to `pack.zip`
5. Open the file you renamed, go to `overrides`
6. Copy/extract the folder `configs` out to the modpack folder you previously opened
   * You may delete the `pack.zip` after you're done
7. Launch the game. Modpack's defaults are now applied!

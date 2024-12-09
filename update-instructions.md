# Update instructions

### Disclaimers

- As with any update, *things may break*. Probably not due to the modpack itself, but maybe your launcher, your custom mods or your hard drive. If worried, make backups.
- Upgrades from stable to unstable (alpha, beta) versions of the modpack are **never** supported (make a separate instance!), while updates from unstable versions to stable ones are.
- Any kind of instance downgrading is **never** supported. Make a separate old instance or use something like [ViaFabricPlus](https://modrinth.com/mod/viafabricplus) if your server hasn't updated yet.
- If you follow these instructions properly, all custom mods and most mod settings you have will persist (except those that need to change). If you want, you can [reset your settings](#resetting-settings) to get the latest changes.

#### Updating mods

* If you are using a supported version of Fabulously Optimized and you haven't added any extra mods, **do not update any mods manually**, just update the modpack instead.
   * If you did add extra mods, **update those individually** after you've ensured you're on latest version of Fabulously Optimized.
   * Updating mods that are in FO may cause unexpected issues which FO releases would prevent, so manual updates only make your own life harder.
* If you are using an unsupported (legacy) version of Fabulously Optimized, **you may carefully update the mods**.
   * Keep in mind that we haven't tested those updates, so you may run into issues and need to revert back to previous versions.
* Some launchers have options to update all mods at once. **Do not use this feature** for reasons listed above.
    * Even for legacy versions of FO, updating everything at once like that may cause problems like mod loader mismatch, Minecraft version mismatch, mod platform variances (more recent version on one platform vs another) and so on.
    * It is always safer to update each mod individually so that you can see the update was successful and valid for your MC version/mod loader.
* If you did any of the things above and are having issues, simply update Fabulously Optimized again.
  * This will reset your mod list to the specified FO version ones, even if you used the same version of FO beforehand.

### CurseForge App

If you haven't changed the mods:

1. Select _Minecraft_ from the grid or sidebar
2. On My Modpacks, right click _Fabulously Optimized_, then `⇄ Change Version`
   * Don't see that option? Follow the other instructions below.
3. Click `Continue`.
   * Optional: Select the version you want by selecting it on the dropdown before you click `Continue`.
4. Modpack will now update.
5. Run it and check the version difference in the bottom right corner.

If you added or removed some mods:

1. Select _Minecraft_ from the grid or sidebar
2. On My Modpacks, click _Fabulously Optimized_
3. Click `⫶`→ `Profile Options`
4. Uncheck "Allow content management for this profile". This will not affect added content and you can re-enable content management after the update.
5. Click `Continue`
6. Click `⫶` → `⇄ Change Version`.
7. Click `Continue`.
   * Optional: Select the version you want by selecting it on the dropdown before you click `Continue`.
8. Modpack will now update.
9. Run it and check the version difference in the bottom right corner.

### Modrinth App

1. Select existing FO instance
2. Click `🔄 Update modpack` on top right
3. Click `⇆`
   * Optional: Select the version you want by selecting it on the dropdown before you click `⇆`.
  
<details>
  <summary>Error: "Invalid game version"</summary>
  If you are getting an error, such as "Error launching Minecraft: Invalid game version: 1.21.4", then you need to delete the cache on the app. 
  
  To do that:
  
  1. Go to settings in the bottom left corner
  2. Under "App cache", click `🗑️ Purge cache` and again `🗑️ Purge cache`
  3. Restart the app just in case
  4. Update the modpack with the instructions above

  **Note:** "Cache" refers to internal things like the list of Minecraft and Fabric versions. Purging the cache will never affect your instances or worlds!
</details>

### Prism Launcher

1. Select existing FO instance
2. Click `Edit` on the sidebar
3. Select `Modrinth` on the tab list
4. Click `Update pack`
   * Optional: Select the version you want by selecting it on the dropdown before you click `Update pack`.
5. Once the name prompt comes up, click `Yes`

### MultiMC

1. Click `Add Instance`
2. Select `Modrinth` tab from the left
3. Select "Fabulously Optimized"
4. Click `OK`
   * Optional: Select the version you want by selecting it on the dropdown before you click `OK`.
5. The modpack will now install.
6. Click that version you just created, then `Minecraft Folder`
7. Click the previous version, then `Minecraft Folder`
8. Copy the important files and folders over:
   * `saves` - your local worlds
   * `resourcepacks` - if you added any (it is not needed to copy [the modpack defaults](changed-options.md#resource-packs))
   * `shaders` - if you use any
   * `screenshots` - screenshots you've taken with F2 or F9
   * `servers.dat` - your multiplayer servers
   * `options.txt` - if you want to keep your vanilla option and all hotkey changes
   * Ignore the `Copy all 3 folders!` file, that's for vanilla launcher users 
9. Close the folders and run the new version
10. If everything looks right, delete the old version

### MultiMC (auto-update)

In most cases:

1. Run the existing version, wait for the progress bar to fill up
   * If you get a popup "This modpack uses new versions of the following...", just click `Update`.
2. Check the version difference in the bottom right corner.

If there is a new Minecraft version:

1. [Download the pack for your preferred Minecraft version](install-instructions.md#multimc-auto-update)
2. Drag the ZIP-archive to MultiMC window
3. Click that version, then `Minecraft Folder`
4. Click the previous version, then `Minecraft Folder`
5. Copy the important files and folders over:
   * `saves` - your local worlds
   * `resourcepacks` - if you added any (it is not needed to copy [the modpack defaults](changed-options.md#resource-packs))
   * `shaders` - if you use any
   * `screenshots` - screenshots you've taken with F2 or F9
   * `servers.dat` - your multiplayer servers
   * `options.txt` - if you want to keep your vanilla option and all hotkey changes
   * Ignore the `Copy all 3 folders!` file, that's for vanilla launcher users 
6. Close the folders and run the new version
7. If everything looks right, delete the old version

<details>
  <summary>Got asked to download a mod manually?</summary>

  If you get asked to download a specific jar, it means we are not allowed to bundle it and you must add it manually:

  1. Copy and paste the given address to your browser
  2. Click `Cancel Launch`
  3. Click `Download` on the mod
  4. On MultiMC, click on the instance, then click `View Mods`
  5. Drag the downloaded mod into the mod list
  6. Click `Launch`

</details>

### Minecraft Launcher (vanilla)

1. Download [Fabulously Optimized Installer](https://download.fo/vanilla) and run it
    * In most cases, you may also use the older version of the installer if you have it already.
    * Windows: Open the .exe file, click `More info` and then `Run anyway`.
    * macOS: See instructions below
    * Linux: Open the .appimage file and click `Run once` when prompted.
3. Select preferred FO/Minecraft version and install
4. Run Minecraft Launcher. You'll see the new installation, click PLAY.

Note: you may now see a new file _paigaldaja_meta.json_ next to the installer. This is a configuration file that ensures smoother upgrades and remembers some of your install settings.

<details>
  <summary>MacOS installer opening instructions</summary>

  #### macOS Sequoia 15 and later
  1. Open the downloaded .dmg file
  2. Double-click the "Fabulously Optimized Installer". You will get a warning, press `Done`.
  3. On your menubar, press Apple logo, then `System Settings`, then click `Privacy & Security` in the sidebar
  4. Scroll down on the right view, you should see the button `Open anyway`
  5. Enter your password or fingerprint. The installer should open.
  6. Future launches of the same installer version open the installer directly on double-click.

  #### macOS Sonoma 14 and older
  1. Open the downloaded .dmg file
  2. **Right click** the "Fabulously Optimized Installer" and click `Open`
  3. Click `Open` again when asked in a prompt. The installer should open.
  4. Future launches of the same installer version open the installer directly on double-click.

  #### Why is this necessary?
  Apple requires 99$ a year to get a program "verified". This is not feasible for this modpack.
  If you are concerned, feel free to use manual instructions or a different launcher.
  
</details>
<details>
   <summary>Manual installation - Minecraft 1.19.4+</summary>

1. Download and install [Fabric Loader](https://fabricmc.net/use/) **version 0.16.9**
   * Remember that the _installer version_ doesn't matter, what matters is the _loader version_ that appears when you run the installer.
2. Open Minecraft Launcher, click `Installations`, then click 📂 on the Fabric installation
3. [Open this site](https://download.fo/vanilla), then click the ⬇️ button
   * Optional: Select the version you want by selecting it on the dropdown before you click ⬇️.
   * If you got a prompt for popup windows or multiple downloads, please accept it - technical limitation.
4. Open the zip file and copy **all folders** [(why?)](vanilla-launcher-faq.md#so-i-just-copy-the-mods-right) to your _.minecraft_ folder
   * If asked - replace the files.
5. Recommended: delete `options.txt` to get [FO default settings](changed-options.md)
    * Your vanilla options like selected resource packs, language, keybinds will be reset but you can reapply them later.
    * If you choose not to do this, please at least enable bundled resource packs manually.
6. Launch the installed Fabric profile
7. If you now see "Fabulously Optimized" in the right bottom corner, you're done!

</details>

<details>
  <summary>Manual installation - Minecraft 1.16.1-1.19.3</summary>

  1. Download and install [Fabric Loader](https://fabricmc.net/use/)
     * Minecraft 1.19-1.19.3: Fabric Loader **0.14.24** and [Java 17](https://download.fo/java17)
     * Minecraft 1.17-1.18.2: Fabric Loader **0.14.12** and [Java 17](https://download.fo/java17)
     * Minecraft 1.16.5: Fabric Loader **0.13.3** and [Java 8](https://download.fo/java8)
     * Remember that the _installer version_ doesn't matter, what matters is the _loader version_ that appears when you run the installer.
  2. Open Minecraft Launcher, click `Installations`, then click 📂 on the Fabric installation
  3. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files?showAlphaFiles=show) on CurseForge
  4. Click the version you need, then click "Additional files"
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

## Resetting options

Because the pack is using YOSBR, your vanilla options and most of the mod ones will not change when you upgrade, [despite what is stated in the changelog](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/CHANGELOG.md). This is made so that you can upgrade without having to reconfigure your options all the time. 

However, at some point you may still want to do that in order to get the latest changes.

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

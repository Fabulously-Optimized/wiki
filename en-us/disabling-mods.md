# Disabling mods

Don't like a feature or having a mod conflict? Easiest way to resolve it is to disable the mod. For resource pack-related issues, [see this page](resource-pack-issues.md).

Notes:

* You can also delete the mod(s), but that will make it harder to [use them later](adding-more-mods.md), unless you remember the mod's name exactly.
* Don't disable anything that says "API", other mods need it to work.

### Mod Menu

1. With the game open, click `Mods`
2. Scroll down to the specific mod you want to disable, note the third row with the pencil icon ✏️
   * If the pencil is blue and the text says "Toggle mod", click the config button ![config](https://i.ibb.co/j35cBtn/image.png) and find the setting that disables the mod
   * If the pencil is blue and the text says something else, click the config button ![config](https://i.ibb.co/j35cBtn/image.png) and see if you can disable the specific feature you need
   * If the pencil is gray and there is no config button, follow your launcher-specific instructions below
   * If you don't see any pencils, you don't have the Mod Menu Helper resource pack enabled for some reason.
     1. Click `Done` -> `Options...` -> `Resource Packs...` -> `⏵` on "Mod Menu Helper.zip" -> `Done` -> go to point 1 of this tutorial

### CurseForge Launcher

1. Open CurseForge Launcher
2. Go to `My Modpacks`, click on Fabulously Optimized
3. Click on the three dots, select `Profile Options`
4. Check "Allow content management for this profile", click `Done`
5. Find the mod you need, toggle the knob.

**Note: you must disable "Allow content management for this profile" in order to update the modpack.**

### GDLauncher

1. Open GDLauncher
2. Right click Fabulously Optimized, click on `Manage`
3. Select `Mods`
4. Find the mod you need, toggle the knob.

### MultiMC

1. Open MultiMC
2. Click on Fabulously Optimized, then `Edit Instance`
3. Go to `Loader mods`
4. Find the mod you need, uncheck the checkbox.

### MultiMC (auto-update)

Unfortunately, the normal MultiMC method won't work with this as it redownloads disabled mods on launch. There are workarounds though, [tutorials written here](multimc-auto-update.md#can-i-ignore-some-of-the-mods).

### PolyMC

1. Open PolyMC
2. Click on Fabulously Optimized, then `Edit Instance`
3. Go to `Mods`
4. Find the mod you need, uncheck the checkbox.

### Minecraft Launcher (vanilla)

1. Open Minecraft Launcher, click on `Installations`
2. Click the folder icon on the profile you've created for the pack (could be named Fabric)
3. Click `mods`
4. Rename the specific mod from "modname.jar" to "modname.jar-old"
   * Don't see ".jar" at the end of the name? [See this page for help.](https://www.thewindowsclub.com/show-file-extensions-in-windows)
   * Rename ".jar-old" back to ".jar" to use the mod again.

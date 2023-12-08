# Vanilla launcher FAQ

This FAQ gives answers to questions you might have about using Fabulously Optimized in [the official Minecraft Launcher](https://www.minecraft.net/en-us/download), also known as simply "vanilla launcher". If you have any additional questions, please join our [Discord](https://fabulously-optimized.github.io/discord) and ask in #support. 

### How to install?

To install Fabulously Optimized on the vanilla launcher, [please follow this guide](https://fabulously-optimized.gitbook.io/modpack/readme/install-instructions#minecraft-launcher-vanilla).

### So I just copy the mods, right?

No. Fabulously Optimized consists of mods, configs and resourcepacks. 

If you try to install FO to the vanilla launcher by copying just the `mods` folder, you may notice these issues:

* Some of your resource packs are broken
* Zoom is broken and new unexpected keybinds exist 
* Confusing mod buttons and texts appear in the interface
* Mod list does not contain the simplified descriptions and has some confusing ones
* No version number in the title screen (main menu)
* Other features do not work as advertised

### I only copied the mods, what should I do now?

Don't worry, we can fix that!

1. Open Minecraft Launcher, click `Installations` and then click 📂 on the Fabric installation
2. Backup and delete `config` folder and `options.txt` file
   * `config` contains all of your mod configs.
   * `options.txt` contains vanilla settings and keybinds
   * "Backup" means copying the existing folder and file to a different location, in case you need to reference or copy it back later. If you don't care about your existing settings, you don't have to do this.
   * If your FO is not up to date, also delete the `mods` folder.
3. Open the ZIP file of Fabulously Optimized that you have or [download it again](https://download.fo/vanilla)
4. Go to _Fabulously Optimized x.x.x_ > _.minecraft_
5. Copy **all folders** from zip's .minecraft folder to your .minecraft folder; if asked - replace the files
6. Launch the Fabric profile
7. If you now see "Fabulously Optimized" in the right bottom corner, you're done!
8. Optional: copy back any mod settings you need from the folder you backed up

### What is the MultiMC ZIP?

The MultiMC ZIP is a packaged instance for the launcher called [MultiMC](https://multimc.org). It is distributed in CurseForge because MultiMC itself no longer supports downloading CurseForge modpacks and downloads from CurseForge support the creator of FO. This also allows for an easy installation of FO for vanilla launcher users.

### What is in the ZIP file?

- `Fabulously Optimized x.x.x` - the folder containing the MultiMC instance
  - `minecraft` - the main folders that make the modpack
     - `config` - configuration files that adjust the mods for best experience
     - `mods` - mods that are included in the modpack
     - `resourcepacks` - small resource packs that improve the experience [(what do they do?)](changed-options.md#resource-packs)
     - `Copy all 3 folders!` - a dummy file that reminds you to do just that
  - `instance.cfg` - manifest file describing the name, icon, type and notes for the instance
  - `mmc-pack.json` - manifest file describing the Minecraft, Fabric and other dependency versions
  - `pack.png` - an icon for the instance

### Why try a different launcher?

There are a variety of launchers available, each with unique features. The vanilla launcher is basic, and it lacks many features that other launchers have. Features include the ability to download the modpack more easily, update the modpack and the version of Minecraft, and add any mod with a few simple clicks. Some launchers have unique features like a built-in modpack and mod browser which allows you to download mods and modpacks without having to go to CurseForge or Modrinth and support for more platforms like Steam Deck.

### Why is FO not a client?

- We would need explicit permission from the mod authors to use their mods in a client
- The authors of each mod would receive no benefits by being included (unless ads or similar are included)
- Less flexibility in mods that we could include at all
- The client would need to be coded and maintained to keep it up to date

Being a modpack makes it easier for the users to add their own mods in and use Fabulously Optimized as base pack for their own needs. This also makes it easier for the creator to add, remove and swap any mods at any time.

### Is there an easier way to install FO?

Soon there will be an installer that will make it easier to install the modpack on the vanilla launcher. You can follow the [relevant issue](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/110) to know when it is released. 

However, we still advise you to prefer other launchers like CurseForge Launcher, as they make installing, updating and adding mods much easier than vanilla launcher ever can.

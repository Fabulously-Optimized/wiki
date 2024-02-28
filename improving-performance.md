# Improving performance

Fabulously Optimized consists of mods and settings that aim to improve performance for most devices. But sometimes you need more targeted optimizations, this page describes some of those.

## Video settings

* Render distance - affects how far you see and has a high impact on performance. Lowering that is the first thing to try.
* Simulation distance - affects entity (mob) spawning and movement. If you're using big mob farms, you may want to lower this.
* VSync - limits your framerate to your screen's Hz, which may give you a smooth game that uses less system resources, but may also add input lag or reduce framerate with shaders.
   * If available, try using Adaptive VSync rather than ON first.
   * [See this article for more info](https://www.howtogeek.com/853225/what-is-vsync-and-should-you-enable-it/)
* Max framerate - similar to Vsync, but instead of being automatic, you control the maximum frame rate.
* Weather/leaves - using the "fast" mode may give you a better experience. It is advised to change these separately and keep Graphics on "fancy".
* Particles - FO allows you to either reduce the rate of particles (all/decreased/minimal) or toggle the ones individually.
* Entity distance - unlike simulation distance, this affects just the distance where you _see_ the mobs, which means it also works in multiplayer.

Hint: the tooltips of the options usually give you good info on the impact and the effects of each option.

## Adding RAM

Usually, you'd not need to add RAM just to play Minecraft. However, if you want to run intensive shaders or high-resolution resource packs, it may be a good idea. 

Try: 

* 2GB for light use (if you also lower your video settings)
* 4GB for most users
* 6GB only if you want to play with shaders, high render distance, high-resolution resource pack/shaders, etc.

Click the link for a tutorial that is made for your launcher.

* [CurseForge App](https://serverminer.com/article/how-to-add-more-ram-to-your-curseforge-launcher-overwolf/)
* [Modrinth App](https://www.bisecthosting.com/clients/index.php?rp=/knowledgebase/573/How-to-allocate-more-ram-in-the-Modrinth-launcher.html)
* [Prism Launcher](https://prismlauncher.org/wiki/help-pages/java-settings/#memory)
* [MultiMC](https://github.com/MultiMC/Launcher/wiki/Increasing-Java%27s-memory-allocation)
* [Minecraft Launcher](https://www.wikihow.com/Allocate-More-RAM-to-Minecraft#Using-Launcher-Version-1.6.X)

## Dedicated GPU

Own a gaming computer? Follow these instructions to ensure your computer will take full advantage of FO's optimizations.

Before changing any settings, ensure your drivers are up to date:

* [Intel](https://www.intel.com/content/www/us/en/support/intel-driver-support-assistant.html)
* [NVIDIA](https://www.nvidia.com/en-us/geforce/geforce-experience/)
* [AMD](https://www.amd.com/support)

And these instructions tell you how to enable specific optimizations or make the software recognize Minecraft as a game:

* [NVIDIA (GeForce Experience)](https://www.addictivetips.com/windows-tips/add-games-geforce-experience/)
* [NVIDIA (Control Panel)](https://www.nvidia.com/content/Control-Panel-Help/vLatest/en-us/mergedProjects/nv3d/to_configure_uniques_3D_settings_for_my_applications_and_gamess.htm)
  * [Additional settings](https://www.pcgamer.com/nvidia-control-panel-a-beginners-guide/)
* [AMD (Radeon Software)](https://minecrafthopper.net/help/amd-dedicated-gpu/)
  * [Alternative method](https://www.amd.com/en/support/kb/faq/dh2-012#faq-Creating-Application-Profiles)
* [MSI AfterBurner](https://www.msi.com/support/technical_details/VGA_MSI_Utility_AfterBurner)
* On Linux, Intel and AMD GPUs on Linux usually do not need additional configuration, but ensure your system is up to date.

Please note that Fabulously Optimized moderators may not have these graphics cards and as such may not be help you with this. You can search online or ask in a community such as [Fabric Discord](https://discord.gg/v6v4pMv).

## Additional mods

Mods that may improve performance in specific scenarios, but are not necessarily stable or relevant to be included in FO itself. No guarantees and no support is provided by FO for these mods.

* [Nvidium](https://modrinth.com/mod/nvidium) - improves performance with NVIDIA GPUs, as long as you don't use shaders
* [Methane](https://modrinth.com/mod/methane) - optimizes the game by removing light calculations, aka using the "fullbright" effect
* [C2ME](https://modrinth.com/mod/c2me-fabric) - improve chunk loading by using very experimental optimizations

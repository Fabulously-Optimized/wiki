---
hidden: true
hidden: true
---

# Other Options

Although FO's mods do an admirable job at optimizing the game's performance for most devices, you may sometimes need more targeted optimizations.

## Video Settings

{% hint style="info" %}
Check the tooltips in Video Settings for detailed information about each option's impact.
{% endhint %}

| Option                  | Description                                                                                                                                                                                                                                             |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Render Distance**     | Determines how far you can see. Lowering this is your best bet, as it has a high impact on performance.                                                                                                                                                 |
| **Simulation Distance** | Affects entity spawning and movement. Reduce it for large mob farms.                                                                                                                                                                                    |
| **VSync**               | Limits your frame rate to your screen's refresh rate. Can reduce resource usage but may add input lag. Adaptive VSync is recommended when available. [Learn more about VSync](https://www.howtogeek.com/853225/what-is-vsync-and-should-you-enable-it). |
| **Max Framerate**       | Controls FPS like VSync, but manually instead of automatically.                                                                                                                                                                                         |
| **Weather/Leaves**      | Switching to "fast" mode may improve performance. Try changing them individually, while keeping Graphics on "fancy".                                                                                                                                    |
| **Particles**           | Adjust the particle rate (all/decreased/minimal) or toggle specific ones individually.                                                                                                                                                                  |
| **Entity Distance**     | Alters how far away you see mobs, both in singleplayer and in multiplayer.                                                                                                                                                                              |

## Adding RAM

You usually don’t need to allocate more RAM for Minecraft, but for intensive shaders or high-resolution resource packs, consider:

* `2 GB`: Light use with reduced video settings
* `4 GB`: Standard use for most players
* `6 GB`: For shaders, high render distance, or high-resolution resource packs

Follow these guides to allocate more RAM for your launcher:

* [CurseForge App](https://serverminer.com/article/how-to-add-more-ram-to-your-curseforge-launcher-overwolf/)
* [Modrinth App](https://www.bisecthosting.com/clients/index.php?rp=/knowledgebase/573/How-to-allocate-more-ram-in-the-Modrinth-launcher.html)
* [Prism Launcher](https://prismlauncher.org/wiki/help-pages/java-settings/#memory)
* [MultiMC](https://github.com/MultiMC/Launcher/wiki/Increasing-Java%27s-memory-allocation)
* [Minecraft Launcher](https://www.wikihow.com/Allocate-More-RAM-to-Minecraft#Using-Launcher-Version-1.6.X)

## Dedicated GPU

Using a gaming computer? Ensure your GPU optimizations are configured:

### Update Drivers

* [Intel](https://www.intel.com/content/www/us/en/download-center/home)
* [NVIDIA](https://www.nvidia.com/en-us/software/nvidia-app)
* [AMD](https://www.amd.com/en/support)

### Optimization Guides

* [NVIDIA GeForce Experience](https://www.addictivetips.com/windows-tips/add-games-geforce-experience)
* [NVIDIA Control Panel](https://www.nvidia.com/content/Control-Panel-Help/vLatest/en-us/mergedProjects/nv3d/to_configure_uniques_3D_settings_for_my_applications_and_gamess)
  * [Additional NVIDIA Settings](https://www.pcgamer.com/nvidia-control-panel-a-beginners-guide)
* [AMD Radeon Software](https://minecrafthopper.net/help/amd-dedicated-gpu)
  * [Alternative AMD Settings](https://www.amd.com/en/support/kb/faq/dh2-012#faq-Creating-Application-Profiles)
* [MSI AfterBurner](https://www.msi.com/support/technical_details/VGA_MSI_Utility_AfterBurner)

For Linux users, Intel and AMD GPUs generally require no additional setup, but keeping your system updated is essential.

{% hint style="info" %}
Fabulously Optimized moderators may not have access to all GPU configurations. Seek additional help from online communities like [Fabric Discord](https://discord.gg/v6v4pMv).
{% endhint %}

## Additional Mods

Here are some [mods you can add](../../how-to/add-mods/) that may improve performance in specific scenarios.

{% hint style="warning" %}
These mods may introduce instability or be unsuitable for every setup. Because of this they are not officially supported by FO.
{% endhint %}

* [Nvidium](https://modrinth.com/mod/nvidium): Optimizes performance with NVIDIA GPUs (not compatible with shaders)
* [Methane](https://modrinth.com/mod/methane): Removes light calculations, resulting in a "fullbright" effect
* [C2ME](https://modrinth.com/mod/c2me-fabric): Optimizes chunk loading (very experimental)

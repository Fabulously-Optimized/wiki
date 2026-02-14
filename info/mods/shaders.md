---
hidden: true
---

# Shaders

FO supports shaders through [Iris](https://modrinth.com/mod/iris). You can find [shaders from Modrinth](https://modrinth.com/shaders?g=categories:iris) or [shaders from CurseForge](https://www.curseforge.com/minecraft/search?class=shaders).

To install an Iris shader:

1. Download any shader. You should get a `zip` file
2. In Minecraft's main menu, click on <kbd>**Options...**</kbd>
3. Click on <kbd>**Video Settings...**</kbd>
4. Click on <kbd>**Shader Packs...**</kbd>
5. Drag the `zip` file you downloaded in _step 1_ to the screen you opened in _step 4_
6. Select the shader
7. Make sure <kbd>**Shaders**</kbd> is enabled
8. If you want to configure the shader, use the <kbd>**Shader Pack Settings...**</kbd> button
9. Click on <kbd>**Apply**</kbd>

{% hint style="info" %}
If you run into any issues, please report them on the [Iris issue tracker](https://github.com/IrisShaders/Iris/issues).
{% endhint %}

## Internal Shaders

To get OptiFine's internal shaders, you can use:

* ["internal-shaders" shader](https://modrinth.com/shader/internal-shaders)
* ["Simply No Shading" mod](https://modrinth.com/mod/simply-no-shading)
* ["Flat Lighting" mod](https://modrinth.com/mod/flat-lighting)

## Fabulous Shaders

Fabulous shaders are vanilla shaders which work by enabling <kbd>**Fabulous!**</kbd> graphics in video settings.

Examples of Fabulous Shaders include:

* [Fabulousity](https://github.com/ScottoMotto/Fabulousity#fabulousity) ([preview on YouTube](https://youtu.be/luzgOwKt6_c?t=126))
* [Basic Shaders](https://github.com/bradleyq/mc_vanilla_shaders) ([preview on YouTube](https://youtu.be/dRnlaRx3zBY?t=24))
* [Sildur's Fabulous Shaders](https://sildurs-shaders.github.io/downloads) ([configuration instructions](https://sildurs-shaders.github.io/install/#fabulous))
* [Depth Shaders](https://github.com/onnowhere/depth_shaders/releases)
* [More from Modrinth](https://modrinth.com/shaders?g=categories:vanilla)

## Core Shaders

Core shaders are used by resource packs to adjust the HUD and add special effects to some blocks. Not all core shaders are compatible with FO.

Examples from [Vanilla Tweaks](https://vanillatweaks.net/) include:

* Translucent Spyglass Overlay
* No Spyglass Overlay
* Mob Spawn Indicator (does not work in FO)
* Wavy Leaves/Plants/Water (do not work in FO)
* [More from Vanilla Tweaks](https://vanillatweaks.net/picker/resource-packs)
* [More from Modrinth](https://modrinth.com/resourcepacks?f=categories:core-shaders)

The ones which do not work may be replicated by [adding a mod](../../how-to/add-mods/).

For developers: You may make your resource pack work with the [Sodium manifest](https://github.com/CaffeineMC/sodium-fabric/pull/2206) or with the [Sodium Shader Support mod](https://modrinth.com/mod/sodium-shader-support).

## Canvas Shaders

Canvas shaders are a kind of shader optimized for powerful computers, to be used with the [Canvas Renderer mod](https://www.curseforge.com/minecraft/mc-mods/canvas-renderer).

Examples include:

* [Lumi Lights](https://spiralhalo.github.io/)
* [More from Modrinth](https://modrinth.com/shaders?g=categories:canvas)

Canvas shaders are not supported by FO, but you can replace some mods to support them:

1. [Disable the following mods](../../how-to/disable-mods/):
   * Sodium
   * Sodium Extra
   * Reese's Sodium Settings
   * Iris
2. [Add](../../how-to/add-mods/) the [Canvas Renderer mod](https://www.curseforge.com/minecraft/mc-mods/canvas-renderer)
3. [Install the shader](shaders.md#shaders) you want
4. Enable it from <kbd>**Options...**</kbd> → <kbd>**Video Settings...**</kbd> → <kbd>**Canvas**</kbd> → <kbd>**Pipeline Options**</kbd> → <kbd>**Pipelines**</kbd>

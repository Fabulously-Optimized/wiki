# Getting shaders

### OptiFine shaders

OptiFine shaders are supported by default using [Iris](https://www.curseforge.com/minecraft/mc-mods/irisshaders)!

#### Installation

1. Open Minecraft with Fabulously Optimized installed
2. Open `Options...` → `Video Settings...` → `Shader Packs...`
3. Download any OptiFine shader pack [from recommended list](https://github.com/IrisShaders/Iris/blob/1.16.5/docs/supportedshaders.md) or [Modrinth](https://modrinth.com/shaders?g=categories%3A%27iris%27)
4. Drag the ZIP file into the shader pack screen
5. Select the shader, make sure _Shaders_ is set to enabled and click `Apply`
6. The shader has been applied! If you run into any problems with shaders, [please report them here](https://github.com/IrisShaders/Iris/issues).

#### Configuring settings

1. Click a shader
2. Click `Shader Pack Settings...` below
3. Adjust settings as needed
4. Click `Shader Pack List...`
5. Click `Done`

### Fabulous shaders

"Fabulous shaders" are vanilla shaders that work by enabling _Fabulous!_ graphics in video settings and getting a specific resource pack. _May or may not work in FO._

* [Fabulousity shader resource pack](https://github.com/ScottoMotto/Fabulousity#fabulousity)

{% embed url="https://youtu.be/luzgOwKt6_c?t=126" %}

* [Basic Shaders for Vanilla 1.16 resource pack](https://github.com/bradleyq/mc\_vanilla\_shaders#basic-shaders-for-vanilla-116)

{% embed url="https://youtu.be/dRnlaRx3zBY?t=24" %}

* Sildur's [Fabulous Shaders resource pack](https://sildurs-shaders.github.io/downloads/) [(configuring instructions)](https://sildurs-shaders.github.io/install/#fabulous)
* [Depth Shaders resource pack](https://github.com/onnowhere/depth\_shaders/releases)
* [More shaders can be found on Modrinth](https://modrinth.com/shaders?g=categories%3A%27vanilla%27)

#### Installation 

1. Go to `Options` -> `Video Settings` -> `Quality` -> `Graphics: Fabulous!`
2. Download any [Fabulous shader pack](https://modrinth.com/shaders?g=categories%3A%27vanilla%27)
3. Move the shader pack to `resourcepacks` folder or drag it into the resourcepacks screen
4. Apply the resource pack in resource packs screen

### Core shaders

"Core shaders" are a kind of vanilla shaders utilized by resource packs to adjust the vanilla HUD and add special effects to specific blocks. These usually do _not_ change landscapes overall and _may or may not work in FO._

Examples of working core shaders of [Vanilla Tweaks](https://vanillatweaks.net/picker/resource-packs/):
* Translucent Spyglass Overlay
* No Spyglass Overlay

Examples of **not** working core shaders of [Vanilla Tweaks](https://vanillatweaks.net/picker/resource-packs/):
* ~~Mob Spawn Indicator~~
* ~~Wavy Leaves~~
* ~~Wavy Plants~~
* ~~Wavy Water~~

Luckily those features can be replicated with [OptiFine shaders](#optifine-shaders) or [other mods](adding-more-mods.md), so you're not missing out.

**Resource pack developers**: you may try to make your pack work in Sodium [with this mod](https://modrinth.com/mod/sodium-shader-support).

#### Installation

1. [Download a core shader-using resource pack from Modrinth](https://modrinth.com/resourcepacks?f=categories%3A%27core-shaders%27)
2. Move the resource pack to `resourcepacks` folder or drag it into the resourcepacks screen
3. Apply the resource pack in resource packs screen
4. See if it works.
   * If yes, enjoy!
   * If not, it is recommended to use OptiFine shaders or other mods for the same purpose. 
       * You may, alternatively, disable Sodium and related mods if you really want them to work, but that will harm your performance too.

### Canvas shaders

[Canvas Renderer](https://www.curseforge.com/minecraft/mc-mods/canvas-renderer) is a mod that provides a new type of shaders that may be better optimized for powerful computers. 

Canvas shaders are **not supported by default on FO**. By replacing some mods, you can still make them work, however.

<details>

<summary>Read more</summary>

* [Lumi Lights resource pack](https://spiralhalo.github.io)
* [More shaders can be found on Modrinth](https://modrinth.com/shaders?g=categories%3A%27canvas%27)

#### Installation

1. [Disable the following mods](disabling-mods.md):
    1. Sodium
    2. Sodium Extra
    3. Reese's Sodium Settings
    4. Iris
2. Install [Canvas Renderer](https://www.curseforge.com/minecraft/mc-mods/canvas-renderer)
3. Download any [Canvas-compatible shader pack](https://modrinth.com/shaders?g=categories%3A%27canvas%27)
4. Move the shader pack to `resourcepacks` folder or drag it into the resourcepacks screen
5. Apply the resource pack in resource packs screen
6. Go to `Options` -> `Video Settings` -> `Canvas` -> `Pipeline Options` -> `Pipelines` and select the shader you'd like to use.
  
</details>

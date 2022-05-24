# Give up OptiFine

One of the goals of Fabulously Optimized is to provide feature parity with [OptiFine](https://optifine.net/home), in order to make it easier for users to transition away from it. 

Here is the list of OptiFine features that are supported in this modpack:

### Definitons

✔️ = **Supported**

🚧 = **Partly supported**

🔜 = **Soon supported**

❌ = **Not supported**

## Video Options

| Option | Is supported? | Mod providing the feature |
|-|-|-|
| Smooth Lighting Level | ❌ | There's [an  issue](https://github.com/FlashyReese/sodium-extra-fabric/issues/125) in the [Sodium Extra mod](https://www.curseforge.com/minecraft/mc-mods/sodium-extra).
| Dynamic Lights | ✔️ | [Lambda Dynamic Lights](https://www.curseforge.com/minecraft/mc-mods/lambdynamiclights)
| Shaders | 🚧 | [Iris](https://www.curseforge.com/minecraft/mc-mods/irisshaders) ([Tutorial](./getting-shaders.md)). Some shaders don't work. [PBR textures unsupported](https://discord.com/channels/774352792659820594/774354933436645478/967251726304415784).
| Details | ✔️ | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra) |
| Animations | ✔️ |  [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra) |
| Particles | ✔️ |  [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra) |
| 32+ Render Distance | 🔜 | There's [a Pull Request](https://github.com/FlashyReese/sodium-extra-fabric/pull/211) in the [Sodium Extra mod](https://www.curseforge.com/minecraft/mc-mods/sodium-extra). Alternatively, use [Bobby](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/INCLUDED-MODS.md#alternative-mods). |
| Smart Leaves² | ✔️ | [Cull Less Leaves](https://www.curseforge.com/minecraft/mc-mods/cull-less-leaves) |
| Performance | ✔️ | [Sodium](https://www.curseforge.com/minecraft/mc-mods/sodium), [Lithium](https://www.curseforge.com/minecraft/mc-mods/lithium), [Starlight](https://www.curseforge.com/minecraft/mc-mods/starlight) [etc.](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/INCLUDED-MODS.md#smooth) |
| "Other" | ✔️ |  [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra) |
| Zoom | ✔️ | [Zoomify](https://www.curseforge.com/minecraft/mc-mods/zoomify) |
| Capes | ✔️ | [Fabric Capes](https://www.curseforge.com/minecraft/mc-mods/capes) ([Tutorial](./free-cape.md)) |

## Custom ("OptiFine only") resource pack featrues

| Option | Is supported? | Mod providing the feature |
|-|-|-|
| Emissive Textures | 🔜 | [Continuity](https://www.curseforge.com/minecraft/mc-mods/continuity) (blocks), [Entity Texture Features](https://www.curseforge.com/minecraft/mc-mods/entity-texture-features-fabric) (entities) |
| Better Grass/Snow¹ | ✔️ | [LambdaBetterGrass](https://www.curseforge.com/minecraft/mc-mods/lambdabettergrass) |
| HD Fonts | ✔️ | [Vanilla feature since 1.13](https://minecraft.fandom.com/wiki/Java_Edition_1.13-pre7) |
| Connected Textures | ✔️ | [Continuity](https://www.curseforge.com/minecraft/mc-mods/continuity) |
| Custom Sky | ❌ | See [#72](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/72) |
| Custom Entity Models | 🚧 | [Custom Entity Models](https://www.curseforge.com/minecraft/mc-mods/custom-entity-models-cem). **Doesn't** support all entities [yet](https://github.com/dorianpb/cem#current-state-of-this-mod). |
| Random Entities | ✔️ | [Entity Texture Features](https://www.curseforge.com/minecraft/mc-mods/entity-texture-features-fabric)
| Custom Colors | ✔️ | [Colormatic](https://www.curseforge.com/minecraft/mc-mods/colormatic) |
| Natural Textures | ✔️ | [Vanilla feature since 1.9](https://minecraft.fandom.com/wiki/Model#Block_states) |
| Custom Items | ✔️ | [CIT Resewn](https://www.curseforge.com/minecraft/mc-mods/cit-resewn) |
| Custom GUIs | ✔️ | [OptiGUI](https://www.curseforge.com/minecraft/mc-mods/optigui) |
| Animated Textures | ✔️ | [Animatica](https://www.curseforge.com/minecraft/mc-mods/animatica) |
| HD Screenshots | ✔️ | [Fabrishot](https://www.curseforge.com/minecraft/mc-mods/fabrishot) |
| Resource pack splash screen | 🚧 | [Puzzle](https://www.curseforge.com/minecraft/mc-mods/puzzle). See https://github.com/PuzzleMC/Puzzle/issues/29 |
| Anisotropic Filtering | ❌ | There's [an early build](https://discord.com/channels/756612889787498627/872543494554648637/892202839361875979) for a mod that does this job (1.17) |

¹ Snow is opt-in in via settings as it changes some textures too, making it weird with some resource packs.

² Not identical to OptiFine as people did not prefer the look. If you want it to be identical, [disable this mod](./disabling-mods.md), [install](./adding-more-mods.md) the original [Cull Leaves](https://www.curseforge.com/minecraft/mc-mods/cull-leaves), enable its bundled resource pack and disable "Use Block Face Culling" in video settings.

Additionally, you can enjoy:

* Better mod compatibility
* [Easy installation](https://github.com/Fabulously-Optimized/fabulously-optimized#downloads) for various launchers
* [Some extra features](https://github.com/Fabulously-Optimized/fabulously-optimized#included-mods) OptiFine does not provide

Parity with OptiFine is an ongoing process. If you're interested in what's coming, [see this list](https://github.com/Fabulously-Optimized/fabulously-optimized/issues?q=is:issue%20is:open%20label:parity).

If you're having issues with OptiFine's resource pack features, [see this wiki](./resource-pack-issues.md).

_See also: [Recommended OptiFine alternatives on Fabric](https://lambdaurora.dev/optifine_alternatives), a list that inspired me to create this modpack in the first place._

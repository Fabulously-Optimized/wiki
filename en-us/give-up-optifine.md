# Give up OptiFine

One of the goals of Fabulously Optimized is to provide feature parity with [OptiFine](https://optifine.net/home), in order to make it easier for users to transition away from it.

Here is the list of OptiFine features that are supported in this modpack:

✔️ = **Supported**

🚧 = **Partly supported**

🔜 = **Soon supported**

❌ = **Not supported**

### Video Options

| Option                | Is supported? | Mod providing the feature                                                                                                                                                                                                                                                                                  |
| --------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Animation toggles     | ✔️            | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra)                                                                                                                                                                                                                                  |
| Capes                 | ✔️            | [Fabric Capes](https://www.curseforge.com/minecraft/mc-mods/capes) ([Tutorial](free-cape.md))                                                                                                                                                                                                              |
| Detail toggles        | ✔️            | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra)                                                                                                                                                                                                                                  |
| Dynamic Lights        | ✔️            | [Lambda Dynamic Lights](https://www.curseforge.com/minecraft/mc-mods/lambdynamiclights)                                                                                                                                                                                                                    |
| Miscellaneous toggles | ✔️            | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra)                                                                                                                                                                                                                                  |
| Particle toggles      | ✔️            | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra)                                                                                                                                                                                                                                  |
| Performance           | ✔️            | [Sodium](https://www.curseforge.com/minecraft/mc-mods/sodium), [Lithium](https://www.curseforge.com/minecraft/mc-mods/lithium), [Starlight](https://www.curseforge.com/minecraft/mc-mods/starlight) [etc.](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/INCLUDED-MODS.md#smooth) |
| Smart Leaves¹         | ✔️            | [Cull Less Leaves](https://www.curseforge.com/minecraft/mc-mods/cull-less-leaves)                                                                                                                                                                                                                          |
| Zoom²                  | ✔️            | [Zoomify](https://www.curseforge.com/minecraft/mc-mods/zoomify)                                                                                                                                                                                                                                            |
| Shaders               | 🚧            | [Iris](https://www.curseforge.com/minecraft/mc-mods/irisshaders) ([Tutorial](getting-shaders.md)). Some shaders don't work. [PBR textures unsupported](https://discord.com/channels/774352792659820594/774354933436645478/967251726304415784) [(via)](https://discord.gg/jQJnav2jPu).                      |
| Smooth Lighting Level | ❌             | There's [an issue](https://github.com/FlashyReese/sodium-extra-fabric/issues/125) in the [Sodium Extra mod](https://www.curseforge.com/minecraft/mc-mods/sodium-extra).                                                                                                                                    |
| 32+ Render Distance   | ❌             | Use [Bobby](https://www.curseforge.com/minecraft/mc-mods/bobby) [(why is it not in FO?)](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/46#issuecomment-1067105734).                                                                                                                  |

### Custom resource pack features

| Option                      | Is supported? | Mod providing the feature                                                                                                                                                                     |
| --------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Animated Textures           | ✔️            | [Animatica](https://www.curseforge.com/minecraft/mc-mods/animatica)                                                                                                                           |
| Better Grass/Snow³          | ✔️            | [LambdaBetterGrass](https://www.curseforge.com/minecraft/mc-mods/lambdabettergrass)                                                                                                           |
| Connected Textures          | ✔️            | [Continuity](https://www.curseforge.com/minecraft/mc-mods/continuity)                                                                                                                         |
| Custom Colors               | ✔️            | [Colormatic](https://www.curseforge.com/minecraft/mc-mods/colormatic)                                                                                                                         |
| Custom GUIs                 | ✔️            | [OptiGUI](https://www.curseforge.com/minecraft/mc-mods/optigui)                                                                                                                               |
| Custom Items                | ✔️            | [CIT Resewn](https://www.curseforge.com/minecraft/mc-mods/cit-resewn)                                                                                                                         |
| Emissive Blocks             | ✔️            | [Continuity](https://www.curseforge.com/minecraft/mc-mods/continuity)                              |
| Emissive Entities           | ✔️            | [Entity Texture Features](https://www.curseforge.com/minecraft/mc-mods/entity-texture-features-fabric)                                                                                        |
| HD Fonts                    | ✔️            | [Vanilla feature since 1.13.](https://minecraft.fandom.com/wiki/Java\_Edition\_1.13-pre6#Changes) [Download some from my profile](https://www.curseforge.com/members/robotkoer/projects)                                                                                             |
| HD Screenshots              | ✔️            | [Fabrishot](https://www.curseforge.com/minecraft/mc-mods/fabrishot)                                                                                                                           |
| Natural Textures            | ✔️            | [Vanilla feature since 1.8](https://minecraft.fandom.com/wiki/Java\_Edition\_14w17a#Model%20format%20improvements)                                                                            |
| Random Entities             | ✔️            | [Entity Texture Features](https://www.curseforge.com/minecraft/mc-mods/entity-texture-features-fabric)                                                                                        |
| Resource pack splash screen | ✔️            | [Puzzle](https://www.curseforge.com/minecraft/mc-mods/puzzle)                                                                                                                                 |
| Custom Entity Models        | 🚧            | [Custom Entity Models](https://www.curseforge.com/minecraft/mc-mods/custom-entity-models-cem). [Doesn't support all entities yet](https://github.com/dorianpb/cem#current-state-of-this-mod). |                                             |
| Anisotropic Filtering       | ❌             | Please check [this Discord discussion](https://discord.com/channels/756612889787498627/876567546390777856/978673913770950687) [(via)](https://discord.gg/7rnTYXu)                             |
| Custom Sky                  | ❌             | See [#72](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/72)                                                                                                             |

¹ Not identical to OptiFine as people did not prefer the look. If you want it to be identical:

1. [Disable Cull Less Leaves](disabling-mods.md)
2. [Install](adding-more-mods.md) the original [Cull Leaves](https://www.curseforge.com/minecraft/mc-mods/cull-leaves)
3. Enable Cull Leaves' bundled resource pack
4. Disable "Use Block Face Culling" in <kbd>Options</kbd> -> <kbd>Video Settings...</kbd> -> <kbd>Performance</kbd>.

² The defaults do not match OptiFine, because people preferred a smoother zoom. To make it identical to OptiFine:

1. Click <kbd>Mods</kbd> button, search for `Zoomify`, click it and on the top left hit the `Configure` icon.
2. Head over to Misc tab, set the preset to `OptiFine`

³ Better Snow is opt-in, because changes some textures too, making it weird with some resource packs:

1. Click <kbd>Mods</kbd>, search for `LambdaBetterGrass`, click it and on the top left hit the `Configure` icon.
2. Set Better Snow to `ON`

---

Additionally, you can enjoy:

* Better mod compatibility
* [Easy installation](https://github.com/Fabulously-Optimized/fabulously-optimized#downloads) for various launchers
* [Some extra features](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/INCLUDED-MODS.md#functional) OptiFine does not provide

Parity with OptiFine is an ongoing process. If you're interested in what's coming, [see this list](https://github.com/Fabulously-Optimized/fabulously-optimized/issues?q=is:issue%20is:open%20label:parity).

If you're having issues with OptiFine's resource pack features, [see this wiki](resource-pack-issues.md).

_See also:_ [_Recommended OptiFine alternatives on Fabric_](https://lambdaurora.dev/optifine\_alternatives)_, a list that inspired me to create this modpack in the first place._

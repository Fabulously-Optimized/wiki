# Included OptiFine Alternatives

One of the goals of Fabulously Optimized is to provide feature parity with [OptiFine](https://optifine.net/home), in order to make it easier for users to transition away from it. So, all you need to do is to [install Fabulously Optimized](install-instructions.md) to get all those mods at once!

Here is the list of OptiFine features that are supported in this modpack:

✔️ = **Supported**

🚧 = **Partly supported**

🔜 = **Soon supported**

❌ = **Not supported**

### Video Options

| Option                | Is supported? | Mod providing the feature                                                                                                                                                                                                                                                                                  |
| --------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Animation toggles     | ✔️            | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra)                                                                                                                                                                                                                                  |
| Custom capes                 | ✔️            | [Capes](https://www.curseforge.com/minecraft/mc-mods/capes) ([Tutorial](free-cape.md))                                                                                                                                                                                                              |
| Detail toggles        | ✔️            | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra)                                                                                                                                                                                                                                  |
| Dynamic Lights        | ✔️            | [LambDynamicLights](https://www.curseforge.com/minecraft/mc-mods/lambdynamiclights)                                                                                                                                                                                                                    |
| Miscellaneous toggles | ✔️            | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra)                                                                                                                                                                                                                                  |
| Particle toggles      | ✔️            | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra)                                                                                                                                                                                                                                  |
| Performance           | ✔️            | [Various mods](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/INCLUDED-MODS.md#smooth) |
| Shaders               | ✔️            | [Iris](https://www.curseforge.com/minecraft/mc-mods/irisshaders) ([Tutorial](getting-shaders.md))                      |
| Smart Leaves¹         | ✔️            | [MoreCulling](https://www.curseforge.com/minecraft/mc-mods/moreculling)                                                                                                                                                                                                                         |
| Zoom²                  | ✔️            | [Zoomify](https://www.curseforge.com/minecraft/mc-mods/zoomify)                                                                                                                                                                                                                                            |
| Better Grass          | 🚧            | [Fast Better Grass](https://github.com/Fabulously-Optimized/fabulously-optimized/tree/main/Resource%20Packs/Fast%20Better%20Grass) (fancy mode is currently unsupported, [but planned](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/717))  |                                                                                                         |
| 32+ Render Distance   | ❌             | Available through [Farsight](https://www.curseforge.com/minecraft/mc-mods/farsight-fabric), but [removed from FO due to platform limits.](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/656)                                                                                                     |

### Custom resource pack features

| Option                      | Is supported? | Mod providing the feature                                                                                                                                                                     |
| --------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Animated Textures           | ✔️            | [Animatica](https://www.curseforge.com/minecraft/mc-mods/animatica)                                                                                                                           |
| Connected Textures          | ✔️            | [Continuity](https://www.curseforge.com/minecraft/mc-mods/continuity)                                                                                                                         |
| Custom GUIs                 | ✔️            | [OptiGUI](https://www.curseforge.com/minecraft/mc-mods/optigui)                                                                                                                               |
| Custom Items                | ✔️            | [CIT Resewn](https://www.curseforge.com/minecraft/mc-mods/cit-resewn)                                                                                                                         |
| Custom Sky                  | ✔️             | [FabricSkyboxes](https://www.curseforge.com/minecraft/mc-mods/fabricskyboxes) + [FabricSkyBoxes Interop](https://www.curseforge.com/minecraft/mc-mods/fabricskyboxes-interop)   |
| Emissive Blocks             | ✔️            | [Continuity](https://www.curseforge.com/minecraft/mc-mods/continuity)                              |
| Emissive Entities           | ✔️            | [Entity Texture Features](https://www.curseforge.com/minecraft/mc-mods/entity-texture-features-fabric)                                                                                        |
| HD Fonts                    | ✔️            | [Vanilla feature since 1.13.](https://minecraft.wiki/w/Java\_Edition\_1.13-pre6#Changes) [Download some from author's profile](https://www.curseforge.com/members/robotkoer/projects)                                                                                             |
| HD Screenshots              | ✔️            | [Fabrishot](https://www.curseforge.com/minecraft/mc-mods/fabrishot)                                                                                                                           |
| Removal of gaps (see-through lines) in items | ✔️            | [Model Gap Fix](https://www.curseforge.com/minecraft/mc-mods/model-gap-fix) |
| Natural Textures            | ✔️            | [Vanilla feature since 1.8](https://minecraft.wiki/w/Java_Edition_14w17a#General_2)                                                                            |
| Random Entities             | ✔️            | [Entity Texture Features](https://www.curseforge.com/minecraft/mc-mods/entity-texture-features-fabric)                                                                                        |
| Resource pack splash screen | ✔️            | [Puzzle](https://www.curseforge.com/minecraft/mc-mods/puzzle)                                                                                                                                 |
| Custom Entity Models        | ✔️            | [Entity Model Features](https://www.curseforge.com/minecraft/mc-mods/entity-model-features) |
| Custom Colors               | ✔️            | [Polytone](https://www.curseforge.com/minecraft/mc-mods/polytone) |                                             
| Anisotropic Filtering       | ❌             | Not yet possible, check [this Discord discussion](https://discord.com/channels/756612889787498627/876567546390777856/978673913770950687) [(via)](https://discord.gg/7rnTYXu)    |


¹ Not identical to OptiFine as people did not prefer the look. If you want it to be identical:

1. [Disable MoreCulling](disabling-mods.md)
2. [Install](adding-more-mods.md) the original [Cull Leaves](https://www.curseforge.com/minecraft/mc-mods/cull-leaves)
3. Enable Cull Leaves' bundled resource pack
4. Disable "Use Block Face Culling" in `Options` → `Video Settings...` → `Performance`.

² The defaults do not match OptiFine, because people preferred a smoother zoom. To make it identical to OptiFine:

1. Click `Mods` button, search for `Zoomify`, click it and on the top left hit the `Configure` icon.
2. Head over to Misc tab, set the preset to `OptiFine`

---

Additionally, you can enjoy:

* Better mod compatibility
* [Easy installation](install-instructions) for various launchers
* [Some extra features](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/INCLUDED-MODS.md#functional) OptiFine does not provide

Parity with OptiFine is an ongoing process. If you're interested in what's coming, [see this list](https://github.com/Fabulously-Optimized/fabulously-optimized/issues?q=is:issue%20is:open%20label:parity).

If you're having issues with OptiFine's resource pack features, [see this wiki](resource-pack-issues.md).

_See also:_ [_Recommended OptiFine alternatives on Fabric_](https://optifine.alternatives.lambdaurora.dev/)_, a list that inspired me to create this modpack in the first place._

# Included OptiFine Alternatives

One of the goals of Fabulously Optimized is to provide feature parity with [OptiFine](https://optifine.net/home), in order to make it easier for users to transition away from it. So, all you need to do is to [install Fabulously Optimized](install-instructions.md) to get all those mods at once!

Here is the list of OptiFine features that are supported in this modpack:

✔️ = **Supported**

🚧 = **Partly supported**

🔜 = **Soon supported**

❌ = **Not supported**

### Video Options

| Option | Is supported? | Mod providing the feature |
|---|---|---|
| Animation toggles | ✔️ | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra) |
| Anisotropic Filtering | ✔️ | Available in vanilla since 1.21.11 |
| Anti-Aliasing | ✔️ | [Iris](https://www.curseforge.com/minecraft/mc-mods/irisshaders) ([Available via shaders](getting-shaders.md), such as the [TAA Project](https://modrinth.com/shader/taa)) |
| Better Grass | ✔️ | [BetterGrassify](https://curseforge.com/minecraft/mc-mods/bettergrassify) |
| Custom capes | ✔️ | [Capes](https://www.curseforge.com/minecraft/mc-mods/capes) ([Tutorial](free-cape.md)) |
| Detail toggles | ✔️ | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra) |
| Dynamic Lights | ✔️ | [LambDynamicLights](https://www.curseforge.com/minecraft/mc-mods/lambdynamiclights) |
| HD Screenshots | ✔️ | [Fabrishot](https://www.curseforge.com/minecraft/mc-mods/fabrishot) |
| Miscellaneous toggles | ✔️ | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra) |
| Particle toggles | ✔️ | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra) |
| Performance | ✔️ | [Various mods](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/INCLUDED-MODS.md#smooth) |
| Shaders | ✔️ | [Iris](https://www.curseforge.com/minecraft/mc-mods/irisshaders) ([Tutorial](getting-shaders.md)) |
| Smart Leaves | ✔️ | [MoreCulling](https://www.curseforge.com/minecraft/mc-mods/moreculling)¹ |
| Zoom | ✔️ | [Zoomify](https://www.curseforge.com/minecraft/mc-mods/zoomify)² |
| Vanilla UI design | 🚧 | Vanilla video settings screen viewable by <kbd>Shift</kbd>+<kbd>P</kbd>³ |
| 32+ Render Distance | ❌ | Available through [Farsight](https://www.curseforge.com/minecraft/mc-mods/farsight-fabric), but [removed from FO due to platform limits.](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/656) |

### Custom resource pack features

| Option | Is supported? | Mod providing the feature |
|---|---|---|
| Animated Textures | ✔️ | [Animatica](https://www.curseforge.com/minecraft/mc-mods/animatica) / [MoreMcmeta](https://www.curseforge.com/minecraft/mc-mods/moremcmeta-fabric) |
| Connected Textures | ✔️ | [Continuity](https://www.curseforge.com/minecraft/mc-mods/continuity) |
| Custom Entity Models | ✔️ | [Entity Model Features](https://www.curseforge.com/minecraft/mc-mods/entity-model-features) |
| Custom GUIs | ✔️ | [OptiGUI](https://www.curseforge.com/minecraft/mc-mods/optigui) |
| Custom Loading Screen | ✔️ | [Puzzle](https://www.curseforge.com/minecraft/mc-mods/puzzle) |
| Custom Sky | ✔️ | [Optiboxes](https://www.curseforge.com/minecraft/mc-mods/optiboxes) / [FabricSkyboxes](https://www.curseforge.com/minecraft/mc-mods/fabricskyboxes) + [FabricSkyBoxes Interop](https://www.curseforge.com/minecraft/mc-mods/fabricskyboxes-interop) |
| Emissive Blocks | ✔️ | [Continuity](https://www.curseforge.com/minecraft/mc-mods/continuity) |
| Emissive Entities | ✔️ | [Entity Texture Features](https://www.curseforge.com/minecraft/mc-mods/entity-texture-features-fabric) |
| HD Fonts | ✔️ | [Possible in vanilla since 1.13.](https://minecraft.wiki/w/Java\_Edition\_1.13-pre6#Changes) [Download some from author's profile](https://www.curseforge.com/members/robotkoer/projects) |
| Natural Textures | ✔️ | [Possible in vanilla since 1.8](https://minecraft.wiki/w/Java_Edition_14w17a#General_2). [See also](https://discord.com/channels/859124104644788234/1148531768157290537/1148531768157290537) [(via)](https://download.fo/discord) |
| Random Entities | ✔️ | [Entity Texture Features](https://www.curseforge.com/minecraft/mc-mods/entity-texture-features-fabric) |
| Removal of gaps (see-through lines) in items | ✔️ | Available in vanilla since 1.21.11 |
| Custom Colors | ✔️ | [Polytone](https://www.curseforge.com/minecraft/mc-mods/polytone) |
| Custom Items | 🚧 | [CIT Resewn](https://www.curseforge.com/minecraft/mc-mods/cit-resewn) _until FO 7.0.0_ / Partly in vanilla since 1.21.5 [(conversion tool)](https://github.com/DimucaTheDev/VaniFine) |

¹ Not identical to OptiFine as people did not prefer the look. If you want it to be identical:

1. [Disable MoreCulling](disabling-mods.md)
2. [Install](adding-more-mods.md) the original [Cull Leaves](https://www.curseforge.com/minecraft/mc-mods/cull-leaves)
3. Enable Cull Leaves' bundled resource pack
4. Disable "Use Block Face Culling" in `Options` → `Video Settings...` → `Performance`.

² The defaults do not match OptiFine, because people preferred a smoother zoom. To make it identical to OptiFine:

1. Click `Mods` button, search for `Zoomify`, click it and on the top left hit the `Configure` icon.
2. Head over to Misc tab, set the preset to `OptiFine`

³ Sodium, which is the mod providing a more performant rendering engine also has a redesigned video settings screen. 
This is persisted in the modpack, as users consider it to be more organized and better-looking than the vanilla one. Additionally, it adds new and hides some vanilla options that reflect the changed engine more accordingly.

Users who prefer the old look can do one of the following:

- Enter the video settings and press <kbd>Shift</kbd>+<kbd>P</kbd>. This will persist until toggled again or exited the screen.
- Add [Better Sodium Video Settings](https://modrinth.com/mod/better-sodium-video-settings-button) - shows vanilla video settings by default, with a button to show Sodium ones
- Add [Enchanted's Sodium Options](https://modrinth.com/mod/enchanteds-sodium-options) - redesigns Sodium video settings to match vanilla look more closely
- Add [Xander's Sodium Options](https://modrinth.com/mod/xanders-sodium-options) or [its updated fork](https://modrinth.com/mod/xso) - redesigns Sodium video settings to have tabs on top and use vanilla UI elements throughout

---

Additionally, you can enjoy:

* Better mod compatibility
* [Easy installation](install-instructions) for various launchers
* [Some extra features](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/INCLUDED-MODS.md#functional) OptiFine does not provide

Parity with OptiFine is an ongoing process. If you're interested in what's coming, [see this list](https://github.com/Fabulously-Optimized/fabulously-optimized/issues?q=is:issue%20is:open%20label:parity).

If you're having issues with OptiFine's resource pack features, [see this wiki](resource-pack-issues.md).

_See also:_ [_Recommended OptiFine alternatives on Fabric_](https://optifine.alternatives.lambdaurora.dev/)_, a list that inspired creating this modpack in the first place._

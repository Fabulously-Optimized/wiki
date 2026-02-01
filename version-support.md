# Version support

## Installer

{% hint style="warning" %}
Cannot see versions 11.3.0 or 12.0.0? [Please update your installer.](https://download.fo/vanilla)
{% endhint %}

### Why does the installer show less versions than other platforms?

As the installer is intended for users with least Minecraft knowledge, the versions are also primarily limited to the stable versions.

Due to high interest, it will still always include the latest Minecraft version, even if the equivalent modpack version is still in alpha or beta. This can be selected by clicking on the version list and selecting the topmost item.

### Where are versions older than 5.12.0?

These versions are not available on the installer due to technical and platform limits. Please [use manual install](install-instructions.md#minecraft-launcher-vanilla) or other launchers if you'd like to use them.

## Versions

### How often does Fabulously Optimized receive updates?

The goal is to push out a new version once per week or two weeks. This is not a guarantee and can change depending on the amount of mod updates, Mojang's schedules, real-life duties and others.

### How do the modpack version numbers work?

* **X**.Y.Z stands for "major versions"
  * 1.x.x-6.x.x directly map to Minecraft's A.**B**.C [full releases](https://minecraft.wiki/w/Java_Edition_version_history#Full_release) (1.16.x was 1, 1.17.x was 2, etc)
  * 8.x.x and onwards the versions are mapped to [game drops](https://minecraft.wiki/w/Game_drop), beginning with The Garden Awakens
* X.**Y**.Z stands for minor versions which may map to Minecraft's A.B.**C** or just refer to bigger changes like added mods
* X.Y.**Z** stands for patch versions - no breaking changes, no mod additions/removals

Here is how you should think about the version types in relation to Minecraft's:

| Minecraft term    | Modpack equivalent term |
| ----------------- | ----------------------- |
| snapshot          | alpha                   |
| pre-release       | beta                    |
| release candidate | beta\*                  |
| release           | stable                  |

\* Fabulously Optimized does not explicitly mark release candidates as such, because its releases often depend on external factors (the included 3rd party mods).

### What versions are supported?

The latest stable version and if available, also latest beta and/or alpha versions. Older versions are listed for your convenience, but may not receive any more updates.

### Are snapshots or April Fools releases supported?

No. Only stable versions of Minecraft are supported as they are available on all platforms/launchers and support the most mods.

### What do symbols mean in a version's title?

- ⚠️ - version contains known vulnerabilities or bugs. These are available for archival purposes only and may cause problems in multiplayer or your worlds. Please see the version's notes before installing and know that you will not get support.
- ▪️ - version that is not necessarily vulnerable, but is still experimental and was superseded by a newer Minecraft version. Not advised.
- ▫️ - an extra version that is important in some way, but may not be the latest or stable. Read notes for more info.

### Where can I find the oldest Minecraft versions?

[CurseForge listing](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files?showAlphaFiles=show) contains all latest versions down to Minecraft 1.16.1. Note that due to technical reasons they may not even directly work anymore.

If you need to play in a server that uses a version not supported by the modpack, your best bet is installing the latest version of the modpack and adding [ViaFabric](https://www.curseforge.com/minecraft/mc-mods/viafabric) to your modpack profile [(instructions are here)](adding-more-mods.md). It is recommended to keep the mod enabled only while playing the server where you need it.

### Will newer modpack changes get backported to older versions?

Occasionally yes. Cases may include:

* a major breakage
* after introducing a new major stable release
* major updates to most important mods (e.g. Sodium)

This is done to help you while you _transition_ to the new version, old Minecraft versions are still unsupported and will not receive full parity.

## Other mod loaders

### Will the modpack move to [Forge](https://files.minecraftforge.net) or [NeoForge](https://neoforged.net/)?

No. Forge and NeoForge receive mod updates slower and do not have all the same performance and graphics-enhancing mods as Fabric.

### Can I use (Neo)Forge mods in this modpack?

No, but [there are many equivalents anyway](https://gist.github.com/TrueCP6/4853f15015b210fd3b1e210e9e485f83). [Ask us on Discord](https://download.fo/discord) if you need an alternative for a specific mod!

### Will the modpack move to [Quilt](https://quiltmc.org)?

It may be considered if the majority of mod developers do it, but currently that does not seem to be the case. [issue #257](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/257).

### Can I use Quilt mods in this modpack?

"No. Quilt mods are distinct from Fabric mods, and not defined in the same way." [Source](https://quiltmc.org/en/about/faq/) However, many Quilt-only mods have moved to Fabric in recent versions of the game.

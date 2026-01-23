# Version support

## Versions

#### How often does Fabulously Optimized receive updates?

The goal is to push out a new version once per week or two weeks. This is not a guarantee and can change depending on the amount of mod updates, Mojang's schedules, real-life duties and others.

#### How do the modpack version numbers work?

- **X**.Y.Z stands for "major versions"
   - 1.x.x-6.x.x directly map to Minecraft's A.**B**.C [full releases](https://minecraft.wiki/w/Java_Edition_version_history#Full_release) (1.16 was 1, 1.17 was 2, etc)
   - 7.x.x and onwards the versions are mapped to [game drops](https://minecraft.wiki/w/Game_drop), beginning with Bundles of Bravery
- X.**Y**.Z stands for minor versions which may map to Minecraft's A.B.**C** or just refer to bigger changes like added mods
- X.Y.**Z** stands for patch versions - no breaking changes, no mod additions/removals

Here is how you should think about the version types in relation to Minecraft's:

| Minecraft term            | Modpack equivalent term |
| ----------------- | ------------------------- |
| snapshot                           | alpha                                              |
| pre-release                        | beta                                               |
| release candidate                  | beta*                                              |
| release                            | stable                                             |

\* Fabulously Optimized does not explicitly mark release candidates as such, because its releases often depend on external factors (the included 3rd party mods).

#### What versions do you support?

The latest stable version and if available, also latest beta and/or alpha versions. Older versions are listed for your convenience, but may not receive any more updates.

#### Why won't the installer show versions older than 5.12.0?

These versions are old and therefore no longer recommended for most users. Please [use manual install](install-instructions.md#minecraft-launcher-vanilla) if you'd like to use them.

#### Will you support Minecraft snapshots?

No, they are not supported on CurseForge App and are released too fast for the author and the modders to keep up with.

#### What does ⚠️ mean in a version's title?

Versions with a warning triangle ⚠️ contain known vulnerabilities or bugs. These are available for archival purposes only and may cause problems in multiplayer or your worlds. Please prefer versions that do not have warnings or see the version's notes before installing.

#### What if I want to play on an older Minecraft version?

[CurseForge listing](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files?showAlphaFiles=show) contains all latest versions down to Minecraft 1.16.1.

If you need to play in a server that uses a version not supported by the modpack, your best bet is installing the latest version of the modpack and adding [ViaFabric](https://www.curseforge.com/minecraft/mc-mods/viafabric) to your modpack profile [(instructions are here)](adding-more-mods.md). It is recommended to keep the mod enabled only while playing the server where you need it.

#### Will you backport newer modpack changes to older versions?

Occasionally yes. Cases may include:

* a major breakage
* after introducing a new major stable release
* major updates to most important mods (e.g. Sodium, Lithium, Phosphor)

This is done to help you while you _transition_ to the new version, old Minecraft versions are still unsupported and will not receive full parity.

## Other platforms

#### Will you make a [Forge](https://files.minecraftforge.net) or [NeoForge](https://neoforged.net/) modpack?

No. Forge and NeoForge receive mod updates slower and do not have all the same performance and graphics-enhancing mods as Fabric.

#### Can I use (Neo)Forge mods in this modpack?

No, but [there are many equivalents anyway](https://gist.github.com/TrueCP6/4853f15015b210fd3b1e210e9e485f83). [Ask us on Discord](https://download.fo/discord) if you need an alternative for a specific mod!

#### Will you make a [Quilt](https://quiltmc.org) modpack?

Probably not, that depends on modders' general stances on that mod loader compared to Fabric. See [issue #257](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/257).

#### Can I use Quilt mods in this modpack?

"Probably not. Quilt mods will eventually have their own metadata format which will likely not be compatible with Fabric." [Source](https://quiltmc.org/faq/)

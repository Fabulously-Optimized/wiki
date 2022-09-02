# Version support

## Versions

#### How often does Fabulously Optimized receive updates?

That depends on my time, Mojang releases, CurseForge support (when versions appear in launcher), mod updates, mod additions... there are a lot of factors. I do try to push out a release as soon as possible when Minecraft or some of the more important mods update though.

#### What versions do you support?

I support the latest stable modpack version and latest development modpack version (if any), other versions are listed just for your convenience. To make it even simpler, I usually keep only one modpack version per Minecraft version visible on CurseForge.

#### Will you support Minecraft snapshots?

No, they are not supported on CurseForge Launcher and are released too fast for me and the modders to keep up with.

#### What if I want to play on an older Minecraft version?

See the [CurseForge page](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files) for the existing stable versions down to 1.16.1.

**Versions with a warning triangle ⚠️** [**are not safe for multiplayer**](https://www.minecraft.net/en-us/article/important-message--security-vulnerability-java-edition) **and are kept just for archival purposes.**

If you need to play in a server that uses a version not supported by the modpack, your best bet is installing the latest version of FO and adding [ViaFabric](https://www.curseforge.com/minecraft/mc-mods/viafabric) to your modpack profile [(instructions are here)](adding-more-mods.md). I recommend keeping the mod enabled only while playing the server where you need it.

#### Will you backport newer modpack changes to older versions?

Occasionally yes. Cases may include:

* a major breakage
* after introducing a new major stable release
* major updates to most important mods (e.g. Sodium, Lithium, Phosphor)

This is done to help you while you _transition_ to the new version, old Minecraft versions are still unsupported and will not receive full parity.

## Other platforms

#### Will you make a [Forge](https://files.minecraftforge.net) modpack?

No. Forge is slower to update and run and it doesn't have the same capabilities for optimization as Fabric.

#### Can I use Forge mods in this modpack?

No, but [there are many equivalents anyway](https://gist.github.com/TrueCP6/4853f15015b210fd3b1e210e9e485f83). There is also work going on to make Forge mods work on Fabric though, if you're a developer [you can check it out](https://patchworkmc.net).

#### Will you make a [Quilt](https://quiltmc.org) modpack?

Too early to tell, that likely depends on how many Fabric modders will start using that exclusively. See [issue #257](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/257).

#### Can I use Quilt mods in this modpack?

"Probably not. Quilt mods will eventually have their own metadata format which will likely not be compatible with Fabric." [Source](https://quiltmc.org/faq/)

## Distribution

#### Will you ever support Minecraft Launcher (vanilla) properly?

[Yes, this is planned](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/110) as soon as Packwiz adds support for it!

#### How does the auto-updating MultiMC pack work?

[See this page.](multimc-auto-update.md)

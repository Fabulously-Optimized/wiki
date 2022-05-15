# Version support

## Versions

#### How often does Fabulously Optimized receive updates?

That depends on my time, Mojang releases, Curseforge support (when versions appear in launcher), mod updates, mod additions... there are a lot of factors. I do try to push out a release as soon as possible when Minecraft or some of the more important mods update though.

#### What versions do you support?

I support the latest stable modpack version and latest development modpack version (if any), other versions are listed just for your convenience. To make it even simpler, I usually keep only one modpack version per Minecraft version visible on Curseforge.

#### Will you support Minecraft snapshots?

No, they are not supported on Curseforge Launcher and are released too fast for me and the modders to keep up with.

#### What if I want to play on an older Minecraft version?

See the [Curseforge page](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files) for the existing stable versions down to 1.16.1.

**Note that versions 1.1.2-1.7.0 (MC 1.16.1-1.16.4) and 2.0.0b4 (MC 1.17)** [**are not safe for multiplayer**](https://www.minecraft.net/en-us/article/important-message--security-vulnerability-java-edition) **and are kept just for archival purposes.** Any newer versions listed there are patched and should be upgraded to ASAP.

If you need to use Minecraft 1.15 or older, your best bet is adding [multiconnect](https://www.curseforge.com/minecraft/mc-mods/multiconnect), [ViaFabric](https://www.curseforge.com/minecraft/mc-mods/viafabric) or both to your modpack profile [(instructions are here)](adding-more-mods.md). See also [why I can't add it for everyone just yet.](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/15#issuecomment-786175477)

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

#### Will you ever support Minecraft launcher (vanilla) properly?

[Yes, this is planned](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/110) as soon as packwiz adds support for it!

#### Will you publish the modpack to Modrinth?

[It is actually already there](https://modrinth.com/modpack/fabulously-optimized), but [no supported launchers can install it from there yet.](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/63)

#### How does the auto-updating MultiMC pack work?

[See this page.](multimc-auto-update.md)

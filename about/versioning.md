---
hidden: true
icon: code-merge
---

# Versioning

FO is consistently one of the first packs to upgrade to new Minecraft versions, thanks to its efficient versioning model.

Of course, the speed at which FO is updated depends on multiple factors, including but not limited to:

* Mojang's releases: new features, breaking changes...
* Mods' updates: Fabric (which usually updates very quickly), mods...
* New additions or removals of mods, which need testing
* The time FO's author has to work on updates

Generally, the development version of FO, which may not include all mods of a stable release, is released as soon as possible, often every week or two. Once a release is published, important updates to mods are usually quickly available.

## Version Numbers

An FO version is indicated by three numbers `X.Y.Z`, and a suffix for development versions. The three numbers now indicate:

<table><thead><tr><th width="100" align="center">Number</th><th width="150">Meaning</th><th>Description</th></tr></thead><tbody><tr><td align="center"><code>X</code></td><td>Major versions</td><td><strong>Starting from 7.y.z</strong>: mapped to Minecraft's <a href="https://minecraft.wiki/w/Game_drop">game drops</a> or <a href="https://minecraft.wiki/w/Java_Edition_version_history#Full_release">full releases</a><br><strong>From 1.y.z ~ 6.y.z</strong>: mapped to Minecraft's full releases from 1.16</td></tr><tr><td align="center"><code>Y</code></td><td>Minor versions</td><td>Minecraft patches or changes to FO</td></tr><tr><td align="center"><code>Z</code></td><td>Patches</td><td>Non-breaking changes, no mod changes</td></tr></tbody></table>

The suffix is a term that approximately corresponds to the stages of Minecraft's development:

|  Minecraft  |   FO   |  Suffix  |
| :---------: | :----: | :------: |
|   snapshot  |  alpha | `-alpha` |
| pre-release |  beta  |  `-beta` |
|   release   | stable |  _none_  |

{% hint style="info" %}
FO and its mods may not keep up with all snapshots, as they are released very quickly and they may break a lot of stuff behind the scenes. Also, support is not provided for these, see [Supported Versions](versioning.md#supported-versions) below.
{% endhint %}

## Supported Versions

Support is provided for the latest stable version of FO, and for the latest development version of FO if any.

Older versions of FO, and for older Minecraft versions, are available but no longer supported. If you want to play them at your own risk, you may find a [list of older versions on CurseForge](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files?showAlphaFiles=show).

{% hint style="danger" %}
While FO does not support outdated versions, it especially warns its users against some which are known to have vulnerabilities and are only kept for archival purposes. Those are indicated in the websites with a triangle warning sign: ⚠️.

For example, some versions are known to be unsafe for multiplayer: see the [official article on Minecraft's website](https://minecraft.net/en-us/article/important-message--security-vulnerability-java-edition).
{% endhint %}

On the other hand, if a server you're playing on is out-of-date, you may want to [add](../how-to/add-mods/) the [ViaFabricPlus mod](https://modrinth.com/mod/viafabricplus). You should only enable it for servers where it's needed.

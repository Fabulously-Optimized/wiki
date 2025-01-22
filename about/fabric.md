---
hidden: true
icon: scroll-old
---

# Fabric

FO uses Fabric, instead of NeoForge, for the following reasons:

* **Popular**: there are [at least 10000 Fabric mods on CurseForge](https://www.curseforge.com/minecraft/search?gameVersionTypeId=4) and [over 20000 Fabric mods on Modrinth](https://modrinth.com/mods?g=categories:fabric)
  <!--
  Modrinth: `total_hits` from https://api.modrinth.com/v2/search?facets=[[%22categories=fabric%22]]
  CurseForge: `10000+ Projects found` in https://www.curseforge.com/minecraft/search?gameVersionTypeId=4
  TODO: find reliable API result for CurseForge
  -->
* **Supported**: most authors of NeoForge mods nowadays support Fabric as well, if not exclusively
* **Compatible**: Fabric mod developers work together to keep their mods compatible with each other
* **Easy installation**: there's a [Fabric installer](https://fabricmc.net/use/installer), which supports many launchers
* **Fast updates**: on the same day as Minecraft, and so do many mods
* **Fast loading**: roughly the same as vanilla Minecraft
* **Small size**: no huge libraries, just the [Fabric Loader](https://fabricmc.net/use) and the [Fabric API](https://www.curseforge.com/minecraft/mc-mods/fabric-api)

{% hint style="success" %}
If you're coming from NeoForge, you can find a community-maintained [list of Fabric mods corresponding to NeoForge mods](https://gist.github.com/TrueCP6/4853f15015b210fd3b1e210e9e485f83).
{% endhint %}

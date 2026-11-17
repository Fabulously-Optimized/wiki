---
icon: server
---

# Server setup

Fabulously Optimized is a strictly client-sided modpack, meaning it works and behaves mostly the same on **every server that allows vanilla clients**.

The CurseForge listing used to have "server packs", but [those were actually just the MultiMC packages](install-instructions/minecraft-launcher.md) that were marked as server packs for better visibility.

**Disclaimer: All content on this page should be treated as a suggestion. If you need any help with server setup, please ask in the respective mod or platform support site.**

## Tips

* [Do you even need a server?](server-setup.md#world-sharing)
* [Use speedy server software](server-setup.md#software)
* [Be aware of chat reporting](server-setup.md#chat-reporting)
* [Give users flexibility with client version](server-setup.md#client-version-flexibility)
* [Allow Bedrock users to join](server-setup.md#bedrock-compatibility)
* [Server-side content mods](server-setup.md#server-side-content-mods)
* [Restrict mod behaviours, not names](server-setup.md#mods-in-rules)
* [Prevent cheats and exploits](server-setup.md#exploit-prevention)

### World sharing

Did you know Fabulously Optimized lets you play with anyone in your singleplayer worlds, even if they are on a different network? If that's all you need, then you don't need to create a full-fledged server.

1. Open your world
2. Press Esc -> `Open to Internet`
3. Confirm settings and `Open to Internet`
4. Check the chat for an address (host domain), copy it
5. Send your friend the address. Your friend needs to use the same version of Minecraft, but not necessarily the modpack.

[More info about how it works](disclaimers.md#privacy-and-security)

### Software

For server software it is recommended to use [Paper](https://papermc.io) or [Purpur](https://purpurmc.org), which are performance-optimized forks of Spigot, but support all the same plugins found on [Modrinth](https://modrinth.com/discover/plugins?g=categories:paper) and [SpigotMC](https://www.spigotmc.org/resources/categories/spigot.4). Using Realms is not advised - read about their [proactive moderation](https://help.minecraft.net/hc/en-us/articles/8047895358605-Our-Commitment-to-Player-Safety#h_01G95X76WR1PM97XBXDE7G25KE).

If you still like Fabric a lot, you can [install it on a server as well](https://fabricmc.net/use/?page=server) and use [server-side optimization mods](https://modrinth.com/discover/mods?e=server&g=categories:fabric&f=categories:optimization), [including those in Fabulously Optimized](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/INCLUDED-MODS.md#smooth).

If you need a host, [check out BisectHosting](https://www.bisecthosting.com/clients/aff.php?aff=2604). [This affiliate link](https://www.bisecthosting.com/clients/aff.php?aff=2604) will give you 25% off for the first month.

### Chat Reporting

Minecraft 1.19.1 added a feature that lets users report chat messages to Mojang. Server admins are advised to [learn how it works](https://minecraft.wiki/w/Social_interactions), as their players could be banned for messages that go against Minecraft's, but not server's rules.

### Client version flexibility

Ever wondered, how some servers are able to update the same day a new Minecraft version is released? Chances are, they are using a plugin that enables this without having to change the server version (yet).

**ViaVersion** and **ViaBackwards** are plugins that transform the network packets to let users join your server with a different client version. This is especially welcome for users who mod their client, such as Fabulously Optimized users, as not every mod is updated as soon as the new version of Minecraft is released, so users may be inclined to use outdated clients for a bit longer.

* **ViaVersion** lets users join with a _newer_ client version. For example, if your server is still using 1.19.2, this will let users join with 1.19.3 and later.
  * By default, ViaVersion allows users to join from your server's Minecraft version up to the latest stable Minecraft version. This can be filtered in the ViaVersion configuration file.
  * Download for: [Paper/Spigot/Purpur/Velocity](https://hangar.papermc.io/ViaVersion/ViaVersion) | [Fabric/Quilt\*](https://www.curseforge.com/minecraft/mc-mods/viafabric)
* **ViaBackwards** lets users join with an _older_ client version. For example, if your server is using 1.19.4, users can join with 1.19.3 and older.
  * By default, ViaBackwards allows users to join from Minecraft 1.8 up to your server's Minecraft version. This can be filtered in the ViaVersion configuration file.
  * Any new blocks, items and entities will be shown as older types with equivalent properties (like mobs of similar size or blocks of similar breaking speed). Users with newer clients will see them as normal.
  * Download for: [Paper/Spigot/Purpur/Velocity](https://hangar.papermc.io/ViaVersion/ViaBackwards) | [Fabric/Quilt\*](https://www.curseforge.com/minecraft/mc-mods/viabackwards)

Depending on your server, you can choose to use only ViaVersion or both. If your server is hub-based, it is recommended to install the plugin(s) to each backend server and _not_ the proxy itself.

_\* Fabric/Quilt versions can also work in the client, though this is not advised due to potential conflicts with anticheats. It is recommended to keep it on the server only. Quilt support is untested for both server and client._

### Bedrock compatibility

Interested in allowing Bedrock users to join? Check out [GeyserMC](https://geysermc.org/).

Note that there can be incompatibilities and weird glitches (e.g. with anticheat plugins) because of big differences between Bedrock Edition and Java Edition.

### Server-side content mods

_These mods are usually not compatible with [ViaVersion and ViaBackwards](server-setup.md#server-side-content-mods) and they require a Fabric server._

Did you know that it is possible to have content mods (e.g. new blocks and items) on the server without requiring them to be installed on the client? That means that you can add new stuff to the server while your users use unmodified Fabulously Optimized!

* [Check out these mods](https://github.com/Patbox/polymer/blob/dev/1.21/MODS.md) built for [Polymer](https://modrinth.com/mod/polymer) to provide this seamlessly
* [Check out PolyMc](https://theepicblock.github.io/PolyMc/), which can work with even more mods but requires your testing first

### Mods in rules

Some servers tend to put a list of allowed mods into their rules. While it may sound like a good idea in theory, it actually creates more problems due to its vagueness.

> **DON'T:** "Only OptiFine allowed."

This would disallow Fabulously Optimized, despite it having mods that do exactly the same thing.

> **DO**: "Performance and visual-enhancing mods are allowed."

This would allow Fabulously Optimized in your server without requiring further clarification.

***

> **DON'T:** "Only minimap mod X is allowed."

The players would only depend on that single mod's updates, even if there are alternatives available.

> **DO:** "Any minimap mod with player radar disabled."

This allows users to use any minimap mods by configuring them by themselves. Many minimap mods also have server-side enforcement options.

***

> **DON'T:** "Maximum 25 mods can be used."

This would already disqualify Fabulously Optimized, as it has more.

> **DO:** (don't mention it)

Arbitrary mod count limits do not benefit anything at all. Some mods may be big and do a lot, while others may be small and do very little, hence users may have very different mod counts.

***

> **DON'T:** "Only Forge mods are allowed."

Fabulously Optimized does not use Forge.

> **DO:** (don't mention it)

Restricting certain mod loaders or clients is bad for the user and harmful for the Minecraft ecosystem as a whole. Just restrict behaviours.

### Exploit prevention

It is important to keep server platform and mods up to date to prevent client exploits. Additionally you may consider:

* Anti-cheat plugins: [Paper/Spigot](https://www.spigotmc.org/wiki/anti-cheat-list-bukkit-and-spigot-1-19-x/) or [Fabric/Quilt](https://serverside.infra.link/#:~:text=Anticheat/Anti%20X%2Dray)
* Anti-exploit mods [Fabric/Quilt/NeoForge/Forge](https://modrinth.com/mod/crashexploitfixer)
* Finding volunteer moderators to spectate users

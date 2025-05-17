
# Server setup

Fabulously Optimized is a strictly client-sided modpack, meaning it works and behaves mostly the same on **every server that allows vanilla clients**. 

The CurseForge listing used to have "server packs", but [those were actually just the legacy MultiMC versions](vanilla-launcher-faq.md#what-is-the-multimc-zip) that were marked as server packs for better visibility.

**Disclaimer: all content on this page are just suggestions. If you need any help with server setup, please ask in the respective mod or platform support site.**

## Tips

* [Use speedy server software](#software)
* [Protect users from chat reporting](#chat-reporting)
* [Give users flexibility with client version](#client-version-flexibility)
* [Allow Bedrock users to join](#bedrock-compatibility)
* [Server-side content mods](#server-side-content-mods)
* [Restrict mod behaviours, not names](#mods-in-rules)

### Software

For server software it is recommended to use [Paper](https://papermc.io), [Pufferfish](https://github.com/pufferfish-gg/Pufferfish) or [Purpur](https://github.com/PurpurMC/Purpur/), which are performance-optimized forks of Spigot, but support [all the same plugins](https://www.spigotmc.org/resources/categories/spigot.4/). [Using Realms is not advised](chat-reporting-faq.md#does-mojang-monitor-my-chats).

If you still like Fabric a lot, you can [install it on a server as well](https://fabricmc.net/use/?page=server) and use [server-side optimization mods](https://modrinth.com/mods?f=categories!=cursed&f=categories:optimization&e=server&g=categories:fabric), [including those in FO](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/INCLUDED-MODS.md#smooth).

If you need a host, [check out BisectHosting](https://www.bisecthosting.com/clients/aff.php?aff=2604). [This affiliate link](https://www.bisecthosting.com/clients/aff.php?aff=2604) will give you 25% off for the first month.

### Chat Reporting

Minecraft 1.19.1 added a feature [that lets users report chat messages to Mojang](chat-reporting-faq.md). Most servers disable it, as it can result users being banned for things that are allowed by server rules.

#### How your server works in Fabulously Optimized

The following icons show the status of the server. Icons are shown on the bottom right corner of the chat box.

* **1.18.2 or below (e.g. ViaVersion)**: FO users will see ![optional](https://i.ibb.co/hstcjW7/neutral.png).
    * No messages can be reported by anyone. On vanilla clients, gray bars are displayed on the left of the messages.
* **1.19 or up**:
    1. Using [one of the mods/plugins](#how-to-protect-your-users): FO users will see ![disabled](https://i.ibb.co/QDFzXCT/secure.png)
        * No messages can be reported by anyone. On vanilla clients, gray bars are displayed on the left of the messages.
    2. In other cases, FO users will see ![unknown](https://i.ibb.co/Yb1n6fW/unknown.png) until they send the first chat message.
        1. If `enforce-secure-profile` = `true` (default), FO users will see ![enabled](https://i.ibb.co/2YgMHpR/insecure.png).
            * All messages can be reported.
        2. If `enforce-secure-profile` = `false` (recommended), FO users will see ![optional](https://i.ibb.co/hstcjW7/neutral.png).
            * Vanilla users' messages can be reported and disabled FO users' messages can not. On vanilla clients, gray bars are displayed on the left of FO users' messages.
* **Realms**: FO users will see ![realms](https://i.ibb.co/gTxw84X/realms.png).
    * All messages can be reported and [Mojang monitors all chats](chat-reporting-faq.md#does-mojang-monitor-my-chats).

#### How to protect your users

Make sure you follow _all_ steps that match your server's configuration, not just one of them.

- **All 1.18- backend servers**: no changes necessary, chat reporting doesn't exist.
- **All 1.19+ backend servers**: set `enforce-secure-profile` to `false` in _server.properties_
  - This doesn't disable chat reporting by itself, but allows users to join without requiring them to sign their messages, to protect their privacy.
  - If no other measures are taken alongside this:
      - FO users will see ![optional](https://i.ibb.co/hstcjW7/neutral.png) and their messages cannot be reported.
      - Vanilla users will see a warning toast in the top right corner and their messages can be reported. To avoid those problems, use one of the plugins/mods below.
- **Vanilla server**: no known methods exist.
   - You can disable forced signing for clients using "All 1.19+ backend servers" instructions above.
   - For preventing reporting entirely, consider using another server platform, such as Paper, or [alternative chat methods](chat-reporting-faq.md#are-there-alternative-ways-to-chat).
- **Velocity**: set `force-key-authentication` to `false` in _velocity.toml_
  - Same comments apply as for "all 1.19+ backend servers" above.
- **BungeeCord**: set `enforce_secure_profile` to `false` in _config.yml_
  - Same comments apply as for "all 1.19+ backend servers" above.
- **Paper/Purpur/Pufferfish**: install the [FreedomChat](https://modrinth.com/mod/freedomchat) plugin.
   - Ensure `rewrite-chat` and `send-prevents-chat-reports-to-client` are set to `true` inside the FreedomChat's config file to make FO users see a ![disabled](https://i.ibb.co/QDFzXCT/secure.png) icon near chat.
- **Fabric/Forge/NeoForge**: install [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports)
   - FO users will get a ![disabled](https://i.ibb.co/QDFzXCT/secure.png) icon near chat.
- **Quilt**: no known methods exist.
   - You can disable forced signing for clients using "All 1.19+ backend servers" instructions above.
   - For preventing reporting entirely, consider using another mod loader, such as Fabric, or [alternative chat methods](chat-reporting-faq.md#are-there-alternative-ways-to-chat).
- **Realms**: impossible to circumvent seamlessly; [Mojang monitors all chats in Realms!](chat-reporting-faq.md#does-mojang-monitor-my-chats)
  - [Use alternative methods to chat](chat-reporting-faq.md#are-there-alternative-ways-to-chat). 
  - Consider [getting a real host](https://www.bisecthosting.com/clients/aff.php?aff=2604) to avoid surveillance altogether (affiliate link - 25% off first month).
- **LAN worlds**: host from Fabulously Optimized or install [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports) on the client
  - FO users will get a ![disabled](https://i.ibb.co/QDFzXCT/secure.png) icon near chat.
- **LAN-like worlds** ([e4mc](https://e4mc.link/) - in FO, [World Host](https://modrinth.com/mod/world-host), [Essential](https://essential.gg/) etc): host from Fabulously Optimized or install [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports) on the client
  - FO users will see ![optional](https://i.ibb.co/hstcjW7/neutral.png) and their messages cannot be reported.

_This section is also reposted to [No Chat Reports wiki](https://github.com/Aizistral-Studios/No-Chat-Reports/wiki/Protecting-server-players)._

### Client version flexibility

**Before adding this, it is [recommended to disable chat reporting](#chat-reporting) to ensure it works properly on 1.19.2 and below.**

Ever wondered, how some servers are able to update the same day a new Minecraft version is released? Chances are, they are using a plugin that enables this without having to change the server version (yet).

**ViaVersion** and **ViaBackwards** are plugins that transform the network packets to let users join your server with a different client version. This is especially welcome for users who mod their client, such as Fabulously Optimized users, as not every mod is updated as soon as the new version of Minecraft is released, so users may be inclined to use outdated clients for a bit longer. 

* **ViaVersion** lets users join with a _newer_ client version. For example, if your server is still using 1.19.2, this will let users join with 1.19.3 and later.
   * By default, ViaVersion allows users to join from your server's Minecraft version up to the latest stable Minecraft version. This can be filtered in the ViaVersion configuration file.
   * Download for: [Paper/Spigot/Purpur/Velocity](https://hangar.papermc.io/ViaVersion/ViaVersion) | [Fabric/Quilt*](https://www.curseforge.com/minecraft/mc-mods/viafabric) 
* **ViaBackwards** lets users join with an _older_ client version. For example, if your server is using 1.19.4, users can join with 1.19.3 and older.
  * By default, ViaBackwards allows users to join from Minecraft 1.8 up to your server's Minecraft version. This can be filtered in the ViaVersion configuration file.
  * Any new blocks, items and entities will be shown as older types with equivalent properties (like mobs of similar size or blocks of similar breaking speed). Users with newer clients will see them as normal.
  * Download for: [Paper/Spigot/Purpur/Velocity](https://hangar.papermc.io/ViaVersion/ViaBackwards) | [Fabric/Quilt*](https://www.curseforge.com/minecraft/mc-mods/viabackwards)

Depending on your server, you can choose to use only ViaVersion or both. If your server is hub-based, it is recommended to install the plugin(s) to each backend server and _not_ the proxy itself.

_* Fabric/Quilt versions can also work in the client, though this is not advised due to potential conflicts with anticheats. It is recommended to keep it on the server only. Quilt support is untested for both server and client._

### Bedrock compatibility

Interested in allowing Bedrock users to join? Check out [GeyserMC](https://geysermc.org/).

Note that there can be incompatibilities and weird glitches (e.g. with anticheat plugins) because of big differences between Bedrock Edition and Java Edition.

### Server-side content mods

**These mods are usually not compatible with [ViaVersion and ViaBackwards](#server-side-content-mods) and they require a Fabric server.**

Did you know that it is possible to have content mods (e.g. new blocks and items) on the server without requiring them to be installed on the client? That means that you can add new stuff to the server while your users use unmodified Fabulously Optimized!

- [Check out these mods](https://github.com/Patbox/polymer/blob/dev/1.21/MODS.md) built for [Polymer](https://modrinth.com/mod/polymer) to provide this seamlessly
- [Check out PolyMc](https://theepicblock.github.io/PolyMc/) [(_not_ the launcher!)](install-instructions.md#polymc), which can work with even more mods but requires your testing first

### Mods in rules

Some servers tend to put a list of allowed mods into their rules. While it may sound like a good idea in theory, it actually creates more problems due to its vagueness. 

> **DON'T:** "Only OptiFine allowed."

This would disallow Fabulously Optimized, despite it having mods that do exactly the same thing.

> **DO**: "Performance and visual-enchancing mods are allowed."

This would allow Fabulously Optimized in your server without requiring further clarification.

---

> **DON'T:** "Only minimap mod X is allowed."

The players would only depend on that single mod's updates, even if there are alternatives available.

> **DO:** "Any minimap mod with player radar disabled."

This allows users to use any minimap mods by configuring them by theirselves. Many minimap mods also have server-side enforcement options.

---

> **DON'T:** "Maximum 25 mods can be used."

This would already disqualify Fabulously Optimized, as it has more.

> **DO:** (don't mention it)

Arbitary mod count limits do not benefit anything at all. Some mods may be big and do a lot, while others may be small and do very little, hence users may have very different mod counts.

---

> **DON'T:** "Only Forge mods are allowed."

Fabulously Optimized does not use Forge.

> **DO:** (don't mention it)

Restricting certain mod loaders or clients is bad for the user and harmful for the Minecraft ecosystem as a whole. Just restrict behaviours.

---

Other recommendations:

* Get voluntary moderators for your server
* Use anti-cheat plugins: [Paper/Spigot](https://www.spigotmc.org/wiki/anti-cheat-list-bukkit-and-spigot-1-19-x/) or [Fabric/Quilt](https://serverside.infra.link/#:~:text=Anticheat/Anti%20X%2Dray)

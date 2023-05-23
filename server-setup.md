# Server setup

Fabulously Optimized is a strictly client-sided modpack, meaning it works and behaves mostly the same on **every server that allows vanilla clients**. 

The CurseForge listing has a section of "server packs", but [those are actually just the MultiMC versions](install-instructions.md#multimc) that are marked as server packs for better visibility.

## Tips

* [Use speedy server software](#software)
* [Protect users from chat reporting](#chat-reporting)
* [Restrict mod behaviours, not names](#mods-in-rules)

### Software

For server software it is recommended to use [Paper](https://papermc.io), [Pufferfish](https://github.com/pufferfish-gg/Pufferfish) or [Purpur](https://github.com/PurpurMC/Purpur/), which are performance-optimized forks of Spigot, but support [all the same plugins](https://www.spigotmc.org/resources/categories/spigot.4/). Using Realms is not advised.

If you still like Fabric a lot, you can [install it on a server as well](https://fabricmc.net/use/?page=server) and use [server-side optimization mods](https://modrinth.com/mods?f=categories%3A%27optimization%27&g=categories%3A%27fabric%27&e=server), including those in FO.

If you need a host, [check out BisectHosting](https://www.bisecthosting.com/clients/aff.php?aff=2604). [This affiliate link](https://www.bisecthosting.com/clients/aff.php?aff=2604) will give you 25% off for the first month.

### Chat Reporting

Minecraft 1.19.1 added a feature [that lets users report chat messages to Mojang](chat-reporting-faq.md). This is unwanted for most servers, as it can result users being banned for things that are allowed by server rules.

#### How your server works in Fabulously Optimized

The following icons show the status of the server. Icons are shown on the bottom right corner of the chat box.

* **1.18.2 or below (e.g. ViaVersion)**: FO users will see ![optional](https://i.ibb.co/hstcjW7/neutral.png).
    * Chat reporting is disabled for everyone. On vanilla clients, gray bars are displayed on the left of the messages.
* **1.19 or up**:
    1. Using [one of the mods/plugins](#how-to-protect-your-users): FO users will see ![disabled](https://i.ibb.co/QDFzXCT/secure.png)
        * Chat reporting is disabled for everyone. On vanilla clients, gray bars are displayed on the left of the messages.
    2. In other cases, FO users will see ![unknown](https://i.ibb.co/Yb1n6fW/unknown.png) until they send the first chat message.
        1. If `enforce-secure-profile` = `true` (default), FO users will see ![enabled](https://i.ibb.co/2YgMHpR/insecure.png).
            * Chat reporting is enabled for everyone.
        2. If `enforce-secure-profile` = `false` (recommended), FO users will see ![optional](https://i.ibb.co/hstcjW7/neutral.png).
            * Chat reporting is enabled for vanilla users' messages and disabled for FO users' messages. On vanilla clients, gray bars are displayed on the left of FO users' messages.
* **Realms**: FO users will see ![realms](https://i.ibb.co/gTxw84X/realms.png).
    * Chat reporting is enabled for everyone and [Mojang monitors all chats](chat-reporting-faq.md#does-mojang-monitor-my-chats).

#### How to protect your users

- **All 1.18- backend servers**: no changes necessary, chat reporting doesn't exist.
- **All 1.19+ backend servers**: set `enforce-secure-profile` to `false` in _server.properties_
  - This doesn't disable chat reporting by itself, but allows users to join without requiring them to sign their messages, to protect their privacy.
  - If no other measures are taken alongside this:
      - FO users will see ![optional](https://i.ibb.co/hstcjW7/neutral.png) and their messages cannot be reported.
      - Vanilla users will see a warning toast in the top right corner and their messages can be reported. To avoid those problems, use one of the plugins/mods below.
- **Velocity**: set `force-key-authentication` to `false` in _velocity.toml_
  - Same comments apply as for "all 1.19+ backend servers" above.
- **BungeeCord/Waterfall**: set `enforce_secure_profile` to `false` in _config.yml_
  - Same comments apply as for "all 1.19+ backend servers" above.
- **Paper/Purpur/Pufferfish**: install the [FreedomChat](https://modrinth.com/mod/freedomchat) plugin.
   - Ensure `rewrite-chat`, `claim-secure-chat-enforced` and `send-prevents-chat-reports-to-client` are all set to `true` inside the FreedomChat's config file to make FO users see a ![disabled](https://i.ibb.co/QDFzXCT/secure.png) icon near chat.
- **Fabric/Quilt/Forge**: install [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports)
   - FO users will get a ![disabled](https://i.ibb.co/QDFzXCT/secure.png) icon near chat.
- **Realms**: impossible to circumvent seamlessly; [Mojang monitors all chats in Realms!](chat-reporting-faq.md#does-mojang-monitor-my-chats)
  - Consider [encrypting your chat messages](chat-reporting-faq.md#can-i-encrypt-my-chat-messages) to protect yourself, 
    - You obviously need to let other members of the server also know how to do that and what method/key will you be using. 
  - [There is a workaround datapack](https://www.planetminecraft.com/data-pack/no-more-chat-reports-datapack/) where you can use a book to chat, but you are only protected if you use it instead of normal chat text box.
  - Consider [getting a real host](https://www.bisecthosting.com/clients/aff.php?aff=2604) to avoid surveillance altogether (affiliate link - 25% off first month).

_This section is also reposted to [No Chat Reports wiki](https://github.com/Aizistral-Studios/No-Chat-Reports/wiki/Protecting-server-players)._

### Mods in rules

Some servers tend to put a list of allowed mods into their rules. While it may sound like a good idea in theory, it actually creates more problems due to its vagueness. 

> **DON'T:** "Only OptiFine allowed." - this would disallow Fabulously Optimized, despite it having mods that do exactly the same thing.
>
> **DO**: "Performance and visual-enchancing mods are allowed." - this would allow Fabulously Optimized in your server without requiring further clarification.

> **DON'T:** "Only minimap mod X is allowed." - the players would only depend on that single mod's updates, even if there are alternatives available.
>
> **DO:** "Any minimap mod with player radar disabled." - this allows users to use any minimap mods by configuring them by theirselves. Many minimap mods also have server-side enforcement options.

> **DON'T:** "Maximum 25 mods can be used." - this would already disqualify Fabulously Optimized, as it has more.
>
> **DO:** (don't mention it) - arbitary mod count limits do not benefit anything at all.

> **DON'T:** "Only Forge mods are allowed." - Fabulously Optimized does not use Forge.
>
> **DO:** (don't mention it) - restricting certain mod loaders or clients is bad for the user and harmful for the Minecraft ecosystem as a whole. Just restrict behaviours.

Other recommendations:

* Get voluntary moderators for your server
* Use anti-cheat plugins: [Paper/Spigot](https://www.spigotmc.org/wiki/anti-cheat-list-bukkit-and-spigot-1-19-x/) [Fabric/Quilt](https://serverside.infra.link/#:~:text=Anticheat/Anti%20X%2Dray)

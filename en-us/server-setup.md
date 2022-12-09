# Server setup

Fabulously Optimized is a strictly client-sided modpack, meaning it works and behaves mostly the same on **every server that allows vanilla clients**. 

Yes, the CurseForge listing has a section of "server packs", but [those are actually just the MultiMC versions](install-instructions.md#multimc) that are marked as server packs for better visibility.

### Software

For server software I recommend using [Paper](https://papermc.io), [Pufferfish](https://github.com/pufferfish-gg/Pufferfish) or [Purpur](https://github.com/PurpurMC/Purpur/), which are performance-optimized forks of Spigot, but support [all the same plugins](https://www.spigotmc.org/resources/categories/spigot.4/). 

If you still like Fabric a lot, you can [install it on a server as well](https://fabricmc.net/use/?page=server) and use [server-side optimization mods](https://modrinth.com/mods?f=categories%3A%27optimization%27&g=categories%3A%27fabric%27&e=server), including those in FO.

If you need a host, [check out BisectHosting](https://www.bisecthosting.com/clients/aff.php?aff=2604). [This affiliate link](https://www.bisecthosting.com/clients/aff.php?aff=2604) will give you 25% off for the first month.

### Chat Reporting

Minecraft 1.19.1 added a feature [that lets users report chat messages to Mojang](chat-reporting-faq.md). 

#### How your server works in Fabulously Optimized

* If your server is based on 1.18.2 or below with a protocol tweak (e.g. ViaVersion), nothing will change. FO users will see ![disabled](https://i.ibb.co/WPcZsxp/secure.png) on the bottom right corner of the chat box.
* If your server is based on 1.19 or up and chat signatures are not enforced, FO users will not sign the messages either. FO users will see ![optional](https://i.ibb.co/Zd86KN0/warning.png) on the bottom right corner of the chat box.
  * If you're using a plugin that uses system messages for chat (e.g. the ones below), the report button will be disabled,
  * If you're using vanilla-like chat, vanilla users may see a gray bar on the left of FO users' messages. FO users can report vanilla users, but vanilla users cannot report FO users (by default).
  * If you're using the [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports) mod, FO users will get a ![disabled](https://i.ibb.co/WPcZsxp/secure.png) and the report button will be disabled.
* If your server is based on 1.19 or up and chat signatures are enforced, FO users will have their messages signed as well. FO users will see ![enabled](https://i.ibb.co/3k1H6VV/insecure.png) on the bottom right corner of the chat box.
* If you're using Realms, everyone is monitored by Mojang and has chat messages signed. FO users will see ![realms](https://i.ibb.co/KsCBwVb/realms.png) on the bottom right corner of the chat box.

#### How to protect your users

- **All 1.18- backend servers**: no changes necessary, chat reporting doesn't exist.
- **All 1.19+ backend servers**: set `enforce-secure-profile` to `false` in _server.properties_
  - This doesn't disable chat reporting by itself, but allows users to join without requiring them to sign their messages, to protect their privacy,
  - If no other measures are taken alongside this, _vanilla clients_ will see a warning toast in the top right corner and they will still sign the messages. That means anyone can report them, but they cannot report FO users. To avoid those problems, use one of the plugins/mods below.
- **Velocity**: set `force-key-authentication` to `false` in _velocity.toml_
  - Same comments apply as for "all servers" above.
- **BungeeCord/Waterfall**: set `enforce_secure_profile` to `false` in _config.yml_
  - Same comments apply as for "all servers" above.
- **Paper/Purpur/Pufferfish/Spigot**: install the [FreedomChat](https://modrinth.com/mod/freedomchat) plugin and ensure `rewrite-chat`, `claim-secure-chat-enforced` and `send-prevents-chat-reports-to-client` are all set to `true` inside the FreedomChat's config folder. FO users will get a ![disabled](https://i.ibb.co/WPcZsxp/secure.png) icon near chat.
  - Spigot itself will however not be able to support the `send-prevents-chat-reports-to-client` feature itself as a whole.
- **Fabric/Quilt/Forge**: install [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports) - same mod as in FO; FO users will get a ![disabled](https://i.ibb.co/WPcZsxp/secure.png) icon near chat.
- **Realms**: impossible to circumvent seamlessly; [Mojang monitors all chats in Realms!](https://help.minecraft.net/hc/en-us/articles/8047895358605-Our-Commitment-to-Player-Safety#h_01G95X76WR1PM97XBXDE7G25KE)
  - Consider [encrypting your chat messages](chat-reporting-faq.md#can-i-encrypt-my-chat-messages) to protect yourself, 
    - You obviously need to let other members of the server also know how to do that and what method/key will you be using. 
  - [There is a workaround datapack](https://www.planetminecraft.com/data-pack/no-more-chat-reports-datapack/) where you can use a book to chat, but you are only protected if you use it instead of normal chat text box,
  - Consider [getting a real host](https://www.bisecthosting.com/clients/aff.php?aff=2604) to avoid surveillance altogether (affiliate link - 25% off first month).

_This section is also reposted to [No Chat Reports wiki](https://github.com/Aizistral-Studios/No-Chat-Reports/wiki/Protecting-server-players)._

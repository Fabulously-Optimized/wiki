# Server setup

Fabulously Optimized is a strictly client-sided modpack, meaning it works and behaves mostly the same on **every server that allows vanilla clients**. 

Yes, the CurseForge listing has a section of "server packs", but [those are actually just the MultiMC versions](install-instructions.md#multimc) that are marked as server packs for better visibility.

### Software

For server software I recommend using [Paper](https://papermc.io), which is a performance-optimized fork of Spigot, but supports [all the same plugins](https://www.spigotmc.org/resources/categories/spigot.4/). 

If you still like Fabric a lot, you can [install it on a server as well](https://fabricmc.net/use/?page=server) and use [server-side optimization mods](https://modrinth.com/mods?f=categories%3A%27optimization%27&g=categories%3A%27fabric%27&e=server), including those in FO.

If you need a host, [check out BisectHosting](https://www.bisecthosting.com/clients/aff.php?aff=2604). [This affiliate link](https://www.bisecthosting.com/clients/aff.php?aff=2604) will give you 25% off for the first month.

### 1.19.1+

Minecraft 1.19.1 added a feature [that lets users report chat messages to Mojang](chat-reporting-faq.md). 

#### How it works in Fabulously Optimized

* If your server is based on 1.18.2 or below with a protocol tweak (e.g. ViaVersion), nothing will change. FO users will see ![yellow ℹ️](https://i.ibb.co/YXQdJRr/yellow.png) on the bottom right corner of the chatbox.
* If your server is based on 1.19 or up and chat signatures are not enforced, FO users will not sign the messages either. FO users will see ![yellow ℹ️](https://i.ibb.co/YXQdJRr/yellow.png) on the bottom right corner of the chatbox.
  * If you're using a plugin that uses system messages for chat (e.g. the ones below), the report button will be disabled
  * If you're using vanilla-like chat, vanilla users may see a red bar on the left of the message and ![red markings](https://i.ibb.co/ftRMqHL/exclamation.png) on the right on FO users' messages. FO users can report vanilla users, but vanilla users cannot report FO users.
  * If you're using the [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports) mod, FO users will get a ![green ✅](https://i.ibb.co/LPXNKRM/green.png) and the report button will be disabled
* If your server is based on 1.19 or up and chat signatures are enforced, FO users will have their messages signed as well. FO users will see ![red ⚠️](https://i.ibb.co/tzd8CvB/red.png) on the bottom right corner of the chatbox.

#### How to protect your users

- **All 1.19+ backend servers**: set `enforce-secure-profile` to `false` in _server.properties_
  - This doesn't disable chat reporting by itself, but allows users to join without requiring them to sign their messages, to protect their privacy.
  - If no other measures are taken alongside this, _vanilla clients_ will see a warning toast in the top right corner and they will still sign the messages.
    - That means anyone can report them, but they cannot report FO users. To avoid those problems, use one of the plugins/mods below.
- **Velocity**: set `force-key-authentication` to `false` in _velocity.toml_
  - Same comments apply as for "all servers" above.
- **BungeeCord** / **Waterfall**: set `enforce_secure_profile` to `false` in _config.yml_
  - Same comments apply as for "all servers" above.
- **Paper/Spigot/Purpur**: install the [FreedomChat](https://modrinth.com/mod/freedomchat) plugin - no config required
- **Fabric/Quilt/Forge**: install _one_ of the following plugins:
  - [NoChatReport](https://modrinth.com/mod/no-chat-report) - compatible with most chat mods/vanilla chat, no config required 
  - [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports) - same mod as in FO; FO users will get a ![green ✅](https://i.ibb.co/LPXNKRM/green.png) icon near chat
    - If you want to allow vanilla clients to join, set `demandOnClient` to `false` and `convertToGameMessage` to `true`. 
- **Realms**: impossible to circumvent seamlessly; [Mojang monitors all chats in Realms!](https://help.minecraft.net/hc/en-us/articles/8047895358605-Our-Commitment-to-Player-Safety#h_01G95X76WR1PM97XBXDE7G25KE)
  - [There is a workaround datapack](https://www.planetminecraft.com/data-pack/no-more-chat-reports-datapack/) where you can use a book to chat, but you are only protected if you use it instead of normal chat textbox
  - Consider [getting a real host](https://www.bisecthosting.com/clients/aff.php?aff=2604) (affiliate link - 25% off first month).

_This section is also reposted to [No Chat Reports wiki](https://github.com/Aizistral-Studios/No-Chat-Reports/wiki/Protecting-server-players)._

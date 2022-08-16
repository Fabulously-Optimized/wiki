# Server setup

Fabulously Optimized is a strictly client-sided modpack, meaning it works and behaves mostly the same on **every server that allows vanilla clients**. 

Yes, the CurseForge listing has a section of "server packs", but those are actually just the MultiMC versions that are marked as server packs for better visibility.

### Software

For server software I recommend using [Paper](https://papermc.io), which is a performance-optimized fork of Spigot, but supports all the same plugins. 

If you still like Fabric a lot, you can also [use that on a server too](https://fabricmc.net/use/?page=server) and check out [comp500's list](https://github.com/comp500/fabric-serverside-mods#performance) for some great server-side mods.

If you need a host, [check out BisectHosting](https://www.bisecthosting.com/clients/aff.php?aff=2604). [This affiliate link](https://www.bisecthosting.com/clients/aff.php?aff=2604) will give you 25% off for the first month.

### 1.19.1+

Minecraft 1.19.1 added a feature [that lets users report chat messages to Mojang](chat-reporting-faq.md). 

#### How it works in Fabulously Optimized

* If your server is based on 1.18.2 or below with a protocol tweak (e.g. ViaVersion), nothing will change. FO users will see ![yellow ℹ️](https://i.ibb.co/YXQdJRr/yellow.png) on the bottom right corner of the chatbox.
* If your server is based on 1.19 or up and chat signatures are not enforced, FO users will not sign the messages either. FO users will see ![yellow ℹ️](https://i.ibb.co/YXQdJRr/yellow.png) on the bottom right corner of the chatbox.
  * If you're using a plugin that uses system messages for chat (e.g. the ones below), the report button will be disabled
  * If you're using vanilla-like chat, vanilla users may see a red bar on the left of the message and ![red markings](https://i.ibb.co/ftRMqHL/exclamation.png) on the right on FO users' messages. 
  * If you're using the [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports) mod, FO users will get a ![green ✅](https://i.ibb.co/LPXNKRM/green.png) and the report button will be disabled
* If your server is based on 1.19 or up and chat signatures are enforced, FO users will have their messages signed as well. FO users will see ![red ⚠️](https://i.ibb.co/tzd8CvB/red.png) on the bottom right corner of the chatbox.

#### How to protect your users

- **All servers**: set `enforce-secure-profile` to `false` in _server.properties_
  - This doesn't disable chat reporting by itself, but allows users to join without requiring them to sign their messages, to protect their privacy.
  - If no other measures are taken alongside this, _vanilla clients_ will see a warning toast in the top right corner and they will still sign the messages.
    - That means anyone can report them, but they cannot report FO users. To avoid those problems, use one of the plugins/mods below.
- **Velocity**: set `force-key-authentication` to `false` in _velocity.toml_
  - Same comments apply as for "all servers" above.
- **Paper/Spigot/Purpur**: install _one_ of the following plugins:
  - [FreedomChat](https://modrinth.com/mod/freedomchat) - compatible with most chat plugins/vanilla chat, no config required
  - [No Chat Reports](https://www.spigotmc.org/resources/no-chat-reports-spigot-1-19.102931/) - claims to be compatible with vanilla chat; not by the dev of the Fabric mod
- **Fabric/Quilt/Forge**: install _one_ of the following plugins:
  - [NoChatReport](https://modrinth.com/mod/no-chat-report) - compatible with most chat mods/vanilla chat, no config required 
  - [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports) - same mod as in FO; FO users will get a ![green ✅](https://i.ibb.co/LPXNKRM/green.png) icon near chat
    - If you want to allow vanilla clients to join, set `demandOnClient` to `false` and `convertToGameMessage` to `true`. 
  

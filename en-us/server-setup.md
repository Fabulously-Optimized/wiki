# Server setup

Fabulously Optimized is a strictly client-sided modpack, meaning it works and behaves mostly¹ the same on **every server that allows vanilla clients**. 

Yes, the CurseForge listing has a section of "server packs", but those are actually just the MultiMC versions that are marked as server packs for better visibility.

### Software

For server software I recommend using [Paper](https://papermc.io), which is a performance-optimized fork of Spigot, but supports all the same plugins. 

If you still like Fabric a lot, you can also [use that on a server too](https://fabricmc.net/use/?page=server) and check out [comp500's list](https://github.com/comp500/fabric-serverside-mods#performance) for some great server-side mods.

If you need a host, [check out BisectHosting](https://www.bisecthosting.com/clients/aff.php?aff=2604). [This affiliate link](https://www.bisecthosting.com/clients/aff.php?aff=2604) will give you 25% off for the first month.

### 1.19.1+

Minecraft 1.19.1 added a feature [that lets users report chat messages to Mojang](chat-reporting-faq.md). 

¹ Fabulously Optimized has chosen to opt-out of the system by default, meaning:

* If your server is based on 1.18.2 or below with a protocol tweak (e.g. ViaVersion), nothing will change
* If your server is based on 1.19 or up and chat signatures are not enforced, FO users will not sign the messages either. 
  * If you're using a plugin that adds custom chat formatting, e.g. the ones below, nothing will change
  * If you're using vanilla-based chat, users may see a red bar on the left of the message and ![red markings](https://i.ibb.co/ftRMqHL/exclamation.png) on the right.
* If your server is based on 1.19 up and chat signatures are enforced, FO users will have their messages signed as well. The bottom right corner of the chatbox will have a ![red ⚠️](https://i.ibb.co/tzd8CvB/red.png) icon to inform the users of this state.

**It is highly recommended to protect your users from chat reports by doing the following:**

- **All servers**: set `enforce-secure-profile` to `false` in _server.properties_
  - This doesn't disable chat reporting by itself, but allows users to join without requiring them to sign their messages, to protect their privacy.
  - When disabled, vanilla (not FO) users will see a warning toast in the top right corner. To avoid that as well, use one of the plugins/mods below.
- **Velocity**: set `force-key-authentication` to `false` in _velocity.toml_
  - Same comments apply as for "all servers" above.
- **Paper/Spigot/Purpur**: install _one_ of the following plugins:
  - [FreedomChat](https://github.com/Oharass/FreedomChat) - claims to be compatible with most chat plugins
  - [No Chat Reports](https://www.spigotmc.org/resources/no-chat-reports-spigot-1-19.102931/) - claims to be compatible with vanilla chat; not by the dev of the Fabric mod
- **Fabric/Quilt/Forge**: install _one_ of the following plugins:
  - [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports) - same dev as the mod in FO; FO users will get a ![green ✅](https://i.ibb.co/LPXNKRM/green.png) icon near chat
    - If you want to allow vanilla clients to join, set `demandOnClient` to `false` and `convertToGameMessage` to `true`. 
  - [NoChatReport](https://modrinth.com/mod/no-chat-report) - lightweight, simply converts all messages to system messages

# Server setup

Fabulously Optimized is a strictly client-sided modpack, meaning it works and behaves the same¹ on **every server that allows vanilla clients**. 

Yes, the CurseForge listing has a section of "server packs", but those are actually just the MultiMC versions that are marked as server packs for better visibility.

<sub><sup>¹ _As of 1.19.1, chat signing will be done only if the server requires it, read [chat reporting FAQ](chat-reporting-faq.md) for more info_</sup></sub>

### Software

For server software I recommend using [Paper](https://papermc.io), which is a performance-optimized fork of Spigot, but supports all the same plugins. 

If you still like Fabric a lot, you can also [use that on a server too](https://fabricmc.net/use/?page=server) and check out [comp500's list](https://github.com/comp500/fabric-serverside-mods#performance) for some great server-side mods.

If you need a host, [check out BisectHosting](https://www.bisecthosting.com/clients/aff.php?aff=2604). [This affiliate link](https://www.bisecthosting.com/clients/aff.php?aff=2604) will give you 25% off for the first month.

### 1.19.1+

1.19.1 added a feature [that lets users report chat messages to Mojang](chat-reporting-faq.md). If you'd like to disable that feature for your players, do the following:

- **All servers**: set `enforce-secure-profile` to `false` in _server.properties_
  - This doesn't disable chat reporting by itself, but allows users to join without requiring them to sign their messages, to protect their privacy.
  - When disabled, vanilla (not FO) users will see a warning toast in the top right corner. To avoid that as well, use one of the plugins/mods below.
- **Velocity**: set `force-key-authentication` to `false` in _velocity.toml_
  - Same comments apply as for "all servers" above.
- **Paper/Spigot/Purpur**: install _one_ of the following plugins:
  - [FreedomChat](https://github.com/Oharass/FreedomChat)
  - [No Chat Reports](https://www.spigotmc.org/resources/no-chat-reports-spigot-1-19.102931/) (not by the dev of the Fabric mod)
  - [No Encryption](https://www.spigotmc.org/resources/noencryption.102902/)
- **Fabric/Quilt/Forge**: install [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports).
  - If you want to allow vanilla clients to join, set `demandOnClient` to `false` and `convertToGameMessage` to `true`. 

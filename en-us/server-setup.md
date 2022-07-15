# Server setup

Fabulously Optimized is a strictly client-sided modpack, meaning it works and behaves the same on **every server that allows vanilla clients**. 

Yes, the CurseForge listing has a section of "server packs", but those are actually just the MultiMC versions that are marked as server packs for better visibility.

For server software I recommend using [Paper](https://papermc.io), which is a performance-optimized fork of Spigot, but supports all the same plugins. 

If you still like Fabric a lot, you can also [use that on a server too](https://fabricmc.net/use/?page=server) and check out [comp500's list](https://github.com/comp500/fabric-serverside-mods#performance) for some great server-side mods. There is a mod called Cardboard that lets you use Fabric with Spigot, [but is not recommended](https://gist.github.com/Patbox/e44844294c358b614d347d369b0fc3bf) - just pick one or the other.

If you need a host, [check out BisectHosting](https://www.bisecthosting.com/clients/aff.php?aff=2604). This affiliate link will give you 25% off for the first month.

### 1.19.1

1.19.1 added a feature [that lets users report chat messages to Mojang](1-19-1-faq.md). If you don't like that as a server owner, do the following:

- All servers: set `enforce-secure-profile` to `false` in _server.properties_. This doesn't disable chat reporting by itself, but allows users to join without requiring them to sign their messages, to protect their privacy. 
- Paper/Spigot: install **one** of the following mods:
  - [No Encryption](https://www.spigotmc.org/resources/noencryption.102902/)
  - [No Chat Reports](https://www.spigotmc.org/resources/no-chat-reports.102990/)
  - [No Report](https://www.spigotmc.org/resources/noreport.102844/)

- Fabric/Quilt: install [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports)

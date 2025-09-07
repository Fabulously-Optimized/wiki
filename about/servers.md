---
hidden: true
icon: server
---

# Servers

FO does not require any special setup server-side: any server compatible with vanilla should be supported. However, we've compiled a list of recommendations for server-side setup.

{% hint style="warning" %}
All content on this page is just a suggestion, and FO does not offer support for server setup. If you need help with it, please ask in the respective mod or platform support site.
{% endhint %}

## Share Your World

Did you know FO allows you to play with anyone on your singleplayer worlds, even on different networks? If that's all you'd need a server for, there's no need for it:

1. Open your singleplayer world
2. Press <kbd>Esc</kbd>
3. Click on <kbd>**Open to Internet**</kbd>. You should see an address in chat
4. Send the address from chat to your friend. Your friend will need to use your same version of Minecraft.

## Optimize Server Software

{% hint style="danger" %}
Avoid using Realms! Read more in the [Player Reporting article](../info/mods/player-reporting.md).
{% endhint %}

For the best performance, use one of the following server software options:

* [Paper](https://papermc.io/)
* [Pufferfish](https://github.com/pufferfish-gg/Pufferfish)
* [Purpur](https://github.com/PurpurMC/Purpur)

Those are optimized forks of Spigot, and support all Spigot plugins.

If you want to use Fabric instead:

1. [Install Fabric on a server](https://fabricmc.net/use/?page=server).
2. Add [server-side optimization mods](https://modrinth.com/mods?o=20\&f=categories:%27optimization%27\&g=categories:%27fabric%27\&nf=categories:cursed\&v=1.21.1\&e=server).

If you need a host, consider [BisectHosting (affiliate link)](https://download.fo/host) for a 25% discount for the first month, while supporting FO financially. Thank you!

## Write Rules for Your Server

Please be careful when writing rules for your server, to avoid putting unnecessary restrictions on users:

| ❌ DON'T                          | ✅ DO                                                 | Rationale                                                                                                                                                                                                                                           |
| -------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Only OptiFine allowed            | Performance and visual-enhancing mods are allowed    | There are multiple mods tackling and solving the same issues, you shouldn't limit players to one specific mod                                                                                                                                       |
| Only mini-map mod "X" is allowed | Mini-map mods with player radar disabled are allowed | <p>Allowing one mod by name ties users to its updates, excluding all alternatives.</p><p>Also, mods may change their default configuration or add features your rules disallow at any time, so you should specify which features are acceptable</p> |
| Max 25 mods allowed              | _nothing_                                            | Arbitrary mod counts do not benefit anything at all, since some may be huge and do many things, while others are very small                                                                                                                         |
| Only Forge mods are allowed      | _nothing_                                            | Restricting certain mod loaders does more harm than good to your player base and to the Minecraft ecosystem as a whole                                                                                                                              |

{% hint style="success" %}
A generally good rule of thumb is: restrict behaviors, not mods.
{% endhint %}

## Configure Player Reporting

{% hint style="info" %}
Read more on the ["Protecting Server Players" page in the No Chat Reports wiki](https://github.com/Aizistral-Studios/No-Chat-Reports/wiki/Protecting-server-players).
{% endhint %}

Minecraft 1.19.1 introduced chat reporting, which many servers disable. As a server admin, you can do the following:

* If you're on **1.18.2 or earlier**, there's no need to do anything, as Player Reporting didn't exist yet
  * FO users will see this icon: ![Chat Reporting is optional](https://i.ibb.co/hstcjW7/neutral.png)
  * Vanilla users will see a gray bar next to the messages, and their messages will not be reportable
* If you're on **1.19 or newer**:
  * Set `enforce-secure-profile` to `false` in `server.properties`, to allow users to not sign messages
    * FO users will see this icon: ![Chat Reporting is optional](https://i.ibb.co/hstcjW7/neutral.png)
    * Vanilla users will see a warning toast in the top-right corner, but their messages will still be reportable
    * Some hosts use different configuration files:
      * Velocity: set `force-key-authentication` to `false` in `velocity.toml`
      * BungeeCord: set `enforce_secure_profile` to `false` in `config.yml`
  * Install a plugin to completely disable Player Reporting:
    * Vanilla: no known workarounds exist. Please consider using a mod loader
    * Paper/Purpur/Pufferfish: install the [FreedomChat plugin](https://modrinth.com/mod/freedomchat)
      * Set `rewrite-chat` and `send-prevents-chat-reports-to-client` to `true` in FreedomChat's configuration
      * FO users will see this icon: ![Chat Reporting is disabled](https://i.ibb.co/QDFzXCT/secure.png)
      * Vanilla users will see a gray bar next to the messages, and their messages will not be reportable
    * Fabric/NeoForge: install the [No Chat Reports mod](https://modrinth.com/mod/no-chat-reports)
      * FO users will see this icon: ![Chat Reporting is disabled](https://i.ibb.co/QDFzXCT/secure.png)
      * Vanilla users will see a gray bar next to the messages, and their messages will not be reportable
    * Quilt: no known workarounds exist. Please consider using another mod loader
    * LAN worlds: host with FO or install the [No Chat Reports mod](https://modrinth.com/mod/no-chat-reports) on the clients
      * FO users will see this icon: ![Chat Reporting is disabled](https://i.ibb.co/QDFzXCT/secure.png)
      * Vanilla users will see a gray bar next to the messages, and their messages will not be reportable
    * LAN-like worlds ([e4mc](https://e4mc.link/), [World Host](https://modrinth.com/mod/world-host), [Essential](https://essential.gg/)...): host with FO or install the [No Chat Reports mod](https://modrinth.com/mod/no-chat-reports) on the clients
      * FO users will see this icon: ![Chat Reporting is optional](https://i.ibb.co/hstcjW7/neutral.png)
      * Vanilla users will see a warning toast in the top-right corner, but their messages will still be reportable
    * Realms: almost impossible to circumvent
      * Mojang monitors ALL chats in Realms! Read more in the [Player Reporting article](../info/mods/player-reporting.md)
      * FO users will see this icon: ![Chat Reporting is mandatory on Realms](https://i.ibb.co/gTxw84X/realms.png)
      * Vanilla users will not be warned at all, but their messages will be reportable
      * You could:
        * Use alternative methods to chat. Read more in the [Player Reporting article](../info/mods/player-reporting.md)
        * Use the [No More Chat Reports datapack](https://www.planetminecraft.com/data-pack/no-more-chat-reports-datapack), and use the book only to chat
        * Consider relying on [BisectHosting (affiliate link)](https://download.fo/host) for a 25% discount for the first month, while supporting FO financially and avoiding surveillance altogether. Thank you!

## Allow Client Version Flexibility

{% hint style="warning" %}
Before following this section, you should [configure Player Reporting](servers.md#configure-player-reporting).
{% endhint %}

Some servers rely on plugins for support of multiple client versions. These plugins transform network packets, so they can, for example, allow users of FO who temporarily play on outdated versions to still join such servers.

* To allow users to join with a client version _newer_ than the server's, use **ViaVersion**
  * This by default allows versions between your server's and the latest release
* To allow users to join with a client version _older_ than the server's, use **ViaBackwards**
  * This by default allows versions between `1.8` and your server's
  * Newer blocks and entities will show as older types with equivalent properties
* If you're running Fabric on your server, consider using **ViaFabric**

If your server is hub-based, prefer installing the plugins on each backend server rather than the proxy.

## Allow Minecraft: Bedrock Edition Players to Join

With [GeyserMC](https://geysermc.org/), you can allow Minecraft: Bedrock Edition players to join your Java server. Note that there can be incompatibilities and glitches, particularly with anti-cheat plugins, as the two editions are very different technically.

## Add Server-Side Content Mods

You can add new content like blocks and items to the server, without requiring users to install mods! Check out [Patbox's _Mods using Polymer_ list](https://github.com/Patbox/polymer/blob/dev/1.21/MODS.md), built for [Polymer](https://modrinth.com/mod/polymer).

Alternatively, check out [PolyMc](https://theepicblock.github.io/PolyMc) (not to be confused with the [PolyMC launcher](unsupported.md#polymc)). Note that PolyMc may not be compatible with ViaVersion and ViaBackwards.

## Other Recommendations

* Recruit voluntary moderators for your server
* Use anti-cheat plugins

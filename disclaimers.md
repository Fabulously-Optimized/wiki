# Disclaimers

By using this modpack, you agree to the following:

### Server rules and policies

* The modpack has been set up to be compatible with the rules of most public third-party servers, but it is your responsibility to verify whether you are allowed to use it or not. [The mod list may help.](https://download.fo/mods)
* The modpack supports using controllers with analog input, whose usage may trigger anticheats on some servers due to unexpectedly smooth movement. If the playing server rules disallow analog input, the user is expected to manually add the server to mod whitelist, or disable analog input entirely.
   * The user is reminded of said fact upon joining any new server with a controller and analog input enabled.

### Changed default options

* The modpack hides the [third-party server disclaimer](https://minecraft.wiki/w/File:Multiplayer_disclaimer.png), therefore by using the multiplayer function, you implicitly agree to the following: 
    > Caution: Online play is offered by third-party servers that are not owned, operated, or supervised by Mojang Studios or Microsoft. During online play, you may be exposed to unmoderated chat messages or other types of user-generated content that may not be suitable for everyone. 
* The modpack hides a hotkey disclaimer for [the "social interactions" screen](https://minecraft.wiki/w/Social_interactions#Usage). Said screen can be opened by pressing the key `P` in-game or the `Player Reporting` button in the pause menu.
* Other [changed default options can be found here.](changed-options.md)

### Privacy and security

* The modpack features [e4mc](https://modrinth.com/mod/e4mc), which gives users the ability to let their friends connect to their world through the internet, without the use of additional software or mods on the friend side.
  * The feature is (only!) activated by the usual means of opening a world to LAN, so the world can be connected both through LAN and from Internet.
  * A proxy server in one of the four locations in the world is used to generate a randomized "IP" (technically, a subdomain) where other players can connect to. The host's own IP address is never shared, and the generated "IP" varies every time.
  * LAN-sharing and Internet-sharing are automatically disabled once the host disconnects the world. The host can also close the Internet sharing manually for the session by clicking on the link in chat that appeared during creation.
  * Both LAN and Internet variants use the same world settings (gamemode, cheats enabled, etc.), including the player limit of host + up to 7 players.
* The modpack disables Mojang's telemetry, as the data collection is not anonymous and because modified game statistics would skew collected data. [Read more](changed-options.md#telemetry)
* The modpack disables certain mod network services (where present), including mod update checkers and cosmetic donor features, to avoid confusion and privacy concerns. These can be re-enabled by users [in the respective configs.](changed-options.md#configuring-mods)
* An indicator icon is added to inform players of the chat signing status in the server (whether the server supports [Mojang's chat safety features](https://help.minecraft.net/hc/en-us/articles/7317376541197-Minecraft-Java-Edition-Player-Reporting-FAQ)). On servers where chat signing is optional, the modpack opts out of it for the playing user to adhere to the server's intent. [Read more](chat-reporting-faq.md#what-does-this-modpack-do-for-me).

### License and legal

* By installing this modpack you agree that the modpack author, the mod developers and Mojang provide no warranties for using this modpack, every action you do with it is your own.
* Fabulously Optimized does not host any capes or other cosmetics, nor does it encourage users to buy them from any provider. Instead, the modpack encourages users to [prefer free cosmetics](free-cape.md), while also giving them options to use any paid cosmetics they've previously obtained from certain providers.
* Yes, you can fork/remix this pack [according to the license](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/LICENSE.md). You cannot, however, use the "Fabulously Optimized" name or logo to _represent_ your fork (but you can mention that you forked it).
  * That also goes for the Mod Menu Helper resource pack (which uses the same license) - you may include it, if you change the logo and any references to "Fabulously Optimized".
* NOT AN OFFICIAL MINECRAFT PRODUCT. NOT APPROVED BY OR ASSOCIATED WITH MOJANG OR MICROSOFT.

### Badges for forks 

If you have forked the modpack, you can optionally use these badges in your description to show it. For CurseForge, just select and copy the image to get it with the link; for Modrinth and GitHub select the Markdown or HTML variant. [Made by Devin](https://intergrav.github.io/devins-badges-docs)
  
<a href="https://download.fo"><img alt="Built on Fabulously Optimized" height="56" src="https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/cozy/built-with/fabulously-optimized_vector.svg"></a>

Markdown
```html
[![Built on Fabulously Optimized](https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/cozy/built-with/fabulously-optimized_64h.png)](https://download.fo)
```
HTML
```html
<a href="https://download.fo"><img alt="Built on Fabulously Optimized" height="56" src="https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/cozy/built-with/fabulously-optimized_vector.svg"></a>
```
<a href="https://download.fo"><img alt="Built on Fabulously Optimized" height="40" src="https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/compact/built-with/fabulously-optimized_vector.svg"></a>

Markdown
```html
[![Built on Fabulously Optimized](https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/compact/built-with/fabulously-optimized_46h.png)](https://download.fo)
```
HTML
```html
<a href="https://download.fo"><img alt="Built on Fabulously Optimized" height="40" src="https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/compact/built-with/fabulously-optimized_vector.svg"></a>
```

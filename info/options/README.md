---
hidden: true
icon: sliders
---

# Options

FO uses [Your Options Shall Be Respected](https://modrinth.com/mod/yosbr) to manage settings and to allow updates without losing your settings, but you will not get FO's latest recommendations. You can find [FO's settings file on GitHub](https://github.com/Fabulously-Optimized/fabulously-optimized/tree/main/Packwiz/1.21.1/config).

If you want to start fresh, you can always [reset to FO's recommended settings](../../how-to/reset/). You can also check out [other options you may want to change](other.md).

{% hint style="info" %}
Click on each option to get a description of what it does.
{% endhint %}

<table><thead><tr><th>Option</th><th width="100">Vanilla</th><th width="100">FO</th><th>Reason</th></tr></thead><tbody><tr><td><a data-footnote-ref href="#user-content-fn-1"><code>advancedItemTooltips</code></a></td><td><code>false</code></td><td><code>true</code></td><td><p>Advanced tooltips are useful for more than just debugging: for using commands, getting the durability value, knowing the name in English...</p><p>Plus, this setting is hidden in the debug menu, so many people might not know about it</p></td></tr><tr><td><a data-footnote-ref href="#user-content-fn-2"><code>darkMojangStudiosBackground</code></a></td><td><code>false</code></td><td><code>true</code></td><td>Black background is less intrusive than red, parity with Bedrock Edition</td></tr><tr><td><a data-footnote-ref href="#user-content-fn-3"><code>enableVsync</code></a></td><td><code>true</code></td><td><code>false</code></td><td><p>Disabling VSync reduces input lag, increases frame rate with shaders, and emphasizes the benefits of FO.</p><p>The benefits of VSync vary by system; some systems also support Adaptive VSync</p></td></tr><tr><td><a data-footnote-ref href="#user-content-fn-4"><code>guiScale</code></a></td><td><code>0</code></td><td><code>3</code></td><td>The automatic setting can get too large on Full HD or larger screens, including Apple Retina displays</td></tr><tr><td><a data-footnote-ref href="#user-content-fn-5"><code>incompatibleResourcePacks</code></a></td><td><code>[]</code></td><td>(varies)</td><td><p>Mod-provided resource packs known to be compatible despite the old manifest version.</p><p>Usually contains <a href="https://curseforge.com/minecraft/mc-mods/continuity">Continuity</a>'s resource packs</p></td></tr><tr><td><a data-footnote-ref href="#user-content-fn-6"><code>joinedFirstServer</code></a></td><td><code>false</code></td><td><code>true</code></td><td>Users of FO are expected to already know about Social Interactions; the screen is easily accessible through the <strong>Player Reporting</strong> button</td></tr><tr><td><a data-footnote-ref href="#user-content-fn-7"><code>maxFps</code></a></td><td><code>120</code></td><td><code>260</code></td><td><code>260</code> means "unlimited", which allows you to get the full frame rate your system supports</td></tr><tr><td><a data-footnote-ref href="#user-content-fn-8"><code>onboardAccessibility</code></a></td><td><code>true</code></td><td><code>false</code></td><td>This screen is just an added annoyance, since Minecraft already has an accessibility button in the main menu. Read more about <a href="../../about/accessibility.md">accessibility in FO</a></td></tr><tr><td><a data-footnote-ref href="#user-content-fn-9"><code>operatorItemsTab</code></a></td><td><code>false</code></td><td><code>true</code></td><td>It already only appears if you have the permission for it, it's weird Mojang even made it an option</td></tr><tr><td><a data-footnote-ref href="#user-content-fn-10"><code>resourcePacks</code></a></td><td><code>[]</code></td><td><a data-footnote-ref href="#user-content-fn-11">...</a></td><td>Enabled some mod-provided and FO-exclusive resource packs by default. See <a href="../resource-packs/">Resource Packs</a></td></tr><tr><td><a data-footnote-ref href="#user-content-fn-12"><code>lang</code></a></td><td><code>en_us</code></td><td>(your OS' language)</td><td>Enables user's system language by default, courtesy of <a href="https://curseforge.com/minecraft/mc-mods/language-reload">Language Reload</a></td></tr><tr><td><a data-footnote-ref href="#user-content-fn-13"><code>simulationDistance</code></a></td><td><code>12</code></td><td><code>6</code></td><td>Better performance regardless of the rendering distance you use</td></tr><tr><td><a data-footnote-ref href="#user-content-fn-14"><code>skipMultiplayerWarning</code></a></td><td><code>false</code></td><td><code>true</code></td><td>Users of FO are expected to already know that third-party servers are not managed by Mojang Studios or Microsoft.</td></tr><tr><td><a data-footnote-ref href="#user-content-fn-15"><code>telemetryOptInExtra</code></a></td><td><code>false</code></td><td><code>false</code></td><td>Even though "minimal" is the default, FO enforces it further. See <a href="../telemetry.md">Telemetry</a></td></tr><tr><td><a data-footnote-ref href="#user-content-fn-16"><code>tutorialStep</code></a></td><td><code>movement</code></td><td><code>none</code></td><td>Users of FO are expected to not need those tutorials anymore</td></tr></tbody></table>

[^1]: Enables [advanced tooltips](https://online-tech-tips.com/wp-content/uploads/2021/01/Armor-Tooltips-610x571.png), which show item ID, durability, and exact color hex code for dyed armor

[^2]: Makes the Mojang Studios splash screen white-on-black instead of white-on-red

[^3]: Toggle [VSync](https://en.wikipedia.org/wiki/Screen_tearing#Vertical_synchronization), a FPS-limiting system

[^4]: Size of the menu and interface elements

[^5]: A list of resource packs which have been forcefully enabled, despite being marked as incompatible

[^6]: Whether to display the hint for [Social Interactions](https://minecraft.wiki/w/Social_Interactions_screen)

[^7]: The maximum framerate

[^8]: Indicates whether the user has not seen the accessibility onboarding screen

[^9]: Shows operator-only items (command blocks, lights, barriers, etc.) in a Creative inventory tab, when you have operator access (`/op`)

[^10]: Adjusts which resource packs are enabled by default

[^11]: `["vanilla","fabric","continuity:glass_pane_culling_fix","continuity:default","file/SodiumTranslations.zip","file/Mod Menu Helper.zip","file/Chat Reporting Helper.zip","file/Fast Better Grass.zip"]`

[^12]: Adjusts the game's language

[^13]: Redstone and mob spawning distance

[^14]: Whether to skip the [legal disclaimer](https://minecraft.wiki/w/File:Multiplayer_disclaimer.png) when opening the multiplayer screen

[^15]: Sets the telemetry (analytics data collection) toggle to "minimal".

[^16]: The next step of [tutorial hints](https://minecraft.wiki/w/Tutorial_hints)

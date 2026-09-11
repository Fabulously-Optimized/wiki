---
icon: sparkles
---

# How to add shaders

{% tabs %}
{% tab title="Iris/OptiFine" %}
Mod [Iris](https://modrinth.com/mod/iris) is in the modpack to provide support for Iris and OptiFine shaders.

{% tabs %}
{% tab title="Install" %}
1. Open Minecraft with Fabulously Optimized installed
2. Open `Options...` → `Video Settings...` → `Shader Packs...`
3. Download any shader pack from [Modrinth](https://modrinth.com/shaders?g=categories:iris) or [CurseForge](https://www.curseforge.com/minecraft/search?page=1\&pageSize=20\&sortBy=relevancy\&class=shaders)
4. Drag the ZIP file into the shader pack screen
5. Select the shader, make sure _Shaders_ is set to enabled and click `Apply`
6. The shader has been applied!
{% endtab %}

{% tab title="Configure" %}
1. Click a shader
2. Click `Shader Pack Settings...` below
3. Adjust settings as needed
4. Click `Shader Pack List...`
5. Click `Done`
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Looking for OptiFine's internal shaders? \
Try [internal-shaders](https://modrinth.com/shader/internal-shaders) (shader), [Simply No Shading](https://modrinth.com/mod/simply-no-shading) (mod) or [Flat Lighting](https://modrinth.com/mod/flat-lighting) (mod).
{% endhint %}
{% endtab %}

{% tab title="Vulkan/Aperture" %}
You may have noticed that Iris shaders do not work when using the [Vulkan rendering engine](https://www.minecraft.net/en-us/article/another-step-towards-vibrant-visuals-for-java-edition). This is known and expected, as these shaders are built for the older format, OpenGL.

Therefore, a successor to Iris is being built by the same developers, called [Aperture](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/1122). This is expected to be more performant and supported by the same shader projects you already know from Iris.

Currently, it is unknown when Aperture is ready for use. The modpack will likely include it once OpenGL is actually deprecated by Mojang.

{% hint style="warning" %}
There are also other mods available now that claim to provide shaders in Vulkan. These have limited selection, limited functionality and will not be supported by this modpack.
{% endhint %}
{% endtab %}

{% tab title="Fabulous" %}
{% hint style="warning" %}
These kinds of shaders are rare and may not work in the modpack. Prefer Iris/OptiFine shaders whenever possible.
{% endhint %}

"Fabulous shaders" are vanilla-compatible shaders that work by enabling _Fabulous!_ graphics in video settings and getting a specific resource pack.

* [Fabulousity shader resource pack](https://github.com/ScottoMotto/Fabulousity#fabulousity)
* [Basic Shaders for Vanilla 1.16 resource pack](https://github.com/bradleyq/mc_vanilla_shaders#basic-shaders-for-vanilla-116)
* Sildur's [Fabulous Shaders resource pack](https://sildurs-shaders.github.io/downloads/) [(configuring instructions)](https://sildurs-shaders.github.io/install/#fabulous)
* [Depth Shaders resource pack](https://github.com/onnowhere/depth_shaders/releases)

#### Installation

1. Go to `Options` -> `Video Settings` -> `Quality` -> `Graphics: Fabulous!`
2. [Download any Fabulous shader pack](https://modrinth.com/discover/shaders?g=categories:vanilla). Ensure the shader mentions "fabulous", not just "core"!
3. Move the shader pack to `resourcepacks` folder or drag it into the resourcepacks screen
4. Apply the resource pack in resource packs screen
{% endtab %}

{% tab title="Core" %}
{% hint style="danger" %}
These kinds of shaders are likely to cause crashes and visual issues. Proceed with caution. [Read more](resource-pack-issues.md#core-shaders-incompatible-with-sodium)
{% endhint %}

"Core shaders" are a kind of vanilla shaders included in resource packs to adjust the vanilla HUD and add special effects. These usually do _not_ change landscapes overal&#x6C;_._

Examples of working core shaders of [Vanilla Tweaks](https://vanillatweaks.net/picker/resource-packs/):

* Translucent Spyglass Overlay
* No Spyglass Overlay

Examples of **not** working core shaders of [Vanilla Tweaks](https://vanillatweaks.net/picker/resource-packs/):

* ~~Mob Spawn Indicator~~
* ~~Wavy Leaves~~
* ~~Wavy Plants~~
* ~~Wavy Water~~

Luckily those features can be replicated with [Iris shaders](getting-shaders.md#iris-optifine) or [other mods](adding-more-mods/), so you're not missing out.

{% hint style="warning" %}
Avoid using core shaders for "fullbright", [use a dedicated mod instead.](resource-pack-issues.md#fullbright)
{% endhint %}

#### Installation

1. [Download a core shader resource pack from Modrinth](https://modrinth.com/discover/resourcepacks?f=categories:core-shaders)
2. Move the resource pack to `resourcepacks` folder or drag it into the resourcepacks screen
3. Apply the resource pack in resource packs screen
4. See if it works.
   * If yes, enjoy!
   * If not, use Iris shaders or other mods for the same purpose.
{% endtab %}
{% endtabs %}

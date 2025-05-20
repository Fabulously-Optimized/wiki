---
hidden: true
icon: bug
---

# Bug Fixes

FO includes some mods which fix vanilla bugs. If there's another bug you think FO can fix, you should [request a bug fix](bugs.md#request-a-bug-fix).

| Bug                                                   | Description                                                                                         | Fixed by                                                                          |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| [MC-577](https://bugs.mojang.com/browse/MC-577)       | Mouse buttons block all inventory controls that are not default                                     | [Debugify](https://www.curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-22882](https://bugs.mojang.com/browse/MC-22882)   | Ctrl + Q won't work on Mac                                                                          | [Debugify](https://www.curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-59810](https://bugs.mojang.com/browse/MC-59810)   | Cannot break blocks while sprinting (Ctrl+Click = right-click on macOS)                             | [Debugify](https://www.curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-73186](https://bugs.mojang.com/browse/MC-73186)   | Gaps between the faces of item models                                                               | [Item Model Fix](https://www.curseforge.com/minecraft/mc-mods/item-model-fix)     |
| [MC-81098](https://bugs.mojang.com/browse/MC-81098)   | Redstone dust updates cause lag (Singleplayer only)                                                 | [Lithium](https://www.curseforge.com/minecraft/mc-mods/lithium)                   |
| [MC-89146](https://bugs.mojang.com/browse/MC-89146)   | Pistons forget update when being reloaded                                                           | [Debugify](https://www.curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-90683](https://bugs.mojang.com/browse/MC-90683)   | "Received unknown passenger" - Entities with differing render distances as passengers outputs error | [Debugify](https://www.curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-112730](https://bugs.mojang.com/browse/MC-112730) | Beacon beam and structure block render twice per frame                                              | [Debugify](https://www.curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-121884](https://bugs.mojang.com/browse/MC-121884) | Server → Client custom payload packets can leak resources                                           | [MemoryLeakFix](https://www.curseforge.com/minecraft/mc-mods/memoryleakfix)       |
| [MC-122477](https://bugs.mojang.com/browse/MC-122477) | Linux/GNU: Opening chat sometimes writes 't'                                                        | [Debugify](https://www.curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-132488](https://bugs.mojang.com/browse/MC-132488) | Ticking animated textures is very inefficient                                                       | [Sodium](https://www.curseforge.com/minecraft/mc-mods/sodium)                     |
| [MC-154966](https://bugs.mojang.com/browse/MC-154966) | Hunger and experience bar invisible on horses and all other animal mounts                           | [Better Mount Hud](https://www.curseforge.com/minecraft/mc-mods/better-mount-hud) |
| [MC-165595](https://bugs.mojang.com/browse/MC-165595) | Guardian beam does not render when over a certain "Time" in level.dat                               | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra)         |
| [MC-199467](https://bugs.mojang.com/browse/MC-199467) | Certain entity animations stop after they've existed in world for too long                          | [Debugify](https://www.curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-226729](https://bugs.mojang.com/browse/MC-226729) | Memory leakage problem in native operations                                                         | [MemoryLeakFix](https://www.curseforge.com/minecraft/mc-mods/memoryleakfix)       |
| [MC-227302](https://bugs.mojang.com/browse/MC-227302) | Smooth lighting doesn't work properly on the water surface                                          | [Sodium](https://www.curseforge.com/minecraft/mc-mods/sodium)                     |
| [MC-228976](https://bugs.mojang.com/browse/MC-228976) | Entity collision is run on render thread                                                            | [Lithium](https://www.curseforge.com/minecraft/mc-mods/lithium)                   |
| [MC-237493](https://bugs.mojang.com/browse/MC-237493) | Telemetry cannot be disabled                                                                        | [Debugify](https://www.curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-237493](https://bugs.mojang.com/browse/MC-263865) | Fullscreen state isn't saved                                                                        | [Debugify](https://www.curseforge.com/minecraft/mc-mods/debugify)                 |

## Request a Bug Fix

{% hint style="warning" %}
FO will only fix a bug if it affects a large majority of its users (at least 70% of them). Read more in [FO's principles](../about/).
{% endhint %}

1. Find the bug on [Mojang's bug tracker](https://bugs.mojang.com/browse/MC)
2. Request it or find its status on [Debugify's bug tracker](https://github.com/IsXander/Debugify/issues)
3. If you're sure the bug fix is in Debugify, [request an option change](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/new?labels=option\&template=setting-request.yml)

# 4.x.x/5.x.x FAQ

### What happened?

[Sodium now requires OpenGL 4.5](). That means some computers may now be unsupported, especially Macs.

### Why did FO jump to 5.x.x?

So you'd have an option to use 5.x.x or 4.x.x depending on what's supported on your computer. I try to support 4.x.x for as long as feasible, but it will probably have to stay on Minecraft 1.19.1.

### What can I do?

* **First of all, just try to run FO 5.x.x.** If that doesn't work, try the following steps:
  * Update your graphics drivers, if possible
  * [Remove]() Sodium, Sodium Extra, Iris and Indium 
      * Possibly install [Canvas](https://www.curseforge.com/minecraft/mc-mods/canvas-renderer) instead
      * See also: "Can't you just remove Sodium?" below
  * Mac users: use Metal workaround or something
  * [Switch to Linux](https://www.pcworld.com/article/427298/how-to-get-started-with-linux-a-beginners-guide.html), as it may have drivers that work with it (plus Minecraft runs better on Linux overall)
* Continue using FO 4.x.x until you get a new computer

### Can't you just remove Sodium?

Not really.

It is currently the best performance mod available for Minecraft, and a reason why I created FO.
If I removed Sodium (and Extra, Iris etc), you  would just not have the same performance, options and shaders you're used to. At that point, why use FO at all? Or rather, why would I create FO at all?

Switching to [Canvas](https://www.curseforge.com/minecraft/mc-mods/canvas-renderer) or making a version with it would still have similar effect. Even if it had some positive effect, it is just not the same smooth experience FO is known for. Of course, you are free to do it yourself by [disabling the existing mods](disabling-mods.md) and [installing Canvas](adding-mods). 

### Can't you just maintain a separate version with Canvas?

No, I already maintain a lot of things! Creating a new version that bases on Canvas is pretty much like creating a completely new modpack, I just don't have the time for it.

### I want to shout at somebody!

Feel free to shout at:

* [Apple, for not supporting OpenGL](https://www.anandtech.com/show/12894/apple-deprecates-opengl-across-all-oses)
* Your computer vendor, if they don't provide updated graphics drivers

Do not shout at:

* Any maintainers of Sodium because the change was done for getting drastic performance increases and fixing many bugs. An investment for the future of Sodium, if you will.
* The creator of Fabulously Optimized, because realistically I can only work with mods and versions that are available for me. I do not have the capability or interest in developing a competitor to Sodium.

# Unofficial FAQ for Minecraft's Player Reporting

This wiki article describes the aspects of player reporting, which is a feature added into Minecraft: Java Edition in 2022. Most of the aspects detail on _chat_ reporting, although later added username and skin reporting are described as well. While the article is in the perspective of [Fabulously Optimized](https://github.com/Fabulously-Optimized/fabulously-optimized), a lot of answered questions are universal and applicable for every user of the game.

The intent of this article is to educate [good-minded users](#i-already-follow-the-server-rules-am-a-nice-person.-why-should-i-care) about the pitfalls of the newly introduced player reporting system, including important details and answers to questions that [Mojang's official resources](#official-posts) don't provide. 

The article, nor the modpack does not encourage breaking any rules, and to the author's knowledge (not a lawyer), none of the advice, including described mods, break Mojang's [Community Standards](https://www.minecraft.net/en-us/community-standards) or [Terms of Service](https://www.minecraft.net/en-us/eula) either. The article is provided solely for educational purposes, as-is, without a warranty of any kind.

## Chat reporting

### What is chat reporting?

In [Minecraft 1.19.1](https://www.minecraft.net/en-us/article/minecraft-java-edition-1-19-1) and up, players can report other players' chat messages to Mojang, which may result in a temporary or permanent ban from all multiplayer servers, on all versions of Minecraft: Java Edition.

Technically, "chat reportability" would be a more accurate phrase than "chat reporting", as no server [except Realms](#does-mojang-monitor-my-chats) reports any chat to Mojang automatically. However, in the Minecraft community the term "chat reporting" was coined and is now better understood.

### How are reports created?

[The official help page](https://help.minecraft.net/hc/en-us/articles/7149823936781-Player-Reporting-in-Minecraft-Java-Edition) states the following:

> Reporting can be accessed via the social interactions screen (default keybind is P) or via the pause menu. 
> 
> [...]
> 
> - A player creates a report, selects the offending chat, name, or skin, a category and details, and submits it.
> - The report is sent to our team of Minecraft Investigators.
> - A moderator reviews the report and the evidence and assigns an appropriate action (if any). 
> - If action is taken, a moderator can take one of the following actions:
>   - Suspend the player from online play for some duration of time, or in extreme cases permanently
>   - Remove the player’s skin and replace it with a default skin.
>      - This action applies to any player using the same skin, and future players will not be able to select it.
>   - Suspend the player from online play until they change their username.
>      - No player will be allowed to use this name once it has been removed.


### Why was it implemented?

[Minecraft: Java Edition Player Reporting FAQ](https://help.minecraft.net/hc/en-us/articles/7317376541197) states the following:

> [...] We need to provide safeguards that will help keep all our players safe and welcome in the online environments where they play Minecraft. Player Reporting will help to keep Minecraft communities free from hate speech, bullying, harassment, sexual solicitation, and personal threats. We believe that human moderation and community guidelines are critical to reducing harmful behavior and promoting healthy Minecraft online communities. 

### Why is chat reporting controversial?

Because the current implementation of it is vaguely described, sustainability not guaranteed and ethics questionable. [Skin/username reports have different concerns - see here](#skin-and-username-reporting).

* **Banned from all multiplayer** - instead of getting punished on one server, you are getting punished on all, including Realms and others' LAN servers. Maybe you just got angry and swore at someone on one server and want to go to another to relax again? Nope, you can't do that.

* **Some swearing is interpreted too strictly** - some swear words are interpreted as bannable offenses even if the players know each other and know that the other party will not get offended by it. [Read more about one user's experience from this post](https://old.reddit.com/r/Minecraft/comments/xfh3ee/suspended_from_playing_minecraft_for_swearing_in/).

* **Realms chat is constantly monitored** - [according to Our Commitment to Player Safety](https://help.minecraft.net/hc/en-us/articles/8047895358605-Our-Commitment-to-Player-Safety#h_01G95X76WR1PM97XBXDE7G25KE), Mojang/Microsoft monitors all Realms chat and will take action regardless of whether you get reported and regardless of whether the other party actually took your message seriously or not. This was not possible before they introduced chat signing and global bans.

* **Realms subscriptions don't get cancelled** - if you get banned, Mojang will not automatically [pause the subscription](https://help.minecraft.net/hc/en-us/articles/4410000696077-Minecraft-Java-Edition-Realms-Billing-Issues-FAQ#h_01FGCST20673JYZ76PB9BN4BNK) of any Realms servers you own, meaning you'll continue to pay for server(s) you cannot access or control. This makes sense for short-term bans like up to a week, but any longer than that should give an explicit option at least.

* **Not sent to server admins** - sending reports to Mojang will result in different judgement and outcomes of the cases - while server admins could punish faster, with a shorter penalty, with different kinds of punishments like mutes and jails, Mojang can only ban people from the entirety of multiplayer or not punish at all.

* **Report reviewers lack context** - players can select 1-4 messages, to which the system will add up to 9 messages before the selected ones - at most 40 messages in total. That is a very partial context for serious offenses as it is missing player builds, signs, books, Discord/forum messages, daily general behavior etc. In other words, it assumes the player only offends another within one hour, not for a longer period.

* **Fairness doesn't scale** - Minecraft has a huge playerbase and if lots of players play it, lots can report each other as well. How can Mojang guarantee a _fair action_ to be taken on _thousands_ of reports every day? The investigators may accidentally overlook a part of the conversation or misintepret the intent due to words used. Compare that to a single server that has less players, therefore less reports and less admins needed, appeals that are dealt with faster.

* **Categories don't match server rules** - for example, there can be an adult-only server that may discuss things like world politics, alcohol and drugs freely, but when an underage player stumbles upon it, they can report others for things that are clearly allowed and intended by the server.
   
* **Categories are vague** - as of 1.20.2, the reason "I want to report them" was added, which implies that "being annoying" is also a possible cause of punishment.

* **Ban reasons and appeals are vague** - [while there is a way to appeal](#is-there-a-way-to-appeal-the-ban), it is not described when and how many times it will be accepted. The fact that _some_ bans are temporary is not really the solution - an unjust ban gives a bad impression of the game overall. [This issue has already been prevalent in Bedrock Edition.](https://youtu.be/kEfyaAq90kg?t=108)

* **Reports may not be sufficient** - in the case of most serious offenses (e.g. threatening, abuse, harassment), you should really feel that proper action is taken. With these reports, Mojang does not actually elaborate on [what their "appropriate actions" are](https://help.minecraft.net/hc/en-us/articles/7149823936781-Player-Reporting-in-Minecraft-Java-Edition#h_01GD13PG9R60SYNDV88FKFSHRH). They may send a player suicide prevention info for example, but there is no guarantee Mojang will contact the police for you. [Do it yourself!](#what-should-i-do-instead-when-someone-breaks-the-rules)

* **Servers can and do opt out** - most public servers, including Hypixel, have already opt out of the chat reporting system. Obviously the system cannot work if servers opt out. This is another reason for the game to [add clear indication](#what-does-this-modpack-do-for-me) about whether a server enabled the system or not, instead of making players assume it is everywhere (or even nowhere).

This is a non-exhaustive list. People have voiced more concerns in various Minecraft communities and the feedback site, search around.

### I already follow the server rules/am a nice person. Why should I care?

That is _exactly_ why you should. Previously, all you had to do was to follow the server's rules, so any actions you took were judged by the server administration.

Now, with this system, all your actions are now judged by _two_ parties: the server administration and Mojang's interpretation of [Community Standards](https://www.minecraft.net/en-us/community-standards).

Even if the server admins know your intent is positive/ethical/legal and have all the context to prove it, Mojang on the other hand has very limited context of what you _say_ and what you _meant_ by it.

### Can I be banned without anyone reporting me?

On Realms, yes. See [does Mojang monitor my chats](#does-mojang-monitor-my-chats).

On public servers, no. You can be banned by server admins throughout the same server or server network, but multiplayer-wide bans as described here must still be initiated by a player reporting another player's individual messages, [if the system is enabled on the server](#i-am-a-player-how-do-i-know-if-chat-reporting-is-enabled).

### Is there a way to appeal the ban?

Yes, if you [meet their criteria (see "how to submit an appeal...")](https://www.minecraft.net/en-us/community-standards#main-content:~:text=HOW%20TO%20SUBMIT%20AN%20APPEAL). It is unknown how many appeals are accepted.

1. [Open the Case Review request](https://help.minecraft.net/hc/en-us/requests/new?ticket_form_id=360003469452)
2. Select "Minecraft: Java" as the game.
3. Fill the form throughly with all information you have
4. Submit the form
5. Wait patiently for their response

If you own a Realm, you may want to [pause your subscription](https://help.minecraft.net/hc/en-us/articles/4410000696077-Minecraft-Java-Edition-Realms-Billing-Issues-FAQ#h_01FGCST20673JYZ76PB9BN4BNK) as well.

### What if I'm permanently banned?

Then you can only play singleplayer, not even LAN-worlds.

### How could Mojang improve the system?

In the best scenario, one of the following:

- Sending the reports to server admins instead of Mojang, as they have the most context to take the appropriate action
- Making the whole system opt-in (or out) as then only the servers that need this help would enable it
- Implementing the system only on Realms or other Mojang-partnering servers
- Not implementing the system at all because there are enough moderation tools built already

If core changes to the system will not be made, Mojang could still improve its communication about the feature in-game and on help pages:

- Make it clear that reports are sent to Mojang instead of server admins
- Add a clear, yet unobtrusive indicator that shows whether the system is in place or not for given server
  - Current vanilla indicators are small and per chat line which are easy to miss or unwillingly ignore; the warning toast is annoying and technically easy to disable.
- Be very clear and truthful about the system in help pages 
   - For example, Mojang repeatedly claims that [they do not monitor chat](https://help.minecraft.net/hc/en-us/articles/7317376541197) while [that is not actually the case in Realms](#does-mojang-monitor-my-chats).
- Use less cryptic terminology in errors related to the system
- Write a technical overview about the system's working so that users inclined would be able to read it from the official source

That said, credit where credit due: [several technical issues have been fixed since 1.19.3 already](#history-of-changes), which made the experience smoother for users who do not prefer the system.

This is a non-exhaustive list. People have posted more ideas in various Minecraft communities and the feedback site, search around.

### How does this affect Realms?

See [does Mojang monitor my chats](#does-mojang-monitor-my-chats).

### Was player reporting possible at all before 1.19.1?

Yes, [Mojang has had a web form for it](https://help.minecraft.net/hc/en-us/requests/new?ticket_form_id=4416074743565), that still exists.

But it wasn't really an issue in the same way, because:

- few people knew about it (higher chances of actual reports instead of jokes/bullying)
- chat messages were not verifiable to be sent by the username next to them
- ban system itself did not exist

Therefore, it is unknown, how chat reports in the form were or are handled. Usernames and skins were/are probably handled [as in the newly introduced system](#skin-and-username-reporting).

### Where can I learn more about it?

#### Explanatory videos

- [Explanation as of 1.19.3 by Aizistral](https://youtu.be/48H5nMQ_8Yg?t=79) (~7 min)
- [_Written_ technical explanation as of 1.19.3 by Aizistral](https://gist.github.com/Aizistral/61553d6d76b998da9a52afd49c9ead76#the-absolute-state-of-chat-reporting) (~33 min)
- [Explanation as of 1.19.2 by AntVenom](https://youtu.be/IKgucpgVraY) (~20 min)
- [Explanation as of 1.19.1-rc.1 by FitMC](https://youtu.be/rdoFUhd0EkI) (~10 min)
- [Timeline of events as of 1.19.1-rc.1 by TheMisterEpic](https://youtu.be/kEfyaAq90kg) (~14 min)
- [Technical explanation as of 1.19.2 by Aizistral](https://youtu.be/DobmW1ZUcbQ?t=10) (~48 min)
- [Clearing some misconceptions for 1.19.2 by Aizistral](https://youtu.be/bF_37BrWBSM?t=87) (~22 min)
   
All videos are suitable for describing the interactions and ethical concerns, but for technical details only videos about 1.19.3 and later versions are still relevant. Aizistral is the developer of [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports).

#### Official posts

- [Help page](https://help.minecraft.net/hc/en-us/articles/7149823936781-Player-Reporting-in-Minecraft-Java-Edition)
- [FAQ](https://help.minecraft.net/hc/en-us/articles/7317376541197)
- [Why have I been banned FAQ](https://help.minecraft.net/hc/en-us/articles/4408964729869-Why-Have-I-Been-Banned-from-Minecraft-)
- [Our Commitment to Player Safety](https://help.minecraft.net/hc/en-us/articles/8047895358605-Our-Commitment-to-Player-Safety)
- [Community Standards](https://www.minecraft.net/en-us/community-standards)
- [How to report a player](https://help.minecraft.net/hc/en-us/articles/13019118732429#:~:text=MINECRAFT:%20JAVA)

### History of changes

- **2021 or earlier** Minecraft adds a [player reporting form](https://help.minecraft.net/hc/en-us/requests/new?ticket_form_id=4416074743565) to its website.
- **1.19**
   - [22w17a](https://minecraft.wiki/w/Java_Edition_22w17a#Gameplay) introduced the concept of signed messages, which is a verification method that ensures each message was sent by that user and not the server. It also added a toggle for servers to prevent entering players who did not sign theirs, though the option was disabled by default.
   - [22w18a](https://minecraft.wiki/w/Java_Edition_22w18a#General) started signing the messages sent by `/say`, `/msg`, `/teammsg`, and `/me`.
   - [22w19a](https://minecraft.wiki/w/Java_Edition_22w19a#General) added an option for players to hide messages by other players who did not sign their messages.
   - Some snapshot also introduced a way to modify chat messages by filtering words, [presumably for Realms](#does-java-edition-have-a-profanity-filter).
- **1.19.1**
   - [22w24a](https://minecraft.wiki/w/Java_Edition_22w24a#General) introduced the chat reporting interface.
   - [1.19.1-pre.1](https://minecraft.wiki/w/Java_Edition_1.19.1_Pre-release_1#General) introduced account-wide bans.
   - [1.19.1-rc.1](https://minecraft.wiki/w/Java_Edition_1.19.1_Release_Candidate_1) removed the "Extreme violence or gore", "Nudity or pornography", and "Profanity" categories. It was also Mojang's initial "final" plan of how the reporting system would work. Due to major exploits found by the community though, the release of 1.19.1 was postponed by a month.
   - [1.19.1-pre.2](https://minecraft.wiki/w/Java_Edition_1.19.1_Pre-release_2#General) introduced red bars and `(!)` indicators on unsigned messages, yellow bars and `(?)` indicators on "modified" messages. It also made the system enabled on new servers by default.
   - [1.19.1-pre.3](https://minecraft.wiki/w/Java_Edition_1.19.1_Pre-release_3#General_2) introduced gray indicators for system messages.
   - [1.19.1-pre.4](https://minecraft.wiki/w/Java_Edition_1.19.1_Pre-release_4#General) fixed an exploit where players could add new messages to a report that weren't there previously. It also introduced the concept of deleted messages, where the server can remove any message from the client.
   - [1.19.1-rc.2](https://minecraft.wiki/w/Java_Edition_1.19.1_Release_Candidate_2#General) introduced a warning toast to players entering a server where the server does not restrict the joining of non-signing users. Practically, this toast mostly affected vanilla and vanilla-like servers, as other servers quickly found a way to remove it.
 - **[1.19.2](https://minecraft.wiki/w/Java_Edition_1.19.2#Fixes)** fixed an exploit where some players could kick everyone else by abusing chat signing features.
 - **1.19.3**
    - [22w42a](https://minecraft.wiki/w/Java_Edition_22w42a#Gameplay) did the following:
        - removed red `(!)` indicators on unsigned messages and made the bar gray
        - on modified messages the `(?)` indicator is now gray and the icon is no longer displayed if only the style was changed
        - deleted messages are now displayed for 3 seconds and are replaced by a system message
        - players are now able to join all servers and use most commands (except any message-related commands) even if they don't sign their chat.
   - [22w43a](https://minecraft.wiki/w/Java_Edition_22w43a#General) introduced chat report drafts.
- **1.19.4**
   - [23w03a](https://minecraft.wiki/w/Java_Edition_23w03a#General_2) made clients attempt to start signing their messages on server join, if it didn't happen on client start.
   - [1.19.4-pre.4](https://minecraft.wiki/w/Java_Edition_1.19.4_Pre-release_4#Fixes) fixed a bug where the user could get kicked due to signing requirement after changing their chat settings.
- **2023-08-02** [Minecraft changed its EULA](https://www.minecraft.net/en-us/article/minecraft-eula-and-commercial-usage-guidelines-updates) and created a new page called [Minecraft Usage Guidelines](https://www.minecraft.net/en-us/usage-guidelines). Among other things it states: 
   - > Regardless of how you choose to make money to support your server, you may only do so if: 
     > [...] You don’t hide or alter any of the dialogs or prompts that are part of Minecraft (this includes the End User License Agreement (EULA), warning messages, and error messages)"
      - To comply with that, No Chat Reports [no longer allows hiding "messages cannot be verified" toast serverside](https://github.com/Aizistral-Studios/No-Chat-Reports/blob/118eff66e6da2ea5507f568d7ade8741434005b3/docs/CHANGELOG.md#build-1202-v230).
      - As of 2023-09-28, other servers and plugins are likely not aware of the change, as even Hypixel still hides the toast.
- **1.20.2**
   - [23w32a](https://minecraft.wiki/w/Java_Edition_23w32a) made clients no longer disconnect when receiving invalid chat messages, instead a placeholder message will be shown in chat.
   - [23w33a](https://minecraft.wiki/w/Java_Edition_23w33a) added [skin and username reporting](#skin-and-username-reporting), removed "impersonation" as a report category and added "generic" report category.
- **2023-11-07** - [Mojang announced the Official Minecraft Server List](https://www.minecraft.net/en-us/article/the-official-minecraft-server-list-live), which features [the "Beacon of Safety badge"](https://findmcserver.com/parents#features) that requires the server to have chat reporting, profanity filter and a manual review by the site's admins. No Java Edition servers have the badge yet.
- **[1.21.5-pre2](https://minecraft.wiki/w/Java_Edition_1.21.5_Pre-Release_1#General)** - implemented some changes for clientside exploit prevention (against servers sending messages with incorrect timestamps)

_See also: Minecraft Wiki's history sections for [Social Interactions](https://minecraft.wiki/w/Social_interactions#History) and [Chat](https://minecraft.wiki/w/Chat#History)._

## Chat reporting and Fabulously Optimized

### What does this modpack do for me?

Fabulously Optimized includes [(why?)](#why-does-fabulously-optimized-take-a-stance-on-the-matter):
- A mod called [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports) that:
   - adds new consistent chat indicators
   - disables inconsistent vanilla chat indicators and the annoying toast
   - disables chat signing on servers that state they do not want it
   - provides optional features for users who want to configure their experience
- A resource pack called [Chat Reporting Helper](https://www.curseforge.com/minecraft/texture-packs/chat-reporting-helper) that:
   - makes No Chat Reports icons more neutral
   - improves vanilla and No Chat Reports tooltips to be shorter, clearer and unbiased
  
In order to get the status of the server, open the chat box (press `T`) and look at the right bottom corner:

- ![police badge with a question mark icon](https://i.ibb.co/Yb1n6fW/unknown.png) - status not yet known, you must send one chat message to get it
- ![grayed out police badge with a line through it icon](https://i.ibb.co/QDFzXCT/secure.png) - no chat messages can be reported to Mojang
- ![outlined police badge icon](https://i.ibb.co/hstcjW7/neutral.png) - most chat messages can be reported to Mojang, but the server does not prefer it and the playing user opts out
   - In some cases, no messages can be reported but that is not reflected on the icon. You can confirm by seeing if you can report anyone on Social Interactions.  
- ![blue police badge with gold star icon](https://i.ibb.co/2YgMHpR/insecure.png) - all chat messages can be reported to Mojang
- ![blue police badge with red recording dot icon](https://i.ibb.co/gTxw84X/realms.png) - only on Realms: all chat messages can be reported to Mojang and [Mojang is passively monitoring the chat for violations](#does-mojang-monitor-my-chats)

_(Expected different icons? Disable Chat Reporting Helper resource pack and [see No Chat Reports wiki.](https://github.com/Aizistral-Studios/No-Chat-Reports/wiki/Configuration-Files#option-showserversafety))_

The behaviour can be configured per-server, hover on the icon for more details.

### I don't want to join such servers at all!

If you don't think the ![enabled](https://i.ibb.co/2YgMHpR/insecure.png) icon is enough, you can also be prompted before sending a signed message or block sending all signed messages altogether (on such servers, you can only use commands then).

1. Click Mods
2. Search for "No Chat Reports" and click ![config](https://i.ibb.co/j35cBtn/image.png)
3. Set "Default signing mode" to `Prompt` or `Never`
4. `Save changes`

The behaviour can also be configured per-server, hover on the status icon (bottom right corner of the chatbox) for more details.

### I can't chat in my server!

Some poorly configured servers require chat reportability, but fail to communicate it in a standard way. Then you may see vague messages like "Please relog to chat" or "Please disable mods to chat". 

Actually, all you have to do is:

1. Click ![optional](https://i.ibb.co/hstcjW7/neutral.png) 2 times until it says "Signing mode: **Always**"
2. Say something
3. Your message went through and you'll see the ![enabled](https://i.ibb.co/2YgMHpR/insecure.png) icon
4. Optionally: [report the server IP to Fabulously Optimized](https://fabulously-optimized.github.io/discord), so that it can be fixed for everyone

### Is No Chat Reports itself a risk?

No. The mod disables chat signing on servers that explicitly tell the clients "chat reportability is not required here!". In servers that enforce the system, chat signing will work as it does in vanilla.

### I think chat reporting is fair.

Understandable. If you join a server and see a ![enabled](https://i.ibb.co/2YgMHpR/insecure.png) in the bottom right corner of the chat, that server enforces the report system and the modpack will adhere to it, just like vanilla. 

In vanilla itself there is no such clear indication as the toast and chat line icons do not accurately work on every server, hence the mod.

### Why does Fabulously Optimized take a stance on the matter?

Fabulously Optimized is not "just a performance pack" or an "OptiFine clone". While these are its core priorities, indeed, the priorities also include [the community itself, privacy and transparency](principles.md).

When the system was first visibly introduced in 22w24a, [the players were clearly upset](https://old.reddit.com/r/Minecraft/comments/vcz7ou/this_is_getting_out_of_hand_now_there_are_two/). Not only was there zero prior communication about the system - [except the introduction of chat signing](#history-of-changes), which most users didn't think much of at the time - but also within said snapshot and [the next one](#history-of-changes) (supposedly "the last one before 1.19.1") Mojang did not communicate with the users. Not via QnA, no tweets, no help pages. There were practical exploits and ethical concerns which stayed unanswered. [1.19.1-rc.1 removed 3 of the most concerning report categories](#history-of-changes), but still did not communicate with users.

Then they took a step back. Postponed the release by a month to rework the system internally, [made it visually more annoying than before](#history-of-changes) and eventually released 1.19.1. After that, Mojang started working on some help pages to explain the feature in fuller detail. Due to aforementioned concerns and players spreading misinformation, this modpack received a FAQ (which you're reading now) to explain the system as it actually is, while taking a very protective stance in-game. [Step by step](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/376), while discussing with the players and learning more about the feature, Fabulously Optimized changed its stance from "protective" towards "unobtrusive".

After the release of FO 4.2.0 (MC 1.19.2), there were more discussions about the feature, with [users requesting even more neutrality](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/497) from the modpack. By discussing and evaluating the pain points of chat reporting and [Mojang's positive improvements made in 1.19.3](#history-of-changes), a solution was found - [neutral texts and icons](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/499). The resource pack [was released in FO 4.6.0](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/CHANGELOG.md#460-2023-03-24) and separately distributed as of [FO 4.9.0](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/CHANGELOG.md#490-2023-05-02).

As of Minecraft 1.21.5, Mojang has still not fully [fixed the issues](#why-is-it-controversial) or [the communication](#how-could-mojang-improve-the-system). 
Therefore, Fabulously Optimized cannot fulfill the [principles of being transparent and prioritizing its users](principles.md) without also giving them [clear indicators](#what-does-this-modpack-do-for-me), honest phrasing and customizable options so that users could make their own decisions about the new feature. It is very important that every user is aware of the system's existence, where and how it works, because it doesn't work everywhere, nor does it align with users' previous expectations of chat in general. At the same time, it is important to reiterate that neither the mod or the resourcepack will actually break any rules or prevent users from reporting if the server prefers it. 

If Mojang will improve their communication or overhaul the system again, it is possible that both the mod and resource pack will be removed from the modpack.

_See also: [why does this article exist](#what-is-the-intent-of-this-article) and [history of chat reporting](#history-of-changes)_

## Protection, awareness, alternatives to chat reporting

### What should I do instead when someone breaks the rules?

Do what you always did.

- If an user is being annoying, hide their messages by clicking the chat icon near the username in Social Interactions or, in some servers, `/ignore (username)`.
- If an user has broken the rules of the server, report it to server administration. This is usually done by `/report`, `/helpop`, server forum or Discord.
- If an user is talking about commiting suicide, talk to them and [give local help resources](https://en.wikipedia.org/wiki/List_of_suicide_crisis_lines). 
- If an user is doing or threatening illegal actions, report it to server admins and local police. Provide them with as much context as possible, including screenshots.

### I am a player. How do I know if chat reporting is enabled?

* If you're using Fabulously Optimized or No Chat Reports with Chat Reporting Helper, [click here.](#what-does-this-modpack-do-for-me)
* If you're using just No Chat Reports, [click here.](https://github.com/Aizistral-Studios/No-Chat-Reports/wiki/Configuration-Files#option-showserversafety)
* If you the server is very popular, you may find it on the [Official Minecraft Server List](https://findmcserver.com/). In there, look for the existence of the light blue [Beacon of Safety badge](https://findmcserver.com/badges-explained).

<details>
<summary>If you're not using No Chat Reports or using vanilla client, click here</summary>

In vanilla (1.20.2), there are also ways to determine whether chat reportability is enabled in a given server, but it requires paying attention to small clues:

* Are you able to join the server with 1.18.2 or older client? If yes, then chat reporting is disabled.
* When you type something in the chat or as a private message, do you see a gray bar on the left? If yes, then chat reporting is disabled.
   * Remember to only look at _chat messages_. System messages always have the gray bar.
* When someone else types something, press `P` ([Social interactions](https://minecraft.wiki/w/Social_interactions)). Can you report that player's chat? If not, that player or server has disabled chat reporting.
* When you joined the server, did you see this toast on top right corner? If yes, chat reporting may be disabled on the server, or players could use a mod like No Chat Reports to disable it for themselves.
   * ![](https://user-images.githubusercontent.com/47505981/183680550-d9bc58f3-f93f-4ee6-bd34-d2879bdfb96a.png)

</details>

### I am a server owner. How can I protect my users?

See [server setup](server-setup.md#how-to-protect-your-users). If you are a player, you can send that page to your server admins.

### Should I/my server stay on 1.19?

No.

- [The modpack tells you clearly where chat reporting exists and where it doesn't](#what-does-this-modpack-do-for-me)
   - [It is easy for server owners to disable chat reporting](#i-am-a-server-owner.-how-can-i-protect-my-users)
- Most mods are not interested in continuing to support it
- No Chat Reports is limited and outdated on 1.19, so you cannot join all servers
- It is buggy, [1.19.1 fixed several bugs and crashes](https://minecraft.wiki/w/Java_Edition_1.19.1#Fixes)
- If you want to keep using it just for the sake of protest, remember that [1.19 already has the basis for chat reporting - the chat signatures](#history-of-changes).

If you want to stay on an older version, please use the latest version of Fabulously Optimized for 1.18.2.

_This section previously claimed that it may be possible for 1.19.1+ players to report 1.19 ones. This turned out to not be the case because [the signing system changed in 1.19.1](https://youtu.be/DobmW1ZUcbQ?t=681)._

### Should I/my server stay on 1.18.2?

Maybe. It is safe from reports, you are free to play it for as long as you like. However, due to the [wide availability of serverside and clientside mods](#i-am-a-server-owner.-how-can-i-protect-my-users), there is no practical reason to _not_ update.

### Should I disable online-mode on my server?

No. While that does disable chat reporting, it makes your server vulnerable in a lot of other ways, and is not allowed by [Minecraft Usage Guidelines](https://www.minecraft.net/en-us/usage-guidelines).

### Can I break the system/avoid getting reported?

No. It is up to the server to decide whether they want the reporting system or not, use that information to choose the servers you play in. Using exploits to break the system clientside may lead to a ban and is not endorsed here.

### Are there alternative ways to chat?

Yes, usually the simplest option is using any kind of voice chat, for example on Discord. [More alternatives are described here.](https://github.com/Aizistral-Studios/No-Chat-Reports/wiki/To-Encrypt-or-Not-to-Encrypt#alternatives)

### I want to give feedback to Mojang.

Great! Use the [official feedback site](https://feedback.minecraft.net/hc/en-us):
* [Give feedback on the chat reporting](https://feedback.minecraft.net/hc/en-us/community/posts/7320990094733-Player-Chat-Reporting-Feedback-)
* [The most popular request for reverting chat reporting](https://feedback.minecraft.net/hc/en-us/community/posts/6977558665997-Mojang-please-for-the-love-of-your-game-don-t-add-a-chat-report-feature-)

## Skin and username reporting

### What is skin and username reporting?

From 1.20.2, it is possible to report players' usernames and skins, besides chat. Therefore, the user can now click the report button on all players' names in Social Interactions, and must choose the category to report for - chat, username or skin.

### Is it bad?

Yes and no.

#### Good

- Skins and usernames are public data that represent you across all servers, launchers, profiles. They affect your (and to an extent, Mojang's) public reputation, so certain limits make sense.
- Usernames were already dealt with proactively, meaning you couldn't choose most of the offensive ones anyway. 
- Several servers ban users for offensive usernames and skins, so knowing whether a skin/username is bad beforehand can prevent you from getting banned in the servers.

#### Bad

- It limits user creativity and contextual jokes, if the player wanted to make a joke in one server/context only.
- Words that are offensive in English but not in a different language may still be punished/prevented.
- Multiple strikes on an account may accumulate to a ban from all multiplayer servers.
- In 2025 there have already been [two](https://old.reddit.com/r/Technoblade/comments/1iamhgb/comment/m9h3bsj/) [cases](https://old.reddit.com/r/Minecraft/comments/1juxfi6/so_apparently_this_skin_is_inappropriate/) of unexplained skin bans.

### Are all users' skins/usernames reportable?

On online-mode servers, yes. 

On offline-mode servers, it is not certain yet - it may be possible to report but due to technical differences the reports will likely not get acted on.

### What happens when I'm punished?

For the first few offenses, not much. 

- If your skin was the offense, it will be reset to default and can already continue to play on multiplayer. You can also change the skin again (to a different one).
- If your username was the offense, you will get unbanned from multiplayer as soon as you change your username.

If you have repeated offenses, you will get a permanent ban from all multiplayer servers.

### Can I appeal a punishment?

Yes, [you can do it with those instructions.](#is-there-a-way-to-appeal-the-ban)

### Can I still use a banned skin/username?

No. Trying to circumvent the ban will likely get you caught again and with several strikes, you'll be banned from multiplayer permanently.

### Can reports/bans be prevented server-side?

Yes. Servers could use nickname or skin changing plugins, which everyone will see but cannot report (as the report will show the original name/skin). 

Do your own research if interested.

### Can reports/bans be prevented client-side?

Partially. Clients could use custom cosmetic and title/pronoun mods to avoid using Mojang's servers in the first place. 

However, other players _will_ need the same mods to see them, and the mods probably have certain rules/reporting features of their own. Do your own research if interested.

## Related questions

### Does Java Edition have a profanity filter?

Yes, but currently only on Realms chat. If you are an adult, you can disable it for yourself [in your minecraft.net profile](https://www.minecraft.net/en-us/msaprofile/accountsettings). [Learn more](https://help.minecraft.net/hc/en-us/articles/6160517019149)

Profanity by itself is no longer a category one can report other players for. **Swearing at friends, even jokingly, is bannable though** - read the next section for more info. 

Bedrock Edition has the filter on chat, signs, item names, books etc. across all servers and content, including singleplayer.

### Does Mojang monitor my chats?

Yes, but only on [Realms](https://support.xbox.com/en-US/help/games-apps/game-titles/minecraft-realms-overview) (Java and Bedrock) and [Featured Servers](https://web.archive.org/web/20230610202006/https://help.minecraft.net/hc/en-us/articles/4408873961869-Minecraft-Dedicated-and-Featured-Servers-FAQ-) (only Bedrock).

[Our Commitment to Player Safety](https://help.minecraft.net/hc/en-us/articles/8047895358605-Our-Commitment-to-Player-Safety#h_01G95X6ZSKYQ6SGC8D6AB7XCNB) says

> For Bedrock and Java Realms as well as partnered Bedrock servers, we leverage an automated proactive chat filtering system.
> 
> We use it to classify, filter, and escalate online harms for human review and moderation to promote safe and welcoming interactions on Minecraft games. That includes behaviors such as harassment, abuse, and hate speech.

Similarly, the [why have I been banned FAQ](https://help.minecraft.net/hc/en-us/articles/4408964729869-Why-Have-I-Been-Banned-from-Minecraft-) says

> Specifically, our highly trained moderation staff is looking at the most egregious violations in public Featured Servers and Realms [...]

Consider using [alternative chat methods instead.](#are-there-alternative-ways-to-chat).

Though, it is worth pointing out that _monitoring_ and "automated proactive chat filtering" in this case likely refers to automatic reports triggered by specific keywords used, not that there is a person or team specifically looking at your messages.

### Does Bedrock Edition also have player reporting?

[Yes, it does.](https://help.minecraft.net/hc/en-us/articles/13019118732429) It is unknown if there is any way to prevent chat reporting there.

### How many servers actually have chat reporting?

**Update: [Mojang released an official server list](https://findmcserver.com/parents#features), which indicates chat reporting with a "Beacon of Safety badge". As of Feb 2025, no Java Edition servers have the badge yet.**

There is no easy way to get this statistic, as it is only obtainable once the player has sent the first message, and the server can change its stance at any time.

However, what we do know:

* Any server that allows 1.18.2 or older clients to enter cannot have chat reporting. Yes, that includes Hypixel and many other minigame servers.
* Any server that allows versions between 1.19-1.19.2 and/or 1.19.2-1.19.3 to join _cannot_ have chat reporting. This is because these versions have different implementations of chat signing/reporting, and as such they cannot coexist.
* [There are many plugins and ways to disable chat reporting](server-setup.md#chat-reporting), and these are popular among server owners.
* Any vanilla server from 1.19 and up enables chat reporting by default, but may or may not allow players to disable it for themselves.
* Cracked servers cannot have chat reporting.
* Realms always has chat reporting.

Public server listings usually only list the latest version a player can join with, not all versions, so even the 1.19.3+ server count is hard to determine.

### I have more questions.

Write to `#support` [in our Discord](https://download.fo/discord).

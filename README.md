# RYMPLAYLISTS

## Promotion
Anytime I say rateyourmusic or RYM, I am talking about https://rateyourmusic.com/,
the website used to make these playlists possible. Their charts are super
powerful, and they have the largest database of music ratings/reviews 
(as far as I know). Check it out! It's a super cool music review website. 
And check me out while you're there, https://rateyourmusic.com/~Caelohm

## TL;DR
Using rateyourmusic's charts, I have created a systematic way of making Spotify
playlists that try to introduce the most popular songs from the most popular artists 
within every genre of rateyourmusic. I have set limitations on the number of albums 
added to save some time and set rating caps for the popularity charts. Each song on 
every playlist represents an album in the charts, it's position in popularity, and the 
most popular song of that album. The playlists are located on my Spotify profile
under the folder Rateyourmusic Genres 2021. link to my 
[Spotify](https://open.spotify.com/user/226ny2ikdvr7wi2lq62guxtfy?si=9ded19b0b7ec4267).

## Albums I Couldn't Find
Text files in the genre folders **WITHOUT** " Missing" are the inital copy/paste 
from the rateyourmusic charts webpage. Text files **WITH** " Missing" are albums that 
could not be found on Spotify. Sometimes Spotify albums are only available in 
certain regions, I based everything off of the albums available in the US. They 
may still be available on other streaming platforms, I just checked Spotify.

See rateyourmusic, they have links to streaming sources on album
pages and charts. All else fails, you can try to aquire the audio files by
some other means or look it up on Youtube.

**WHEN YOU LIKE A PLAYLIST, IT IS HIGHLY RECOMMENDED TO CHECK THE " MISSING" ALBUM 
TEXT FILE OR THE RATEYOURMUSIC CHARTS FOR THE SPECIFIC SUB-GENRE.**

## Methodology/Creation of the Playlists
The charts used for the playlists are in order of popularity.
There is a serious debate to be had on what chart to use for the genres.
Live and Archived albums are included, but I am thinking of getting rid of them. If 
number 50 on the first page of the most popular albums for a subgenre does not have 
greater than 100 ratings, I skip making that subgenre playlist. This is to prevent 
making playlists that are extremely short with only 20 songs that meet 100 ratings 
(for example).

The album average rating cap and number of ratings cap is based on 
personal preference. For example, in the Comedy Rap sub-genre, albums are rated 
very poorly from the beginning, so it has an album rating cap of 2/5.

Usually I will set a low number of ratings cap if it will add a couple hundred 
songs to a short playlist. Vice versa, I will probably set a high number of ratings 
cap if I feel the playlist will be too long otherwise. Usually it is hard for me to 
set a high cap because to me, ideally, every album above 100 ratings should be on 
a playlist. If I had other people working on this with me, maybe that would be more
feasible. I am also interested in making these types of playlist for year ranges, like
1970 - 1974, 1975 - 1979 playlists.

Each song on **EVERY** playlist represents an album's most played song. If 
a song stands out like a sore thumb in juxiposition to the rest of the songs in 
a playlist, I may change the song from the album or remove that song entirely. 
I will remove the song if I feel it is improperly categorized in a sub-genre.
This usually happens when an album has < 100 ratings. The song will not always 
be a good representation of the album.

So **CHECK OUT THE ALBUM IF YOU LIKE A SONG!**

## Python Code
The python code in this repository titled "rym_scrape.py" helps search for a large 
quantity of albums on Spotify by using a copy of the text from the rateyourmusic charts 
and parsing it. It also writes missing albums to the " Missing" text files. I wrote it
in it's entirity, although it may go through new iterations as time goes on.

## Annoying Issues
Keep in mind, some albums often add extra songs to the album (deluxe 
version, extended version, 20th Anniversary edition, UK vs. US release, etc.) 
or maybe some songs are missing, or maybe the song order is all wrong, or maybe 
the whole album is one song! Sometimes this issues arise without any warning! 
		
Welcome to hell.

The reason this is annoying is because people often put on an album 
and leave it playing. Usually you expect an album to stop playing when it is 
officially over, but then the song quality drops drastically as you enter a 
bonus track or demo version on the tail end. **CAN'T ARTISTS JUST MAKE UP THEIR 
MIND ABOUT WHAT THEY WANT ON AN ALBUM BEFORE RELEASE??? IF YOU WANT TO ADD 
EXTRA MATERIAL, PUT IT ON A DIFFERENT ALBUM OR COLLECTION FOR THE HARDCORE FANS. 
JESUS.
IF THIS HAPPENS BECAUSE OF SOME CORPORATE MANIPULATION, FUCK YOU RECORD LABEL OR
WHOEVER APPROVES THIS SHIT.**

Often reviewers do a good job of setting an official tracklist for an album. 
I tried my best to avoid annoying album versions, but if you stumble upon a
weird album version that I added, look it up on rateyourmusic and look at the "track
listing". Often the deluxe version is the only version available. smh.

## Message Me
Please **MESSAGE ME** on [Reddit](https://www.reddit.com/user/Caelohm) when you believe 
something in the playlist is wrong based on the rules I have set to make them. Do keep 
in mind, when new albums are released, they will not be put into these playlists. The 
only time I will add more albums is when I redo these playlists. If you want to know 
why, ask me on reddit.

Some potential places it is very possible I fucked up:
1. Missing a sub-genre. 
There are a lot of subgenres and one me.

1. Missing an album on Spotify. 
Sometimes, it is really hard to find an album on
Spotify. I am disincentivized to spend time looking for albums because it takes
longer to complete the playlist. The easiest way for me to find an album when 
I can't find it searching the album and artist is through rateyourmusic's 
streaming links on album pages, or by looking at an artist page scrolling 
through their albums in Spotify. So, If you find some album that doesn't have a 
streaming link on rateyourmusic, PLEASE add it by copying the share link and putting it 
on the album page. You can find the albums I wanted to add but couldn't find in
the " Missing" text files.

1. Adding the wrong "most popular" song for an album. 
This is the least likely of all of these, but it can still happen because humans are 
imperfect. I would automate the process of finding the most popular song off an album 
believe me, but it is not possible with the current state of Spotify's API, and is more 
complicated than it seems.

1. Adding two of the same songs on one playlist. 
I try not to have two songs that are the same. Sometimes I make an exception (if it's 
the same song but has some serious differences). This rule applies to the classical 
playlists and every playlist when the song is the same but the artist isn't. I keep 
picking the next most popular song on an album if a song overlaps, even when there are 
multiple overlapping songs.


## FAQ:

	WHY NOT APPLE MUSIC?

Apple Music's Windows Desktop app is very outdated and annoying to use.
The automation I used to make these playlists would need to be reworked to search
in Apple Music. I don't have an apple computer to use Apple Music. I personally am
switching off of it because Spotify, for the most part, has everything I want. It
used to be debatable which was better but since the new update, in my opinion, 
Spotify is better hands down. Also, these playlist would've taken 2x longer.

	WHY IS THERE A LIMITATION OF ONE SONG PER ALUBM?

Because people have lives to live. I'm pretty sure people would rather 
listen to a 200 song playlist rather than a 400 song playlist (2 songs per album).
Also, the more songs added, the longer it takes to make the playlist. Personally, 
I would rather go to an album rather than have songs in a playlist. The more 
songs I add from an album, the closer the playlist is to just listening to the album. 
Yes, there are songs that are literally an entire album on the playlist, but that's is 
a small minority of the songs. I would rather include an album with one song than exclude it.

The point of these playlists is to make it easier to find new artists. If 
I had two songs per album, you would at some point listen to the same artist twice.
That's overexposure and counterproductive when trying to find new artists because 
most of the time, two songs on one album will give you the same vibe that the album 
inhabits. If we really want it to be equal, lets set a certain time each album is 
allowed to be represented on the playlist. Ok, now I have to add up songs on each 
album to make sure I don't add too many and go over the playtime per album. 

You see how this is getting complicated? The more complicated, the longer it takes. 
One song works in my opinion and I stuck to it. 
I listen to the playlists more than anyone and have been making these sorts of
playlists since 2018, take my word for it. 

I know what you're thinking, *but what if a song that's picked is the one song 
I don't like on that album?*

Ok, if you are really that concerned that the songs you don't like could have gems on 
the album, be my guest, listen to the album even when you hate the most popular song. 
Yes, you will find gems. That's the point, to compile a list of very popular albums that 
other people enjoy for you. When you don't like a song, just take it with a grain of 
salt.

Sorry if ^^this^^ sounds condescending, I get a little sassy when someone questions 
something I'm so passionate about and have been working on for months. If you're reading this, 
!!THANK YOU!! for reading, I know most people won't read this. :D

If you have any other questions, feel free to message me on 
[Reddit](https://www.reddit.com/user/Caelohm) !!!


RYM hire me plz ｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡ lmao jk gotta finish my degree

## MTSA: 

```
===================================================
        ../../Dataset-MTSA/tweets_50-50.csv
===================================================

Model: "model"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to
==================================================================================================
input_1 (InputLayer)            [(None, 64)]         0
__________________________________________________________________________________________________
embedding (Embedding)           (None, 64, 300)      2250000     input_1[0][0]
__________________________________________________________________________________________________
bidirectional (Bidirectional)   (None, 64, 64)       85248       embedding[0][0]
__________________________________________________________________________________________________
conv1d (Conv1D)                 (None, 62, 16)       14416       embedding[0][0]
__________________________________________________________________________________________________
conv1d_1 (Conv1D)               (None, 61, 16)       19216       embedding[0][0]
__________________________________________________________________________________________________
conv1d_2 (Conv1D)               (None, 60, 16)       24016       embedding[0][0]
__________________________________________________________________________________________________
dropout (Dropout)               (None, 64, 64)       0           bidirectional[0][0]
__________________________________________________________________________________________________
global_max_pooling1d (GlobalMax (None, 16)           0           conv1d[0][0]
__________________________________________________________________________________________________
global_max_pooling1d_1 (GlobalM (None, 16)           0           conv1d_1[0][0]
__________________________________________________________________________________________________
global_max_pooling1d_2 (GlobalM (None, 16)           0           conv1d_2[0][0]
__________________________________________________________________________________________________
bidirectional_1 (Bidirectional) (None, 64)           24832       dropout[0][0]
__________________________________________________________________________________________________
concatenate (Concatenate)       (None, 112)          0           global_max_pooling1d[0][0]
                                                                 global_max_pooling1d_1[0][0]
                                                                 global_max_pooling1d_2[0][0]
                                                                 bidirectional_1[0][0]
__________________________________________________________________________________________________
dropout_1 (Dropout)             (None, 112)          0           concatenate[0][0]
__________________________________________________________________________________________________
dense (Dense)                   (None, 1)            113         dropout_1[0][0]
==================================================================================================
Total params: 2,417,841
Trainable params: 2,417,841
Non-trainable params: 0
__________________________________________________________________________________________________

Scores on test:
1202/1202 [==============================] - 1s 1ms/sample - loss: 0.5932 - acc: 0.6855 - rec: 0.4388 - prec: 0.8612 - f1: 0.5686
[0.5931774951058894, 0.6855241, 0.43879008, 0.86115867, 0.5686226]

Scores on no proc test:
1202/1202 [==============================] - 1s 936us/sample - loss: 0.5995 - acc: 0.6947 - rec: 0.4589 - prec: 0.8566 - f1: 0.5862
[0.5994769560913873, 0.69467556, 0.45890546, 0.85658044, 0.58623904]


y_pred
------
-> POS 0 -> 1 true - (0.092):
         b'I miss football :('
-> POS 0 -> 0 true - (0.060):
         b'The new Thor movie is very good! Loki is still my favorite lol \xf0\x9f\x98\x82'
-> POS 0 -> 0 true - (0.037):
         b"But I don't have a iphone x"
-> POS 0 -> 0 true - (0.039):
         b'This iPhone X is amazing lol'
-> POS 0 -> 0 true - (0.077):
         b'@prataemin did u pour the cereal already?\xf0\x9f\x98\x94\xf0\x9f\x98\x94'
-> NEG 1 -> 1 true - (0.904):
          b'Watched a video on Facebook about pork... that shit just turnt me off\xf0\x9f\xa4\xa2\xf0\x9f\xa4\xae'
-> POS 0 -> 0 true - (0.084):
         b'Okay I love Chance the Rapper.'
-> NEG 1 -> 1 true - (0.968):
          b'I bought an android, but I\xe2\x80\x99m not THAT stupid'
-> NEG 1 -> 1 true - (0.940):
          b'Amazon tickets is fucking mint'
-> POS 0 -> 0 true - (0.078):
         b'finally watching the defenders so i can watch the punisher this week'
-> POS 0 -> 0 true - (0.055):
         b'@NHL united states has the best neighbors in the world.   Thanks,  Canada'
-> POS 0 -> 0 true - (0.031):
         b'@JohnLegere If you give me an iPhone X I\xe2\x80\x99ll switch to T-Mobile'
-> POS 0 -> 0 true - (0.066):
         b'@br_CBB hard watching these college basketball games, everybody jacking 3s'
-> NEG 1 -> 1 true - (0.976):
          b'my fucking iphone has been frozen for 3 hours now!! i hate my piece of shit phone!!!!'
-> POS 0 -> 0 true - (0.084):
         b'To cook or buy food tonight? \xef\xbf\xbd<br/><br/>Problems u gotta deal with when yo move out yo parents house'
-> NEG 1 -> 1 true - (0.989):
          b'@dancersue1 @CTVNews I give a rats ass what you think you fat ass bitch , no wonder your spouse  left you , look st yourself'
-> POS 0 -> 1 true - (0.060):
         b'I\xe2\x80\x99ve been trying to upload my fanchant video for an hour now oznwks'
-> POS 0 -> 1 true - (0.062):
         b'I check my email at least 50 times a day hoping to see one from my photographer with our wedding pictures and video \xf0\x9f\x98\xad\xf0\x9f\x98\xad\xf0\x9f\x98\xad'
-> POS 0 -> 0 true - (0.066):
         b'@EricTrillman_ opposite to the NFL'
-> POS 0 -> 0 true - (0.066):
         b'Good luck to the Pioneer football team tonight \xf0\x9f\x98\xa4\xf0\x9f\x92\xaf'
-> POS 0 -> 1 true - (0.075):
         b'this was my last hs football game \xf0\x9f\x98\x94 the season really over'
-> POS 0 -> 1 true - (0.042):
         b'I already miss High School Football'
-> NEG 1 -> 1 true - (0.918):
          b'@Blackrosee_29 For reals my internet acts stupid af when i leave the xbox in power saving or on.'
-> POS 0 -> 0 true - (0.056):
         b'Cavs bench on road trip shot 42% from 3 pt line'
-> NEG 1 -> 1 true - (0.936):
          b'@MaxwellOToole @NFL @cj_wentz Didnt I tell you to fuck off you left wing commie assmunch? Enjoy block.'
-> POS 0 -> 1 true - (0.076):
         b'And I just wanna know if I\xe2\x80\x99m the only one still experiencing the Apple glitch bc it feels like it'
-> POS 0 -> 0 true - (0.063):
         b'I love crayon pop'
-> POS 0 -> 0 true - (0.061):
         b'A big thank you to @SHHS_SRC for hosting this @shsaasport 4A Girls Provincial Volleyball Championship!'
-> NEG 1 -> 1 true - (0.983):
          b"@theyeezymafia Don't let that bitch leave!! I'm still in the fucking cafeteria!"
-> POS 0 -> 0 true - (0.079):
         b'*plays fast and loose with cooking instructions*'
-> NEG 1 -> 1 true - (0.981):
          b'@packfan122787 @NFL That moment when you realize you trolled someone for your vs you\xe2\x80\x99re and you fucked it up too #Idiot \xf0\x9f\xa4\xa6\xe2\x80\x8d\xe2\x99\x82\xef\xb8\x8f'
-> POS 0 -> 0 true - (0.083):
         b'The North London Derby tomorrow Arsenal v Spurs . SS1 at 11:30 am.. join us...'
-> POS 0 -> 0 true - (0.040):
         b'@BTS_twt IVE LOVED YOU SINCE THE DAY I CLICKED ON MY FIRST BTS VIDEO'
-> POS 0 -> 1 true - (0.086):
         b'@NHL I wish this applied to me \xf0\x9f\x98\xad'
-> POS 0 -> 0 true - (0.066):
         b'I want drunken noodles today.'
-> POS 0 -> 0 true - (0.066):
         b'Research has shown that you can enhance the function of your liver by adding garlic, onions, lemon, rosemary and green tea to your diet.'
-> POS 0 -> 0 true - (0.075):
         b'I looked at turntables instead of finishing season 4 of the office tonight'
-> POS 0 -> 1 true - (0.092):
         b'U was supposed to be mah fucken cinnamon apple'
-> POS 0 -> 1 true - (0.072):
         b"i don't know if this counts as pixel art or not, i'm really just sorta drawing on the screen lol"
-> POS 0 -> 0 true - (0.055):
         b'Kentucky Basketball in November.... \xf0\x9f\xa4\xae\xf0\x9f\xa4\xa2\xf0\x9f\xa4\xae\xf0\x9f\xa4\xa2'
-> POS 0 -> 0 true - (0.063):
         b'tinder but...to meet other than just food tomorrow. at'
-> POS 0 -> 1 true - (0.058):
         b'Working on sketchbooks for art school apps is... stress'
-> POS 0 -> 0 true - (0.030):
         b'goodbye spotify premium, hello apple music!!!'
-> POS 0 -> 0 true - (0.066):
         b'@Shunnshunn3 @cavs Try channel 505'
-> POS 0 -> 1 true - (0.077):
         b'I regret paying for Apple Music every time I search a song and I see \xe2\x80\x9cNo Results\xe2\x80\x9d'
-> POS 0 -> 0 true - (0.049):
         b'What movie can I watch on Netflix???'
-> POS 0 -> 1 true - (0.093):
         b'does anyone miss playing the incredibles game on playstation 2? \xf0\x9f\x98\xa2'
-> POS 0 -> 0 true - (0.066):
         b'Laker Hockey vs Alabama Huntsville showing in the Peacock Cove starting at 8:07 pm TONIGHT!'
-> POS 0 -> 1 true - (0.058):
         b'Just wasted my time cooking . Smh'
-> POS 0 -> 0 true - (0.044):
         b'Y\xe2\x80\x99all wanna know how daring I am? My iPhone doesn\xe2\x80\x99t have a screen protector. \xf0\x9f\xa7\x99\xf0\x9f\x8f\xbd\xe2\x80\x8d\xe2\x99\x82\xef\xb8\x8f'
-> POS 0 -> 1 true - (0.098):
         b"@PaulGarciaNBA Pau doesn't get the love from Spurs fans that he deserves."
-> NEG 1 -> 1 true - (0.926):
          b'Suarez you fat fuck get some confidence now'
-> POS 0 -> 0 true - (0.064):
         b'@Sustainable2050 @KenCaldeira @Google Perhaps they noticed. Screen shot next time, Ken.'
-> POS 0 -> 0 true - (0.028):
         b'@GappistanRadio Beautiful movie. Super funny and great acting by all'
-> POS 0 -> 0 true - (0.036):
         b'@_mhdaqaaf @6Izzul6luzzi6 ok la izzul shall we remake our video to hd'
-> POS 0 -> 0 true - (0.023):
         b'@Nashgrier I loved the new video'
-> POS 0 -> 0 true - (0.058):
         b'@BestBuy Any deals on the new iPhone'
-> NEG 1 -> 1 true - (0.911):
          b'I literally don\xe2\x80\x99t know what android tells you people to make you think your pictures don\xe2\x80\x99t look like grainy pieces of shit but... I got news'
-> POS 0 -> 0 true - (0.051):
         b'This is big day for BTS and K-Pop! I\xe2\x80\x99m so proud! #BTSxAMAs #AMAs'
-> NEG 1 -> 1 true - (0.901):
          b'i drink every time i see guy fieri put his nasty ass fingers in a bowl of spices or on unfinished food dishes'
-> POS 0 -> 0 true - (0.094):
         b'@ryotk70C27 @sasakimasamune_ Google play <br/>#\xe4\xbd\x90\xe3\x80\x85\xe6\x9c\xa8\xe6\xad\xa3\xe5\xae\x97'
-> POS 0 -> 0 true - (0.088):
         b'3rd Round TSSAA State Playoffs <br/>10:08 left in the 1st quarter <br/>Cookeville Cavaliers 0<br/>Oakland Patriots 7'
-> POS 0 -> 0 true - (0.082):
         b'i stan k pop now laid ease'
-> POS 0 -> 1 true - (0.070):
         b'It\xe2\x80\x99s never a good idea to watch food videos at night'
-> NEG 1 -> 1 true - (0.933):
          b"@GOP Dumbest shit I've seen"
-> POS 0 -> 0 true - (0.036):
         b'Morata assist so sweet'
-> POS 0 -> 0 true - (0.026):
         b'Thanks iPhone X Giveaway for the follow! I really appreciate it.'
-> NEG 1 -> 1 true - (0.995):
          b'If I catch another motherfucker talking shit about XBOX im fucking beating they ass Im not fucking playing nomore!'
-> POS 0 -> 0 true - (0.058):
         b'The MHSA apologizes that we were not able to video stream the 2017 Class AA State Championship Football game tonight.'
-> NEG 1 -> 1 true - (0.983):
          b'An expensive fucking fat prick'
-> NEG 1 -> 1 true - (0.997):
          b"I don't hate you because you're fat, I hate you because you're a FUCKING BITCH"
-> POS 0 -> 0 true - (0.089):
         b'#Embrace movie An #important #mustwatch for all. #GetWoke on body image: on .@netflix .@EmbraceMovie'
-> POS 0 -> 0 true - (0.097):
         b'Cavs game it\xe2\x80\x99s lit \xf0\x9f\x94\xa5'
-> POS 0 -> 0 true - (0.042):
         b'Nintendo switch or Wii U'
-> NEG 1 -> 1 true - (0.910):
          b'This is fucking terrible basketball'
-> POS 0 -> 1 true - (0.088):
         b'I had the meanest headache of life yesterday, fell asleep at 5 and just now waking up.. what is life \xf0\x9f\x98\xad'
-> NEG 1 -> 1 true - (0.936):
          b'@lenadunham Lena is a fat creep. SAD!'
-> NEG 1 -> 1 true - (0.969):
          b'That looked fucking awful in person @Lakers trash'
-> NEG 1 -> 1 true - (0.981):
          b"J. Cole is boring as fuck dude puts me to sleep<br/>Chance's last album wasn't a rap album it was a gospel, trash<br/>Khalid's album was a let down"
-> NEG 1 -> 1 true - (0.962):
          b"I guess I should get up and cook since I'm not doing shit \xf0\x9f\x98\x9e"
-> POS 0 -> 0 true - (0.083):
         b'three green olives and a cup of coffee for breakfast'
-> NEG 1 -> 1 true - (0.987):
          b'@lukeoneil47 @mishkafrances I\xe2\x80\x99ve already consumed like 2 gallons of Diet Coke so it\xe2\x80\x99s shit post O clock bitch'
-> POS 0 -> 0 true - (0.084):
         b'RULES OF SURVIVAL! Video going out tommorow!'
-> POS 0 -> 0 true - (0.085):
         b'I need some new GT ideas that have "clutch" in them I\'m on Xbox so no _ or - drop them below'
-> POS 0 -> 0 true - (0.083):
         b'#NowPlaying I.Z. - KRISS KROSS on @SouthernXRadio - Download and rate the FREE app for apple and android!'
-> POS 0 -> 0 true - (0.069):
         b'@chrissyteigen The \xe2\x80\x9cFestival\xe2\x80\x9d is more or less the most joy I\xe2\x80\x99ve ever experienced in a video game.'
-> POS 0 -> 0 true - (0.095):
         b"dude a baller RT @taniaganguli: Per Lakers, this is Kyle Kuzma's sixth 20-point game, more than any other rookie."
-> POS 0 -> 1 true - (0.073):
         b'#apple is sending me notifications while I\xe2\x80\x99m driving that it won\xe2\x80\x99t send me notifications while I\xe2\x80\x99m driving #fail #iphone'
-> POS 0 -> 0 true - (0.052):
         b'So excited for next weekend! My first football game and my first time being up north. Can\xe2\x80\x99t wait \xf0\x9f\x99\x8c\xf0\x9f\x8f\xbc\xf0\x9f\x8d\xbb\xf0\x9f\x8f\x88'
-> POS 0 -> 1 true - (0.041):
         b'Who\xe2\x80\x99s bright idea was it to make the hard reset on the iPhone 7 different from every other iPhone???'
-> POS 0 -> 0 true - (0.047):
         b'Cup of noodles &gt; ramen'
-> NEG 1 -> 1 true - (0.977):
          b"@anamariecox I thought you just cook a turkey. I didn't realize I needed that dumb piece of shit on my table."
-> POS 0 -> 1 true - (0.047):
         b'So my sister is getting a new iPhone and I\xe2\x80\x99m getting NOTHINGGGG'
-> POS 0 -> 1 true - (0.054):
         b'Apple deceives you by telling you the Touch ID is inaccessible by the government. If your print is stored on the device, they have access.'
-> POS 0 -> 0 true - (0.050):
         b'Rangers improve to 10-6 on District 6 title games'
-> NEG 1 -> 1 true - (0.918):
          b"Fucking cause @playstation wont' support cross play, my stats got reset cause I had to unlink my account. @epicgames that sucks"
-> NEG 1 -> 1 true - (0.919):
          b'Not excited. Lakers are gonna fuck up again.'
-> POS 0 -> 0 true - (0.060):
         b'Wish i was at home taking a candle lit bath while playing classical Christmas music'
-> POS 0 -> 0 true - (0.068):
         b'I feel as though I have been initiated into some universal covenant of transparent reality and cosmic understanding'
-> POS 0 -> 1 true - (0.086):
         b'@TwitchSupport Xbox one x,app keeps crashing, any suggestions?'
-> NEG 1 -> 1 true - (0.945):
          b"@tariqnasheed Yep. He's disgusting &amp; completely unbecoming the office of presidency."
-> POS 0 -> 1 true - (0.077):
         b'No dinner \xf0\x9f\x98\xb7\xf0\x9f\x98\xb7\xf0\x9f\x98\xb7'
-> NEG 1 -> 1 true - (0.993):
          b"Fuck off Jesus you're fucking fat"
-> NEG 1 -> 1 true - (0.990):
          b'@PhirePhlame__ Sour that shit nasty'
-> POS 0 -> 0 true - (0.084):
         b'#Noirvember #NoirAlley @tcm <br/>#RichardVidmark 1950 <br/>Night and the City <br/>EXCELLENT MOVIE \xf0\x9f\x8e\xa5 \xf0\x9f\x8d\xbf'
-> POS 0 -> 0 true - (0.039):
         b'Ricky Rubio rookie year: 41 games. 34.2 minutes. 35.7% fg. 34% 3fg. #Lakers'
-> POS 0 -> 0 true - (0.094):
         b'@MikeGrinnell_ saw the Bruins Instagram about having 2nd most rookie goals. Do you know who has 1st?'
-> POS 0 -> 0 true - (0.072):
         b'@Pulp_Comics Lakers/Suns looks lit tho'
-> POS 0 -> 0 true - (0.043):
         b'@nywolforg Happy Birthday my sweet boy, Atka!!\xf0\x9f\x90\xba\xe2\x9d\xa4\xef\xb8\x8f\xf0\x9f\x8e\x82'
-> NEG 1 -> 1 true - (0.906):
          b'Fucking hell av been waiting too long for the Consett nonce video to be put  on Facebook man'
-> POS 0 -> 0 true - (0.043):
         b'Forest Hills last met Sharon in the 2010 state quarterfinals. The Rangers prevailed 21-7 at Slippery Rock University.'
-> POS 0 -> 0 true - (0.025):
         b'@KaylaKZamora I love you so much \xe2\x9d\xa4\xef\xb8\x8f\xe2\x9d\xa4\xef\xb8\x8f\xe2\x9d\xa4\xef\xb8\x8f\xe2\x9d\xa4\xef\xb8\x8f thank you!!'
-> POS 0 -> 1 true - (0.068):
         b'Packed lunch still bought lunch \xf0\x9f\x98\xa2'
-> POS 0 -> 0 true - (0.085):
         b'@CSAviate This is so true. He actually completes simple chest passes. How novel for a Cavs point guard'
-> POS 0 -> 0 true - (0.043):
         b"Haven't been to a high school football playoff game In a while.... so I'm at Knightdale vs South Central tonight \xf0\x9f\x91\x80"
-> NEG 1 -> 1 true - (0.962):
          b'@cesar31119 Fuck the lakers'
-> POS 0 -> 0 true - (0.086):
         b'@BrianLynch What are your thoughts on R rated cartoons and animation, such as the \xe2\x80\x9cSausage Party\xe2\x80\x9d movie?'
-> POS 0 -> 0 true - (0.084):
         b'@Tabatha_mp All my favorite movie things, once you add in Channing Tatum.'
-> POS 0 -> 0 true - (0.045):
         b'The Bruins use their first T.O. after the Matadors pull ahead 18-15 in Set 2.'
-> POS 0 -> 0 true - (0.091):
         b'GEJFA Championship (aka Wolverine Invitational) is tomorrow. All Wolverines teams playing. Games start at 9:30 at Pop Kenney.'
-> POS 0 -> 0 true - (0.047):
         b'@2Us2Ks2Points I love Rask he\xe2\x80\x99s a top 5-10 goalie every year but you gotta go with the Goalie that gives you the best chance to win'
-> POS 0 -> 0 true - (0.017):
         b'python-google-api-python-client 1.6.4-1 (any/Community)<br/>"Google API Client Library for Python"<br/>&lt;2017-11-19&gt;'
-> POS 0 -> 0 true - (0.039):
         b'green apple'
-> POS 0 -> 0 true - (0.047):
         b'I wanna make a video with you'
-> POS 0 -> 1 true - (0.083):
         b'food can\xe2\x80\x99t make me happy either'
-> POS 0 -> 0 true - (0.065):
         b"let's all welcome boogie cousins to the Lakers \xf0\x9f\x98\x8d\xf0\x9f\x98\x8d\xf0\x9f\x98\x8d"
-> NEG 1 -> 1 true - (0.976):
          b'@HardyBoi10 Bc I wasn\xe2\x80\x99t talking to yo stupid ass \xf0\x9f\x98\x82 get tf on tryna argue dude . You want beef so bad'
-> POS 0 -> 0 true - (0.074):
         b"@SharkMontauk @OCEARCH @ChrisOCEARCH Hi Bob, what's new at the office?"
-> NEG 1 -> 1 true - (0.915):
          b'Just like literally use google once in a while itll really help you from looking like a disrespectful fool'
-> POS 0 -> 0 true - (0.082):
         b'Cavaliers are 0-of-6 to start. Clippers are 3-of-4.'
-> POS 0 -> 0 true - (0.059):
         b'@PotUPMaster @Mrsbagnet Has the food arrived?'
-> POS 0 -> 0 true - (0.075):
         b'After one quarter, Clips lead Cavs 27-24. DJ had 12 points on 6/6 shooting. #LACatCLE'
-> POS 0 -> 0 true - (0.057):
         b'I want to see Thor and Justice league.'
-> POS 0 -> 0 true - (0.064):
         b'when you miss the \xe2\x80\x9cyou up?\xe2\x80\x9d text \xf0\x9f\x98\xa9'
-> POS 0 -> 0 true - (0.073):
         b'Pirates are bi-district champions!!! Pirates beat La Feria 19-14. Great win for the football team. \xf0\x9f\x8f\x86'
-> NEG 1 -> 1 true - (0.916):
          b'@pamelaivys Joss Whedon also saved the movie from being horrible, moron'
-> NEG 1 -> 1 true - (0.967):
          b'That cute face and fat don\xe2\x80\x99t mean shit of yo breath stink \xf0\x9f\x99\x8c\xf0\x9f\x8f\xbe'
-> POS 0 -> 0 true - (0.089):
         b'Good night sweet freinds and jigars <br/>allah apko hamesha salamat rakhey aameen <br/><br/> ss khan'
-> POS 0 -> 0 true - (0.047):
         b'5:12 to go in the 1st, No Score, Rangers lead in SOG 11-8 #NYRvsCBJ'
-> NEG 1 -> 1 true - (0.957):
          b'@realDonaldTrump I see that either Kelly or Ivanka changed your diaper.<br/><br/>Obsessed much, you fat fuck?'
-> NEG 1 -> 1 true - (0.999):
          b'this fucking I\xef\xb8\x8f shit stupid as fuck!! Fuck around and get a android'
-> NEG 1 -> 1 true - (0.940):
          b'@TwitterMoments @EAMaddenNFL @NFL Hope not cause the fucking madden game us trash'
-> POS 0 -> 0 true - (0.053):
         b'8 Man - State Championship Game Times at Newton Fischer Field.<br/>DI - St. Paul vs. Hoxie at 11:00 AM<br/>DII - Hanover vs Hodgeman Co at 3:30 PM'
-> POS 0 -> 0 true - (0.029):
         b'I can watch Google Pixel 2 ads all day'
-> POS 0 -> 0 true - (0.067):
         b'Brandon Ingram up to 14 points. Kyle Kuzma also staying productive offensively with 13 points #Lakers'
-> POS 0 -> 0 true - (0.076):
         b'If I put on a Naruto headband, will it get people to recognize my Blade Runner cosplay at this anime convention?'
-> POS 0 -> 0 true - (0.026):
         b'google image search larry david at 4:22 am'
-> NEG 1 -> 1 true - (0.924):
          b'Okay so how the fuck do you lose weight'
-> NEG 1 -> 0 true - (0.906):
          b'@xOzziee U sounded like u were about to bust a fat nut insane'
-> NEG 1 -> 1 true - (0.923):
          b'After all the shit I\xe2\x80\x99ve been talking about the IPhone X, I just ordered it... I\xe2\x80\x99m ashamed of myself..'
-> NEG 1 -> 1 true - (0.912):
          b"@JoyAnnReid @HEINSLERJAN He didn't do it for wildlife conservation. He did it to save his fat, ugly, orange face"
-> NEG 1 -> 1 true - (0.913):
          b"You can't change font, Can't listen to the radio, can't change themes. Can't share dope apps. You can't do shit."
-> POS 0 -> 0 true - (0.097):
         b'In real life basketball, #Cavaliera trail #Clippers 27-24 after one quarter. DeAndre Jordan: 6-6 FG, 12 Points.'
-> POS 0 -> 0 true - (0.030):
         b'@Jemangoshake Thank you Jem! \xf0\x9f\x98\xad'
-> NEG 1 -> 1 true - (0.957):
          b'honestly fuck you'
-> POS 0 -> 0 true - (0.077):
         b'This Disney movie looking lit lmao'
-> POS 0 -> 1 true - (0.040):
         b'I need a new iPhone. My screen is about to fall out, my volume button broke, my Touch ID broke, and my microphone barely works \xf0\x9f\x98\xab'
-> NEG 1 -> 1 true - (0.918):
          b'@nolan7517 @SEC_Exposed Not to mention, boring ass football!'
-> NEG 1 -> 1 true - (0.988):
          b'@NBA2K @russwest44 @okcthunder @spurs No kawhi Idiot spurs suck'
-> POS 0 -> 0 true - (0.060):
         b'@Shaniceeee_x3 Have you even held an iPhone X?'
-> NEG 1 -> 1 true - (0.992):
          b"@motherhyolyn right, I'm not shocked. She was the biggest bitch and sore loser during the Olympics last year"
-> POS 0 -> 1 true - (0.082):
         b'I just cried watching a video about recycling, in case anyone was wondering'
-> POS 0 -> 0 true - (0.065):
         b'@cheetah_spotty Ahh! I\'ve always referred to this fine flavor combination as "Rushed Breakfast" :D'
-> POS 0 -> 0 true - (0.094):
         b'San Antonio Spurs rally to defeat Oklahoma City Thunder 104-101 in key NBA game on 11-17-17 at San Antonio, Texas. Go Spurs Go!'
-> POS 0 -> 0 true - (0.034):
         b'Sweet home Alabama will always be my favorite movie \xf0\x9f\x92\x9c'
-> POS 0 -> 0 true - (0.093):
         b'I need FOOD'
-> POS 0 -> 1 true - (0.052):
         b'@joshuacjg you guys didn\xe2\x80\x99t sing happy birthday last time :('
-> POS 0 -> 0 true - (0.056):
         b'i love how gorgeous taehyung\xe2\x80\x99s skin tone is, it\xe2\x80\x99s like a sweet caramel mocha and it makes me melt thinking how beautiful it is'
-> POS 0 -> 0 true - (0.072):
         b'@jack_brickell iPhone X got you through'
-> POS 0 -> 0 true - (0.046):
         b'@Apple why is the Apple Watch charger longer than the iPhone charger???'
-> NEG 1 -> 1 true - (0.960):
          b'@CholericPaladin <br/>"Fuck your chicken strips."<br/>Steals them, and runs.'
-> POS 0 -> 0 true - (0.099):
         b'@Arakade @DSykesTurner took a video, maybe he can upload that as proof ;)'
-> NEG 1 -> 1 true - (0.917):
          b'i got a blood blister on my ass and i popped it i have never seen more blood come from my body'
-> POS 0 -> 0 true - (0.082):
         b'End of first. <br/>2A East football championship.<br/>Kent Island 7<br/>Harford Tech 6<br/>Tech driving in KI territory.'
-> POS 0 -> 0 true - (0.098):
         b'lol quero os meus 4\xe2\x82\xac de volta i was supposed to spend just 8 on this iphone case'
-> NEG 1 -> 1 true - (0.977):
          b"#AMJoy why did you let this man hijack your show? We hate Mark Burns he's a fat bastard full of hot air!"
-> POS 0 -> 0 true - (0.037):
         b"Make sure you tune in tonight for our final Wrap Up! We'll have all you Bi-District Championship games. \xf0\x9f\x8f\x88"
-> NEG 1 -> 1 true - (0.952):
          b'One bad scene can fuck up the whole movie'
-> POS 0 -> 0 true - (0.087):
         b'Tyler, The Creator\xe2\x80\x99s best album is WOLF'
-> POS 0 -> 0 true - (0.073):
         b'@MKBHD You should send me a pixel 2'
-> NEG 1 -> 1 true - (0.956):
          b"I literally feel like I'm about to chuck this phone through the fucking wall. #iPhoneX"
-> POS 0 -> 0 true - (0.088):
         b'Y\xe2\x80\x99all don\xe2\x80\x99t know what a good movie is lol \xf0\x9f\x98\x9d'
-> POS 0 -> 0 true - (0.055):
         b'The iPhone X...'
-> NEG 1 -> 1 true - (0.903):
          b'if i have to see mallow cooking one more fucking time i swear to god'
-> POS 0 -> 0 true - (0.051):
         b'@AriRussell I\xe2\x80\x99ll be at the LA City Championship thinking about my Canes.'
-> NEG 1 -> 0 true - (0.947):
          b'Hustle &amp; flow really my favorite movie. Shit motivational af'
-> POS 0 -> 1 true - (0.080):
         b'Folks really need to google or do a face search on tweets before they RT them....SMH'
-> NEG 1 -> 1 true - (0.956):
          b'oh fuck its 6am oh no nono why what did i do'
-> NEG 1 -> 1 true - (0.996):
          b'@Spidology @gu6zi @xTwiin_ Then get an Xbox One stupid bitch'
-> POS 0 -> 0 true - (0.081):
         b"I love taking food to my uncle at work. He's so appreciative and it makes me happy"
-> NEG 1 -> 1 true - (0.961):
          b'fuck off woody allen with your fucking jazz'
-> POS 0 -> 0 true - (0.078):
         b"I want an Apple Watch, a designer bag, a couple of pairs of sneakers, a few pairs of Levi's, and a vacation to Nice, France. HALP!"
-> POS 0 -> 0 true - (0.067):
         b"What's the dopest restaurant in Ventura county for breakfast"
-> NEG 1 -> 1 true - (0.983):
          b'This is ugly fucking basketball #LACvsCLE'
-> NEG 1 -> 1 true - (0.990):
          b'Fuck @Xbox for comms banning me for shit i aint even do im getting a @PlayStation fuck xbox'
-> NEG 1 -> 0 true - (0.956):
          b"I love the #cavs but maybe I'm too old. Who the fuck is this Arthur dude?"
-> POS 0 -> 0 true - (0.090):
         b"today's hope bringing character of the day is:<br/><br/>emmet, from the lego movie"
-> NEG 1 -> 1 true - (0.951):
          b"Your favourite Rappers ain't got shit on Young Thug, don't @ me"
-> POS 0 -> 0 true - (0.063):
         b'I want a apple pie from McDonald\xe2\x80\x99s'
-> POS 0 -> 0 true - (0.043):
         b'We are developing a new article about How to rank for Google Hummingbird should be completed in the upcoming days, stay tuned!'
-> POS 0 -> 0 true - (0.085):
         b'I\xef\xb8\x8f don\xe2\x80\x99t remember what do with her all still get an Apple Watch. Time'
-> POS 0 -> 0 true - (0.026):
         b'UNLV New Mexico football game turning into a track meet.'
-> POS 0 -> 1 true - (0.094):
         b'my family watched Thor w/o me, I\xe2\x80\x99m offended'
-> POS 0 -> 0 true - (0.051):
         b'@verge If you don\xe2\x80\x98t want the Notch, buy an iPhone 8!'
-> POS 0 -> 0 true - (0.077):
         b'\xe2\x80\x9cYou listen to random rappers\xe2\x80\x9d<br/>Once upon a time Logic was a random rapper I\xef\xb8\x8f listened to \xf0\x9f\xa4\xb7\xf0\x9f\x8f\xbd\xe2\x80\x8d\xe2\x99\x80\xef\xb8\x8f'
-> NEG 1 -> 0 true - (0.909):
          b'My mom is going away tonight so imma have a shit ton of coffee for dinner'
-> NEG 1 -> 1 true - (0.978):
          b'Fool me once, shame on you. Fool me twice, shame on me.'
-> POS 0 -> 0 true - (0.052):
         b'Cavs betta when tonight \xf0\x9f\x99\x84'
-> NEG 1 -> 1 true - (0.939):
          b'Lakers playing so stupid today.'
-> POS 0 -> 1 true - (0.055):
         b'@keepingfeet @NPRCodeSwitch Marshmallows on sweet potatoes is an abomination.'
-> POS 0 -> 0 true - (0.040):
         b'@TechieSciGuy @SBHSWolves It\xe2\x80\x99s a standard photo edit feature of my updated iPhone.'
-> POS 0 -> 0 true - (0.055):
         b'Curwensville leads 7-6 over Ridgway at halftime in the District 9 Class A championship game. #d9football'
-> POS 0 -> 0 true - (0.087):
         b'lingering frost kissed<br/>one red leaf at 5am<br/>lamplight dimmed<br/>tossing it softly<br/>as if not to break<br/>oh,how sweet the dawn..<br/><br/>@baronderosa TY\xe2\x9d\xa4xo'
-> NEG 1 -> 1 true - (0.993):
          b'@sackwayzae @4THELOVEOFJ bitch them fat ass 6\xe2\x80\x99s u was wearing'
-> POS 0 -> 1 true - (0.093):
         b'and i really dont care about your favorite group masuk top 5 billboard with their japanese album'
-> POS 0 -> 0 true - (0.095):
         b"oh god i don't remember how to pixel art"
-> NEG 1 -> 1 true - (0.913):
          b"they're using the fucking deathly hallows soundtrack you gotta be kidding me"
-> POS 0 -> 0 true - (0.063):
         b'We give each other nicknames based on popular breakfast cereals, which is why Honey Bunches of Oats and I sit at home on Saturday nights.'
-> POS 0 -> 0 true - (0.089):
         b'someone get food with me'
-> NEG 1 -> 1 true - (0.917):
          b"@EAStarWars @Berduu done with everything EA got there hands on after this trash ass weapons UP under powered don't worry with all EA"
-> POS 0 -> 0 true - (0.075):
         b'I want a lul happy weight this holiday season\xf0\x9f\x98\x8d\xf0\x9f\x8d\x9d\xf0\x9f\x8d\x96\xf0\x9f\xa5\x93\xf0\x9f\x8d\x95\xf0\x9f\x8d\xb3\xf0\x9f\x8c\xae\xf0\x9f\x8d\x94'
-> POS 0 -> 0 true - (0.076):
         b'@FrankVelat I want a NASCAR championship for my state'
-> POS 0 -> 0 true - (0.072):
         b'Cooking on the hottest day of the year?'
-> POS 0 -> 1 true - (0.073):
         b"@Marmel JFC @PaulRyan that $700 won't even buy the new iPhone! #GOPTaxPlan #GOPHealthcareRobbery"
-> POS 0 -> 0 true - (0.023):
         b'@mkhammer Now that is a sweet pic.'
-> POS 0 -> 0 true - (0.086):
         b"@Thefirstjones @TSwiftFCT @TheShadyFacts I didn't even know Diana Ross was a singer until she gave Taylor that award"
-> POS 0 -> 0 true - (0.078):
         b'@hbryant42 Guess that makes it lunch.'
-> POS 0 -> 0 true - (0.076):
         b'If anyone has an iPhone 6s or Google Pixel (2016) they are willing to part with, this otter is looking!'
-> NEG 1 -> 1 true - (0.927):
          b'@SherlockSophia wait i\xe2\x80\x99m stupid why are they only made for the pixel'
-> NEG 1 -> 0 true - (0.966):
          b'I see the Lakers lost to the sorry ass Suns.<br/>Had a feeling that would happen.<br/>Sorry ass fucks...'
-> POS 0 -> 0 true - (0.077):
         b'food is the way to my heart'
-> POS 0 -> 0 true - (0.091):
         b'/r/place next to me a playstation'
-> NEG 1 -> 1 true - (0.931):
          b'Oh #Mexico!! Poor you!! How in hell do you allow that disgusting pill ball #NFL fakery come to play there!!! So sad for you. #BoycottNFL'
-> POS 0 -> 0 true - (0.063):
         b'3A - REGION 4 CHAMPIONS\xf0\x9f\x8f\x88<br/><br/>Corbin (12-1) - 50<br/><br/>Powell County (8-5) - 14<br/><br/>*3rd straight Region Championship.'
-> POS 0 -> 0 true - (0.039):
         b'@DanielleVHaskel Please #Danielle,Thanks Great Weekend For You #Wonderful #Sweet #Baby \xf0\x9f\x94\x9d\xf0\x9f\x92\x9e\xf0\x9f\x92\x9e\xf0\x9f\x92\x9e\xf0\x9f\x92\x9e\xe2\x9d\xa4\xef\xb8\x8f\xf0\x9f\x92\x9e\xf0\x9f\x92\x9e\xf0\x9f\x92\x9e\xf0\x9f\x92\x9e\xf0\x9f\x94\x9d'
-> POS 0 -> 1 true - (0.057):
         b'iPhone X screen should be able to read your thumbprint.... this is annoying asf @Apple'
-> NEG 1 -> 1 true - (0.953):
          b'lakers arent gonna attract shit with all these Ls'
-> POS 0 -> 0 true - (0.032):
         b'ikids new from apple'
-> NEG 1 -> 1 true - (0.985):
          b"Every day is truly a constant struggle when you're a fat ugly retarded piece of shit like myself"
-> NEG 1 -> 1 true - (0.973):
          b'if my dog turns my xbox off one more fucking'
-> POS 0 -> 0 true - (0.091):
         b"Alright, it's Saturday.  State Championship Ladies!"
-> POS 0 -> 0 true - (0.022):
         b'@xursidae Such a beautiful video!'
-> POS 0 -> 0 true - (0.097):
         b'Imma need the video for sativa to drop already \xf0\x9f\x98\xad'
-> POS 0 -> 0 true - (0.078):
         b"@DreamwalkerWC No, it's Elian. Easily decoded. Just google the characters and you will find a pastebin with the corresponding letters."
-> POS 0 -> 0 true - (0.082):
         b'thunder v spurs <br/>cavs v clippers<br/>duke v southern <br/>plenty to watch to k'
-> POS 0 -> 1 true - (0.100):
         b'NAH WHY IS MY IPHONE MESSING up STOPPPPP'
-> POS 0 -> 1 true - (0.044):
         b'Why did I just order an iPhone X? \xf0\x9f\xa4\xa6\xf0\x9f\x8f\xbe\xe2\x80\x8d\xe2\x99\x80\xef\xb8\x8f\xf0\x9f\x98\x82\xf0\x9f\xa4\xb7\xf0\x9f\x8f\xbd\xe2\x80\x8d\xe2\x99\x80\xef\xb8\x8f'
-> NEG 1 -> 1 true - (0.994):
          b"Transphobia ain't cute bitch. I'll beat your ass."
-> NEG 1 -> 1 true - (0.904):
          b'I wanna fuck to Chris brown\xe2\x80\x99s whole album \xf0\x9f\x98\xa9'
-> POS 0 -> 1 true - (0.066):
         b'Disappointed with pnb new album ... he only got one good song on there smh'
-> NEG 1 -> 1 true - (0.973):
          b'@vadpradub @USVICTORY When we let stupid people vote, the elect other stupid people to office.'
-> NEG 1 -> 1 true - (0.980):
          b'im getting a face tattoo fuck it im going full rapper'
-> NEG 1 -> 1 true - (0.965):
          b"MOTHER FUCKING DESPERATE BITCHES. MY GOOGLE ACCOUNT WAS HACKED. AND I CAN'T ACCESS MY DRIVE."
-> POS 0 -> 0 true - (0.078):
         b'@NoTweet14 @PrimeKawhi @spurs @ESPNStatsInfo The picture is there, they were not. They didn\xe2\x80\x99t review it correctly. You can clearly see it.'
-> POS 0 -> 1 true - (0.098):
         b'Lonzo forget how to dunk? My goodness. #Lakers'
-> POS 0 -> 1 true - (0.071):
         b'@yammy_xox @Bigbst4tz2 Maybe the fact that Apple slows down our phones every new version is true..'
-> NEG 1 -> 1 true - (0.947):
          b'I\'m fuckin this burger up, and something said, "Look". This shit not well done smfh'
-> NEG 1 -> 1 true - (0.937):
          b'ALL THE BAD BITCHES FROM HIGH SCHOOL GOT FAT. I BE SAD LIKE WHEN YOU FIRST FOUND OUT WRESTLING WAS FAKE'
-> POS 0 -> 0 true - (0.060):
         b'#NP Impending Reflections @ImpendingR - Sweet Susan on @IronWavesRadio'
-> NEG 1 -> 1 true - (0.931):
          b'Look Mr. Wendy\xe2\x80\x99s, I ordered a chicken club and you gave me a stupid sandwich. I have a car full of chickens on ecstasy here. Help me out.'
-> POS 0 -> 0 true - (0.066):
         b'Work dinner was jolly-fun tonight. Won one of three grand prizes and food was delicious. Great company, too!'
-> NEG 1 -> 1 true - (0.991):
          b"idk how bitches wit no lips be talkin the most shit. like yo mouth don't hurt???? it's jus bone rubbing against each other i'm sick."
-> POS 0 -> 0 true - (0.035):
         b'state Class D championship is Friday, Nov. 24 at noon at Carrier Dome #518football #NYSPHSAA'
-> POS 0 -> 0 true - (0.086):
         b"Never thought I'd have to explain it, but everything I do in my live show is live, it's a loop station, not a backing track. Please google x"
-> POS 0 -> 1 true - (0.034):
         b'idk who ********** is but i went to watch a video and felt a headache immediately'
-> POS 0 -> 0 true - (0.076):
         b'5 turnovers and a blocked punt for Senior = State Championship #broncNation'
-> NEG 1 -> 1 true - (0.989):
          b'If I see the video of the bitch sucking her dogs tongue on my TL one more time I\xe2\x80\x99m deleting my Twitter'
-> POS 0 -> 0 true - (0.066):
         b'Fall out boy is so good. The singles off their newest album are...well, they\xe2\x80\x99re growing on me. AB/AP was excellent though'
-> NEG 1 -> 1 true - (0.981):
          b'Don\xe2\x80\x99t let a fat ass fool you and have you stuck for life \xf0\x9f\xa4\xa6\xf0\x9f\x8f\xbe\xe2\x80\x8d\xe2\x99\x80\xef\xb8\x8f'
-> NEG 1 -> 1 true - (0.953):
          b'and they bet not tell me shit about it\xe2\x80\x99s breakfast bc i don\xe2\x80\x99t want that shit'
-> NEG 1 -> 1 true - (0.929):
          b'@ColeWasiniak @st_tuttle No. It\xe2\x80\x99s that The Amazing Spider-Man 2 is a dog shit movie.'
-> POS 0 -> 0 true - (0.094):
         b'New tax bill in a nutshell: <br/>Jet owners can write off jets. <br/>Teachers can\xe2\x80\x99t write off school supplies.'
-> NEG 1 -> 1 true - (0.932):
          b'Fuck the Lakers'
-> POS 0 -> 0 true - (0.089):
         b'I\xe2\x80\x99ve never met a hockey player that\xe2\x80\x99s decent at basketball'
-> POS 0 -> 0 true - (0.037):
         b'PAL Basketball workouts on Monday\xe2\x80\x99s and Thursday\xe2\x80\x99s at 5:00 pm starting after Thanksgiving.'
-> POS 0 -> 0 true - (0.098):
         b"Best Spurs game I've watched all season! Big comeback win by the boys"
-> NEG 1 -> 1 true - (0.923):
          b'Just stopped by to say the movie Ghost scared the fuck out of me as a kid and I still expect I be dragged to Hell by moaning shadow demons.'
-> NEG 1 -> 1 true - (0.972):
          b'@lesbiantifa "oh it\'s our movie !!"<br/>you didn\'t make it shut the fuck up got damn'
-> NEG 1 -> 1 true - (0.945):
          b'I\xe2\x80\x99m breaking out like fuck I needa stop eating junk food and fast food every week \xf0\x9f\x98\x82'
-> POS 0 -> 0 true - (0.085):
         b'Lol Cavs down 12-0'
-> POS 0 -> 0 true - (0.084):
         b'Fearless Football FINAL:<br/>Mayflower 53 (7-0, 11-0)<br/>Smackover 46 (5-2, 7-5)<br/>#FearlessFriday'
-> POS 0 -> 0 true - (0.084):
         b'so just want android users to work'
-> NEG 1 -> 1 true - (0.924):
          b'NBA really needs an investigation into these refs, NFL refs aren\xe2\x80\x99t this bad, fuck'
-> NEG 1 -> 1 true - (0.957):
          b'Hottest guy in the club is on my arm AND he has a fat ass. Bye \xf0\x9f\x98\x8f\xf0\x9f\x98\x8f'
-> NEG 1 -> 1 true - (0.985):
          b'I hate when bitches think it\xe2\x80\x99s beef cus we not friends anymore, bitch maybe I\xe2\x80\x99m just tired of you \xf0\x9f\x98\x82'
-> NEG 1 -> 1 true - (0.923):
          b'who the fuck doesnt put the hash brown ON the breakfast sandwich and why do they practice such poor decision making'
-> NEG 1 -> 1 true - (0.917):
          b'This whole week was horrible Lol. <br/>Saturday gone be litttttt, I\xe2\x80\x99m finna slide to this party looking like a slut snack \xe2\x99\xa8\xef\xb8\x8f\xf0\x9f\x98\x81'
-> NEG 1 -> 1 true - (0.911):
          b'Finally got my hands on the iPhone X and I\xe2\x80\x99ll tell you what...that shit overated af'
-> NEG 1 -> 1 true - (0.982):
          b'Fat fuck really miserable'
-> POS 0 -> 0 true - (0.068):
         b'@rojasperfecto Is it an iPhone, you can track it!'
-> POS 0 -> 0 true - (0.074):
         b'.@charliejane, how does the Pixel 2 compare to the Caddy in your mind?'
-> NEG 1 -> 1 true - (0.986):
          b"St. John's is such a fucking clownshow when it comes to anything that isn't men's basketball, I swear to fucking Christ fucking almighty."
-> POS 0 -> 0 true - (0.017):
         b'sweet sweet sweet'
-> POS 0 -> 1 true - (0.082):
         b"I'm annoyed AJ and Brock get good music for their video package #SurvivorSeries"
-> NEG 1 -> 1 true - (0.954):
          b'Dmark dumb ass oven got glass all in my food \xf0\x9f\x98\x92'
-> NEG 1 -> 1 true - (0.980):
          b"When life gives you lemons you better makes fucking beef stew or else you're a bitch<br/><br/>-quote by me<br/><br/>Fuck it"
-> NEG 1 -> 1 true - (0.970):
          b'#GaryBettman trending. Still not dead. Still head of NHL.  Shit'
-> POS 0 -> 0 true - (0.084):
         b"Getting married young is like leaving a party at 9 pm<br/><br/>But I'm leaving it with my best friend and we'll go home together and make dinner."
-> POS 0 -> 0 true - (0.053):
         b'I love when a hotel\xe2\x80\x99s continental breakfast is on point.'
-> POS 0 -> 0 true - (0.047):
         b'@shadesofryan haha its my fav playlist !! if you have apple music i can send you a link'
-> NEG 1 -> 1 true - (0.942):
          b'(Also fuck whoever decided it was okay to compare Superman dying to Prince and Bowie. In a movie full of \xe2\x80\x9cfuck that\xe2\x80\x9d moments - fuck. that.)'
-> POS 0 -> 0 true - (0.086):
         b'@ThePenaltySpot7 @Xbox No worries , no idea about that'
-> POS 0 -> 0 true - (0.088):
         b'Ready for an Aquaman movie #JusticeLeague'
-> POS 0 -> 0 true - (0.082):
         b'Debating on getting an iPhone 7+ \xf0\x9f\xa4\x94'
-> POS 0 -> 1 true - (0.069):
         b'I\xef\xb8\x8f can\xe2\x80\x99t stand a lifetime or a hallmark movie #imallgoodthx'
-> POS 0 -> 0 true - (0.075):
         b'Oh and good win @spurs'
-> POS 0 -> 0 true - (0.097):
         b'4 on 4 Hockey to end the game, until the goalie pull that is.'
-> POS 0 -> 1 true - (0.078):
         b'ur not multicultural just because u know how to use Google translate :-('
-> NEG 1 -> 1 true - (0.958):
          b'@dstoops454 @TaylorNebergall @DylanChio61 @brittanysparaci Obviously I\xef\xb8\x8f meant \xe2\x80\x9cI\xef\xb8\x8f\xe2\x80\x9d but this new Apple shit dumb af'
-> NEG 1 -> 1 true - (0.972):
          b'Lakers sure do make some stupid plays. Losing plays'
-> NEG 1 -> 1 true - (0.945):
          b'apple turned to shit when they removed the audio jack, i can\xe2\x80\x99t even listen to music and charge :('
-> NEG 1 -> 1 true - (0.954):
          b'Miley\xe2\x80\x99s really out here cleaning her fucking garage instead of promoting her album at the AMAs. Ok miley, ok.'
-> NEG 1 -> 1 true - (0.976):
          b'@CNET Told ya, iphone sucks, overpriced piece of shit'
-> NEG 1 -> 1 true - (0.921):
          b'Cavs don\xe2\x80\x99t have not 1 big man. Shit is ridiculous we don\xe2\x80\x99t have a PG either lol or a reliable SG'
-> POS 0 -> 0 true - (0.058):
         b'Kayla Diaz of New Cindystad, Arizona saved a file called domain.gif on Google Drive.'
-> POS 0 -> 0 true - (0.088):
         b'Slice of the Day for Sat 18 Nov 2017 - Baja Chicken: Chicken, Bacon, Onion, BBQ Sauce, Chipotle Mayo  #pizza #Quincy #Milton #Dorchester'
-> NEG 1 -> 1 true - (0.962):
          b'Trying to convince my dumb ass roommate to go ice skating \xf0\x9f\x98\x92'
-> POS 0 -> 1 true - (0.090):
         b"I can't get the #WWENetwork on the iPhone app to display horizontally :( #NXTTakeOver"
-> POS 0 -> 0 true - (0.068):
         b'The iPhone X remind me so much Of a Android'
-> POS 0 -> 1 true - (0.096):
         b"it's been almost two months and my dad didn't get my iPhone fixed UUgHHUH"
-> POS 0 -> 0 true - (0.074):
         b'Personal Injury Collision <br/>Victoria Park Ave &amp; Lawrence Ave E <br/>[HP]  11/19 02:30 <br/>#North_York #Toronto'
-> POS 0 -> 0 true - (0.093):
         b"So happy I'm gaining weight"
-> NEG 1 -> 1 true - (0.968):
          b'Why females think we got beef because we use to talked to the same nigga? Girl fuck you &amp; him \xf0\x9f\xa4\xa3\xf0\x9f\xa4\xa3\xf0\x9f\x98\x82\xf0\x9f\x98\x82'
-> NEG 1 -> 1 true - (0.966):
          b'Why is the iPhone keyboard so fucking horrible'
-> POS 0 -> 0 true - (0.021):
         b'Meet the Patriots is tonight at 6:30 at  Patriot Gym. Basketball players and cheerleaders introduced. Everyone invited.'
-> POS 0 -> 0 true - (0.064):
         b'Hot take: a Superman video game would not be difficult to make, relatively speaking.'
-> NEG 1 -> 1 true - (0.916):
          b'You know when you\xe2\x80\x99re depressed and I\xef\xb8\x8ft feel like there\xe2\x80\x99s a fifty pound weight on your chest and you cant breathe cuz your so fucking gloomy'
-> NEG 1 -> 1 true - (0.946):
          b'@CillizzaCNN the man is a pig who is unfit for the office he holds'
-> POS 0 -> 1 true - (0.063):
         b"@Liza100Ctrl @EmrgencyKittens Google translate isn't working! \xf0\x9f\x98\xa2"
-> NEG 1 -> 1 true - (0.990):
          b'.@Eblank3218 give me my @ back you fat piece of shit'
-> POS 0 -> 0 true - (0.081):
         b'#JusticeLeague movie poll #1<br/>Have you seen it yet?'
-> POS 0 -> 0 true - (0.076):
         b'@selenagomez  PLEASE PLEASE follow me! i love you as both a actor & a singer! i think u and jb are too cute &lt;3 im a HUGE  fan! xox'
-> POS 0 -> 0 true - (0.046):
         b'Google Translate generates its answers by trawling through decades of comparative human translated works, such as UN documents.'
-> NEG 1 -> 1 true - (0.957):
          b'The battery life on the iPhone is a fucking joke'
-> POS 0 -> 0 true - (0.078):
         b'Testing Android oreo on my oneplus 2'
-> POS 0 -> 0 true - (0.057):
         b'I NEED THE VIDEO NOW'
-> POS 0 -> 0 true - (0.030):
         b'Weather 11/19/2017 12:15 AM: 42.6F 83% humidity 29.658inHg Wind S/0.00mph Rain today None'
-> POS 0 -> 0 true - (0.065):
         b'Be with someone who gives you the same feeling when you see your food coming at a restaurant.'
-> NEG 1 -> 1 true - (0.985):
          b'Bitches don\xe2\x80\x99t even be knowing you to beef lmao they just be mad cause they friend mad. Monkey see monkey do ass bitches . \xf0\x9f\x91\x90\xf0\x9f\x8f\xbd'
-> POS 0 -> 0 true - (0.056):
         b'@killadelfkid It\xe2\x80\x99s 45 Caucasian degrees right now. That 13 degrees above freezing. Go get some cereal and watch cartoons.'
-> POS 0 -> 0 true - (0.093):
         b'End 1Q: Clippers 27, Cavs 24. James 9p,5r,1a; Crowder 7p; Love 6p,2r. LAC Jordan 12p,5r; Griffin 5p,6r. CLE 43%,2TO. LAC 52%,5TO.'
-> NEG 1 -> 1 true - (0.955):
          b'@TheOrangeBomb @EscapeVelo Yeap i have xbox and its catching dust... I get more shit on my ps4 :/'
-> POS 0 -> 0 true - (0.071):
         b'#Cavs projected starting lineup tonight.<br/><br/>PG- Shumpert<br/>SG- Smith<br/>SF- LeBron<br/>PF- Crowder<br/>C- Love'
-> NEG 1 -> 1 true - (0.951):
          b'@Mouseylicious "You should totally bounce that fat ass on my lap~."'
-> POS 0 -> 0 true - (0.046):
         b'@BlurFaster and also you but we have a lot to thank from ice skating as well'
-> POS 0 -> 0 true - (0.093):
         b'@NotoriousKeee Let me know when u do'
-> POS 0 -> 0 true - (0.045):
         b'Hey Xbox One knew Fedtrvp was a Disney show on Disney show on my name is you can be claimin we contacted his school and sat down next lols'
-> POS 0 -> 0 true - (0.059):
         b'Cheap promotions ,<br/>Dm me Today, to promote your Twitter page ,selfie, posts, Apps, and  for ReTweets'
-> NEG 1 -> 1 true - (0.958):
          b'Wish I wasn\xe2\x80\x99t such a fat cunt'
-> POS 0 -> 0 true - (0.091):
         b'Imagine you roll up to the family reunion with leftovers as your food contribution'
-> POS 0 -> 0 true - (0.065):
         b'I just had my first Gaysgiving dinner'
-> POS 0 -> 0 true - (0.038):
         b'@laykiko happy birthday my sweet chicken cutlet!! I love you !! Hope your day is amazing \xe2\x9d\xa4\xef\xb8\x8f'
-> POS 0 -> 0 true - (0.075):
         b'Love can be tricky'
-> POS 0 -> 0 true - (0.021):
         b'@eperry2011 Wait...Japanese jazz fusion? \xf0\x9f\xa4\xaf'
-> POS 0 -> 0 true - (0.041):
         b"i'm enjoying this suns v lakers game."
-> POS 0 -> 0 true - (0.079):
         b'don\xe2\x80\x99t see why people be surprised i\xef\xb8\x8f play video games'
-> NEG 1 -> 1 true - (0.993):
          b'I hate nuts in my ice cream, like I\xe2\x80\x99m cool with them in my mouth sometimes but shit nigga not in my chocolate icecream. Fuck outta here'
-> NEG 1 -> 1 true - (0.978):
          b'How was that not a 3? Its cause they on the Spurs homecourt.. That shit was lame'
-> NEG 1 -> 0 true - (0.981):
          b'Niggas be using bitches for head &amp; pussy, but im wrong when I use yall for dick &amp; food. Smh yall not shit lmfaoo'
-> POS 0 -> 1 true - (0.069):
         b'Scared to update my iPhone smh \xf0\x9f\xa4\xa6\xf0\x9f\x8f\xbe\xe2\x80\x8d\xe2\x99\x82\xef\xb8\x8f'
```
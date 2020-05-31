## OLID 

```
===================================================================
        ../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv
===================================================================

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
860/860 [==============================] - 1s 1ms/sample - loss: 0.4178 - acc: 0.8349 - rec: 0.4979 - prec: 0.8273 - f1: 0.6111
[0.4178140885608141, 0.83488375, 0.4978712, 0.8273369, 0.6111303]

Scores on no proc test:
860/860 [==============================] - 1s 909us/sample - loss: 0.4015 - acc: 0.8442 - rec: 0.5569 - prec: 0.8033 - f1: 0.6463
[0.4015098609203516, 0.84418607, 0.55693257, 0.80334574, 0.64625055]

y_pred
------
-> POS 0 -> 0 true - (0.079):
         b'#Watching #Boomer getting the news that she is still up for parole always makes me smile. #Wentworth Finale...@USER is such a treasure. URL'
-> POS 0 -> 0 true - (0.045):
         b'5 Tips to Enhance Audience Connection on Facebook URL @USER #socialmedia #smm URL'
-> POS 0 -> 0 true - (0.092):
         b'#Conservatives - the party of low taxation \xf0\x9f\x98\x82 #Tories #Tory URL'
-> POS 0 -> 0 true - (0.062):
         b'#GreatAwakening #QAnon #PatriotsUnited #WWG1WGA #AreYouAwake  WHEN YOU ARE AWAKE YOU SEE CLEARLY \xe2\x9d\xa4\xef\xb8\x8f\xf0\x9f\xa7\xa1\xf0\x9f\x92\x9b\xf0\x9f\x92\x9a  Check out this video URL URL'
-> NEG 1 -> 1 true - (0.921):
          b'@USER Nigga ware da hits at'
-> POS 0 -> 0 true - (0.070):
         b'Always smack URL'
-> POS 0 -> 0 true - (0.063):
         b'#SilsilaBadallteRishtonKa tag is filled with appreciation of @USER only....   Never watched this serial but I always wanted appreciation for Aditi... She is underrated since starting of the show... She is worth of all this appreciation.. \xf0\x9f\x91\x8f\xf0\x9f\x91\x8f\xf0\x9f\x91\x8f'
-> NEG 1 -> 1 true - (0.904):
          b'@ ALL FAMILY/FRIENDS , do not tell me  bad shit that your bf/gf did to you just to go right back to them!!!'
-> POS 0 -> 1 true - (0.077):
         b'#ChristineBlaseyFord is your #Kavanaugh accuser... #Liberals try this EVERY time... #ConfirmJudgeKavanaugh URL'
-> POS 0 -> 0 true - (0.063):
         b'#osho #quotes via @USER Listen to your being. It is continuously giving you hints. It is a still, small voice. It does not shout at you, that is true. And if you are a little silent you will start feeling your way. Be the person you are. Never try\xe2\x80\xa6 URL URL'
-> POS 0 -> 0 true - (0.043):
         b'#YYC @USER  looking hockey players of all ages/abilities for our Humboldt Tribute game Sunday 9/16. Arrive 2pm, dress, participate in our opening ceremony. Contact lindsay.clothier@USER if you are interested! #WePlayForThem #HumboldtStrong #HockeyIsFamily #GoNucks'
-> POS 0 -> 0 true - (0.095):
         b'#Conservatives #Brexit putting #Britain last.  Sending a chill down the spine of the #UK.'
-> POS 0 -> 0 true - (0.088):
         b'#QuickTip: Find people already working in a company, or within the industry that you are interested in.  We know a lot of people! Send us your resume to info@USER or message us RIGHT NOW URL URL'
-> NEG 1 -> 1 true - (0.984):
          b"#ArianaAsesina? Is that serious?! Holy shit, please your fucking assholes, don't blame someone for the death of other one. She is sad enough for today, don't you see? It isn't fault of none, he had an overdose and died. End. Stop wanting someone to blame, fuckers."
-> NEG 1 -> 1 true - (0.955):
          b'......bitch what URL'
-> POS 0 -> 0 true - (0.073):
         b'#WELOVESEUNGCHEOL @USER   I am happy and proud of the work you have done to train seventeen along with the other members. I see you and you are wonderful and incredible. I really love u \xe3\x85\xa0\xe3\x85\xa0 \xf0\x9f\x92\x95. URL'
-> POS 0 -> 0 true - (0.023):
         b'0-9 : B-1, J-1, R-1, B-2, Q-2, B-3, BX-3, B-4, RB-4, Z-4, B-5, Q-5, B-6, H-6, B-7, H-7, UT-7, B-8 (20:59:36)'
-> POS 0 -> 0 true - (0.059):
         b'#DOJ employee resisters" r looking up conservatives\xe2\x80\x99 license plates, home addresses, legal details in LexisNexis 2give to Dem Socialists/Antifa-project Veritas.But don\'t worry, no govt in history has ever made political opponent lists and oppressed them\xf0\x9f\x99\x84 URL'
-> POS 0 -> 0 true - (0.062):
         b'#GreatAwakening #QAnon #PatriotsUnited #WWG1WGA #AreYouAwake  WHEN YOU ARE AWAKE YOU SEE CLEARLY \xe2\x9d\xa4\xef\xb8\x8f\xf0\x9f\xa7\xa1\xf0\x9f\x92\x9b\xf0\x9f\x92\x9a  Check out this video URL URL'
-> NEG 1 -> 1 true - (0.951):
          b'*gets all the bitches*'
-> POS 0 -> 0 true - (0.042):
         b'#gmm #roastmycat hi @USER  this is Fiona. She is about 10 weeks old. She falls asleep in weird places URL'
-> POS 0 -> 0 true - (0.071):
         b'#Halloween Sign If You Are Reading This #CreepingUp Behind You Wood Wall Decoration #tmtinsta #cwsigns  URL via @USER'
-> POS 0 -> 0 true - (0.079):
         b'And yet everyone seems to lack it URL'
-> NEG 1 -> 1 true - (0.901):
          b'@USER @USER @USER @USER Then why aren\xe2\x80\x99t there so many shootings in Virginia?  Jacksonville shooter got his guns IN MARYLAND!! Among the poster children for gun control!  What good did that do?!  You\xe2\x80\x99re full of crap.'
-> POS 0 -> 0 true - (0.036):
         b"$CERC is now Boyd's #1 stock. And he is the sole holder of the stock among hedge funds we track. URL"
-> POS 0 -> 0 true - (0.038):
         b'#Trump may be many things, but he is entertaining!!!! Thanks #twitter URL'
-> POS 0 -> 0 true - (0.093):
         b'.. Good thing it was responsible US Marines..  I\xe2\x80\x99m pretty sure a group of Antifa members wouldn\xe2\x80\x99t be running that fast in that direction to help anyone let alone elder seniors..  Thank you @USER ..  We salute You\xe2\x9d\x97\xef\xb8\x8f  @USER @USER  @USER URL'
-> POS 0 -> 0 true - (0.058):
         b'#fall #fashion #trending #coats #colors URL We have What You are looking for! #airdrie #calgary #lethbridge #toronto #vancouver #princegeorge URL'
-> POS 0 -> 0 true - (0.042):
         b'#gmm #roastmycat hi @USER  this is Fiona. She is about 10 weeks old. She falls asleep in weird places URL'
-> POS 0 -> 0 true - (0.034):
         b'#MonbebeSelcaDay she is beautiful URL'
-> POS 0 -> 0 true - (0.090):
         b'#LockHimUpNow #MAGA #QAnon @USER best President ever URL'
-> POS 0 -> 0 true - (0.065):
         b"#Liberals #Left #Democrats #Resist #Resistance #Antifa #BlueWave #BlueWave2018 It's \xf0\x9f\x91\x8c to #WalkAway \xf0\x9f\x91\x8d\xf0\x9f\x98\x86 \xf0\x9f\x87\xba\xf0\x9f\x87\xb8 \xf0\x9f\x87\xba\xf0\x9f\x87\xb8 \xf0\x9f\x87\xba\xf0\x9f\x87\xb8 #MAGA \xf0\x9f\x87\xba\xf0\x9f\x87\xb8 \xf0\x9f\x87\xba\xf0\x9f\x87\xb8 \xf0\x9f\x87\xba\xf0\x9f\x87\xb8   URL"
-> POS 0 -> 0 true - (0.062):
         b"#EmailMarketing #sales I will teach you how to create your own exclusive, online 'traffic economy' so you are never short of leads and sales again URL URL"
-> POS 0 -> 0 true - (0.036):
         b'@USER How sweet! Congratulations. Once he is house broken it will get better'
-> POS 0 -> 0 true - (0.078):
         b'#i2 This speaks for itself (NSFW) URL'
-> POS 0 -> 0 true - (0.097):
         b"#JameyComey has been so silent these last few weeks, because he knows he's going to be indicted. 13:35  #FBI #DOJ  #Strzok #Page #TextMessages  #QAnon  #PatriotsFight  ty .@USER  #MAGA  URL"
-> POS 0 -> 0 true - (0.078):
         b'Apple live keynote #AppleEvents   URL'
-> POS 0 -> 0 true - (0.090):
         b'#AntifaHorst - whuuuuut?! \xf0\x9f\x98\x82  #antifa #maassen #seehofer URL'
-> POS 0 -> 0 true - (0.075):
         b'#Antifa ........  Retweet if you can\xe2\x80\x99t stop watching this...   URL'
-> POS 0 -> 0 true - (0.048):
         b'#100NotOut Thank You for following!!  \xf0\x9f\x94\xb7 #Leicester \xf0\x9f\x94\xb9@USER #VoteForChange #LocalElections2019 \xf0\x9f\x94\xb9 #VoteTory #VoteConservative \xf0\x9f\x94\xb7 #CutCrime #CutRedTape #CutTaxes #CutGrass \xf0\x9f\x87\xac\xf0\x9f\x87\xa7#BetterServicesLowerTaxes \xf0\x9f\x87\xac\xf0\x9f\x87\xa7\xf0\x9f\x94\xb5'
-> POS 0 -> 1 true - (0.083):
         b"#MAGA #Qanon #GreatAwakening #inners #WWG1WGA #NowComesThePain #WalkAway #GoodbyeDemocrats   Ellison Accuser Says She's Been Sidelined By Her Own Party URL"
-> POS 0 -> 0 true - (0.070):
         b"#Truth I will show you how to build your own personal, online 'traffic economy' so you are never in short supply of qualified prospects and sales again URL URL"
-> POS 0 -> 0 true - (0.052):
         b'#Antifa has a new cause URL'
-> POS 0 -> 0 true - (0.069):
         b'#Balkan Conservatives Unite at #Family Congress in #Moldova URL'
-> POS 0 -> 0 true - (0.032):
         b'#BBCNews - Cleverly: There have been no cuts to the #NHS James Cleverly on #Conservatives and coalition health spending URL'
-> POS 0 -> 0 true - (0.054):
         b'#TheLadyBam has spoken! \xe2\x9d\xa4 She is simply the BEST! \xf0\x9f\x99\x8f\xf0\x9f\x8f\xbc #SpreadMaryLove \xf0\x9f\x91\xa0\xf0\x9f\x92\x83 #Onward URL'
-> POS 0 -> 0 true - (0.019):
         b'#ALERT   A win for the Progressive Conservatives.   The Ontario Court of Appeal has granted a stay of #Bill5,  which is to cut the number of Toronto city councillors from 47 to 25.'
-> NEG 1 -> 1 true - (0.954):
          b'#TheArchers I want to be brilliant at Karate so I can kick the shit out of everyone""'
-> POS 0 -> 1 true - (0.075):
         b'#DregsOfSociety  ??? #Deplorables   Liberals usually dehumanize those they want to exterminate later URL'
-> POS 0 -> 0 true - (0.050):
         b'#WCE To my favorite girl! Hope your day is as awesome as you are! URL'
-> POS 0 -> 0 true - (0.042):
         b'#DISARMTHEM #ANTIFA  Give Jack here a participation trophy! URL'
-> POS 0 -> 0 true - (0.078):
         b"#Osaka says the crowd was noisy and i really didn't c what was going on. i had to focus cuz she is such a great champ and was confused when the score went to 5-3."
-> POS 0 -> 1 true - (0.056):
         b'#BlueWave #DumpTrump \xe2\x80\xa6give my love 2, or cooperate/compromise w/, conservatives/Trump supporters who constantly vilify marginalized groups, who constantly attack women\xe2\x80\x99s rights 2 make choices about their own bodies,\xe2\x80\xa6'
-> POS 0 -> 0 true - (0.080):
         b'.@USER takes the season opener on Saturday. Highlights: URL'
-> POS 0 -> 0 true - (0.089):
         b'@USER @USER @USER Ummmm fascism actually started with Mussolini in Italy and Antifa is not a part of Anonymous. Anonymous does not censor like Antifa. They are not related as Anonymous is anti censorship URL'
-> NEG 1 -> 1 true - (0.911):
          b'#ArunJaitleyStepDown He is most shameless #FM in history of India and audacity and shamelessness with which is lies in public is disgrace to post.'
-> POS 0 -> 0 true - (0.074):
         b"#Canada's Liberal government rejects @USER recommendation that political parties comply with #privacy laws after #Facebook / #CambridgeAnalytica scandal URL"
-> NEG 1 -> 1 true - (0.936):
          b"2 weeks of resp done and I still don't know shit my ass still on vacation mode \xf0\x9f\x98\xaa"
-> POS 0 -> 0 true - (0.094):
         b'#Analysis: Supporters of the People\'s Party of Canada would likely bristle at being called liberal," but its beliefs fit the classic definition. URL @USER'
-> POS 0 -> 0 true - (0.055):
         b'#Conservatives today... URL'
-> POS 0 -> 0 true - (0.079):
         b'#Antifa #UKLabour, #FBPE, #SUTR  Pay Attention!  This is what #ForBritain is fighting against - you? URL'
-> NEG 1 -> 1 true - (0.950):
          b'@USER These are all  coranated attacks from idiot loons! They will get worse much worse before the election! Can u imagine idiots who want to get rid of the economy and their 401 along with interest rates just because he is not a polished politician? Idiots!'
-> POS 0 -> 0 true - (0.067):
         b'#Censorship  Awake yet?  Ask yourself why these conservatives are being censored? #WalkAway URL'
-> POS 0 -> 0 true - (0.038):
         b'#ICYMI: Welcome Anna Grey Barbour to our Women\xe2\x80\x99s Volleyball Team! Anna is a 2018 Terry Sanford High School graduate. She is studying dental hygiene at our college. We\xe2\x80\x99re proud to make you a Trojan, Anna. Good luck this season! #BlackNGold #Trojans \xf0\x9f\x8f\x90\xf0\x9f\x96\xa4\xf0\x9f\x92\x9b URL'
-> NEG 1 -> 1 true - (0.936):
          b'And\xf0\x9f\xa4\xb7\xf0\x9f\x8f\xbd\xe2\x80\x8d\xe2\x99\x82\xef\xb8\x8f females b on the same shit URL'
-> POS 0 -> 0 true - (0.025):
         b'#Brexit #UKLabour #Labour #Conservatives #PlaidCymru #Greens #Politics #EU URL  - POLL'
-> POS 0 -> 0 true - (0.011):
         b'#BreakingNews, via NYT The New York Times URL'
-> POS 0 -> 0 true - (0.049):
         b'#Sugardaddy Retweet if you are under 30 and you want 400$ daily USA,Canada and UK only #sugarbabyneeded #sugarbabywanted #findom #sugarbaby #Canada'
-> POS 0 -> 0 true - (0.044):
         b'#CarolineForbes You are needed to help with the posted SL. DM me to Audition.'
-> POS 0 -> 0 true - (0.090):
         b'@USER He is obviously getting suspended. He is not an asset for anyone'
-> POS 0 -> 0 true - (0.045):
         b'(URL You can\'t summarize the rankings of a game mode in just one picture" URL'
-> POS 0 -> 0 true - (0.042):
         b'#Emmys sooo lovely I love the dress colour and the design looks like fairy tales and she is very tender \xf0\x9f\x8c\xac URL'
-> POS 0 -> 0 true - (0.042):
         b'An open letter to Mac Miller URL'
-> NEG 1 -> 1 true - (0.982):
          b'!!!!bitch i\xe2\x80\x99m fucking coming back URL'
-> NEG 1 -> 1 true - (0.913):
          b'$uicideboy$ ON HALLOWEEN its aboout to get sooooo FUCKING spooky'
-> POS 0 -> 0 true - (0.073):
         b"@USER He does. And I'm glad he always goes out on something reckless to show who he is going out and coming back everytime! Jeff is the best!!!"
-> POS 0 -> 0 true - (0.071):
         b'#SandraOh...OH how I love that you brought your parents...they (and you) are the epitome of grace and beauty!'
-> POS 0 -> 0 true - (0.098):
         b'#NationalDayofEncouragement #EncouragementDare Therefore #encourage one another and build each other up, just as in fact you are doing!! #Thessalonians #scripture #verse To donate, go to our website(link in bio!), call 404-478-9794 or email donate@USER #community URL'
-> POS 0 -> 1 true - (0.052):
         b'#ArrestGeorgeSoros He Funds #DomesticTerrorists #Antifa URL'
-> POS 0 -> 0 true - (0.049):
         b'#Interesting  Has she gone through any kind of background check similar to the 6 #FBI background checks that #JudgeKavanaugh has? URL'
-> POS 0 -> 1 true - (0.051):
         b'#Conservatives Govt have run up debt in spite of austerity cuts while the rich have doubled their wealth. #inequality  URL via @USER'
-> POS 0 -> 0 true - (0.019):
         b'#ALERT  A win for the Progressive Conservatives.   The Ontario Court of Appeal has granted a stay of #Bill5,  which is to cut the number of Toronto city councillors from 47 to 25.'
-> POS 0 -> 0 true - (0.085):
         b'#WCW #WCE @USER  It\xe2\x80\x99s your special day of the week again. I really miss you and I\xe2\x80\x99m looking forward to see you soon. Don\xe2\x80\x99t forget that I love you. I love you with all my heart because you are my heart! \xe2\x9d\xa4\xef\xb8\x8f URL'
-> POS 0 -> 0 true - (0.077):
         b'#Martina #Navratilova: What #SerenaWilliams Got Wrong   via @USER Be always really liked and respected Martina and here she is the voice of reason. URL'
-> POS 0 -> 0 true - (0.029):
         b'#Backto60 #OneVoice #1950swomen #1950sbornwomen   @USER TOOK SIX YEARS OF OUR PENSIONS  We all agree. WE NEED OUR PENSIONS BACK! URL'
-> POS 0 -> 1 true - (0.071):
         b'#BiggBossTelugu2 how many of you #KaushalArmy cum @USER fans... URL'
-> POS 0 -> 0 true - (0.092):
         b"#CastingCallShow was fantastic!! At first I didn't think I was going to like any of the finalists' shows, but ended up loving all 3. I ultimately voted for An Amazing Business Opportunity by Anna Ladd. She is so funny and I really want to hear more."
-> POS 0 -> 0 true - (0.045):
         b'#LisaxMichaelKors she is sooo talented, love hr too much URL'
-> NEG 1 -> 1 true - (0.924):
          b'#Kalyani is a very stupid teenager. I totally despise her for the atrocities she is doing towards Aunty Anupriya. She blames her for her mom\xe2\x80\x99s death. She should stop and listen to Anupriya side of the story before she makes vile accusation   #TujhseHaiRaabta #ZeeTVSerials'
-> NEG 1 -> 1 true - (0.924):
          b'#Kalyani is a very stupid teenager. I totally despise her for the atrocities she is doing towards Aunty Anupriya. She blames her for her mom\xe2\x80\x99s death. She should stop and listen to Anupriya side of the story before she makes vile accusation   #TujhseHaiRaabta #ZeeTVSerials'
-> POS 0 -> 0 true - (0.095):
         b'#parikshitsolutions Security incidents rarely emerge fully formed with flashing lights to alert you. See if you\xe2\x80\x99re prepared by testing your skills in the following scenario. URL URL'
-> POS 0 -> 0 true - (0.098):
         b'#Analysis: Supporters of the People\'s Party of Canada would likely bristle at being called liberal," but its beliefs fit the classic definition. URL don_pittis"'
-> POS 0 -> 0 true - (0.045):
         b'3,000 is definitely a tad high Puerto Rico. How about you DemocRATS provide proof? Providing names,  locations, and next of kin shouldn\xe2\x80\x99t be that hard.  I hope you don\xe2\x80\x99t mind, but I will not be holding my breath. URL via @USER URL'
-> POS 0 -> 0 true - (0.066):
         b'#BroncoNation #broncos #BroncosVsSeahawks #BroncosCountry Crue was excited for the win she is enjoying her cupcake Go Broncos URL'
-> POS 0 -> 0 true - (0.054):
         b'And why is my hair pink now \xf0\x9f\x98\x82\xf0\x9f\x98\x82\xf0\x9f\x98\x82\xf0\x9f\x98\x82 URL'
-> POS 0 -> 0 true - (0.080):
         b'#SelfCareSeptember You are making a difference! @USER @USER @USER @USER @USER @USER @USER @USER @USER URL'
-> POS 0 -> 0 true - (0.082):
         b'#AndrewScheer wants support from #CanadianCoalitionforFirearmsRights, seeking weakened #guncontrol. #CPC compromised Canadians\xe2\x80\x99 safety enough for these votes by diluting controls. How many lives lost before #Conservatives care? #cdnpoli /via @USER URL'
-> POS 0 -> 0 true - (0.071):
         b'Are we all ready to sit and watch Indakurate Passcott play football?'
-> POS 0 -> 0 true - (0.089):
         b'And dicks. URL'
-> NEG 1 -> 1 true - (0.954):
          b'#OrrinHatch I can\xe2\x80\x99t believe this sexist , clueless, old fart gets to weigh in on another woman\xe2\x80\x99s charges against a Supreme Court nominee. And he is spouting the same old nasty shit he spewed 20+ years ago against Anita Hill. His time\xe2\x80\x99s up! Good riddance Neanderthal!'
-> POS 0 -> 0 true - (0.086):
         b'#BrettKavanaugh   .... social issues being one for Justice Kennedy, but there were other areas where there was growing daylight between him and conservatives, for example in the area of the administrative state, incl. the EPA....'
-> POS 0 -> 0 true - (0.072):
         b'#NowPlaying Arise (You Are Good) - William Murphy on URL  or  URL #ChroniclesChristianRadio #ccradioco'
-> POS 0 -> 0 true - (0.082):
         b'#AIATravelTips Always monitor your luggage at the airport. Do not leave your luggage unattended and do not accept unopened packages.  ---- #Tips #Travel #Explore #AIA #Aircraft #Airport #Caribbean #Destination #Travelling #Connect #TravelTheWorld #Adventure #Adventures #Luggage URL'
-> POS 0 -> 0 true - (0.039):
         b'Always a good day when I get a new member on my site URL'
-> POS 0 -> 0 true - (0.020):
         b'#RealSmart Answer: This is step #1 on your #RealSmart journey! This course is only offered through UBC on behalf of the Real Estate Council of BC by correspondence. Once registered, you are all set to take our #realsmart course! URL'
-> POS 0 -> 0 true - (0.067):
         b'#VT200: @USER is back at @USER for the first time since the year 2000. He is on the pole for the $10,000 to win Vermont 200.  Updates at @USER URL'
-> NEG 1 -> 1 true - (0.965):
          b'And have a bitch thinking you niggas have money and you tf don\xe2\x80\x99t.'
-> POS 0 -> 0 true - (0.063):
         b"#AuthorConfession Day 14: Which tree is your MC's favorite?   I tried to ask Lisette, and she responded with any tree that has flowers. I don't know what to do with her, she won't give me a straight answer. Usually, she's not this difficult, so I suspect she is teasing me. \xf0\x9f\x98\x85\xf0\x9f\x92\x9e URL"
-> POS 0 -> 0 true - (0.087):
         b'#Nattyanplaying AOZORA TRAIN - SiSH(She is so high)'
-> POS 0 -> 0 true - (0.028):
         b'#Antifa excellent idea URL'
-> POS 0 -> 0 true - (0.067):
         b"#IOU project has demonstrated a quality Whitepaper. If you are an ICO-investor, I'm strongly recommend that you explore it, at any rate you will please it. #ico #Crypto #tokensale URL URL"
-> POS 0 -> 0 true - (0.088):
         b'#KavanaughConfirmationHearings #TuesdayThoughts  the women who support #Kavenaugh should fill the hearing gallery. PACK it full so the disruptive liberals cant get in STAND in unison while Kavanaugh testifies *** SOLIDARITY !  cc: @USER @USER'
-> POS 0 -> 0 true - (0.048):
         b'#NaomiOsaka folks. #USOpen The future is here and she is so adorable just as she is talented'
-> POS 0 -> 0 true - (0.059):
         b'#MAGA  .... sounds fair. URL'
-> POS 0 -> 0 true - (0.099):
         b'#MuskokaLakes mayoralty candidate Terry Ledger says she is running her mayoral campaign via social media only. We say this speaks volumes to the kind of behind-closed-doors mayor she plans to be. What do you say Muskoka? Give us your opinion. URL'
-> POS 0 -> 0 true - (0.062):
         b'#GreatAwakening #QAnon #PatriotsUnited #WWG1WGA #AreYouAwake  WHEN YOU ARE AWAKE YOU SEE CLEARLY \xe2\x9d\xa4\xef\xb8\x8f\xf0\x9f\xa7\xa1\xf0\x9f\x92\x9b\xf0\x9f\x92\x9a  Check out this video URL URL'
-> NEG 1 -> 1 true - (0.961):
          b'2018 not surprised it starts from the top!!!  Karma a bitch watch!!!! URL'
-> POS 0 -> 1 true - (0.098):
         b'#Hillary and @ least 16 other #AngryDemocrats #WorldWarQ #WWG1WGA #MAGA #RedTsunami #AmericaFirst #WalkAway #Truth URL'
-> POS 0 -> 0 true - (0.053):
         b'#CodetrainQueens Rachel joined Codetrain in 2017 and helped to organize the Codetrain App Developer Bootcamp and trained as a front end developer. Currently the community manager, she is an ardent advocate for digital skills for youth, especially women. Keep shining, Rachel! URL'
-> POS 0 -> 0 true - (0.083):
         b'#MovieFightsLive @USER @USER your all thinking it... you KNOW you are... URL'
-> NEG 1 -> 1 true - (0.958):
          b'#Hypocrites #DemocratsHateAmerica #LiberalismIsAMentalDisorder EVERYTHING LIBERALS TOUCH TURNS TO ABSOLUTE SHIT... URL'
-> POS 0 -> 0 true - (0.077):
         b'#NationalDayofEncouragement  #TwitterFamily  You\xe2\x80\x99re amazing just the way you are \xf0\x9f\x92\x9f\xe2\x98\xae\xef\xb8\x8f URL'
-> POS 0 -> 0 true - (0.071):
         b'#VaquitaMarina #SaveTheVaquita @USER  @USER  There are less than 12 #Vaquitas left!!!! She is extinguishing!!! Please help!!! Be their voice!l! URL'
-> POS 0 -> 0 true - (0.047):
         b"#Success #Health I will show you the best way to create your own exclusive, online 'traffic economy' so you are never short of qualified prospects and sales again URL URL"
-> NEG 1 -> 1 true - (0.956):
          b'1 tf. He saw that shit. URL'
-> NEG 1 -> 1 true - (0.939):
          b"Anyone who finds M*neta's behavior funny can fuck off and die"
-> NEG 1 -> 1 true - (0.934):
          b'@USER Damn I felt this shit. Why you so loud lol'
-> POS 0 -> 0 true - (0.032):
         b'#MyProtege, a #k12 #Master #Teacher was very excited to report she is the proud owner and supporter of products made by @USER @USER #Bravo! #USOpen'
-> POS 0 -> 0 true - (0.083):
         b'10 years ago today, Taylor Swift released her smash hit \xe2\x80\x98Love Story\xe2\x80\x99. Quote this tweet telling the moment you first heard the song #10YearsOfLoveStory URL'
-> POS 0 -> 0 true - (0.055):
         b'#Chefs, are you in need of some new pans? Find what you are looking for at URL We stock top brands such as Beka Chef, Mauviel and Woll. \xf0\x9f\x8d\xb3\xf0\x9f\xa5\x98\xf0\x9f\x8d\xb2 #chef #restaurants URL'
-> NEG 1 -> 1 true - (0.927):
          b'$b album definitely worth the fucking wait'
-> POS 0 -> 0 true - (0.046):
         b'@USER HIS FANS ARE HAPPY. HE SPREADS LOVE AND BECAUSE OF HIM I LEARNED TO APPRECIATE AND SUPPORT THE LGBTQ. I LOVE HIM  BECAUSE HE NEVER FAILED TO MAKE ME HAPPY. I LOVE HIM BECAUSE HE IS HARRY STYLES AND HARRY STYLES IS THE BEST.'
-> NEG 1 -> 1 true - (0.916):
          b'Ain\xe2\x80\x99t nobody shit if you ask me... including myself.'
-> POS 0 -> 0 true - (0.072):
         b'#MISSING: Imelda Algiers was last seen at about 3 p.m. Sunday.  She is about 5\xe2\x80\x9904\xe2\x80\x9d tall, weighs about 110 pounds, and has white hair. It is unknown what Imelda was wearing. Imelda is diagnosed with Alzheimer\xe2\x80\x99s Disease.  #WestBend URL'
-> POS 0 -> 0 true - (0.064):
         b'#Travel #Movies and Unix #Fortune combined  Visit #Salisbury, see the sights, but wherever you go there you are, the same old you, why not travel as an international spy? Find yourself at the centre of a vast international conspiracy when you return home.   Recall Recall Recall.'
-> POS 0 -> 0 true - (0.085):
         b"#SaveShadowhunters #MalecForever Read Mansikka's latest cause she is awesome. URL"
-> POS 0 -> 0 true - (0.075):
         b"#Brexit is dead. Not because the other EU states won't cooperate, but because the Conservatives have no viable plan to keep it alive. We must have a new vote to carry on playing a central role in the EU, or be buried with Brexit. URL"
-> POS 0 -> 0 true - (0.037):
         b'#WFMMC A very talented team because you are such a prestigious project. An excellent project to promote big market projects. #WFMMC #IcO #Ekolong #Sripuptruzman'
-> POS 0 -> 0 true - (0.036):
         b'@USER this girl is so talented and she is my best friend because you and Ethan brought us together. Please notice this talent. @USER @USER @USER  please\xf0\x9f\x92\x9c\xf0\x9f\xa7\xa1\xf0\x9f\x92\x9c\xf0\x9f\xa7\xa1\xf0\x9f\x92\x9c\xf0\x9f\xa7\xa1\xf0\x9f\x92\x9c\xf0\x9f\xa7\xa1\xf0\x9f\x92\x9c\xf0\x9f\xa7\xa1\xf0\x9f\x92\x9c\xf0\x9f\xa7\xa1\xf0\x9f\x92\x9c\xf0\x9f\xa7\xa1\xf0\x9f\x92\x9c\xf0\x9f\xa7\xa1 URL'
-> POS 0 -> 0 true - (0.070):
         b'9/9/2018 7:00 PM Temp 65.4  Dew Pt 51.1 Barometer 29.997 inches Rain 0.00 Wind 1.8 mph Hi 69.0 at 2:35 PM Low 59.8 at 7:20 AM'
-> POS 0 -> 0 true - (0.076):
         b'#Conservatives VOTE VOTE VOTE, TAKE TWO FRIENDS TO POLLS to MIDTERMS in Nov. #NoComplacency\xe2\x80\xbc\xef\xb8\x8f\xe2\x80\xbc\xef\xb8\x8f URL'
-> NEG 1 -> 1 true - (0.941):
          b'// SO WANT TO KICK TWITTERFUCK ASS.'
-> POS 0 -> 0 true - (0.069):
         b'#RIPMacMiller you are loved. \xf0\x9f\x92\x9a URL'
-> NEG 1 -> 1 true - (0.935):
          b'@USER fuck'
-> NEG 1 -> 1 true - (0.905):
          b'. a grown ass woman, probably 10 years older than me is currently spreading rumors rather than talking to me about it, nice work you got there satan \xe2\x9d\xa4\xef\xb8\x8f'
-> POS 0 -> 0 true - (0.047):
         b'#Antifa #Philly: Keystone United Exposed Part 2: Robert and Melissa Gaus URL'
-> NEG 1 -> 1 true - (0.908):
          b'#IDIOTS Is there nothing beneath them? Lol. What fools Liberals are! #MAGA #KAG \xf0\x9f\x87\xba\xf0\x9f\x87\xb8\xf0\x9f\x87\xba\xf0\x9f\x87\xb8\xf0\x9f\x87\xba\xf0\x9f\x87\xb8\xf0\x9f\x87\xba\xf0\x9f\x87\xb8\xf0\x9f\x87\xba\xf0\x9f\x87\xb8 URL'
-> POS 0 -> 0 true - (0.077):
         b'#DISARMTHEM  #ANTIFA   GOOD LUCK SWEETHEARTS URL'
-> POS 0 -> 0 true - (0.072):
         b'#AGJeffSessions: \xe2\x80\x9cListen To The ACLU, Antifa, Black Lives Matter\xe2\x80\x99 If You Want More Chicago Shootings!!\xe2\x80\x9d @USER @USER  #2AShallNotBeInfringed  Thank You @USER  URL via @USER'
-> NEG 1 -> 1 true - (0.979):
          b'#SugarDaddy Retweet if you are under 30 and would like share memes with each other and we can talk about dumb shit. Cuz baby I\xe2\x80\x99m broke as shit but this love rich URL'
-> POS 0 -> 0 true - (0.070):
         b"@USER Sam's being sam ...she is resting now it's adorable"
-> POS 0 -> 0 true - (0.070):
         b"#FridayNightFun!!   With Halloween events starting in just a week, we of course have to find out what events you are looking forward to most this year.   Obviously, this isn't all of them. There are SO many out there now. URL"
-> POS 0 -> 0 true - (0.099):
         b"#1A #2A   This makes 7 times its been pulled down, @USER , @USER  8th time I've posted it. You pull it down,  I'll repost.  Eric Holder on gun control.  URL"
-> POS 0 -> 0 true - (0.074):
         b'$2,000 iPhone \xe2\x80\x94 gulp. Tech Reporter Josh McConnell breaks down the features and price points of Apple\xe2\x80\x99s new line URL @USER URL'
-> POS 0 -> 0 true - (0.076):
         b'#Conservatives You cannot ride this one out\xe2\x80\xbc\xef\xb8\x8f\xf0\x9f\x87\xba\xf0\x9f\x87\xb8#VoteRed2018 #VoteAmericaFirst #VoteDemsOut #AmericaFirst \xf0\x9f\x87\xba\xf0\x9f\x87\xb8 URL'
-> POS 0 -> 0 true - (0.072):
         b'@USER She is beyond famous. She is Lalisa Manoban \xf0\x9f\x98\x8e URL'
-> NEG 1 -> 1 true - (0.912):
          b'(cr1tikal voice) smef my ass cheeks'
-> POS 0 -> 0 true - (0.086):
         b'@USER #DuckDuckGo!!F Google!'
-> POS 0 -> 0 true - (0.019):
         b'#California Pushing 8 New #Gun Control #Laws \xe2\x80\x93 The Legal Brief ~ VIDEO! URL (via @USER )'
-> POS 0 -> 0 true - (0.090):
         b"#Art #Culture BoJack Horseman Recap: The Apology Tour: Episodes of BoJack Horseman have taken on social issues before. Last season's gun control episode stands out as a shining example, and the show has always had the ability.. via URL URL"
-> POS 0 -> 0 true - (0.057):
         b"#Charlottesvile speech #Trump should've given. URL #tcot #cville #Conservatives #CharlottesvilleKKK #Liberty #GOP"
-> POS 0 -> 0 true - (0.087):
         b'@USER She is better than you.'
-> POS 0 -> 0 true - (0.072):
         b'#Nintendo #AnimalCrossing #SmashBrosUltimate  a little late... But she is just so adorable! I do love Isabelle URL'
-> NEG 1 -> 1 true - (0.938):
          b'#ibelieveblaseyford is liar she is fat ugly libreal #snowflake she sold her  herself to get some cash !! From dems and Iran  ! Why she spoke after  #JohnKerryIranMeeting ?'
-> POS 0 -> 0 true - (0.099):
         b"@USER I've been watching it....She is on our TEAM now. She has some insight into this President that's for sure."
-> POS 0 -> 0 true - (0.079):
         b'#MAGA #KAG2018 U.S. becomes EU\xe2\x80\x99s top supplier of soybeans, strengthening President Trump\xe2\x80\x99s trade deal - URL'
-> POS 0 -> 0 true - (0.068):
         b'#PNP. Results are not out yet for the PNP Vice Presidential race. Those supporting Damion Crawford feel comfotable that he is in.'
-> POS 0 -> 0 true - (0.100):
         b'#WCW goes to my beautiful and sexy @USER Without you I would be lost, you have brought me from the dark and into the light and you are my world. Love you so much. URL'
-> POS 0 -> 0 true - (0.053):
         b',,,just giving #Antifa what they asked for. So what is the problem? URL'
-> NEG 1 -> 1 true - (0.942):
          b'#LifeIsButepu when you are black and can say the word nigga". Feel me my niggas??? URL'
-> POS 0 -> 0 true - (0.090):
         b'#BenJones, Assistant Director of @USER at @USER Republican Party, Conservatives, and the Future of Capital Punishment. URL @USER @USER @USER @USER @USER #deathpenalty'
-> POS 0 -> 0 true - (0.094):
         b'#BREAKING: #ChristineBlasey Ford Published Eight studies about #Abortion Pill" and Works for Company that Produces It  URL   #CorceptTherapeutics Inc.  $CORT #RU486 #Liberals  #Kavanaugh v #CORT #RoevWade #KavanaughConfirmation  @USER @USER URL'
-> POS 0 -> 0 true - (0.093):
         b'#YehUnDinonKiBaatHai i have a special corner for people who define simplicity is the real beauty and after a long time, there is @USER among so many actresses who is personifying this in true sense.   She is just so stunning naturally.\xe2\x9d\xa4\xef\xb8\x8f\xf0\x9f\x92\x95 URL'
-> POS 0 -> 0 true - (0.076):
         b'10 minutes in to Instinct and I love it #AlanCummings #Instinct #Intriguing'
-> POS 0 -> 0 true - (0.080):
         b'@USER @USER @USER @USER @USER Look no further than Chicago or Baltimore as examples of strict gun control laws NOT being effective.'
-> POS 0 -> 0 true - (0.040):
         b'#WeLoveSergioBecause he is a angel and is so pure and so sweet and loves and supports us as much as we love and support him not to mention he is the dancing KING in irl. Love you seg \xf0\x9f\x92\x93 @USER URL'
-> POS 0 -> 0 true - (0.079):
         b'#ConstitutionalDecay isn\xe2\x80\x99t an abstraction. It manifests in every debate where words written in 1787 fall short of providing a useful or relevant framework in 2018. It\xe2\x80\x99s at the root of issues as diverse as gun control, abortion, data privacy, and healthcare. For instance, 8/'
-> POS 0 -> 0 true - (0.060):
         b'@USER And she is a sweetheart.  I hope she gets well soon. Be patient and strong Mr. Capullo.'
-> POS 0 -> 0 true - (0.056):
         b'#BBCbias   #wato   Conservatives built more than twice as much council housing as Labour, who wrecked the economy and almost bankrupted the country ! URL'
-> POS 0 -> 0 true - (0.087):
         b'11:11 @USER follows me!'
-> POS 0 -> 0 true - (0.056):
         b'@USER @USER Awe cute he is cute'
-> POS 0 -> 0 true - (0.061):
         b'#WednesdayWisdom #loveLibraries #Lovetoread Share with us, what you are reading this Wednesday? URL'
-> POS 0 -> 0 true - (0.031):
         b'@USER #Google is awesome'
-> POS 0 -> 0 true - (0.087):
         b"#Kavanaugh #ProfessorChristineFord This started a story he said, she said. Now it's become Liberals vs Conservatives URL"
-> NEG 1 -> 1 true - (0.930):
          b'0-1 lost my acca on the first fucking fight cba'
-> NEG 1 -> 1 true - (0.955):
          b'#LiberalismIsAMentalDisorder #Hypocrites #DemocratsHateAmerica #DemocratsAreDangerous EVERYTHING LIBERALS TOUCH TURNS TO ABSOLUTE SHIT. URL'
-> POS 0 -> 0 true - (0.035):
         b'#ANTIFA grueling training! Goes much better in the video game.\xf0\x9f\xa4\xa3 URL'
-> POS 0 -> 0 true - (0.033):
         b'$69.64 - Best Price Asmodee Board Game, Various  URL'
-> POS 0 -> 0 true - (0.089):
         b'#NOWPLAYING Interview with Monique Rochon she is starring in \xe2\x80\x9cPulpit Secrets\xe2\x80\x9d on September 22 at Landis Theater in Vineland Listen at URL #TheLounge'
-> NEG 1 -> 1 true - (0.936):
          b'88% of these niggas have podcasts and YouTube channels dedicated to this and shit ain\xe2\x80\x99t getting solved so URL'
-> NEG 1 -> 1 true - (0.967):
          b'Anytime I randomly bust out laughing it\xe2\x80\x99s because I remembered some dumb shit Albria said \xf0\x9f\x98\xad\xf0\x9f\x98\xad'
-> POS 0 -> 0 true - (0.083):
         b"#ClimatChange ticks conservatives off. It is hard on their belief system. A rain of toadstools or locusts, no problem. This much Actual rain, unbelievable. Good article full of quotes. It's not my words. URL via @USER URL"
-> NEG 1 -> 1 true - (0.942):
          b'5k Bitches \xf0\x9f\x8e\x89\xf0\x9f\x92\x99'
-> POS 0 -> 0 true - (0.047):
         b'@USER @USER She is an advocate and model for natural beauty.'
-> NEG 1 -> 1 true - (0.905):
          b"#Conservatives just like old #Garbage bags blowing in the wind, here's an old garbage bag now... URL"
-> POS 0 -> 0 true - (0.097):
         b'#Arizona #Tennessee  #Alaska #SC  As soon as these RINOS (aka liberals) are up for reelection vote them out!   #DrainTheSwamp \xf0\x9f\x92\xa5 URL'
-> POS 0 -> 0 true - (0.044):
         b'#BREAKING ITS OFFICIAL! @USER music video for #GTFO has just reached 2 MILLION views on YouTube AND she is still #1 on the US itunes Music Video Charts! Keep streaming #lambs \xf0\x9f\xa6\x8b URL'
-> POS 0 -> 0 true - (0.087):
         b"#Believe I'm going to teach you ways to create your own exclusive, online 'traffic economy' so you are never in short supply of qualified prospects and sales again URL URL"
-> POS 0 -> 0 true - (0.089):
         b'#Trump is going to visit victims of #HurricaneFlorence. #Antifa is planning a rally. In the meantime, they will party. Boats and Bros"  #antifascist #MAGA #KAG #WWG1WGA #GreatAwakening #QAnon #QArmy #FlorenceAftermath #FlorenceNC #NorthCarolina URL'
-> POS 0 -> 0 true - (0.025):
         b'4chan is Hunting Antifa URL via @USER'
-> POS 0 -> 0 true - (0.026):
         b'#WomenWednesday: Meet multiple-award-winning designer @USER BFA 82. She is the in-demand @USER grad is behind @USER recent redesign: URL    Lacava, centre, is pictured with classmates at #Concordia in 1981. #CUalumni URL'
-> POS 0 -> 0 true - (0.051):
         b'#NuevaFotoDePerfil Pic by: @USER  You are awesome! URL'
-> POS 0 -> 0 true - (0.062):
         b'#GreatAwakening #QAnon #PatriotsUnited #WWG1WGA #AreYouAwake  WHEN YOU ARE AWAKE YOU SEE CLEARLY \xe2\x9d\xa4\xef\xb8\x8f\xf0\x9f\xa7\xa1\xf0\x9f\x92\x9b\xf0\x9f\x92\x9a  Check out this video URL URL'
-> POS 0 -> 0 true - (0.087):
         b'#ChooseCruz  let CA and NY  have the LIBERALS  #DontCAmyTEXAS URL'
-> POS 0 -> 0 true - (0.095):
         b'#Conservatives thanks to Tory doctrinaire policies we are all going back in time and losing hard one benefits and prosperity. Go forward with our EU partners URL'
-> NEG 1 -> 1 true - (0.991):
          b'100 Round Goon Bitch Is You Kiddin Me\xf0\x9f\xa4\xa3'
-> POS 0 -> 0 true - (0.059):
         b'#HurricaneFlorence is producing up to 40in of RAIN. Please be safe. URL'
-> POS 0 -> 0 true - (0.097):
         b'@USER @USER @USER Scott Gottlieb doesn\xe2\x80\x99t know what\xe2\x80\x99s an opiod and what\xe2\x80\x99s not. He\xe2\x80\x99s definitely not an expert on anything. However he is a expert at reading bank statements and counting money.'
-> POS 0 -> 0 true - (0.092):
         b'Angels now have 6 runs. Five of them have come courtesy Mike Trout homers. Trout connects on a 3-2 pitch with runners on second and third'
-> POS 0 -> 0 true - (0.077):
         b'#California leads the way in gun safety. URL'
-> POS 0 -> 0 true - (0.076):
         b"#SundayShoutOuts to @USER because.... Because she is amazing and has my boundless support and endless appreciation for her support in return, it's just a loop of love and respect\xe2\x80\xa6 URL"
-> POS 0 -> 0 true - (0.044):
         b'#BESTPOTUSEVER #LOVEMYPRESIDENT #MAGA #BRILLIANT #WINNING #MASTERNEGOTIATOR @USER thank you! URL'
-> POS 0 -> 0 true - (0.074):
         b'#Angel_Dad: If Lawmakers Really Cared About Citizens, They Would Secure the Border URL via @USER URL'
-> NEG 1 -> 1 true - (0.997):
          b'@USER nigga are you stupid your trash dont play with him play with your bitch \xf0\x9f\x98\x82'
-> POS 0 -> 0 true - (0.079):
         b'#JoyfulGlitz#Younique#Blessed#MomLife URL'
-> POS 0 -> 0 true - (0.075):
         b'#HaveYourSay: If you live in #Garston, Jane wants to hear your views on the location of a new Community Police Station. She is proposing to open a new accessible community base in the South Liverpool NHS Treatment Centre on Church Road. What do you think?  URL URL'
-> POS 0 -> 0 true - (0.096):
         b'#Repost @USER with get_repost \xe3\x83\xbb\xe3\x83\xbb\xe3\x83\xbb Happy 34th to the one and only Prince Harry, The Duke of Sussex. \xf0\x9f\xa5\x82 He is such a grounded, compassionate guy, taking after his mother, and I\xe2\x80\x99m\xe2\x80\xa6 URL'
-> POS 0 -> 0 true - (0.048):
         b'#FeelsGoodGirl @USER @USER  you should be proud at her she is amazing in gambit URL'
-> NEG 1 -> 0 true - (0.951):
          b'@USER I guess that\xe2\x80\x99s where swamp ass originated'
-> POS 0 -> 0 true - (0.046):
         b'#Brexit Deal Has Been Reached with #EU?!  Hold onto your hats!  #HardBrexit #BrexitDeal #ChequersDeal #ChuckChequers #MBGA #MEGA #MCGA #MAGA #Conservatives #Patriots #MayOut #MayMustGo URL'
-> POS 0 -> 0 true - (0.077):
         b"*a reminder that david harcourt's 1972 classic EVERYONE WANTS TO BE FUEHRER: A HISTORY OF NATIONAL SOCIALISM IN AUSTRALIA AND NEW ZEALAND is avail as a pdf: #antifa #auspol #FCKNZS URL"
-> POS 0 -> 0 true - (0.075):
         b'#WCW my Zamalek.Zamo!Mapholoba!She was my first friend in Uni upto today she is still my muntu!I love you Pholobs! 8 years strong! @USER   \xe2\x9d\xa4\xef\xb8\x8f\xe2\x9d\xa4\xef\xb8\x8f\xe2\x9d\xa4\xef\xb8\x8f URL'
-> NEG 1 -> 1 true - (0.980):
          b'And she has a pet??? Fucking disgusting URL'
-> POS 0 -> 1 true - (0.093):
         b'#LiberalHypocrisy #TacoBell When Liberals ask why your against illegal immigration? Taco Bell Employee: No Habla Ingles!" URL'
-> POS 0 -> 0 true - (0.060):
         b'.@USER \xe2\x80\x98Listen To The #ACLU, #Antifa, #BlackLivesMatter\xe2\x80\x99 If You Want More Chicago Shootings URL via @USER  #Sessions'
-> POS 0 -> 0 true - (0.042):
         b'#Trademark Attorney Daniela Paull will be in Paris next week attending the 32nd Annual @USER conference - do get in touch if you are also attending and would like to set up a meeting URL #IP'
-> POS 0 -> 0 true - (0.099):
         b'And never regretted it .. not even during our hardest times !! URL'
-> NEG 1 -> 1 true - (0.936):
          b'And that\xe2\x80\x99s why you were at NYFW cause your such a class act.. getcho wack ass outta here URL'
-> POS 0 -> 0 true - (0.061):
         b"#MAGA #Kavanaugh #DrainTheDeepState @USER   I'd like to see @USER interviewed again. In his book ALL OUT WAR he laid out a lot that is happening today. \xe2\x9c\x93DC Secret Resistance Society \xe2\x9c\x93ANTIFA \xe2\x9c\x93 A White House meeting. Be interesting to hear him 2 yrs after Bk. URL"
-> NEG 1 -> 1 true - (0.946):
          b'#disarmthem #antifa Please NO ONE be stupid enough to do this. Most of us DO NOT open carry, most of us carry concealed. Anyone stupid enough to do this, that is considered an act of aggression and you will be shot We also carry more than one weapon. We shoot to kill, not maim.'
-> NEG 1 -> 1 true - (0.966):
          b'All these sick ass ppl from school gave me something and now I have to chug down this nasty drink so it can go away\xf0\x9f\x99\x83'
-> POS 0 -> 0 true - (0.069):
         b'Anyone want to bet it costs more than that $50k election referendum? URL'
-> POS 0 -> 0 true - (0.096):
         b"..While reading this, I feel like I am hearing Cardi B's voice rapping.\xf0\x9f\x98\x82 URL"
-> POS 0 -> 1 true - (0.095):
         b'@USER #Rosie makes me nauseous!\xf0\x9f\xa4\xae URL'
-> POS 0 -> 0 true - (0.053):
         b'@USER Watch ielts liz .. she is amazing'
-> POS 0 -> 1 true - (0.017):
         b'#BREXIT deal HAS been reached - and will be unveiled at special summit in NOVEMBER, Has @USER sold out the #UK to the eu??? She better have not or the @USER are finished!! @USER URL'
-> POS 0 -> 0 true - (0.094):
         b'@USER #Google appears to be a completely testosterone-free work environment.  #SoyBoys  #Fairyland  #HurricaneFlorence'
-> POS 0 -> 0 true - (0.044):
         b'#Congratulations Erika Ikizake who won a 7-Day MARTA Pass courtesy of MARTA and Campus Services! Keep following us for more prizes. #Staytuned #TheStateWay #GoPanthers  @USER @USER URL'
-> POS 0 -> 1 true - (0.092):
         b"#EuropaLeague Song the EU, cash your remaining chips in and p*ss off \xf0\x9f\x91\x8d You've played all your cards and liberals in the U.S too.  Brexiteers and Trump takes it all so be nice eh and life'll be better for everyone.  URL"
-> NEG 1 -> 1 true - (0.989):
          b'$1500 for a phone. You all are fucking dumb.'
-> POS 0 -> 0 true - (0.052):
         b"#Wisdom #Wellness I will teach you the right way to build your own private, online 'traffic economy' so you are never short of prospects and sales again URL URL"
-> NEG 1 -> 1 true - (0.900):
          b"#HowToGetPeopleOutOfYourHome  Tell them that you're a vampire...then threaten to eat them if they don't get their asses out.  *shrugs*  What?  Problem?"
-> POS 0 -> 0 true - (0.058):
         b'0-8 En Taller : S-2, M-5, BX-6 (20:59:35)'
-> POS 0 -> 0 true - (0.088):
         b'9) Pornhub, the thoughtful people they are, are taking suggestions of more category of underserved communities and they are _____'
-> POS 0 -> 0 true - (0.089):
         b'@USER @USER I agree with you. Read the first paragraph and struggled to get past the condescension. She is a lawyer with an educated opinion. There are other lawyers with differing educated opinions.'
-> NEG 1 -> 1 true - (0.945):
          b'@USER oh fuck off \xf0\x9f\x98\x82\xf0\x9f\x98\x82'
-> POS 0 -> 0 true - (0.038):
         b'#BreakingNews:  #Trump issues a statement about Christine Blasey Ford.  See it now!  Visit URL #BlueWave2018 #BlueTsunami2018 #MAGA #Democrats #Liberals #SCOTUS @USER #Crypto URL'
-> POS 0 -> 0 true - (0.028):
         b'.@USER talks about @USER #Vyvx #Cloud Connect now offering secure and reliable connectivity to @USER Direct Connect via @USER @USER  URL URL'
-> POS 0 -> 0 true - (0.048):
         b'#100DaysofCode  day 10: React and Redux with @USER Montreal URL'
-> POS 0 -> 0 true - (0.084):
         b'#ARSYoungjaeDay HAPPY BIRTHDAY CHOI YOUNGJAE \xf0\x9f\x98\xad\xf0\x9f\x98\xad\xf0\x9f\x98\xad with vocals of a god and a contagious laughter, he is the most beautiful man!!! i could never feel sad whenever i see an img of him or just a snippet of him in a video, he always brightens my day. the last img is me when i saw URL'
-> NEG 1 -> 1 true - (0.939):
          b'#StopEtchecopar? Fuck you all \xf0\x9f\x96\x95\xf0\x9f\x96\x95\xf0\x9f\x96\x95\xf0\x9f\x96\x95\xf0\x9f\x96\x95 Que florezcan mil Baby Etchecopar \xf0\x9f\x8c\xbb\xf0\x9f\x8c\xbb\xf0\x9f\x8c\xbb'
-> POS 0 -> 0 true - (0.070):
         b'#Antifa invaded a memorial in recognition of Kate Steinle in Austin, Texas, and tried to comfort him it looked like when it was struggling, but has returned to the Southern District of New York, is recused from the Michael Cohen raid, Trump has my full support. Moving on .'
-> POS 0 -> 0 true - (0.080):
         b'#OnAirNow Jon Bellion - He Is The Same URL #1RSIDANCE URL'
-> POS 0 -> 0 true - (0.057):
         b'#Emmys2018 Sanda Ho is not Asia America she is Canadian this description was on @USER'
-> POS 0 -> 0 true - (0.080):
         b"@USER @USER I'm in NC. Thursday's I work at a nursing home doing hair. Around 10:15 I heard all of the Tv's do the alert. Then afterwards, tests on a few TV'S. I went to lunch and at 11:50, one was on the radio. It was so strange. I keep saying that, but it was unusual"
-> NEG 1 -> 1 true - (0.949):
          b'@USER @USER And Browning looked like dog shit against the same FCS school. What\xe2\x80\x99s your point?'
-> POS 0 -> 0 true - (0.086):
         b'#WCW - @USER does it again with her live coverage and YouTube videos for #textureontherunway! She is the official natural hair media company of NYC, Emmy award winner and so fierce!\xe2\x80\xa6 URL'
-> POS 0 -> 0 true - (0.055):
         b"#CTRiders Hope you are enjoying your Friday! If you're looking for a way to enjoy this nice weather this weekend, September is #ReadANewBookMonth and there is nothing like reading a new book on a patio with a nice cup of coffee :) Anyone ready anything interesting this month? URL"
-> POS 0 -> 0 true - (0.060):
         b'#MeetTheSpeakers \xf0\x9f\x99\x8c @USER will present in our event OIW 2018: Finpact - Global Impact through Financial Technologies. She is Senior Advisor Group Sustainable Finance and worked on green energy and climate risk. Join us to meet Thina URL #oiw2018 URL'
-> POS 0 -> 0 true - (0.092):
         b'#Kavanaugh typical #liberals , #Democrats URL'

```
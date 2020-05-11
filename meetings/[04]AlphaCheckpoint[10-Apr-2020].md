### OZBILJNE BILJESKE

__<div align=”right”> April 10th</div>__

**Predstavili smo plan**
- Plan se cini razuman
- Vjerojatno ce nam se putem radjat nove ideje
- Nemojte razmisljat u smjeru zelimo rijesit task, nego imamo neke podatke i zelimo nesto naucit
- Za hate speech mozemo mozda neke podatke iskoristit dodatne, da li nam modeli fulavaju na nekim vrstama speecha
  - Direktno ispsovat vs suptilno uvrijediti
  - Koji primjeri vise zezaju modele
- Bert mozemo fine tuneat na hate speech podacima pa dal to pomaze ili ne
  - Dodat neke feature pa vidjet dal pomazu
- Imam podatke i zelim naucit nesto novo
- Naprosto naucit nesto o zadatku da pomaze za zadatak a nisam ocekivao da ce pomoc
- Imamo li kontext? 
- Mozemo li uzet kontext iz tvitova prije? 
  - Je li taj tvit odgovor na neki tvit? 
  - Mozda se moze bolje skuzit
- Ne mora sve bit isplanirano unaprijed, vidite sta zanimljivo se moze izvuc
- Research questions su super stvar, okej je ako nesto ne radi
- Imamo vise taskova, ne moramo radit sve taskove - mozemo samo prvi, samo drugi… pretpostavit da je prvi rijesen i izlaz prvog imat kao ulaz drugog… 

JAN: 
- Naglasit mladenove rijeci
- Najbitnije na predmetu je da ne shvatimo ovo kao tipicni inzinjerski zadatak i ubit ga svim alatima i grand rezultat je hrpa brojeva
  - To je okej, ali mi zelimo da se koncentrirate na neku pricu i da izgradimo cijeli projekt oko te price, jer onda stvar postane puno zanimljivije
- Nositelj price je istrazivacko pitanje
- Zelimo vas ohrabrit da to nije “evo mi smo sve isprobali, pa evo rezultati”
- Mi biramo to istrazivacko pitanje
- Slozimo sve oko toga i eksperimenti su oko tog pitanja
- Ako ne uspijemo, to je isto okej
  - Pitanje “moze li se blabla?” okej odgovor je i ne
- “Da li pomaze ovaj tokenizer…?”
- “Da li ovaj feature pomaze…?”
- Pitanje moze failat tako da je dosadno i ne-korisno
  - Sto je tu zgodno pitanje? 
  - Koji fenomen offensive teksta je zanimljiv? 
- Kad budemo prezentirali ekipama ostalim treba to bit zanimljivo
- Trebamo nesto naucit
- Project report / mali znanstveni rad - treba bit koristan ljudima koji ce ga procitat i koji se zele bavit offensive-om
- “Offesn je jako vazzan, ima drustveni znacaj - ljudi su radili x,y,z.. Ali nitko nije radio OVO! Nas rad se fokusira na to”
  - Onda se ljudi zainteresiraju
  - Neko kad je procitao vas rad, jel izaso pametniji? Ako nije - failali smo! 
- Ne moramo odma smisliti istrazivacko pitanje
- Smisao ovog sastanka je gurnuti nas u pravom smjeru
- Citat cemo papere i na predmetu pa cemo skuzit

Fillat jednu rijec? 
- Ima smisla i to, koje rijeci model percipira kao najuvredljivije
- Modeli s attentionom - dobijemo za svaku rijec weights, pa onda najjace rijeci dobiju najveci weight
- Zgodno je da neke rijeci koje ne bi trebale bit, da ih model percipira uvredljivo 
- Ljudi bi vrijedjali indijskog politicara Modi-ja, pa je on skuzio da je to offensive rijec
- Kako detektirat rijeci koje model detektira kao hateful
- Hvala tea uvik cav <3
- Da li na drugom datasetu bolje generalizira model 


Rokovi su pomaknuti 1 tjedan unaprijed!! :D :D 

Sanja: mozemo li neki dodatni dataset? 
- Mozemo i ne moramo, kako hocemo
- Nije obavezno, ali ako ima veze s istrazivackim pitanjem, super, ali ako nema ne moramo
- Dal finetuneamo na wiki il na twitteru, ima li veze? 
Tea: jel okej koristit razlicita pitanja za razlicite modele? 
- Je ali gledajte da bude nekako povezano
- Prica bi morala imat glavu i rep pa je bolje ako sva pitanja imaju zajednicki nazivnik
- Prijedlog: 1-2-3 pitanja… dok cemo radit stvari naci cemo 4-5 zanimljivih stvari pa cemo se oko njih 
Sanja: koliko je vazno da napravimo nesto novo? 
- Ak je novo onda je zanimljivo, ali mozemo pogledat sta su drugi radili i dal mozemo pospajat nesto na nacin na koji niko nije to prije radio
- Probat sta je neko vec radio, oce li to nama isto radit? Ako nije nama, zasto 
- Neko je mozda lematizirao, a mi nismo
- Neko je mozda koristio 10k vocab, mi smo koristili sve rijeci
- Ne moramo probat, ovisi o tim pitanjima 

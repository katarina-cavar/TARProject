


- dal da koristimo neke word embeddinge prije? 
- bolje ako ih nauci na ogromnom corpusu sa strane? 
	- uzet word2vec embeddinge i fiksirat ih i ne ih mijenjat tijekom učenja
	- to bi moglo dosta smanjit overfittanje
	- ne zna napamte, googlat

- Dorotea: sto se radi sa misspellaim rijecima? izbaci? proba dodat u vocab, moze li ih se popravit? 
	- par opcija: guglat twitter tokenizer koji splita stvari koje se koriste na twitteru
	- twitter tokenizer ce mozda imat malo pametnije splittanje
		- ove koje ne riješi, jednostavno neće te riječi gledat
		- ako se te riječi pojave dovoljno puta vjerojatno će bit u vocabu
	- char n-gram 
		- (Tea je probala)
		- to do neke mjere riješi stvari
		- treba da ih ima više različite duljine (svi char n-grami od 2 do 7)
			- hi2 
			- select kbest ( da odrežemo previše n-grama )


- jan: rok za predaju 31. 5. (ne mozemo to produzivati)
	- recenzenti čitaju što tamo piše 
	- ako smo nešto napravili a nismo napisali, iz naše perspektive ko da niste napravili
	- nakon toga online prezentacije preko teamsa 
		- slajdovi i prezentacija
		

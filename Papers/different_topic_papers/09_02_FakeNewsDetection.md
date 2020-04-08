# Paper 09-02: [Understanding User Profiles on Social Media for Fake News Detection](http://www.public.asu.edu/~skai2/papers/fake_news_user.pdf)

- social media - easy news dissemination
- quality of news is lower 
- The performance of detecting fake news only from content is generally not satisfactory, and it is suggested to incorporate user social engagements as auxiliary information to improve fake news detection.
- in-depth understanding of the correlation between user profiles on social media and fake news
- real world datasets measuring users trust level on fake news 
	- experienced vs naive users
- keywords: fake news, user profile, trust analysis


--- 

## 1. Introduction

- social media: easy access, less expensive, fast dissemination
	- quality lower
- bad effects of FN: 
	- people believe fake info
	- people respond differently to real news (confusion, trustworthiness, ...)
- critical to detect fake news
	- hard, it's written to mislead users
	- exploiting user profiles

**Research Questions:**
- RQ1: Are some users more likely to trust/distrust fake news? 
- RQ2: If yes to RQ1, what are the characteristics of these users that are more likely to trust/distrust fake news and are there clear differences? 

**Contribution:**
- investigating if user profiles can be used for fake news detection
- which features of user profioles are helpful for FN detection
- experiments with 2 real-world datasets for studying the discriminative capacity of user profiles features


---

## 2. Related Work

**Fake News Detection on Social Media**
- using news content and social contexts
- *news content*
	- extract features from linguistic and visual information
	- linguistic features: writing styles and clickbait titles
	- visual: fake images
- *social context*
	- features from user profiles, post contents and social networks
- *network-based features*
	- diffusion network
	- co-occurrence network
	- propagination models
	- (whatever these mean)
- new ways: 
	- exploiting relationships among publisher, news and users engagements on social media to detect fake news
- existing user profile approaches: 
	- extracting features without deep understanding
	- this paper: in-depth investigation of user profiles

**Measuring User Profiles on Social Media**
- explicit and implicit features
1. Explicit features
	- raw user meta data
	- info credibility classification, user identity linkage (whatever that is)
2. Implicit features
	- usually very useful
	- age, gender, personality, ... 
- various research on collecting features





---

## 3. Assessing Users' Trust Level in News

### 3.A Dataset
- construct two datasets with news content and social context information
- ground truth for fake/real news is challenging


### 3.B Identifying User Groups

- number of FN user has shared (or RN)
- subsets: only shares RN / FN / both RN and FN
- Fake News Ratio

---

## 4. Characterizing User Profiles

### 4.A Explicit Profile Features

- Profile Related
	- basic user description fields
	- verified
	- registerTime
- Content Related
	- attributes of user activities
	- StatusCount
	- FavorCount
- Network Related
	- social networks attributes
	- FollowerCount
	- FollowingCount
- If a feature f reveal clear differences between U(r) and U(f) , then f has the potential usefulness for detecting fake news
	- statistical tests

### 4.B Implicit Profile Features

- gender, age, and personality
	- gender and age have major impacts on people’s psychology and cognition
	- personality - Five Factor Model (or “Big Five”)
		- Extraversion
		- Agreeableness
		- Conscientiousness
		- Neuroticism
		- Openness
---

## 5. Conclusion and Future Work


- there are specific users who are more likely to trust fake news than real news
- these users reveal different features from those who are more likely to trust real news




---

## Acknowledgements

## References
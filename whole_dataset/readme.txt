GENERAL FILE FORMAT
	All files are formatted as CSV (Comma Separated Values) files. String values
	are delimited with ' (single quote) and missing values are denoted as NULL.


********************************************************************************
*                                   authors                                    *
********************************************************************************

DESCRIPTION:
	Contains data on authors registered on VideoLectures.Net and their
	information. Please note that not all authors did in fact author at least
	one lecture - there are authors with no lectures assigned.
COUNT
	8,092 authors available
ATTRIBUTES:
	id				unique ID assigned to the author
	name			full name of the author
	e_mail			e-mail address of the author
	homepage		author's homepage
	gender			gender of the author, can be either
						"M"	(male)
						"F"	(female)
	organization	the organization that employs the author. Note that the
					value of this field is not normalized - the same
					organization can appear under several different names.

					
********************************************************************************
*                             authors_lectures                                 *
********************************************************************************

DESCRIPTION
	Contains information on which author authored what lecture in a pairwise
	manner. Note that single author can author multiple lectures, and one
	lecture can be authored by multiple authors.
COUNT
	9,733 entries
ATTRIBUTES
	author_id		author's ID
	lecture_id		lecture's ID


********************************************************************************
*                                categories                                    *
********************************************************************************

DESCRIPTION
	Contains information on categories in scientific taxonomy used on
	VideoLectures.Net. The taxonomy, which is a direct acyclic graph (several
	categories have multiple parent categories) in a pairwise form using parent
	and child relations. Note that only the root category does not have a parent.
COUNT
	366 entries, 348 distinct categories
ATTRIBUTES:
	id				unique category ID
	name			the name of the category
	parent_id		the parent (i.e. higher-level) category of the category.
					References through parent_id form the taxonomy.
	wikipedia_url	Wikipedia article corresponding to the category, manually
					selected by one of the editors, not available for every
					category in the dataset


********************************************************************************
*                           categories_lectures                                *
********************************************************************************

DESCRIPTION
	Contains information on what lecture is categorized under which category.
WARNING
	It is possible that a single lecture is categorized under several categories.
COUNT
	7,945 entries
ATTRIBUTES:
	category_id		category's ID
	lecture_id		lecture's ID

********************************************************************************
*                  events, lectures_train, lectures_test                       *
********************************************************************************

DESCRIPTION
	These three files share the same format with slight differences described in
	the following text. They are separated into three files because of semantic
	reasons: lectures which contain one or more videos are separated into train
	and test lectures and events by themselves do not contain videos but rather
	a set of lectures.

	events
		Contains information on events and event taxonomy used to group lectures.
		The event taxonomy is coded in a pairwise manner: by id and parent_id
		attributes. Note that the taxonomy itself is a forest (a disjoint union
		of trees) since each event has only one parent and there are root events
		that do not have a parent.
	lectures_train
		lectures_train contains lectures with publication date prior to 1.7.2009
		with a smaller subset of lectures published after that date.
	lectures_test
		lectures_test contains a subset of lectures published after 1.7.2009, not
		contained in the lectures_train.
COUNT
	events			519 distinct events
	lectures_train	6,983 distinct lectures
	lectures_test	1,122 distinct lectures
ATTRIBUTES
	id				unique ID of an event or a lecture
	type			type of the event or lecture. Can be one of the following
					values:
						project *
						event *
						event section *
						meta project / project group *
						lecture
						keynote
						debate
						tutorial
						invited talk
						introduction
						interview
						opening
						demonstration video
						external lecture
						thesis proposal
						best paper
						panel
						advertisement
						promotional video
						thesis defence
						summary
					Types denoted with * describe events. All other types
					describe lectures.
	language		the language of the event. Normally, this also determines
					the language of the description. Note that usually
					international events are conducted in English, while local
					events can be conducted in local languages.
					Available languages:
						en	English
						sl	Slovene
						fr	French
						cr	Croatian
						pl	Polish
						bg	Bulgarian
						es	Spanish
						nl	Dutch
						ru	Russian
						de	German
						sr	Serbian
	parent_id		parent of an event in the event taxonomy
	views*			the total (aggregated) number of views of this lecture since
					the day it was published online to the day the snapshot was
					taken.
	rec_date		the date when the lecture was recorded. Note that this date
					is sometimes not given, especially for the events and for the
					lectures that were not recorded by the VideoLectures.Net
					team but obtained somehow differently (e.g. found on the
					Web or provided by one of their partners)
	pub_date		the date when the lecture was published on the portal or when
					the event record was created.
	name			the name of the lecture or event in natural language.
					Normally, the language is specified by the language property.
	description		the description of the lecture or event in natural language.
					Normally the language is specified by the language property.
					Note that not all lectures/events are given descriptions.
	slide_titles**	The titles of the slides corresponding to the lecture.
					Normally the language of this content is specified by
					language property. Note that slide titles are not available
					for all lectures.

	* only lectures_train contains views
	** events do not contain slide_titles

********************************************************************************
*                                  pairs                                       *
********************************************************************************

DESCRIPTION
	Each line in the file contains a record about a pair of lectures viewed
	together (not necessarily consecutively) with at least two distinct
	cookie-identified browsers.
COUNT
	363,880 distinct pairs
ATTRIBUTES:
	lecture1_id		ID of the first lecture
	lecture2_id		ID of the second lecture
	frequency		the number of distinct cookie-identified browsers with which
					the respective pair of lectures was viewed together (not
					necessarily consecutively) from the day the "later" lecture
					was published online to the day the snapshot was taken.

********************************************************************************
*                           task1_query.csv                                    *
********************************************************************************
DESCRIPTION
	This is the query file for the task 1. It contains only lecture ids from 
	the subset of the lectures_train.txt file, for which a recommended 
	ordered list of 30 lectures from the lectures_test.txt file is expected 
	in submission.
COUNT
	5704 distinct lecture id's.
ATTRIBUTES:
	id		ID of the query lecture.
	
********************************************************************************
*                       triplets_left_train.csv                                *
********************************************************************************
DESCRIPTION
	This is file containing information on all the triplets and corresponding 
	frequencies in the pooled viewing sequences which can be used for training.
COUNT
	109,044 distinct triplets
ATTRIBUTES:
	id			ID of the triplet set.
	lecture1	ID of the first lecture in triplet set.
	lecture2	ID of the second lecture in triplet set.
	lecture3	ID of the third lecture in triplet set.
	frequency	number of clickstreams that contains this triplet inside.
	
********************************************************************************
*                       triplets_right_train.csv                                *
********************************************************************************
DESCRIPTION
	This is a file containing information on ten or less lectures with highest 
	frequencies that appear on right side of each triplet in pooled viewing 
	sequences. 
COUNT
	1,089,360 distinct lines.
ATTRIBUTES:
	id			ID of the triplet set.
	lecture		ID represents identifier of particular lecture from the right 
				side of corresponding triplet id in pooled viewing sequences
	frequency	number of clickstreams that contain lecture ID on the right 
				side of corresponding triplet id.
				
********************************************************************************
*                           task2_query.csv                                    *
********************************************************************************
DESCRIPTION
	This is the query file for the task 2. It contains triplets from pooled 
	viewing sequences that are not contained in the triplets_left_train.txt 
	file. Contestants should submit an ordered list of 10 lectures (both 
	lectures from lecture_train.txt file and lecture_test.txt file can be 
	part of the list). 
COUNT
	60,274 distinct triplets
ATTRIBUTES:
	id			ID of the triplet set.
	lecture1	ID of the first lecture in triplet set.
	lecture2	ID of the second lecture in triplet set.
	lecture3	ID of the third lecture in triplet set.
	frequency	number of clickstreams that contains this triplet inside.
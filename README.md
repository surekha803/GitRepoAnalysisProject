# GitRepoAnalysisProject
citationcode_gcp python file has the functionality of finding the core contributors of 25k repos.
Functionality of core contributors:If the number of edits or pushes of the contributor is greater than the average number of edits or pushes of all the contributors to a project. He is said to be a Core Contributor of that repository.

Implementation:
Extracted the records from the  GCP  based on the filter on event type PushEvent. 
Used nested dictionary to store the data of each repoid as a Key and its related information like actorid and number of push events information as a value.
Calculated the average of push events for each repo and compared with the individual push events and found the core contributor.

It calculates the number of repositories which has number ofcontriutors.Like example 85 repos have 1 core contributor.



# GitRepoAnalysisProject
citationcode_gcp.py
It has functionality of finding the core contributors of 25k repos.
Functionality of core contributors:If the number of edits or pushes of the contributor is greater than the average number of edits or pushes of all the contributors to a project. They are said to be a Core Contributor of that repository.

Implementation:
1.Extracted the records from the  GCP  based on the filter on event type PushEvent. 
2.Used nested dictionary to store the data of each repoid as a Key and its related information like actorid and number of push events information as a value.
3.Calculated the average of push events for each repo and compared with the individual push events and found the core contributor.

It calculates the number of repositories which has number ofcontriutors.Like example 85 repos have 1 core contributor.

Number of subsequent works citing the focal paper: 
Subsequent repositories are the repositories which are references or cited to the focal repository. These subsequent works can be found through the Core contributor work. Below are the main steps.
1.When the user is a core contributor to the focal repository, we find out what are the other repositories which the user has forked between its first and last push events.
2.Based on the condition we extract the repositories which CC’s have worked while they are working on focal repository. Then we can link draw a citation link between the focal repositories and the extracted repositories.

Implementation:
1.Extracted the unique repositories, there CC’s and there first and last push events on the repository as a data frame. Then created a list of unique repoId’s and kept in the iteration.
2.In each iteration ran the query on the table which extracted the repoid’s on which the CC has forked between the first and last push events.
3.Performed the count of the repoid’s (ni ) (which doesn’t count the duplicates) and appended into the list which the repoid’s and count. The code is present in contri_activeperiod.py file.

Totalteamsize.py
To find the total team size or contributors for all 26,901 repos, I have considered the users who have done both PullEvent and PushEvent  on each repo and calculated the team size.

contri_Activeperiod.py
The time between the first and last edit of the core contributor on a repository. The min time is the first edit and the max time is the last edit of the core contributor. Timestamps have been calculated for each repo by using Pandas Dataframe

citing_references.py
It has the functionality about finding the number of subsequent works citing the references 
Implementation:
1.Find the CC of all repositories, not only the 25k focal repositories.
2.Find the actorid’s who have performed Pull Request Event on the focal repositories.
3.Created a function which finds the core contributors of all the repositories.
4.Once we get the actorid’s in step2 compare with the CC’s in the step 3 and extracts its respective repoid







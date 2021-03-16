GitHub Guide 

1. Log into GitHub on your browser and navigate to https://github.com/madesai22/ocean-motion-2021

2. Navigate to the right side of the window and click "Fork." This will save a new copy of the repository in your GitHUb account

3. Open Terminal. Decide where you want to store your GitHub resository on your computer, and navigate to that place. I made a folder in my Documents called "InternGit", and I store this respository there. 

Remember: 
* to make a directory use **mkdir /path/to/directoryname**
* to navigate to a directory use **cd /path/to/directoryname**

4. Once you're in the right location, clone the repository. This adds a local copy to your own computer, and you can make changes there! To clone:
	* In your browser, go to your GitHub account, open the repositories tab, find the forked repository, and click on the green button on the right side that says "clone or download." Copy the URL it gives you.
	* In Terminal, type **git clone <url>**, where **<url>** is the URL of your forked repository that you just copied from GitHub
	* Make sure you're cloning your *forked* respository, not the original. You can tell because in the top left corner, where it says the name of the repository, it will have a description that identifies where it was forked from.

5. When you clone a repository, GitHub automatically creates a remote called origin that lets you interact with the online repository and make or download changes. Type **git remote -v** in Terminal to see a list of your remotes.

6. Add me as a collaborator to your repository — that way, I'll be able to see your work and integrate it into the main repository. In your browser, under settings in your repository, visit "Collaborators & teams" and add my username (madesai22) into the "Add collaborators" box. 

7. Now, we'll add a new remote that points to the original repository — the one that you forked your own repository from. This way, if any changes are made to that original repository, you will be able to download them.
	* Type git remote add upstream https://github.com/madesai22/ocean-motion-2021
	* Now, type git remote -v again. You should see two remotes: One called origin that points to your own repository, and one called upstream that points to the original. 

	**Important!!!**

go into your ocean-motion-2021 repository and type: 

	find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch

Then type: (this adds .DS_Store into a list of files to be ignored by git)

	echo .DS_Store >> .gitignore

Then type: (this commits the list of files to be ignored by git)

 	git add .gitignore
	git commit -m '.DS_Store banished!'

9. Now practice making a change to your repository and pushing that change: In the 1-5 folder, open newyear.txt in Sublime and add a couple sentences about the conversation you had with your partner. 

10. Now add the change to your repository
	* Type **git add newyear.txt** This lets git know you're ready to make a change.
	* Type **git commit -m "<Your message here>"** Change [Your message here] to explain why you're making the change – i.e. "Added my reflection" etc.
	* Congrats! You've just made your first commit to this repo!

11. Next, you'll upload this change to your online repository. Type **git push origin main** This tells git to send the changes you made on your branch to the main (your forked repository in the browser.)



Credit: this tutorial was modified from [Katy Abbott's tutorial](https://github.com/amnh/BridgeUP-STEM-Oceans-Six/blob/master/git-instructions.md)





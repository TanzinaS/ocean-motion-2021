GitHub Guide 

1. Log into GitHub on your browser and navigate to https://github.com/madesai22/ocean-motion

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
	* Type git remote add upstream https://github.com/madesai22/ocean-motion
	* Now, type git remote -v again. You should see two remotes: One called origin that points to your own repository, and one called upstream that points to the original. 



:earth_asia: :earth_asia: :earth_asia: :earth_asia: :earth_asia: :earth_asia: :earth_asia:
************************************
 ~ Break to discuss and go over what we know already about climate ~ 
In breakout rooms discuss:
1. What are some of the impacts of climate change (local and global)?
2. What are some of the main drivers of climate change?
3. What do we know about the ocean and climate change?
***********************************
:earth_americas: :earth_americas: :earth_americas: :earth_americas: :earth_americas: :earth_americas: :earth_americas:

9. Practice making a change to your repository and pushing that change: In the 10-6 folder, open climate-start.txt in Sublime and add a couple sentences about the conversation you had with your partner. 

10. Now add the change to your repository
	* Type **git add climate-start.txt** This lets git know you're ready to make a change.
	* Type **git commit -m "<Your message here>"** Change [Your message here] to explain why you're making the change – i.e. "Added my reflection" etc.
	* Congrats! You've just made your first commit to this repo!

11. Next, you'll upload this change to your online repository. Type **git push origin master** This tells git to send the changes you made on your branch to the master (your forked repository in the browser.)



Cheat sheet:

* To add a new remote: **git add remote <name> <url>**
* To see your remotes: **git remote -v**
* To add a change: **git add <file-name>**
* To checkout (switch to) a new branch: **git checkout <branch-name>**
* To delete an existing branch (be careful – you may lose your changes!): **git branch -d <branch-name>**
* To commit that change: **git commit -m "<your message here>"**
* To push those changes to your remote repository: **git push origin master**
	* If you're working on a different branch or remote (not master or origin): **git push <remote-name> <branch-name>**
* To sync your forked repository with any changes made to the original:
	* **git fetch upstream**
	* **git checkout master** (replace master with your <branch-name> if you want to merge changes with another branch)
	* **git merge upstream/master** (replace master with your <branch-name> if you want to merge changes with another branch)


Credit: this tutorial was modified from [Katy Abbott's tutorial](https://github.com/amnh/BridgeUP-STEM-Oceans-Six/blob/master/git-instructions.md)





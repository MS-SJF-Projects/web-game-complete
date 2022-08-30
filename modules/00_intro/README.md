# Intro to the project

TODO: write intro

## Setting up the environment

The repository you will be working on is [web-game](https://github.com/MS-SJF-Projects/web-game). To set up your
environment for local development in this repository, you have to create a fork of the web-game repository under your
personal github account. This ensures that your changes don't affect the original repository or the changes of other users.
To fork the web-game repository, follow [these instructions](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository).

**Note:** You do not have to set up the fork to sync with the original repository.


Now, you have to clone the new repository which is under your github account to your computer. To do so,
follow this [github documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
You may use either https or ssh cloning.

Once you have cloned the repository, open it in VSCode. You can either open VSCode manually and open the project from inside VSCode
or you can use a terminal, navigate to the repository folder and use this command:

```
code .
```

The last step for local development is reopening the project inside the development container. Note that for this to work,
Docker must be running on your computer. To run Docker, simply open Docker Desktop.

In VSCode open up the command palette (Ctrl+Shift+P) and search for `Remote-Containers: Reopen in container`.

![Picture of VSCode command palette with command reopen in container](./containercommand.png 'Reopen in container command')

Once the container is running the bottom left of your VSCode window will show at the bottom left that the dev container is running:

![VSCode window shows running dev container](./devcontainer.png 'Dev container is running')

Now you are all set to start developing in your personal fork of the web-game repository. 

TODO: presentation on devcontainers

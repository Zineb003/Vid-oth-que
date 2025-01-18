# TODO

## DOCKER

DockerFile : fichier pour construire l'image docker pour executer l'application

```bash
docker-compose up
docker-compose down
docker exec -it projet_serveur_1  bash

curl -X POST http://10.11.23.130:5000/del_movie \
     -H "Content-Type: application/json" \
     -d '{"title": "The Avengers"}'

```


## GIT

Configure your Git identity globally to use it for all current and future projects on your machine:

```bash
git config --global user.name "tahi0017"
git config --global user.email "zineb.tahir@etudiant.univ-reims.fr"
```

To push an existing folder to an empty GitLab repository, follow these steps:

1. Open a terminal or command prompt and navigate to your existing project folder.

2. Initialize a Git repository in your project folder:
```bash
git init
```

3. Add all files in the folder to the Git repository:
```bash
git add .
```

4. Commit the files:
```bash
git commit -m "Initial commit"
```

5. Add the GitLab repository as a remote:
```bash
git remote add origin git@gitlab-mi.univ-reims.fr:tahi0017/videotheque.git
```

6. Push your local repository to GitLab:
```bash
git push -u origin master
```

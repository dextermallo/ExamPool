#!bin/bash

# Import data to mongodb.
mongoimport --db ExamPool --collection catalog_department --file './data/catalog_department.json'
mongoimport --db ExamPool --collection catalog_article --file './data/catalog_article.json'
mongoimport --db ExamPool --collection catalog_comment --file './data/catalog_comment.json'
mongoimport --db ExamPool --collection users_favorite --file './data/users_favorite.json'
mongoimport --db ExamPool --collection users_icon --file './data/users_icon.json'
mongoimport --db ExamPool --collection users_user --file './data/users_user.json'
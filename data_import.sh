#!bin/bash

# Import data to mongodb.
mongoimport --db ExamPool --collection catalog_department --file './data/Department.json'
mongoimport --db ExamPool --collection catalog_article --file './data/Article.json'
mongoimport --db ExamPool --collection catalog_comment --file './data/Comment.json'
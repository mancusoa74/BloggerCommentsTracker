# BloggerCommentsTracker

Quick and dirty tool which help me to keep track on new comments on my Google Blogger posts.

Blogger UI provide a view on how many comments are present for each article of my blog. However just knowing the number doesn't tell me whether there are new comments for my articles.

This is an issue as decrease the quality of my blog as I am not able to answer to my reader.

I created this simple too (no integration with BLogger API) just to solve this problem.

## How to use the tool

### step 1
In the file blogger_stats.py, define those three constants:

- BLOGGER_DUMP_DIRECTORY = "YOUR/PATH/TO1/blogger_files": contains the file path to the blogger posts' info
- BLOGGER_COUNT_FILE_GLOB = "commentcount*.html": no need to edit this one
- BLOGGER_STATS_DB_FILE = "YOUR/PATH/TO2/blogger_stats.yml": replace the path where you want to store the database

### step 2

go to your blogger post page and right click and save as blogger into YOUR/PATH/TO1/ directory

this will create a YOUR/PATH/TO1/blogger_files directory with a full downloads of the blogger main page

### step 3

execute

```
# python blogger_stats.py
```

this will generate a table with all your blog post and the number of comments for each article.

The article with new comments will be highlighted in green color

| ID  |                   Title                    | #Comments |
|:---:|:------------------------------------------:|:---------:|
|  0  | oscilloscopio-dso138-kit-assemblaggio-e_25 |     1     |
|  1  |  oscilloscopio-dso138-kit-assemblaggio-e   |     1     |
|  2  |       robot-car-con-nodemcu-software       |    10     |
|  3  |           robot-car-con-nodemcu            |     1     |


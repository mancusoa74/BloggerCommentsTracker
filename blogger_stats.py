import glob, os, re, sys
import yaml
from prettytable import PrettyTable


BLOGGER_DUMP_DIRECTORY = "YOUR/PATH/TO/blogger_files"
BLOGGER_COUNT_FILE_GLOB = "commentcount*.html" 
BLOGGER_STATS_DB_FILE = "YOUR/PATH/TO/blogger_stats.yml"


def get_blogger_comments():
    # parse bloger exported files and return a list of dictionary with title and num of commnets
    posts = list()

    files = glob.glob(BLOGGER_COUNT_FILE_GLOB)
    num_files = len(files) #count the number of files
    print("Processing {} file".format(num_files))
    for idx in range(num_files):
        if idx == 0:
            file_name = "commentcount.html"
        else:
            file_name = "commentcount({}).html".format(idx)
        print("Processing file #{} - {}".format(idx, file_name))
        with open(file_name, 'r') as myfile:
            file_data = myfile.read()
            title = re.search('.*blogspot.com.*%2F20[0-9][0-9]%2F[0-9][0-9]%2F(.*).html', file_data, re.IGNORECASE).group(1)
            try:
                num_comments = re.search('.*widget_bounds".*#">(.*)</a>', file_data, re.IGNORECASE).group(1)
            except:
                print("Error processing the file...skipping it!!!")
            else:
                posts.append({'id': idx, 'title': title, 'comments': num_comments})
    return posts

def read_blogger_db():
    #read the yaml DB into a dictionary
    with open(BLOGGER_STATS_DB_FILE, 'r') as myfile:
        db_file = myfile.read()
        db = yaml.load(db_file)

        return db

def write_blogger_db(db):
    #dump the modified blogger db to file
    with open(BLOGGER_STATS_DB_FILE, 'w') as myfile:
        myfile.write(yaml.dump(db))

def main():

    try:        
        os.chdir(BLOGGER_DUMP_DIRECTORY)
    except OSError:
        print("ERROR: The BLOGGER_DUMP_DIRECTORY does not exist")
        sys.exit(0)
    new_posts = get_blogger_comments()

          
    if not os.path.exists(BLOGGER_STATS_DB_FILE):
        write_blogger_db(new_posts)
    old_posts = read_blogger_db()

    if (len(new_posts) != len(old_posts)):
        print("ERROR: the number of post doesn't match!!!")
    else:
        table = PrettyTable(['ID', 'Title', '#Comments'])
        for idx, new_post in enumerate(new_posts):
            if new_post['comments'] != old_posts[idx]['comments']:
                comment_num = '\033[1;32m' + new_post['comments'] + '\033[0m'
                old_posts[idx]['comments'] = new_post['comments']
            else:
                comment_num = new_post['comments']
            table.add_row([idx, new_post['title'], comment_num])
        print(table)
        write_blogger_db(old_posts)

if __name__ == "__main__":
    main()

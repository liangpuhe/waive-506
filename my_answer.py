# import statements
import unittest
import json
import requests

############

## IMPORTANT NOTES: In general, this course expects you to run Python files via
## the command prompt. In some cases, even if you do not do so, assignments will
## work. This assignment, depending upon your setup, is VERY UNLIKELY to work if
## you do not run it via the command prompt (Git Bash or Terminal, etc).

## Remember: run your program early and often to determine what it is doing and whether it is working as you expect it to! DO NOT turn your program in without first running it to make sure that all of the test output is shown and it runs properly.

## You should NOT be writing any additional calls to input besides the one
## that already exists (that's for if you do not paste your Flickr key into this
## code file.

## When you run this program, you will see the print statements provided for you, and you will also see output from the tests.

#########


## [PROBLEM 1]
print("\n***** PROBLEM 1 *****\n") # (Printed statements like this one throughout the problem set are provided to help you figure out where things are when you see output. You should leave them alone.)

## There are tests for this problem.

## We have provided a sample dictionary representing 1 Flickr photo in the format that Flickr returns it, saved in a JSON file, called sample_diction.json.

## Write code to open the file and load its contents as a Python object into the
## variable sample_photo_rep. Then close the file (that'll keep you from running
## into easily-avoidable errors later on!). There are tests for this problem.
diction_file = open('sample_diction.json','r')
sample_photo_rep = json.load(diction_file)
diction_file.close()
## (You may also find it useful, for later in the problem set, to open the file
## "sample_diction.json" in a text editor, or copy and paste its contents into
## http://www.jsoneditoronline.org/ to see what the nested data in this dictionary
## will be structured like.)




## [PROBLEM 2] -- Code setup (get and paste in your Flickr API key)
print("\n***** PROBLEM 2 *****\n")
## Set up code so you, too, can access the Flickr API. (You have probably already done this in class, but it is necessary to complete this assignment.)

## This one's not too bad --
## it's just important to complete so you can access the data you'll need.
## There are NO tests for this problem.
## But the rest of the assignment will not work if you don't complete it!

## You will need a Yahoo!/Hotmail account in order to sign in to Flickr.
## You need such an account in order to complete this assignment. But it does not need to be a "real" account that you will use for anything else besides this, and you do not need to use your real name for it if you do not want to.

## Follow the instructions in the UsingRESTAPIs chapter of the provided textbook to get a key for the Flickr API, so that you can get data from Flickr and paste it below, inside the quotes.

FLICKR_KEY = "e02cfd3748eed43a1f9913d9d5f6585b" # paste your flickr API key here, between those quotation marks, such that the variable flickr_key will contain a string (your flickr key!).


## DO NOT CHANGE ANYTHING ELSE ABOUT THE CODE HERE IN THIS PROBLEM 2.
## Normally you should not share API keys with others. But if you include your key
## in your problem set submission file here, we (graders) will not use it for
## anything nefarious.
## You can also regenerate the key (but do NOT regenerate it until August 25 2017
## or two weeks after you complete the waiver, whichever comes LAST!)
if FLICKR_KEY == "" or not FLICKR_KEY:
    FLICKR_KEY = input("Enter your flickr API key now, or paste it in the assignment .py file to avoid this prompt in the future. (Do NOT include quotes around it when you type it in to the command prompt!) \n>>")




## [PROBLEM 3] - Photo data investigation
print("\n***** PROBLEM 3 *****\n")
## There are tests for this problem.

## The sample_photo_rep variable you defined back in Problem 1 should contain a complex Python object. That represents data about one single photo on Flickr.
## Write code to access the nested data inside sample_photo_rep to create a list of all of the tags of that photo.
## Save the list of tags in a variable called sample_tags_list.
tags = sample_photo_rep["photo"]["tags"]["tag"]
sample_tags_list = []
for tag in tags:
    sample_tags_list.append(tag['_content'])
print(sample_tags_list)
## You will need to do a bunch of nested data investigation and nested iteration in order to complete this.

## Copying the contents of the sample_diction.json file into jsoneditoronline.org may help. Remember, go slowly and step-by-step; understand, then extract, then understand the next bit...

## When you have completed this problem, the tags list in sample_tags_list should look like this: [u'nature', u'mist', u'mountain']

## HINT: Check out the '_content' keys' values deep inside the nested dictionary... (Don't use the "raw" key)





## [PROBLEM 4] - More Flickr data investigation
print("\n***** PROBLEM 4 *****\n")
## There are tests for this problem. It has 2 parts.

## We have ALSO provided a file called sample_flickr_response.json.
## This file contains data that has been gotten from the Flickr API in response to a request for 25 photos tagged with the word "sunset", but the data from the API has been altered slightly so that it is properly formatted in a JSON way (as discussed in class).

## PART 1:
## Write code that will open the sample_flickr_response.json file and load the data inside that file into a variable called search_result_diction.




## PART 2:
## The variable search_result_diction should now contain a very complex dictionary representing information about a bunch of photos that are tagged "sunset". Each photo has an id.
## Write code to create a list of all of the photo ids from each photo that the search_result_diction data represents, and save that list in a variable called sample_photo_ids.




## [PROBLEM 5] - Set up the pattern for caching data
print("\n***** PROBLEM 5 *****\n")
## There are tests for this problem.  But this code will work in conjunction with code you write later, so it can't all be tested until you've completed the whole assignment. In other words, it is possible (if unlikely) to pass the tests for thsi problem, but still have the code you write in this problem cause a difficulty for you. So take your time and be sure you understand what's happening here!

## This problem set will now combine the work you've done already with work much like what you did in Problem Set 6, but this time you will be caching your data so that your code will only make a request to the internet when you don't already have the data you need.

## Translate the following English into code, as described in the caching chapter of the textbook, in order to set up a pattern so you can cache the data you get in this problem set.


##### Write your caching code here. We suggest keeping the comments and writing the code translations above / below / to the left of them...

CACHE_FNAME = "waiver_cached_data.json" # PROVIDED FOR YOU, DO NOT CHANGE
## If you save data in this file that is wrong/not working, not a problem: just delete the file from the folder, or rename it, and run this file again to try and fix the problem!

# Begin a try/except statement
# Inside the try block:
## Open a file with the CACHE_FNAME name.
## Read the file into one big string.
## Close the open file.
## Load the string into a Python object, saved in a variable called CACHE_DICTION.
# Begin the except clause of the try/except statement:
## Create a variable called CACHE_DICTION and give it the value of an empty dictionary.





# In total, this should be five or six lines of code. ^
# We have also provided a file SAMPLE_waiver_cached_data.json, which is like what your code should generate. (You may end up with much more data in your cache file, and will definitely end up with different data in your cache file, which is just fine!)




## [PROBLEM 6]
print("\n***** PROBLEM 6 *****\n")
## There are tests for this problem.

## In this problem, you'll define a function to get data from Flickr which uses the caching framework you just set up -- so it will only go request data from the Flickr API if you have not already made the same request! See below for more detail.

## Utility function provided for your use here (do not change):
# Function to create a unique representation of each request without private data like API keys
def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)

## Code to provide an example of the params_unique_combination function
pd = {}
pd["method"] = "flickr.photos.search"
pd["format"] = "json"
pd["api_key"] = FLICKR_KEY
pd["tags"] = "summer 2013"
pd["tag_mode"] = "all"
pd["per_page"] = 112
print("params diction example", params_unique_combination("https://api.flickr.com/services/rest/", pd))

## Define a function called get_flickr_data which accepts 2 inputs:
## - a REQUIRED parameter: any string representing a tag to search for on Flickr (e.g. if you wanted to search for data on photos tagged with "mountains", you would pass in "mountains" for this parameter)
## - an OPTIONAL parameter: whose default value is 50 (representing how many photos you want in your response data)

## The following is an EXTENDED description of what the function should do.

## FUNCTION BEHAVIOR:
## This function should use the provided utility function called params_unique_combination to get a unique identifier for the data request to the Flickr API.
## The function should check whether or not the unique identifier for each request exists in your cache data, and if it does, should access that data.

### If there is no such data in your cache, the function should make a request to the Flickr Photos Search API for photos tagged with your input string. Your request should use the tag_mode "all" so that if your query string represents multiple tags, it will search for photos with ALL of those tags.

### It should modify the string that is returned from the Flickr API so that it is properly JSON formatted. (You want a version of the string without the first 14 characters or the very last character -- see the textbook example!)

### And then, load that modified string into a Python object.

### Then, the function should add the new dictionary of data to your cache dictionary, associated with the unique identifier key, and save all the data in the cache dictionary to your cache file!

## The get_flickr_data function's RETURN VALUE, regardless of whether it got data from the cache, or made a new request and saved data to the cache, should be a big dictionary representing a bunch of search data from the Flickr Photos Search API.

## API docs here: flickr.com/services/api/flickr.photos.search.html

## The base URL for the Flickr API is: "https://api.flickr.com/services/rest/"

## Recall that all Flickr API endpoints have the same base url, but different values of the "method" parameter! For the Photos Search API, that value should be "flickr.photos.search"

## Recall also that you have a variable FLICKR_KEY in this file which you could reuse in this function, since it is intended as a global variable for your whole program.


## The examples, and thinking/talking through them carefully, will be VERY helpful here, and the other examples of writing functions to request data from an API in the textbook may also be helpful.





## [PROBLEM 7]
print("\n***** PROBLEM 7 *****\n")

## Make an invocation to your get_flickr_data function with the input "mountains" (use the default second parameter). Save the result in the variable flickr_mountains_result. There are tests for this problem.

## (Whether or not this works is also an additional test for your Problem 6, since you'll need to have correctly completed the function definition above to do this.)




## [PROBLEM 8]
print("\n***** PROBLEM 8 *****\n")

## Remember the code you wrote in Problem 4? Modify that code slightly to get a list of all of the photo IDs in the data that's in your flickr_mountains_result variable and save it in a variable photo_ids. There are tests for this problem.

## (Your photo_ids variable should have 50 different photo ids, since your Flickr API response in Problem 7 should have made a request for data about 50 photos! If you run into a problem where a photo has been deleted from Flickr and you do not have 50 photos, please contact instructors on the pinned thread on the Canvas site. Otherwise, check out your answer to problem 6 again!)






## [PROBLEM 9]
print("\n***** PROBLEM 9 *****\n")
## There are tests for this problem.

## You now have a list saved in the variable photo_ids.
## It contains a bunch of ids belonging to photos.
## You also have a list saved in the variable sample_photo_ids that contains a bunch of ids belonging to photos.
## You're now going to go back to using the sample_photo_ids, so we know for sure that you have good data, since you'll be working from data we've provided.
## First:

## You also know about another endpoint of the Flickr API: Photo Info.
## https://www.flickr.com/services/api/flickr.photos.getInfo.html

## It shows that you need a photo id, and a flickr key, to get info about a photo
## that is public, and also need to change the value of the method query parameter (that specifies which endpoint is being accessed!).
## So if you were to make a request to that endpoint of the API,
## you could get a response about each of these photos.
## That's what you'll do in this problem.

## Write a function called get_photo_data that takes 1 parameter: a photo id.

## It should have a similar structure to the get_flickr_data function you wrote in problem 6, but use different query parameters, of course.

## This function should cache data (in the same cache file! You don't need to change anything except for writing this brand new function).

## The get_photo_data function should return a complex dictionary that represents information about 1 photo on Flickr.





## The following two lines of code will invoke the get_photo_data function,
## assuming your photo_ids list from above is correct!
## If you'd like to try it out, uncomment these two lines. You should then see
## a huge dictonary. You could try writing more investigation code here as well if you find that helpful.

# one_photo_id = sample_photo_ids[10]
# respval = get_photo_data(one_photo_id)



## [PROBLEM 10]
print("\n***** PROBLEM 10 *****\n")
## There are tests for this question. This question has 3 parts.

## Now that you have functions to get data from flickr and you've practiced
## writing data to files and getting data out of files, let's put it all together.

## PART 1:
## Iterate over your *** sample_photo_ids list from Problem 4 ***s and invoke your get_photo_data
## function on each of the ids. Append the result of each invocation to a list,
## so you are accumulating a list of dictionaries, each of which represents data
## about one photo. Save that list of dictionaries in a variable called photo_dictions_list.






## PART 2:
## Define a class Photo.
## As input, the class should require 1 dictionary representng a flickr photo.
## The constructor should create the following instance variables:

##### artist, which holds a string representing the flickr username of the person who posted the photo, and should always be a string
##### title, which holds a string representing the title of the photo, and should always be a string
##### tags, which holds a list of strings, each of which is a tag (HINT: look back at the work you did in problem 3!), and should always be a list

## The class should also have a string method (__str__ method) that returns a string like, for example:

"""
Title: This is my Photo Title
Artist: Ansel Adams
Tags: [u'mountains',u'river',u'yosemite']

"""





## PART 3:
## Iterate over the photo_dictions_list you created in Part 1,
## and for each dictionary in that list, create 1 instance of class Photo.
## Save the list of Photo instances in a variable called photo_insts.

## Sort the photo_insts list by the number of tags, in ascending order. So, for example, a photo that has only 3 tags would come earlier in the list than a photo that has 7 tags. Save the sorted list in a variable called sorted_photo_insts.

## Write code to print out the string representation of the first 3 photos in the sorted_photo_insts list.








print("------------OUTPUT OF TESTS APPEARS BELOW THIS LINE------------\n")
##### Code for running tests is below this line. Don't change any code below this line!######


class Problem1(unittest.TestCase):
    def test_sample_photo_rep(self):
        self.assertEqual(sample_photo_rep,{u'photo': {u'people': {u'haspeople': 0}, u'dateuploaded': u'1467709435', u'owner': {u'username': u'Ansel Adams', u'realname': u'', u'path_alias': None, u'iconserver': u'7332', u'nsid': u'48093195@N03', u'location': u'', u'iconfarm': 8}, u'publiceditability': {u'canaddmeta': 1, u'cancomment': 1}, u'id': u'27820301400', u'title': {u'_content': u'Photo1'}, u'media': u'photo', u'tags': {u'tag': [{u'machine_tag': False, u'_content': u'nature', u'author': u'48093195@N03', u'raw': u'Nature', u'authorname': u'ac | photo albums', u'id': u'48070141-27820301400-5470'}, {u'machine_tag': False, u'_content': u'mist', u'author': u'48093195@N03', u'raw': u'Mist', u'authorname': u'ac | photo albums', u'id': u'48070141-27820301400-852'}, {u'machine_tag': False, u'_content': u'mountain', u'author': u'48093195@N03', u'raw': u'Mountain', u'authorname': u'ac | photo albums', u'id': u'48070141-27820301400-1695'}]}, u'comments': {u'_content': u'0'}, u'secret': u'c86034becf', u'usage': {u'canblog': 0, u'canshare': 1, u'candownload': 0, u'canprint': 0}, u'description': {u'_content': u''}, u'isfavorite': 0, u'views': u'4', u'farm': 8, u'visibility': {u'isfriend': 0, u'isfamily': 0, u'ispublic': 1}, u'rotation': 0, u'dates': {u'taken': u'2016-07-05 11:03:52', u'takenunknown': u'1', u'posted': u'1467709435', u'lastupdate': u'1467709679', u'takengranularity': 0}, u'license': u'0', u'notes': {u'note': []}, u'server': u'7499', u'safety_level': u'0', u'urls': {u'url': [{u'type': u'photopage', u'_content': u'https://www.flickr.com/photos/48093195@N03/27820301400/'}]}, u'editability': {u'canaddmeta': 0, u'cancomment': 0}}, u'stat': u'ok'})

class Problem3(unittest.TestCase):
    def test_sample_tags_list(self):
        self.assertEqual(sample_tags_list,[u'nature', u'mist', u'mountain'])

class Problem4(unittest.TestCase):
    def test_search_result_diction(self):
        self.assertEqual(type(search_result_diction),type({}), "Testing that search_result_diction is a dictiionary")
    def test_search_result_diction2(self):
        self.assertTrue("photos" in search_result_diction, "Testing that the photos key is in the loaded flickr response, as it should be")
    def test_sample_photo_ids(self):
        self.assertEqual(type(sample_photo_ids),type([]))
    def test_sample_photo_ids2(self):
        self.assertTrue("35508093542" in sample_photo_ids) # This needs to be changed with any different flickr_response data.

class Problem5(unittest.TestCase):
    def test_cache_diction_existence(self):
        self.assertEqual(type(CACHE_DICTION),type({}),"Testing that CACHE_DICTION is a dictionary")

class Problem6(unittest.TestCase):
    def test_get_flickr_data1(self):
        self.assertEqual(sorted(list(get_flickr_data("alps").keys())),[u'photos',u'stat'], "Testing the keys of the return value of get_flickr_data") # Unicode OK -- need change?
    def test_get_flickr_data2(self):
        self.assertEqual(sorted(list(get_flickr_data("alps")["photos"]["photo"][49].keys())),sorted([u'isfamily', u'title', u'farm', u'ispublic', u'server', u'isfriend', u'secret', u'owner', u'id']), "Testing the keys of one of the photos inside the get_flickr_data response")
    def test_get_flickr_data_resp_type(self):
        self.assertEqual(type(get_flickr_data("alps")["photos"]["photo"][49]),type({}), "Testing that the value of one of the photos in the function's return value is a dictionary")
    def test_get_all_diff_photos(self):
        self.assertTrue(get_flickr_data("sunset")["photos"]["photo"][30]["id"] != get_flickr_data("sunset")["photos"]["photo"][15]["id"], "Testing that the list of photos is not a composed list of all the same photo")
    def test_default_num_photos(self):
        self.assertEqual(len(get_flickr_data("sunset")["photos"]["photo"]),50,"Testing that the default num_photos response has 50 photos")
    def test_cache_in_function(self):
        testfile = open("waiver_cached_data.json","r")
        testfilestr = testfile.read()
        testfile.close()
        self.assertTrue("sunset" in testfilestr,"Testing that the sunset request was cached")
    def test_cache_in_function2(self):
        testfile = open("waiver_cached_data.json","r")
        testfilestr = testfile.read()
        testfile.close()
        self.assertTrue("per_page-50" in testfilestr, "Testing (in part) that the params_unique_combination was used properly in the cache setup")
    def test_cache_in_function3(self):
        get_flickr_data("summer 2013",112) # specific params
        testfile = open("waiver_cached_data.json","r")
        testfilestr = testfile.read()
        testfile.close()
        self.assertTrue("https://api.flickr.com/services/rest/format-json_method-flickr.photos.search_per_page-112_tag_mode-all_tags-summer 2013" in testfilestr, "Testing that params and unique identifer setup are correct in get_flickr_data function")

class Problem7(unittest.TestCase):
    def test_flickr_mountains_result_keys(self):
        self.assertEqual(sorted(list(flickr_mountains_result.keys())),[u'photos', u'stat'],"Testing the keys of the value of flickr_mountains_result, which should be a dictionary")
    def test_fmr_res_type(self):
        self.assertEqual(type(flickr_mountains_result),type({}),"Testing that the type of flickr_mountains_result is a dictionary")
    def test_num_photos_flickr_mountains_res(self):
        self.assertEqual(len(flickr_mountains_result["photos"]["photo"]),50,"Testing that there are 50 photos in flickr_mountains_result, using the default second param value in the function")

class Problem8(unittest.TestCase):
    def test_photo_ids_len(self):
        self.assertEqual(len(photo_ids),50,"Testing that there are 50 photo ids")
    def test_diff_photo_ids(self):
        self.assertTrue(photo_ids[0] != photo_ids[40], "Testing that the photo ids are different, not just 50 of the same one (check out your nested iteration, maybe)")
    def test_ids_in_cache(self):
        testfile = open("waiver_cached_data.json","r")
        testfilestr = testfile.read()
        testfile.close()
        self.assertTrue(photo_ids[4] in testfilestr,"Testing that one of the ids, like the other response data, is inside the cache file.")

class Problem9(unittest.TestCase):
    def test_get_photo_data(self):
        one_photo_id = sample_photo_ids[10]
        one_photo = get_photo_data(one_photo_id)
        self.assertEqual(type(one_photo),type({}))
    def test_get_photo_data(self):
        one_photo_id = sample_photo_ids[11]
        one_photo = get_photo_data(one_photo_id)
        self.assertEqual(sorted(list(one_photo.keys())),[u'photo',u'stat'])

class Problem10(unittest.TestCase):
    def test_photo_dictions_list(self):
        self.assertEqual(type(photo_dictions_list),type([]))
    def test_photo_dictions_list2(self):
        self.assertEqual(type(photo_dictions_list[0]),type({}))
        self.assertEqual(type(photo_dictions_list[-1]),type({}))
    def test_class_photo(self):
        fsample = open("sample_diction.json")
        sample = json.loads(fsample.read())
        fsample.close()
        tmp_photo = Photo(sample)
        self.assertEqual(tmp_photo.title,u"Photo1")
    def test_class_photo1(self):
        fsample = open("sample_diction.json")
        sample = json.loads(fsample.read())
        fsample.close()
        tmp_photo = Photo(sample)
        self.assertEqual(tmp_photo.tags,[u'nature', u'mist', u'mountain'])
    def test_class_photo2(self):
        fsample = open("sample_diction.json")
        sample = json.loads(fsample.read())
        fsample.close()
        tmp_photo = Photo(sample)
        self.assertEqual(tmp_photo.artist, u"Ansel Adams")
    def test_sorted_photo_insts(self):
        self.assertTrue(len(sorted_photo_insts[0].tags)<=len(sorted_photo_insts[-1].tags))
    def test_sorted_photo_insts2(self):
        fsample = open("sample_diction.json")
        sample = json.loads(fsample.read())
        fsample.close()
        tmp_photo = Photo(sample)

        self.assertEqual(type(sorted_photo_insts[1]),type(tmp_photo))


if __name__ == "__main__":
    unittest.main(verbosity=2)

import wikipedia
import re

# with open("C:\\Users\\Justi\\OneDrive\\Desktop\\API keys\\smmry_api.txt", "r") as apiKey:
#     key = apiKey.readlines()
# URL = "https://api.smmry.com"
# SMMRY_URL = URL + "?SM_API_KEY=" + key

# def getIntro(article):
#     return intro

keywords = "Leo Messi"

intro = wikipedia.summary(keywords)

# wiki search retuyrn list get keyword to trigger

'''
Here is an example of PHP using cURL to summarize a block of text:
$text = "Your long text goes here...";

    $ch = curl_init("https://api.smmry.com/&SM_API_KEY=X");
    curl_setopt($ch, CURLOPT_HTTPHEADER, array("Expect:")); // See Note
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, "sm_api_input=".$text);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 20);
    curl_setopt($ch, CURLOPT_TIMEOUT, 20);
    $return = json_decode(curl_exec($ch), true);
    curl_close($ch);
'''

# use smmry api to get summary from intro
# how to use with a block of text

def summarize(article):
    final = ""
    # get the number of sentences
    sentence_break = ". "
    numSentences = article.count(sentence_break)
    if numSentences <= 5:
        article = re.sub("[\(\[].*?[\)\]]", "", article)
        return article
    else:
        article = re.sub("[\(\[].*?[\)\]]", "", article)
        sentences = article.split(". ")
        for i in range(3):
            final += sentences[i] + ". "
    return final


print(summarize(intro))


import wikipedia

# with open("C:\\Users\\Justi\\OneDrive\\Desktop\\API keys\\smmry_api.txt", "r") as apiKey:
#     key = apiKey.readlines()
# URL = "https://api.smmry.com"
# SMMRY_URL = URL + "?SM_API_KEY=" + key

# def getIntro(article):
#     return intro

keywords = "Cristiano Ronaldo"

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

    # get the number of sentences
    sentence_break = ". "
    numSentences = article.count(sentence_break)
    if numSentences <= 5:
        return removeBrackets(article)
    return numSentences

def removeBrackets(article):
    for i in range(le)

print(summarize(intro))
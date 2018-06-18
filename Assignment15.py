# *** Question 1 ***
import re
emails = """zuck26@facebook.com
            page33@google.com
            jeff42@amazon.com"""
pattern = r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})'
a = re.findall(pattern, emails, flags=re.IGNORECASE)
print(a)


# *** Question 2 ***
import re
text = """Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."""
x = re.findall(r'\bB\w+', text, flags=re.IGNORECASE)
print(x)


# *** Question 3 ***
import re
sentence = """A, very   very; irregular_sentence"""
x = " ".join(re.split('[;,\s_]+', sentence))
print(x)


# *** Question 4 ***
import re
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
def clean_tweet(tweet):
    tweet = re.sub('http\S+\s*', '', tweet)
    tweet = re.sub('RT|cc', '', tweet)
    tweet = re.sub('#\S+', '', tweet)
    tweet = re.sub('@\S+', '', tweet)
    tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)
    tweet = re.sub('\s+', ' ', tweet)
    return tweet

print(clean_tweet(tweet))

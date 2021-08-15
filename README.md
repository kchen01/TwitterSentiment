# TwitterSentiment


Given a username, returns current public sentiment on the person by analyzing the tone of recent tweets directed to that account.

For example, running the following

      "python3 main.py exampleUser"
      
yields results like this:

"
Sadness was 1% of Twitter users' recent reactions to exampleUser.
Confident was 15% of Twitter users' recent reactions to exampleUser.
Analytical was 23% of Twitter users' recent reactions to exampleUser.
Joy was 40% of Twitter users' recent reactions to exampleUser.
Tentative was 10% of Twitter users' recent reactions to exampleUser.
Anger was 6% of Twitter users' recent reactions to exampleUser.
Fear was 2% of Twitter users' recent reactions to exampleUser.
"


To run, one must create a Twitter Developer account to use the Twitter API and an IBM Cloud account to use the Watson Tone Analyzer and fill out the codes in "codes.py".

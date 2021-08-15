## TwitterSentiment


Given a username, returns current public sentiment on the person by analyzing the tone of recent tweets directed to that account.

For example, running the following request

      "python3 main.py KeanuReevesoff1"
      
yields results like this:

  
      Sadness was 1% of Twitter users' recent reactions to KeanuReevesoff1.

      Confident was 15% of Twitter users' recent reactions to KeanuReevesoff1.

      Analytical was 23% of Twitter users' recent reactions to KeanuReevesoff1.

      Joy was 40% of Twitter users' recent reactions to KeanuReevesoff1.

      Tentative was 10% of Twitter users' recent reactions to KeanuReevesoff1.

      Anger was 6% of Twitter users' recent reactions to KeanuReevesoff1.

      Fear was 2% of Twitter users' recent reactions to KeanuReevesoff1.


To run, one must create a Twitter Developer account to use the Twitter API, an IBM Cloud account to use the Watson Tone Analyzer, use pip to install "ibm_watson" and "requests", and fill out the corresponding codes in "codes.py".


#### Created by Etienne Richart (github.com/etiennerichart) and Kevin Chen (github.com/kchen01).

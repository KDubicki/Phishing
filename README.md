

## Introduction

This is a project being carried out during my studies. I have decided to share it here and present the results I obtained during the implementation, of course without sensitive data such as emails or links that the scraping script used to collect email addresses.


## Tech

Scraping script, mail sender script, Google Analytics, and ready HTML templates.



## Project process

1. Choosing the target group.
2. Using a scraping script to retrieve email addresses from a public source of the targeted group.
3. Preparing pages that will be used for collecting statistics.
4. Activating Google Analytics and linking it to the pages.
5. Using a script to send emails and waiting for the results.
6. To be happy that interesting information has been gathered.

## Results

| Grupe     | Sended mails |   views   |   Captured users | Return emails |
| --------- | ------------ | --------- | ---------------- | ------------- |
| A         | 17           |    12     |   5              |  1            |
| B         | 23           |    4      |   2              |  0            |
| C         | 35           |    15     |   11             | 1             |

The real number of users who clicked on links in the emails is somewhere between the views and the captured users, because if two users used the same device but at different times, Google Analytics still sees them as the same user.

![Phishing graph](https://i.pinimg.com/236x/c4/48/9a/c4489af34519fb1e90f50c8626bb65cf.jpg){width=400}

Okay, now for the really interesting part. I cannot share the bounce emails here, but thanks to them, I learned that the emails I sent were modified before reaching the recipient by adding a prefix at the beginning of the email content about being cautious and not clicking on any links.

Based on the results, it's clear that even though the recipients were warned to be cautious, a significant number of them still clicked on the links and even replied to the emails, demonstrating that humans are often the weakest part when it comes to cybersecurity.

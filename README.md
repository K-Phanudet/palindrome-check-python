# Palindrome-check-python


## Getting started
---

>Palindrome-check-python is a function for check string is a palindrome or not. It is a basic exercise for thinking of a practical problem-solving algorithm. In this project we choose python to solve problem because it easy to understand for beginner .

To get started with repo you might have to clone or download the repository just as shown below;
>https://github.com/K-Phanudet/palindrome-check-python

## Palindrome
---
#### Definition of palindrome
>a word, verse, or sentence (such as "Able was I ere I saw Elba") or a number (such as 1881) that reads the same backward or forward ( reference: https://www.merriam-webster.com/dictionary/palindrome )

#### Examples 
```python
'anna' -> 'an'|'na'
'civic' -> 'ci'|'v'|'ic' 
'step on no pets' -> 'step on'|'no pets'  
'radar' -> 'ra'|'d'|'ar'
'solos' -> 'so'|'l'|'os'
```

## Demo
---
```python
from algorithms import isPalindrome
text = "noon"
isPalindrome(text)
True
text = "why"
isPalindrome(text)
False
```
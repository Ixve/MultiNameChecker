# MultiNameChecker
A basic and slow name checker for multiple sites

Current sites:
GitHub

Instagram

Kik (!ONLY CHECKS ws2.kik.com!)

PasteBin

Solo.to


It works as you would expect it
Send GET request to website with username from usernames.txt -> if site returns status code 404 -> print "[ website, statuscode ] available + username" & add to available_website.txt
else if site doesnt return status code 404 -> print "[ website, statuscode ] unavailable + username" & go to next

This is veerry basic and is slow, if you need a faster checker try something like https://github.com/checker/cli , it is probably 1000% faster and pretty sure it has proxy support (including more websites it checks)

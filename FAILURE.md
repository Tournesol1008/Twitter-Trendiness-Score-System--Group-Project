In server.py, we documents some failure points including HTTPError(Trouble with requesting the url), ConnectionError(losing internet connection). 
For HTTPError, error code 429 is the only error we encountered, so we decided to write a chuck of code in connection_to_endpoint function to deal with "Too many request"(request_status_code = 429) issue. Basically, it calculates the remaining time that allows us to request the url again and suspends execution for the given remaining time.
For ConnectionError, we catch the error in the main function and the way to handling this issue is to tell users that there is an internet connection issue and will retry after 10 seconds.
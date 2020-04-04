# SFS
StandForSudan historic data for graphs

quickly written scripts to grap data from ebs website to do analysis on the data

## Description
the script when ran will send a request to SFS endpoint to grap numbers
then saves these in json, csv files and printing to terminal

## Content of the repo
1. python script (grabber.py)
2. json file (StandForSudan_DATA.json)
3. csv file (StandForSudan_DATA.csv)
4. terminal log file (log.txt)

## How to run
I recommend running the script in a linux environment however it should work on windows if you install missing libraries

1. create a cron job to run the script every 1 hour

```
crontab -e
*/1 * * * * python3 grabber.py >> ~/log.txt
```

2. you can watch data from the files by cat-ing them in a watch command

```
watch -n 3600 'cat ~/log.txt'
watch -n 3600 'cat ~/StandForSudan.json'
watch -n 3600 'cat ~/StandForSudan.csv'
```
3. putting it all in a background session using tmux because i like it...

```
tmux new -s SFS
watch -n 3600 'cat ~/log.txt'

```


my current setup is like this:
![setup](realtime-analytics.png "real time setup")


## Graphs and illustrations

 Making sense of the data example one - using splunk free:
![splunk](time-chart-01.png "Overtime")



## if you want to help
If you can help create visualizations and graphs from the data please do it and send me a message on twitter jaw33sh and will add it here along with your name
please create an issue or a pull request

### how to write an issue
1. go to issues tab and create a new issue
2. include any relevant information i need to replicate your issue
3. describe the issue as you would for a 10 year old


## Credits
friends and folks who helped on the code:
1. anonymous
2. anonymous
3. anonymous
4. anonymous

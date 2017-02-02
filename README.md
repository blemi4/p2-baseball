# Baseball: Salaries and Wins
An investigation into whether or not the same factors that are correlated with players contributions to winning games are also correlated with salaries.  The goal is to identify any player types (or individuals) that are not valued properly by the MLB.

I began by trimming the data to exclude years before 1980 because I am primarily concerned with the modern game.  I also created new metrics that are popular among stats minded teams and fans.  Read more here: https://en.wikipedia.org/wiki/Sabermetrics.

First I looked at the distribution of team wins for the data from 1980 on.  I expected the plot to be normal, but it is fairly negatively skewed.  It turns out this was mainly due to the player strike in 1994 that led to the season being shortened.

![Wins Histogram](/images/winshisto.png)

Here is what the distribution looks like with 1994 removed:

![Wins Histogram2](/images/winshisto2.png)

The difference is subtle, but you can easily tell that there are far fewer teams with less than 60 wins.

For each team metric, I wanted to see what variables were most related to winning percentage.

![Linear Regression Coefficients](/images/coefficients.png)

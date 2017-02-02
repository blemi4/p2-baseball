# Baseball: Salaries and Wins
An investigation into whether or not the same factors that are correlated with players contributions to winning games are also correlated with salaries.  The goal is to identify any player types (or individuals) that are not valued properly by the MLB.

I began by trimming the data to exclude years before 1980 because I am primarily concerned with the modern game.  I also created new metrics that are popular among stats minded teams and fans.  Read more here: https://en.wikipedia.org/wiki/Sabermetrics.

### What factors are important to winning games?

First I looked at the distribution of team wins for the data from 1980 on.  I expected the plot to be normal, but it is fairly negatively skewed.  It turns out this was mainly due to the player strike in 1994 that led to the season being shortened.

![Wins Histogram](/images/winshisto.png)


Here is what the distribution looks like with 1994 removed:

![Wins Histogram2](/images/winshisto2.png)

The difference is subtle, but you can easily tell that there are far fewer teams with less than 60 wins.

For each team metric, I wanted to see what variables were most related to winning percentage.  I ran a simple linear regression on each metric with win percentage as the dependent variable.  It's worth noting that each variable is standardized.  As you can see, Runs and Runs Against have the highest and lowest coefficients, respectively.  This makes intuitive, because the more runs you score and the less runs you allow on average, the higher you'd expect your win percentage to be.  It's also worth noting that On Base Percentage (OBP), Slugging Percentage (SP), and OPS (On Base Plus Slugging) are all near the top.  These are the metrics I created using other metrics that already existed in the data.  It makes sense why these are so popular among stats gurus across MLB front offices.

![Linear Regression Coefficients](/images/coefficients.png)

I also ran a Random Forest Regressor on all of the metrics at once and charted the feature importance or the information gain from each metric.  Once again, Runs and Runs Against are the most important features, with Earned Run Average (ERA) coming in third.  ERA is essentially the rate at which a pitcher allows runs that are explicitly that pitchers fault, so runs allowed due to fielding errors are not factored in.  Since most runs allowed are indeed the pitchers fault, it makes sense that this comes in third for feature importance.

![Random Forest Feature Importances](/images/feature_importances.png)


### What factors are important to scoring runs?
Because scoring runs is such an important part of winning games, we will now look at what factors are important to scoring runs at the team level.  After we have a good idea of what metrics correlate with scoring, we will be able to look at individual player data to see how those important factors lineup with salaries.

# Work in progress...

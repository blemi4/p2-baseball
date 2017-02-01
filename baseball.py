from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from preprocessing import teams
import statsmodels.api as sm
from patsy import dmatrices

# columns for regression
cols_for_regression = ['singles','doubles', 'triples', 'hr', 'bb', 'r', 'ra',
                        'so','sb', 'cs', 'cg', 'sho', 'sv', 'ba', 'sp',
                         'ipouts', 'ha', 'bba', 'soa', 'e', 'dp', 'era', 'obp',
                          'sp','ops', 'w']

cols_for_regression = ['doubles', 'triples', 'hr', 'bb', 'r', 'ra', 'h',
                        'so','sb', 'cg', 'ha', 'bba', 'soa', 'e', 'ba', 'era', 'obp', 'sp','ops', 'w']

teams = teams.rename(index=str, columns={'1b':'singles', '2b':'doubles', '3b':'triples'})

rteams = teams[cols_for_regression]

def regress(X_train, X_test, y_train, y_test):
    mod = sm.OLS(y_train, X_train)
    res = mod.fit()
    print res.summary()

def rfregress(X_train, X_test, y_train, y_test):
    rf = RandomForestRegressor(n_estimators=50).fit(X_train, y_train)
    preds = rf.predict(X_test)
    # print feature_importances in descending order
    fi = (sorted(zip(X_train.columns.tolist(),
            rf.feature_importances_), key=lambda x: x[1])[::-1])
    nos = [x[1] for x in fi]
    labs = [x[0] for x in fi]
    for lab in labs:
        if lab == 'doubles':
            labs[labs.index(lab)] = '2B'
        elif lab == 'triples':
            labs[labs.index(lab)] = '3B'
    labs = [lab.upper() for lab in labs]
    x = range(len(nos))
    plt.plot(x[:-1],nos[:-1], lw=2)
    plt.xticks(x[:-1], labs[:-1])
    plt.title('Random Forest Feature Importance')
    plt.savefig('images/feature_importances.png')
    plt.show()
    print labs

def linregress(X_train, X_test, y_train, y_test):
    coef = []
    for col in X_train.columns.tolist():
        X = StandardScaler().fit_transform(X_train[col])
        lr = LinearRegression()
        lr.fit(X.reshape(-1, 1), y_train)
        coef.append([col, lr.coef_])
    coef = sorted(coef, key=lambda x: x[1])[::-1]
    nos = [x[1] for x in coef]
    labs = [x[0] for x in coef]
    for lab in labs:
        if lab == 'doubles':
            labs[labs.index(lab)] = '2B'
        elif lab == 'triples':
            labs[labs.index(lab)] = '3B'
        elif lab == 'Intercept':
            idx = labs.index('Intercept')
            labs.pop(idx)
            nos.pop(idx)
    labs = [lab.upper() for lab in labs]
    x = range(len(nos))
    plt.plot(x,nos, lw=2, c='b')
    plt.xticks(x, labs)
    plt.title('Linear Regression Coefficients')
    plt.savefig('images/coefficients.png')
    plt.show()
    print labs

# def rfdrop(X_train, X_test, y_train, y_test):
#     scores = []
#     for col in X_train.columns.tolist():
#         excluded = X_train.pop(col)
#         trash = X_test.pop(col)
#         rf = RandomForestRegressor().fit(X_train, y_train)
#         preds = rf.predict(X_test)
#         mse = mean_squared_error(y_test, preds)
#         scores.append([col, mse, np.mean(preds)])
#         X_train[col] = excluded
#         X_test[col] = trash
#     print np.array(sorted(scores, key=lambda x: x[2]))

def plot_wins_histo():
    plt.hist(y)
    plt.title('Winning Percentage Histogram')
    plt.savefig('images/winshisto.png')
    plt.show()

def plots(x, y, x_lab, y_lab):
    plt.plot

if __name__ == '__main__':
    plt.close('all')
    plt.style.use('ggplot')
    rteams = teams[cols_for_regression]
    y, X = dmatrices('w ~ {}'.format(' + '.join(cols_for_regression[:-1])), data=rteams, return_type='dataframe')
    y = np.ravel(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=5)
    # scaler = StandardScaler().fit(X_train)
    # X_train = scaler.transform(X_train)
    # X_test = scaler.transform(X_test)
    # regress(X_train, X_test, y_train, y_test)
    # rfregress(X_train, X_test, y_train, y_test)
    # plot_wins_histo()
    linregress(X_train, X_test, y_train, y_test)

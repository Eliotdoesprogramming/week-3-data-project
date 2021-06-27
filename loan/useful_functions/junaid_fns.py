import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_curve
def feature_plot(coef, columns, y_title = 'coefficients',plt=plt):
    feature_imp = pd.DataFrame(coef.T, columns = ['importance'])#features.columns)
    feature_imp['feature'] = columns
    feature_imp.sort_values(by = ['importance'], ascending = False, inplace = True)
    feature_imp.plot(x='feature', kind = 'bar', figsize = (16,4))
    plt.title(y_title)
    plt.ylabel(y_title)
    return

def print_report(search_results, top_n = 2): # top 2 if top_n not given!
    
    # I want top 5, means 1 to 5, I need to start from 1 using range and add 1 in upper limit (top_n)
    for i in range(1, top_n + 1):
        
        # tow things:
        # Notice, you have 'rank_test_score' in keys above {random_search.cv_results_.keys()}
        # flatnonzero return indices that are non-zero in the flattened version
        # of array random_search_results['rank_test_score']
        rank = np.flatnonzero(search_results['rank_test_score'] == i)

        for val in rank: # val is the index location!
            print("Model rank: ", i)
            print("Mean validation score: {:.3f}".format(search_results['mean_test_score'][val]))
            print("std_test_score: {:.3f}".format(search_results['std_test_score'][val]))
            print("Parameters: {}\n".format(format(search_results['params'][val])))

def plot_rocs(y_test, prob, AUC_ROC, ax, title = 'title'):#, y_label = 'y_label', x_label = 'x_label'):
    """
    This is going to be our docstring! Good for your practice
    y_test = test data
    prob = predicted probabilities from our trained model
    AUC_ROC = Area Under ROC Curve
    ax = figure axis on which we want to put our plot
    title = given title
    """
    fpr, tpr, thresholds = roc_curve(y_test, prob[:,1])
    
    # plot no skill - A line for random guess
    ax.plot([0, 1], [0, 1], linestyle='--', label = 'Random guess' )
    #plt.plot([0, 1], [0, 1], linestyle='--', label = 'Random guess' )
    
    # plot the roc curve for the model
    ax.plot(fpr, tpr, marker='.', label = 'ROC - Area Under The Curve: %.3f' % AUC_ROC)
    
    # let's set the limits (0,1)
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])

    # good to put title and labels
    ax.set_title(title)
    ax.set_ylabel('True Positive Rate')
    ax.set_xlabel('False Positive Rate')
    
    # putting the legends  
    ax.legend();
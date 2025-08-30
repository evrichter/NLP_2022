from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import seaborn

def build_classification(final_data, data):
    X_train,X_test,y_train,y_test = train_test_split(final_data,data['label'],test_size=.2)

    nb_model = MultinomialNB(fit_prior = True).fit(X_train, y_train)
    nb_prediction = nb_model.predict(X_test)
    nb_precision,nb_recall,nb_fscore,nb_support = score(y_test,nb_prediction,pos_label=1,average='binary')
    print('Precision: {} / Recall: {} / Accuracy: {}'.format(round(nb_precision, 3),
                                                            round(nb_recall, 3),
                                                            round((nb_prediction==y_test).sum() / len(nb_prediction),3)))


def build_confusion_matrix(y_test, nb_prediction):
    cf_matrix = confusion_matrix(y_test, nb_prediction, labels=['ham','spam'])
    seaborn.heatmap(cf_matrix, annot=True)
    # seaborn.heatmap(cf_matrix/numpy.sum(cf_matrix), annot=True, 
    #         fmt='.2%', cmap='Blues')

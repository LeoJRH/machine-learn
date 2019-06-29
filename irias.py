from sklearn.datasets import load_iris, fetch_20newsgroups
from sklearn.model_selection import train_test_split


li = load_iris()

# print("Get TZ:")
# print(li.data)
# print("Get MB:")
# print((li.target))
# print(li.DESCR)
# Return both train x_train,ytrain and test x_test y_test
#x ---TZ    y ---XL
# x_train,x_test,y_train,y_test = train_test_split(li.data, li.target, test_size=0.25)
#
# print("Train x and y:", x_train, y_train)
# print("Test x and y:", x_test, y_test)

news = fetch_20newsgroups(subset='all')
print(news.data)
print(news.target)
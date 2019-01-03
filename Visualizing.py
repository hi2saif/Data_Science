#Tools for visualizing data -->  Bokeh for creating interactive plots and [Seaborn] for creating "static" (or non-interactive) plots


#Part 0: Downloading some data to visualize
import requests
import os
import hashlib
import io

def download(file, url_suffix=None, checksum=None):
    if url_suffix is None:
        url_suffix = file
        
    if not os.path.exists(file):
        url = 'https://cse6040.gatech.edu/datasets/{}'.format(url_suffix)
        print("Downloading: {} ...".format(url))
        r = requests.get(url)
        with open(file, 'w', encoding=r.encoding) as f:
            f.write(r.text)
            
    if checksum is not None:
        with io.open(file, 'r', encoding='utf-8', errors='replace') as f:
            body = f.read()
            body_checksum = hashlib.md5(body.encode('utf-8')).hexdigest()
            assert body_checksum == checksum, \
                "Downloaded file '{}' has incorrect checksum: '{}' instead of '{}'".format(file, body_checksum, checksum)
    
    print("'{}' is ready!".format(file))
    
datasets = {'iris.csv': ('tidy', 'd1175c032e1042bec7f974c91e4a65ae'),
            'tips.csv': ('seaborn-data', 'ee24adf668f8946d4b00d3e28e470c82'),
            'anscombe.csv': ('seaborn-data', '2c824795f5d51593ca7d660986aefb87'),
            'titanic.csv': ('seaborn-data', '56f29cc0b807cb970a914ed075227f94')
           }

for filename, (category, checksum) in datasets.items():
    download(filename, url_suffix='{}/{}'.format(category, filename), checksum=checksum)
    
print("\n(All data appears to be ready.)")


#Part 1: Bokeh and the Grammar of Graphics ("lite")
	#Setup
	from IPython.display import display, Markdown
	import pandas as pd
	import bokeh

#Philosophy: Grammar of Graphics
#The Grammar of Graphics is an idea of Leland Wilkinson. Its basic idea is that the way most people think about visualizing data is ad hoc and unsystematic, whereas there exists in fact a "formal language" for describing visual displays.

#The reason why this idea is important and powerful in the context of our course is that it makes visualization more systematic, thereby making it easier to create those visualizations through code.

#The high-level concept is simple:

#1Start with a (tidy) data set.
#2Transform it into a new (tidy) data set.
#3Map variables to geometric objects (e.g., bars, points, lines) or other aesthetic "flourishes" (e.g., color).
#4Rescale or transform the visual coordinate system.
#5Render and enjoy!

#Example--> You need to dwnload iris.csv by using above code
from IPython.display import display, Markdown
import pandas as pd
import bokeh
flora = pd.read_csv ('iris.csv')
display (flora.head ())


#1. Histogram
#*The Histogram(f, e) can takes two arguments, frequencies and edges (bin boundaries).
#*These can easily be created using numpy's histogram function as illustrated below.
#The plot is interactive and comes with a bunch of tools. You can customize these tools as well; 
#for your many options, see http://bokeh.pydata.org/en/latest/docs/user_guide/tools.html.

#example 
from bokeh.io import show
import holoviews as hv
import numpy as np
frequencies, edges = np.histogram(flora['petal width'], bins = 5)
hv.Histogram(frequencies, edges, label = 'Histogram')

#2. ScatterPlot
hv.Scatter(flora[['petal width','sepal length']],label = 'Scatter plot')

#3. BoxPlot
hv.BoxWhisker(flora['sepal length'], label = "Box whiskers plot")


#Mid-level charts: the Plotting interface
#Beyond the canned methods above, Bokeh provides a "mid-level" interface that more directly exposes the grammar of graphics methodology for constructing visual displays.

#The basic procedure is

	#Create a blank canvas by calling bokeh.plotting.figure
	#Add glyphs, which are geometric shapes.
	
#example
from bokeh.plotting import figure

# Create a canvas with a specific set of tools for the user:
TOOLS = 'pan,box_zoom,wheel_zoom,lasso_select,save,reset,help'
p = figure(width=500, height=500, tools=TOOLS)
p.triangle(x=flora['petal width'], y=flora['petal length'])
show(p)

#Using data from Pandas. Here is another way to do the same thing, but using a Pandas data frame as input.
from bokeh.models import ColumnDataSource

data=ColumnDataSource(flora)
p=figure()
p.triangle(source=data, x='petal width', y='petal length')
show(p)


#Color maps
#***********************************************************#
#
unique_species = flora['species'].unique()
print(unique_species)

#
from bokeh.palettes import brewer
color_map = dict(zip(unique_species, brewer['Dark2'][len(unique_species)]))
print(color_map)

#
p = figure()
for s in unique_species:
    p.triangle(source=data_sources[s], x='petal width', y='petal length', color=color_map[s])
show(p)
#***************************************************************#

	Part 2: Static visualizations using Seaborn
	
#Plotting univariate distributions
import seaborn as sns

# The following Jupyter "magic" command forces plots to appear inline
# within the notebook.
%matplotlib inline
import numpy as np
x = np.random.normal(size=100)
sns.distplot(x)


#Plotting bivariate distributions
#ScatterPot
mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
df = pd.DataFrame(data, columns=["x", "y"])
sns.jointplot(x="x", y="y", data=df)

#Hexbin plots
mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
df = pd.DataFrame(data, columns=["x", "y"])
sns.jointplot(x="x", y="y", data=df, kind="hex")

#Kernel density estimation.
mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
df = pd.DataFrame(data, columns=["x", "y"])
sns.jointplot(x="x", y="y", data=df, kind="kde")
	
	
		Visualizing pairwise relationships in a dataset
		
sns.pairplot(flora)
sns.pairplot(flora, hue="species")
	
		Visualizing linear relationships
		
tips = pd.read_csv("tips.csv")
tips.head()

#We can use the function regplot to show the linear relationship between total_bill and tip. It also shows the 95% confidence interval.
sns.regplot(x="total_bill", y="tip", data=tips)

		Visualizing higher order relationships
		
anscombe = pd.read_csv("anscombe.csv")
sns.regplot(x="x", y="y", data=anscombe[anscombe["dataset"] == "II"])

#Let's try to fit a polynomial regression model with degree 2.
sns.regplot(x="x", y="y", data=anscombe[anscombe["dataset"] == "II"], order=2)
sns.stripplot(x="day", y="total_bill", data=tips)
sns.boxplot(x="day", y="total_bill", hue="time", data=tips)

titanic = pd.read_csv("titanic.csv")
sns.barplot(x="sex", y="survived", hue="class", data=titanic)


#Box Plot --> are generally useful when we are trying t understa


nd the variation in the values for a given attribute
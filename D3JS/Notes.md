### Notes de D3.js 



> 📣 **IMPORTANT**   
> The `g` element in svg.  
> when we apped to it for examplea circle with cx, cy coordinates
> these coordinates are relative to `g` and not the `svg`  



## DOM selection 

```js
d3.select(css-selector)
```
Returns the first matching element in the HTML document based on specified css-selector

<br>


```js
d3.selectAll(css-selector)
```
Returns all the matching elements in the HTML document based on specified css-selector  


<br>  

```js
d3.select("tr").selectAll("td").style('background-color','yellow');
```
Returns all the matching elements in the HTML document based on specified css-selector


<br>

## DOM Manipulation
text   
append  
insert  
remove  
html   
attr  
property   
style   
classed  

all this can be called on any selected Dom element
also a call back function is given for example 
```js
.text(function(d, i){
    return d +'demo callback'
})
```

So in general we have a selection (it can be one or multiple).
We can append, or text, or remove...etc also give a callback function where we have the d that represents the data in that element and i is the index

## Function of data
each of the above functions in DOM manipulation, when bound to a data (not only when bound, it can work even with not `.data()` )document, it can have a callback function like this: 

```js

var data = [100, 200, 300];
var paragraph = d3.select("body")
        .selectAll("p")
        .data(data)
            .text(function (d, i) {
                console.log("d: " + d);
                console.log("i: " + i);
                console.log("this: " + this);

                return d;
            });

```

`this` refers to the current DOM element




### Event handling in D3


<table>
 <thead>
                <tr>
                    <th>Event Methods
                    </th>
                    <th>Description
                    </th>
                </tr>
</thead>
<tbody>
    <tr>
        <td>selection.on()
        </td>
        <td>Add or remove event listeners to capture event types like click, mouseover, mouseout etc.
        </td>
    </tr>
    <tr>
        <td>selection.dispatch()
        </td>
        <td>Captures event types like click, mouseover, mouseout. Typenames is the eventname, listener is the event listener 
        </td>
    </tr>
    <tr>
        <td>d3.event
        </td>
        <td>Event object to access standard event fields such as timestamp or methods like preventDefault
        </td>
    </tr>
    <tr>
        <td>d3.mouse(container)
        </td>
        <td>Gets the x and y coordinates of the current mouse position in the specified DOM element.
        </td>
    </tr>
    <tr>
        <td>d3.touch()
        </td>
        <td>Gets the touch coordinates to a container
        </td>
    </tr>
</tbody>
</table>

`selection` means a certain selected elements like  
__Example__ 
```js
d3.selectAll("div")
      .on("mouseover", function(){
          d3.select(this)
            .style("background-color", "orange");

          // Get current event info
          console.log(d3.event);
          
          // Get x & y co-ordinates
          console.log(d3.mouse(this));
      })
      .on("mouseout", function(){
          d3.select(this)
            .style("background-color", "steelblue")
      });
```
>**NOTE**  
>careful use function() and not ()=>   
>this keyword changes depend on which one you use

<br>

## Animation in d3
`.transition()`  
`.duration()`
<br>

`.ease()`

  
## Data binding in D3
### We have  
* data()  :
* enter() :
* exit()  :
* remove():
* datum() : 


### data()
D3 is data driven. The data() function is used to **join the specified array** of **data** to the **selected DOM elements** and return the updated selection. D3 works with different types of data like Array, CSV, TSV, JSON, XML etc.


* Also it binds the data ligne to ligne
ceci veut dire que l'orsque par exemple il trouve pas de p et que notre data array contient 5 element. Il va appliquer la fonctin dans text() seulement sur le premier element
pour cela nous introduisons `enter()`


### exemple : 
```html
<body>  
<p></p>
<script>
    var data = [4, 1, 6, 2, 8, 9];
    var body = d3.select("body")
                .selectAll("p")
                .data(data)
    			.text("ici il ya")

                // le cas ou il ne trouve pas d'association
                .enter()
                .append("p")
                .text(function(d) { return d + " "; });
</script>
</body>
```

## Data loading 


### csv 
`d3.csv('filepath', callbackfunc);`  
`d3.json('filepath', callbackfunc);`






## Creating SVG

### SVG Line

```html
<svg width="500" height="500">
    <line x1="100" y1="50" x2="500" y2="50" stroke="black"/>
</svg>
```

### SVG Rectangle
x,y , width, height

(x,y) : les coordonnées du top left corner
width, height comme leur nom l'indique


### circle 
cx,cy et r




## Create SVG chart 

### 🦎 Geometry \<g>
- group element \<g> : for example to hold the bar and the text element

### 🦎 Transform attribute 

On a la translation `translate(tx, ty)`  
<br>

## Scales and Axes


### 🦎 Scales
D3 Scales provide a convenient solution to this. They map our data values to values that would be better represented in visualizations. D3 provides the following scaling methods for different types of charts.

<table >
            <thead>
                <tr>
                    <th>Scale Type
                    </th>
                    <th>Method
                    </th>
                    <th>
                        Description
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td rowspan="6">Continuous</td>
                    <td>d3.scaleLinear()
                    </td>
                    <td>
                        Construct continuous linear scale where input data (domain) maps to specified output range.
                    </td>
                </tr>
                <tr>
                    <td>d3.scaleIdentity()
                    </td>
                    <td>
                        Construct linear scale where input data is the same as output.
                    </td>
                </tr>
                 <tr>
                    <td>d3.scaleTime()
                    </td>
                    <td>
                        Construct linear scale where input data is in dates and output in numbers.
                    </td>
                </tr>
                <tr>
                    <td>
                        d3.scaleLog()
                    </td>
                    <td>Construct logarithmic scale.</td>
                </tr>
                <tr>
                    <td>
                        d3.scaleSqrt()
                    </td>
                    <td>
                        Construct square root scale. 
                    </td>
                </tr>
                <tr>
                    <td>
                        d3.scalePow()
                    </td>
                    <td>
                        Construct exponential scale. 
                    </td>
                </tr>
                <tr>
                    <td>Sequential</td>
                    <td>
                        d3.scaleSequential()
                    </td>
                    <td>
                        Construct sequential scale where output range is fixed by interpolator function. 
                    </td>
                </tr>
                 <tr>
                    <td>Quantize</td>
                    <td>d3.scaleQuantize()
                    </td>
                    <td>
                        Construct quantize scale with discrete output range.
                    </td>
                </tr>
                 <tr>
                    <td>Quantile</td>
                    <td>d3.scaleQuantile()
                    </td>
                    <td>
                        Construct quantile scale where input sample data maps to discrete output range.
                    </td>
                </tr>
                <tr>
                    <td>Threshold</td>
                    <td>d3.scaleThreshold()
                    </td>
                    <td>
                        Construct scale where arbitrary input data maps to discrete output range.
                    </td>
                </tr>                                 
                <tr>
                    <td>Band </td>
                    <td>d3.scaleBand()
                    </td>
                    <td>
                        Band scales are like ordinal scales except the output range is continuous and numeric.
                    </td>
                </tr>
                 <tr>
                    <td>Point </td>
                    <td>d3.scalePoint()
                    </td>
                    <td>
                        Construct point scale.
                    </td>
                </tr>
                <tr>
                    <td>Ordinal</td>
                    <td>d3.scaleOrdinal()
                    </td>
                    <td>
                        Construct ordinal scale where input data includes alphabets and are mapped to discrete numeric output range.
                    </td>
                </tr>
            </tbody>
</table>

<br>

* **Domain**  
Domain denotes minimum and maximum values of your input data. In our data [100, 400, 300, 900, 850, 1000], 100 is minimum value and 1000 is maximum value.


* **Range**  
Range is the output range that you would like your input values to map to.


The main idea is like you have your data [] it has a minimum and maximum, and you want to display it but in a certain range because it depends on your svg width and height.so you will use a scaling method by D3. 

> Exemple
```js
var data = [100, 400, 300, 900, 850, 1000];

var scale = d3.scaleLinear()
            .domain([100, 1000])
            .range([50, 500]);
```


### d3.min() and d3.max()
In the above example, instead of providing minimum and maximum value for our domain manually we can use built-in d3.min() and d3.max() functions which will return minimum and maximum values respectively from our data array.


```js
var scale = d3.scaleLinear()
        .domain([d3.min(data), d3.max(data)])
        .range([50, 500]);

```

### Axes 
In D3 an Axis uses scales 


There is AxisTop
AxisBottom
AxisLeft
AxisRight
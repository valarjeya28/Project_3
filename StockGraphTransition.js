
var svgWidth = 1200;
var svgHeight = 660;

var margin = {
  top: 50,
  right: 50,
  bottom: 50,
  left: 50
};

var height = svgHeight - margin.top - margin.bottom;
var width = svgWidth - margin.left - margin.right;

// d3.csv("company_data.csv", function(error, company) {

// data
var StockPrices = [57.76, 95.3, 68.96, 100.75, 114.71, 112.71, 154.12, 225.74];
var YearEnd = ["2011", "2012", "2013", "2014", "2015", "2016",
"2017", "2018"
];


// append svg and group
var svg = d3.select(".chart")
  .append("svg")
  .attr("height", svgHeight)
  .attr("width", svgWidth);

var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// scales
var xScale = d3.scaleLinear()
  .domain([0, StockPrices.length])
  .range([0, width]);

var yScale = d3.scaleLinear()
  .domain([0, d3.max(StockPrices)])
  .range([height, 0]);


// line generator
var line = d3.line()
  .x((d, i) => xScale(i))
  .y(d => yScale(d));

// create path
chartGroup.append("path")
  .attr("d", line(StockPrices))
  .attr("fill", "none")
  .attr("stroke", "orange");

// append circles to data points
var circlesGroup = chartGroup.selectAll("circle")
  .data(StockPrices)
  .enter()
  .append("circle")
  .attr("r", "12")
  .attr("fill", "blue");

var xAxis = d3.axisBottom(xScale);
var yAxis = d3.axisLeft(yScale);

    // set x to the bottom of the chart
    chartGroup.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(xAxis);

// set y to the y axis
chartGroup.append("g")
    .call(yAxis);

// Event listeners with transitions
circlesGroup.on("mouseover", function() {
  d3.select(this)
    .transition()
    .duration(1500)
    .attr("r", 20)
    .attr("fill", "red");
 })
  .on("mouseout", function() {
    d3.select(this)
      .transition()
      .duration(1000)
      .attr("r", 10)
      .attr("fill", "blue");
  });

// transition on page load
chartGroup.selectAll("circle")
  .transition()
  .duration(1000)
  .attr("cx", (d, i) => xScale(i))
  .attr("cy", d => yScale(d));

function buildMetadata(ticker) {

    // @TODO: Complete the following function that builds the metadata panel
  
    // Use `d3.json` to fetch the metadata for a sample
      // Use d3 to select the panel with id of `#sample-metadata`
      var metadataURL = "/metadata/" + ticker;
      var panelMetadata =d3.select("#sample-metadata");
       panelMetadata.html("");
      // Use `.html("") to clear any existing metadata
  
      // Use `Object.entries` to add each key and value pair to the panel
      d3.json(metadataURL).then(function (data){
        console.log(data.results);
        Object.entries(data.results[0]).forEach(([key,value])=>
        {
          panelMetadata.append("h6").text(`${key}: ${value}`
          );
        });
        
      
      // Hint: Inside the loop, you will need to use d3 to append new
      // tags for each key-value in the metadata.
  
      // BONUS: Build the Gauge Chart
      // buildGauge(data.WFREQ);
  });
  }
  
  function buildCharts(ticker) {
  
    // @TODO: Use `d3.json` to fetch the sample data for the plots
     var chartsURL = "/ticker/" + ticker;
     d3.json(chartsURL).then(function (data){
      console.log(data);
      
      
//       // @TODO: Build a Bubble Chart using the sample data
        console.log(chartsURL);
        xvalue=[];
        yvalue=[];
        for (var i = 0, len = data.length; i < len; i++) {
          xvalue.push(data[i].calendardate);
          yvalue.push(data[i].price)
          
      };
    console.log(xvalue);
      var trace1 = {
        x: xvalue,
        y: yvalue,
        mode: 'lines',
        text: data.ticker,
        marker: {
          color: 'red',
          
      
          colorscale: "Earth"
        }
      };
      var trace1 = [trace1];
      var layout = {
        showlegend: false,
        height: 600,
        width: 900
      };
      
       Plotly.newPlot('line', trace1, layout);
      // // @TODO: Build a Pie Chart
      // // HINT: You will need to use slice() to grab the top 10 sample_values,
      // // otu_ids, and labels (10 each).
      // var data2 = [{
      //   "values": data.sample_values.slice(0, 10),
      //   "labels": data.otu_ids.slice(0, 10),
      //   "hovertext": data.otu_labels.slice(0, 10),
      //   "type": 'pie',
      // }];
      // var layout = {
      //   showlegend: true,
      // };
      // Plotly.newPlot('pie', data2, layout);
  
    
      
  })
     };
    
     
  
  function init() {
    // Grab a reference to the dropdown select element
    var selector = d3.select("#selDataset");
    console.log(selector);
    // Use the list of sample names to populate the select options
    d3.json("/ticker").then((tickerNames) => {
      tickerNames.forEach((ticker) => {
        selector
          .append("option")
          .text(ticker)
          .property("value", ticker);
      });
  
      // Use the first sample from the list to build the initial plots
      const firstSample = tickerNames[0];
       console.log(firstSample);
        buildCharts(firstSample);
       buildMetadata(firstSample);
    });
  }
  
  function optionChanged(newSample) {
    console.log(newSample);
    // Fetch new data each time a new sample is selected
     buildCharts(newSample);
     buildMetadata(newSample);
  }
  
  // Initialize the dashboard
  init();
  
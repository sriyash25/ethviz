import React, { useState } from 'react';
import ForceGraph3D from 'react-force-graph-3d';
import data from './data.json';
import Graph from './Graph';
import { saveAs } from 'file-saver';

function App() {
  const [graphData, setGraphData] = useState(data);
  const [addedNodes, setAddedNodes] = useState([]);

  // function to add a new node to an existing node
  function addNode() {
    const newNode = { id: `node${graphData.nodes.length + 1}`, label: `Node ${graphData.nodes.length + 1}` };
    const targetNode = graphData.nodes[0]; // add node to first node in array

    // add link between new node and target node
    const newLink = { source: newNode.id, target: targetNode.id };

    // update graph data state with new node and link
    setGraphData({
      nodes: [...graphData.nodes, newNode],
      links: [...graphData.links, newLink],
    });

    // update addedNodes state with new node
    setAddedNodes([...addedNodes, newNode]);
  }

  // function to export addedNodes to a file
  function exportNodes() {
    const json = JSON.stringify(addedNodes);
    const blob = new Blob([json], { type: 'application/json' });
    saveAs(blob, 'addedNodes.json');
  }

  return (
    <div className="App">
      <Graph graphData={graphData} setGraphData={setGraphData} />
    </div>
  );
}

export default App;

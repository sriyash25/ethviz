import React, { useRef, useState } from 'react';
import ForceGraph3D from 'react-force-graph-3d';

function Graph({ graphData, setGraphData }) {
  const [hoverNode, setHoverNode] = useState(null);
  const fgRef = useRef();

  function handleNodeHover(node) {
    setHoverNode(node);
  }

  function handleNodeClick(node) {
    const newNode = { id: `node${graphData.nodes.length + 1}`, label: `Node ${graphData.nodes.length + 1}` };
    const newLink = { source: node.id, target: newNode.id };

    setGraphData({
      nodes: [...graphData.nodes, newNode],
      links: [...graphData.links, newLink],
    });
  }

  function exportGraphData() {
    const jsonData = JSON.stringify(graphData, null, 2);
    const blob = new Blob([jsonData], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'graph-data.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  }

  return (
    <div>
      <button onClick={exportGraphData}>Export Graph Data</button>
      <ForceGraph3D
        ref={fgRef}
        graphData={graphData}
        nodeAutoColorBy="group"
        nodeLabel={(node) => node.label}
        linkWidth={2}
        linkDirectionalArrowLength={6}
        linkDirectionalArrowRelPos={1}
        onNodeHover={handleNodeHover}
        onNodeClick={handleNodeClick}
      />
    </div>
  );
}

export default Graph;

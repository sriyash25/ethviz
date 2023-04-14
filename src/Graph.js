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

  return (
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
  );
}

export default Graph;

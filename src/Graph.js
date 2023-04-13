import { ForceGraph3D } from 'react-force-graph';
import React, { useRef } from 'react';

function Graph({ graphData }) {
  const fgRef = useRef();

  function nodeVal(node) {
    if (node && node.label) {
      return node.label;
    }
    return node.id;
  }

  function handleNodeHover(node) {
    if (node) {
      fgRef.current.zoomToFit(400, 200, 20);
    }
  }

  return (
    <ForceGraph3D
      ref={fgRef}
      graphData={graphData}
      nodeVal={nodeVal}
      onNodeHover={handleNodeHover}
    />
  );
}

export default Graph;

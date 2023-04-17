import React, { useState, useEffect } from "react";
import { geoCentroid } from "d3-geo";
import {
  ComposableMap,
  Geographies,
  Geography,
  Marker,
  Annotation
} from "react-simple-maps";

import allStates from "./allstates.json";
import stateData from "./electricity.json";
import scatterData from "./scatter.json";

const geoUrl = "https://cdn.jsdelivr.net/npm/us-atlas@3/states-10m.json";

const offsets = {
  VT: [50, -8],
  NH: [34, 2],
  MA: [30, -1],
  RI: [28, 2],
  CT: [35, 10],
  NJ: [34, 1],
  DE: [33, 0],
  MD: [47, 10],
  DC: [49, 21]
};

const ElectricityChart = () => {
  const [markers, setMarkers] = useState([]);

  useEffect(() => {
    const newMarkers = Object.entries(scatterData)
      .filter(([_, { country }]) => country === "United States")
      .map(([ip, { longitude, latitude }]) => ({
        name: ip,
        coordinates: [longitude, latitude],
        markerOffset: -15,
      }));
    setMarkers(newMarkers);
  }, []);

  return (
    <ComposableMap projection="geoAlbersUsa">
      <Geographies geography={geoUrl}>
        {({ geographies }) => (
          <>
            {geographies.map(geo => {
              const cur = allStates.find(s => s.val === geo.id);
              const stateDatum = stateData.find(d => d.id === cur.id);
              const electricityUsage = stateDatum ? stateDatum.electricityUsage : null;
              console.log(stateDatum)
              return (
                <Geography
                  key={geo.rsmKey}
                  stroke="#FFF"
                  geography={geo}
                  fill={stateDatum ? getColor(electricityUsage) : "#DDD"}
                />
              );
            })}
            {geographies.map(geo => {
              const centroid = geoCentroid(geo);
              const cur = allStates.find(s => s.val === geo.id);
              return (
                <g key={geo.rsmKey + "-name"}>
                  {cur &&
                    centroid[0] > -160 &&
                    centroid[0] < -67 &&
                    (Object.keys(offsets).indexOf(cur.id) === -1 ? (
                      <Marker coordinates={centroid}>
                        <text y="2" fontSize={14} textAnchor="middle">
                          {cur.id}
                        </text>
                      </Marker>
                    ) : (
                      <Annotation
                        subject={centroid}
                        dx={offsets[cur.id][0]}
                        dy={offsets[cur.id][1]}
                      >
                        <text x={4} fontSize={14} alignmentBaseline="middle">
                          {cur.id}
                        </text>
                      </Annotation>
                    ))}
                </g>
              );
            })}
            {markers.map(({ name, coordinates, markerOffset }) => (
              <Marker key={name} coordinates={coordinates}>
                <circle r={5} fill="#0000FF" stroke="#fff" strokeWidth={0.5} />
                {/* <text textAnchor="middle" y={markerOffset} style={{ fontFamily: 'system-ui', fill: '#5D5A6D' }}>
                  {name}
                </text> */}
              </Marker>
            ))}
          </>
        )}
      </Geographies>
    </ComposableMap>
  );
};

function getColor(electricityUsage) {
  const maxUsage = 20.5;
  const minColor = [0, 255, 0];
  const maxColor = [255, 0, 0];
  const color = minColor.map((c, i) => {
    const diff = maxColor[i] - c;
    return Math.round(c + (diff * electricityUsage) / maxUsage);
  });
  return `rgb(${color.join(",")})`;
}

export default ElectricityChart;

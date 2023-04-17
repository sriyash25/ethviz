import React, { useState, useEffect } from 'react';
import { ComposableMap, Geographies, Geography, Marker } from 'react-simple-maps';

const geoUrl =
  "https://raw.githubusercontent.com/deldersveld/topojson/master/world-countries.json"

const MapChart = () => {
  const [markers, setMarkers] = useState([]);

  useEffect(() => {
    fetch('/latlong.json')
      .then((response) => response.json())
      .then((data) => {
        const newMarkers = Object.entries(data).map(([ip, [longitude, latitude]]) => ({
            name: ip,
            coordinates: [longitude, latitude],
            markerOffset: -15,
        }));
        setMarkers(newMarkers);
      });
  }, []);

  return (
    <ComposableMap>
      <Geographies geography={geoUrl}>
        {({ geographies }) =>
          geographies.map((geo) => <Geography key={geo.rsmKey} geography={geo} fill="#808080"/>)
        }
      </Geographies>
      {markers.map(({ name, coordinates, markerOffset }) => (
        <Marker key={name} coordinates={coordinates}>
          <circle r={3} fill="#F00" stroke="#fff" strokeWidth={0.5} />
          <text textAnchor="middle" y={markerOffset} style={{ fontFamily: 'system-ui', fill: '#5D5A6D' }}>
            {name}
          </text>
        </Marker>
      ))}
    </ComposableMap>
  );
};

export default MapChart;
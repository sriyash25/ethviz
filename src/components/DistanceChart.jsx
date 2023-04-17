import React, { useEffect, useRef, useState } from 'react';
import Chart from 'chart.js/auto';
import dataJson from './scatter.json';

const DistanceChart = () => {
  const chartRef = useRef();
  const chartInstanceRef = useRef(null);
  const [data, setData] = useState([]);
  const [pointSizeEnabled, setPointSizeEnabled] = useState(false);

  useEffect(() => {
    setData(dataJson);

    if (chartInstanceRef.current) {
      chartInstanceRef.current.destroy();
    }

    const myChartRef = chartRef.current.getContext('2d');

    const scatterData = Object.values(dataJson).reduce((result, point) => {
      result[point.country] = result[point.country] || {
        label: point.country,
        data: [],
        backgroundColor: [],
        borderColor: [],
        pointRadius: [],
      };

      result[point.country].data.push({ x: point.euclid_dist_normalized, y: point.xor_dist_normalized });
      result[point.country].backgroundColor.push(getColor(point.country, 1));
      result[point.country].borderColor.push(getColor(point.country, 1));
      result[point.country].pointRadius.push(pointSizeEnabled ? point.size_normalized * 20 : 3);

      return result;
    }, {});

    chartInstanceRef.current = new Chart(myChartRef, {
      type: 'scatter',
      data: {
        datasets: Object.values(scatterData),
      },
      options: {
        scales: {
          x: {
            type: 'linear',
            position: 'bottom',
            title: {
              display: true,
              text: 'Euclidean Distance Normalized',
            },
          },
          y: {
            type: 'linear',
            position: 'left',
            title: {
              display: true,
              text: 'XOR Distance Normalized',
            },
          },
        },
      },
    });
  }, [pointSizeEnabled]);

  const getColor = (country, alpha) => {
    const hash = stringToHash(country);
    const color = intToRGB(hash);
    return `rgba(${color.r}, ${color.g}, ${color.b}, ${alpha})`;
  };

  const stringToHash = (str) => {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      hash = str.charCodeAt(i) + ((hash << 5) - hash);
    }
    return hash;
  };

  const intToRGB = (int) => {
    const c = (int & 0x00FFFFFF).toString(16).toUpperCase();
    return {
      r: parseInt(c.substring(0, 2), 16),
      g: parseInt(c.substring(2, 4), 16),
      b: parseInt(c.substring(4, 6), 16),
    };
  };

  const togglePointSize = () => {
    setPointSizeEnabled((prev) => !prev);
  };

  return (
    <>
      <canvas ref={chartRef} />
      <button onClick={togglePointSize}>
        {pointSizeEnabled ? 'Disable Point Size' : 'Enable Point Size'}
      </button>
    </>
  );
};

export default DistanceChart;

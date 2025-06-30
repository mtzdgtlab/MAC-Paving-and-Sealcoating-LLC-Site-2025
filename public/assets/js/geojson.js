const njCountiesData = {
  "type": "FeatureCollection",
  "features": [
    { "type": "Feature", "properties": { "name": "Sussex" }, "geometry": { "type": "Polygon", "coordinates": [[[-74.5, 41.0], [-74.0, 41.0], [-74.0, 41.5], [-74.5, 41.5], [-74.5, 41.0]]] } },
    { "type": "Feature", "properties": { "name": "Passaic" }, "geometry": { "type": "Polygon", "coordinates": [[[-74.5, 40.8], [-74.0, 40.8], [-74.0, 41.2], [-74.5, 41.2], [-74.5, 40.8]]] } },
    { "type": "Feature", "properties": { "name": "Bergen" }, "geometry": { "type": "Polygon", "coordinates": [[[-74.2, 40.8], [-73.8, 40.8], [-73.8, 41.1], [-74.2, 41.1], [-74.2, 40.8]]] } },
    { "type": "Feature", "properties": { "name": "Morris" }, "geometry": { "type": "Polygon", "coordinates": [[[-74.8, 40.7], [-74.3, 40.7], [-74.3, 41.0], [-74.8, 41.0], [-74.8, 40.7]]] } },
    { "type": "Feature", "properties": { "name": "Essex" }, "geometry": { "type": "Polygon", "coordinates": [[[-74.3, 40.7], [-73.9, 40.7], [-73.9, 40.9], [-74.3, 40.9], [-74.3, 40.7]]] } },
    { "type": "Feature", "properties": { "name": "Somerset" }, "geometry": { "type": "Polygon", "coordinates": [[[-74.8, 40.4], [-74.3, 40.4], [-74.3, 40.7], [-74.8, 40.7], [-74.8, 40.4]]] } },
    { "type": "Feature", "properties": { "name": "Union" }, "geometry": { "type": "Polygon", "coordinates": [[[-74.4, 40.6], [-73.9, 40.6], [-73.9, 40.8], [-74.4, 40.8], [-74.4, 40.6]]] } },
    { "type": "Feature", "properties": { "name": "Middlesex" }, "geometry": { "type": "Polygon", "coordinates": [[[-74.6, 40.3], [-74.1, 40.3], [-74.1, 40.6], [-74.6, 40.6], [-74.6, 40.3]]] } },
    { "type": "Feature", "properties": { "name": "Hudson" }, "geometry": { "type": "Polygon", "coordinates": [[[-74.2, 40.6], [-73.8, 40.6], [-73.8, 40.8], [-74.2, 40.8], [-74.2, 40.6]]] } }
  ]
};

// Make the data available globally for other scripts
if (typeof window !== 'undefined') {
  window.njCountiesData = njCountiesData;
}

// Also export for module systems
if (typeof module !== 'undefined' && module.exports) {
  module.exports = njCountiesData;
}

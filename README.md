### TripDocs

#### A Final Project for CS530 Internet, Web and Cloud Systems

This app is meant to be a trip planner, which aggregates information on locales around the world.
It includes the following features:
 - Current weather forecast
 - Embedded map
 - New York Times articles from the Travel section, that highlight possible things to do at the specified location.
 - A section to take notes on items of interest, scheduled itinerary, etc.

This app was created to run on the Google Cloud Platform. It was deployed with Cloud Run. Newly created TripDocs are persistent documents, which are stored in a Datastore database. External APIs are accessed to provide weather, map, and travel articles to the user.


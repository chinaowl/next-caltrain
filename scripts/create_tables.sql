CREATE TABLE stop
(stop_id integer, stop_code integer, stop_name varchar, stop_desc varchar, stop_lat real, stop_lon real, zone_id smallint, stop_url varchar, location_type smallint, parent_station integer, platform_code varchar(2), wheelchair_boarding smallint);

CREATE TABLE stop_time
(trip_id varchar, arrival_time interval, departure_time interval, stop_id integer, stop_sequence smallint, pickup_type smallint, drop_off_type smallint);

CREATE TABLE trip
(route_id varchar, service_id varchar, trip_id varchar, trip_headsign varchar, trip_short_name smallint, direction_id smallint, block_id varchar, shape_id varchar, wheelchair_accessible smallint, bikes_allowed smallint);

\set path '/Users/chinaowl/Documents/github.nosync/next-caltrain/scripts/gtfs/'
\set stopsPath :path 'stops.txt'
\set stopTimesPath :path 'stop_times.txt'
\set tripsPath :path 'trips.txt'

COPY stop FROM :'stopsPath' WITH (FORMAT csv, HEADER true);
COPY stop_time FROM :'stopTimesPath' WITH (FORMAT csv, HEADER true);
COPY trip FROM :'tripsPath' WITH (FORMAT csv, HEADER true);

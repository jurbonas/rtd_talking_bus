# GTFS Python Sample

from google.transit import gtfs_realtime_pb2
import urllib

feed = gtfs_realtime_pb2.FeedMessage()
# Insert RTD .pb URL here
response = urllib.urlopen('URL OF YOUR GTFS-REALTIME SOURCE GOES HERE')
feed.ParseFromString(response.read())
for entity in feed.entity:
  if entity.HasField('trip_update'):
    print entity.trip_update

#parse through Protocol Buffer and do actions for speaking bus stop down here.


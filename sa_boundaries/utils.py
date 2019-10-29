from StringIO import StringIO
import csv

def points2csv(geojson_points):
    """
    Convert aa geojson points structure into a csv
    """

    fp = StringIO()
    writer = csv.writer(fp)
    for idx, feature in enumerate(geojson_points["features"]):
        headers = ["latitude", "longitude"]
        vals = []
        properties = feature["properties"]["data"]
        coordinates = feature["geometry"]["coordinates"]
        vals += coordinates

        for k, v in properties.items():
            vals.append(("%s" % v).encode("utf8"))
            headers.append(k)

        if idx == 0:
            writer.writerow(headers)
        writer.writerow(vals)

    return fp.getvalue()

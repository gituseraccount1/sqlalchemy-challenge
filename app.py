# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
# Used Module 10.3 activity 10-Ins_Flask_with_ORM as a reference
engine = create_engine("sqlite:///.../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
# Define the homepage
@app.route("/")
def homepage():
    return (
        f"Welcome to the homepage!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )


# Define what to do when a user hits the /api/v1.0/precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    all_data_and_perc = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= end_date).all()
    return jsonify(all_data_and_perc)



# Define what to do when a user hits the /api/v1.0/stations
@app.route("/api/v1.0/stations")
def stations():
    total_number_of_stations = session.query(Measurement.station).distinct().count()
    return jsonify(total_number_of_stations)



# Define what to do when a user hits the /api/v1.0/tobs
@app.route("/api/v1.0/tobs")
def tobs():
    most_active_station = session.query(Measurement.tobs, func.count(Measurement.tobs)).group_by(Measurement.tobs).filter(Measurement.station == most_active_station_id).all()
    return jsonify(most_active_station)



# Define what to do when a user hits the /api/v1.0/<start>
@app.route("/api/v1.0/<start>")
def start():



# Define what to do when a user hits the /api/v1.0/<start>/<end>
@app.route("/api/v1.0/<start>/<end>")
def startend():
    


if __name__ == "__main__":
    app.run(debug=True)

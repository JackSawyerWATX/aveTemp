import plotly.express as px
import pandas as pd
import numpy as np

# --- source lists ---
cities = [
"New York, NY","Los Angeles, CA","Chicago, IL","Houston, TX","Phoenix, AZ","Philadelphia, PA",
"San Antonio, TX","San Diego, CA","Dallas, TX","Austin, TX","Jacksonville, FL","Fort Worth, TX",
"Columbus, OH","Charlotte, NC","San Francisco, CA","Indianapolis, IN","Seattle, WA","Denver, CO",
"Oklahoma City, OK","Nashville, TN","El Paso, TX","Washington, DC","Las Vegas, NV","Boston, MA",
"Portland, OR","Detroit, MI","Louisville, KY","Memphis, TN","Baltimore, MD","Milwaukee, WI",
"Albuquerque, NM","Fresno, CA","Tucson, AZ","Sacramento, CA","Mesa, AZ","Kansas City, MO",
"Atlanta, GA","Omaha, NE","Colorado Springs, CO","Raleigh, NC","Long Beach, CA","Virginia Beach, VA",
"Miami, FL","Oakland, CA","Minneapolis, MN","Tulsa, OK","Tampa, FL","Arlington, TX","New Orleans, LA",
"Wichita, KS","Cleveland, OH","Bakersfield, CA","Aurora, CO","Anaheim, CA","Honolulu, HI",
"Santa Ana, CA","Riverside, CA","Corpus Christi, TX","Lexington, KY","Stockton, CA","Henderson, NV",
"St. Louis, MO","Saint Paul, MN","Pittsburgh, PA","Cincinnati, OH","Anchorage, AK","Greensboro, NC",
"Plano, TX","Lincoln, NE","Orlando, FL","Irvine, CA","Newark, NJ","Toledo, OH","Durham, NC",
"Chula Vista, CA","Fort Wayne, IN","Jersey City, NJ","St. Petersburg, FL","Laredo, TX","Chandler, AZ",
"Madison, WI","Lubbock, TX","Scottsdale, AZ","Reno, NV","Buffalo, NY","Gilbert, AZ","Glendale, AZ",
"North Las Vegas, NV","Winston-Salem, NC","Chesapeake, VA","Norfolk, VA","Fremont, CA","Garland, TX",
"Irving, TX","Boise, ID","Richmond, VA","Baton Rouge, LA","Spokane, WA","Des Moines, IA","Tacoma, WA"
]

temps_c = [13.9, 17.6, 11.0, 20.6, 23.6, 13.3, 20.4, 17.6, 19.4, 20.8, 21.0, 19.6, 11.2, 16.7, 14.1, 12.2,
           11.3, 10.3, 15.6, 15.8, 18.6, 14.6, 20.2, 11.1, 12.3, 10.2, 13.9, 17.0, 13.3, 8.9, 14.0, 18.9,
           20.5, 17.6, 23.0, 12.8, 17.0, 11.2, 9.7, 16.0, 18.3, 15.3, 24.6, 15.5, 8.5, 16.1, 23.1, 19.4,
           21.1, 13.9, 10.5, 10.0, 18.6, 24.2, 18.6, 18.5, 20.0, 13.3, 17.7, 20.7, 13.7, 7.8, 10.9, 12.0,
           2.0, 15.2, 19.1, 11.4, 22.8, 17.8, 13.3, 10.6, 15.8, 17.2, 11.6, 13.3, 23.0, 19.1, 8.9, 20.0,
           17.9, 11.6, 9.4, 22.6, 20.4, 20.2, 15.6, 15.5, 15.6, 15.5, 19.4, 19.4, 20.0, 11.5, 14.7, 20.6,
           9.8, 10.6, 11.4]

# --- make lengths match (pad with NaN or trim) ---
if len(temps_c) < len(cities):
    temps_c += [np.nan] * (len(cities) - len(temps_c))
elif len(temps_c) > len(cities):
    temps_c = temps_c[:len(cities)]

# --- build dataframe ---
data = pd.DataFrame({
    "City": cities,
    "Temperature in Celsius": temps_c
})

# --- plot ---
fig = px.bar(
    data,
    x="City",
    y="Temperature in Celsius",
    title="Average Temperature by City (°C)"
)
fig.update_layout(
    xaxis_title="City",
    yaxis_title="Average Temp (°C)",
    xaxis_tickangle=-45,
    bargap=0.15,
    height=650
)
fig.show()

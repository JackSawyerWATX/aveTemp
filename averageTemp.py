import plotly.express as px
import pandas as pd

data = pd.DataFrame({
  "City":["Tokyo", "Dehli", "Cario", "London", "New York City", "Seattle"],
  "Temperature in Celsius":[7.0, 25.0, 20.0, 11.0, 16.0, 11.0]
})

figure = px.bar(data, x='City', y='Temperature in Celsius', title='Average Temperature by Cities')

figure.show()
import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Add page options for the overall app.
ui.page_opts(title = "PyShiny App with Two Plots", fillable=True)

# Create a sidebar with a slider input
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 5, 100, 50)


@render.plot(alt="A histogram")
def histogram():
    # Define the number of points to generate. Use optional type hinting to indicate this is an integer.
    count_of_points: int = 1000
    # Set a random seed to ensure reproducibility.
    np.random.seed(777)
    # Generate random data:
    random_data_array = 200 + 20 * np.random.randn(count_of_points)
    # Create a histogram of the random data using matplotlib's hist() function:
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True, color = "green")
    plt.title("Histogram")
    
@render.plot(alt="A scatterplot")
def scatterplot():
    np.random.seed(777)
    count_of_points = input.selected_number_of_bins()
    X = np.random.randn(count_of_points) #adding the variable count_of_points to include input and keep the slider working to make scatterplot interactive
    Y = np.random.randn(count_of_points) #adding the variable count_of_points to include input and keep the slider working to make scatterplot interactive
    plt.scatter(X,Y)
    plt.title("Scatterplot")

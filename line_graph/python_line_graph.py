import matplotlib.pyplot as plt

## how to check python version in mac terminal
# python --version

## install the matplotlib package using the terminal
# python -m pip install --user matplotlib

## Use built-in styles
## To display available styles, type the ff on the terminal
# print(plt.style.available)
# ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery',
# '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background',
# 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8',
# 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind',
# 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette',
# 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep',
# 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook',
# 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel',
# 'seaborn-v0_8-poster', 'seaborn-v0_8-talk',
# 'seaborn-v0_8-ticks', 'seaborn-v0_8-white',
# 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']

## If abscissa starting point is not specified,
## python assumes that y1 corresponds to x = 0
## abscissa : year
## ordinate : annual average of heat index in LB, Laguna
HI =        [ 31.6, 30.50, 30.28, 30.37, 30.74, 29.41, 28.93]
years =     [ 2016, 2017,  2018,  2019,  2020,  2021,  2022]
HI_std_error = [ 0.14, 0.14,  0.13,  0.13,  0.16,  0.14,  0.11]

## subplot function can generate one or more plots in one figure
#plt.style.use("seaborn")
fig, heat_index = plt.subplots()
heat_index.grid(color='gray', linestyle='--', linewidth=0.6)
#fig, HI_err_bars = plt.subplots()
## create a line plot
#heat_index.plot(years, HI, "--", linewidth = 1, c="black")
## create a scatter plot
#heat_index.scatter(years, HI, c="black", linewidth = 3)
## plot with error bar
heat_index.errorbar(years, HI, linestyle="--", c="black", linewidth=1, yerr=HI_std_error,
                    marker="s", solid_capstyle='projecting', capsize=3)
## emphasize other values
# heat_index.scatter(2020,30.74, s=36)


## Set Chart Title and Label Axes
heat_index.set_title("Annual Average Heat Index in "
                     "Los Baños, Philippines",
                     fontsize=12)
heat_index.set_xlabel("Year", fontsize=12)
## insert degrees Celsius symbol
heat_index.set_ylabel("Heat Index ($^\circ$C)", fontsize=12)

## Set Size of Tick Labels
heat_index.tick_params(axis="both",
                       which="major",
                       labelsize=12)

## Set Range for each axis
# heat_index.axis([2016, 2022, 29, 33])

## opens Matplotlib viewer and display the plot
plt.show()

## To save figures automatically, replace plt.show() with
#plt.savefig("\~\Desktop\Annual_Ave_Heat_Index_Campus.png",
#            bbox_inches="tight")


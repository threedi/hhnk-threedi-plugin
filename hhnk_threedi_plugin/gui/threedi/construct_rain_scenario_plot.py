class PlotVars:
    def __init__(self, x, y, **kwargs):
        self.x = x
        self.y = y
        self.keyword_args = kwargs


class PatchVars:
    def __init__(self, coords, **kwargs):
        self.coords = coords
        self.keyword_args = kwargs


class Legend:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.keyword_args = kwargs


def create_results_plot(rain, detected_rain, days_dry_start, days_dry_end, timestep):
    """
    Initialization:
        create_results_plot(
            rain (list of rain at a node at every hour during scenario (type of node can be 1d or 2d))
            detected_rain (list of indexes in 'rain' where rain was found)
            days_dry_start (number of dry days before rain)
            days_dry_end (number of dry days after rain)
            timestep (list of time passed between timestamp and start sum in minutes (size of slice is constant))
            )
    """
    title = "Neerslag"
    xlabel = "Tijd [dagen]"
    ylabel = "Neerslag [mm/dag]"
    plots = []
    patches = []
    try:
        rain_plot = rain  # Toevoegen zodat er rechte lijnen geplot worden
        rain_plot.insert(detected_rain[-1], rain_plot[detected_rain[-1]])

        rain_plot = rain_plot + [rain_plot[-1]]

        # Plot de regen over de tijd
        x_dagen = [0] + [x / 24 for x in range(1, len(rain) - 1)]

        x_dagen.insert(detected_rain[0] - 1, x_dagen[detected_rain[0] - 1])
        x_dagen.insert(detected_rain[-1] + 1, x_dagen[detected_rain[-1] + 1])
        plots.append(PlotVars(x_dagen, [a * 100000 / 1.05833 for a in rain_plot]))
        plots.append(
            PlotVars(
                [days_dry_start, days_dry_start],
                [0, max(rain) * 100000 / 1.05833],
                c="green",
            )
        )
        plots.append(
            PlotVars(
                [
                    timestep[-1] / 60 / 24 - days_dry_end,
                    timestep[-1] / 60 / 24 - days_dry_end,
                ],
                [0, max(rain) * 100000 / 1.05833],
                c="green",
            )
        )
        patches.append(
            PatchVars(
                [
                    [days_dry_start, 0],
                    [timestep[-1] / 60 / 24 - days_dry_end, 0],
                    [
                        timestep[-1] / 60 / 24 - days_dry_end,
                        max(rain) * 100000 / 1.05833,
                    ],
                    [days_dry_start, max(rain) * 100000 / 1.05833],
                ],
                closed=True,
                alpha=0.2,
                color="green",
            )
        )
        legend = Legend(
            ["Neerslag", "Gedetecteerde neerslagperiode"],
            loc="upper right",
            fancybox=True,
            framealpha=0.5,
        )
        return {
            "plot_list": plots,
            "polygon_patch_list": patches,
            "title": title,
            "xlabel": xlabel,
            "ylabel": ylabel,
            "legend": legend,
        }
    except Exception as e:
        raise e from None

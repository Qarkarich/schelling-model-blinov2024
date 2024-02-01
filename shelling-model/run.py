import matplotlib.pyplot as plot
from matplotlib import colors
import streamlit
from app import App

if __name__ == '__main__':
    window = streamlit.container()
    with window:
        streamlit.title("Модель сегрегации Шеллинга: интерактивная симуляция")
        size = streamlit.sidebar.slider("размер сетки", 5, 100)
        density = streamlit.sidebar.slider("плотность населения", 0., 1.)
        tolerancy = streamlit.sidebar.slider("коэффициент толерантности агента", 1, 8)
        iteration_num = streamlit.sidebar.slider("кол-во итераций", 1)
        progress_bar = streamlit.progress(0)

    application = App(size, density, tolerancy)
    cmap = colors.ListedColormap(['white', 'red', 'royalblue'])
    plot.axis('off')

    plot.imshow(application.return_grid_visual(), cmap=cmap)
    main_plot = streamlit.pyplot(plot)

    if streamlit.sidebar.button('запуск'):
        for i in range(iteration_num):
            application.update()

            # print(application.return_cur_state()[2])

            # print(application.return_grid_visual())

            plot.imshow(application.return_grid_visual(), cmap=cmap)
            main_plot.pyplot(plot)

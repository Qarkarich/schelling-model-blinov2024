import matplotlib.pyplot as plot
from matplotlib import colors
import streamlit
from app import App

if __name__ == '__main__':
    window = streamlit.container()
    with window:
        streamlit.title("Модель сегрегации Шеллинга: интерактивная симуляция")
        size = streamlit.sidebar.slider("Размер сетки", 5, 100)
        density = streamlit.sidebar.slider("Плотность населения", 0., .99)
        tolerancy = streamlit.sidebar.slider("Коэффициент толерантности агента", 0., .99)
        iteration_num = streamlit.sidebar.slider("Кол-во итераций", 1)
        progress_bar = streamlit.progress(0)

    application = App(size * size, density, tolerancy, 1)

    cmap = colors.ListedColormap(['white', 'red', 'royalblue'])
    plot.axis('off')

    plot.imshow(application.city, cmap=cmap)
    main_plot = streamlit.pyplot(plot)

    if streamlit.sidebar.button('Запуск'):
        for i in range(iteration_num):
            application.update()
            plot.imshow(application.city, cmap=cmap)
            main_plot.pyplot(plot)

    main_plot.pyplot(plot)

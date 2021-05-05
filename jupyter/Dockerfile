FROM continuumio/anaconda3

# WORKDIR ./jupyter

RUN apt-get update && apt-get install -y libgtk2.0-dev && \
    rm -rf /var/lib/apt/lists/*

RUN /opt/conda/bin/conda update -n base -c defaults conda
RUN /opt/conda/bin/conda install -c anaconda sqlalchemy
RUN /opt/conda/bin/conda install -c anaconda sqlite
RUN /opt/conda/bin/conda install -c conda-forge pymongo
RUN pip install --upgrade pip
RUN pip install Flask Flask-Pymongo bs4 lxml selenium splinter

# I don't why this takes forever
# RUN /opt/conda/bin/conda install -c defaults --override-channels psycopg2
# RUN /opt/conda/bin/conda install -c conda-forge psycopg2
# RUN pip install psycopg2

# Install Chrome for Selenium
RUN curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /chrome.deb
RUN dpkg -i /chrome.deb || apt-get install -yf
RUN rm /chrome.deb

# Install chromedriver for Selenium
RUN curl https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip -o /usr/local/bin/chromedriver
RUN chmod +x /usr/local/bin/chromedriver

# Jupyter port
EXPOSE 8888

# Store notebooks in this mounted directory
VOLUME /notebooks

COPY ./jupyter.sh ./
RUN chmod +x jupyter.sh
CMD ["/jupyter.sh"] 

FROM python:3.8-slim-buster

# Install system dependencies
#RUN apt-get update && apt-get install ffmpeg -y

#RUN pip3 install --upgrade pip

RUN apt-get update \
        && apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libsndfile1-dev gcc -y 
# Set up python environement
COPY speaker/requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt

# Start
COPY speaker/src/ speaker/src/
WORKDIR /speaker/src
ENTRYPOINT ["python3", "-m", "main"]

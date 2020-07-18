FROM ubuntu
EXPOSE 8888
RUN ["/bin/bash", "-c", "apt-get update > /dev/null 2>&1"]
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata > /dev/null 2>&1
RUN ["/bin/bash", "-c", "apt-get install -y python3 > /dev/null 2>&1"]
RUN ["/bin/bash", "-c", "apt-get install -y python3-pip > /dev/null 2>&1"]
RUN ["/bin/bash", "-c", "apt-get install -y python3-venv > /dev/null 2>&1"]
RUN ["/bin/bash", "-c", "apt-get install -y python3-dev > /dev/null 2>&1"]
RUN ["/bin/bash", "-c", "apt-get install -y libpq-dev > /dev/null 2>&1"]
RUN mkdir /Musify
RUN mkdir /Musify/Musify
RUN mkdir /Musify/MusifyVenv
COPY ./Musify /Musify/Musify
WORKDIR /Musify/MusifyVenv
RUN ["/bin/bash", "-c", "python3 -m venv venv > /dev/null 2>&1"]
RUN ["/bin/bash", "-c", "source venv/bin/activate; python -m pip install grpcio > /dev/null 2>&1"]
RUN ["/bin/bash", "-c", "source venv/bin/activate; python -m pip install grpcio-tools > /dev/null 2>&1"]
RUN ["/bin/bash", "-c", "source venv/bin/activate; python -m pip install --upgrade wheel > /dev/null 2>&1"]
RUN ["/bin/bash", "-c", "source venv/bin/activate; python -m pip install --upgrade pip > /dev/null 2>&1"]
RUN ["/bin/bash", "-c", "apt-get install -y default-jre > /dev/null 2>&1"]
RUN ["/bin/bash", "-c", "apt-get install -y default-jdk > /dev/null 2>&1"]
CMD ["/bin/bash", "-c", "source venv/bin/activate; cd /Musify/Musify/grpc/src; python musify_service_server.py"]

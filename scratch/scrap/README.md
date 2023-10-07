!!for note, still no idea how to connecting drive to local. But can do, Download to zip it all root by these method
#put these command to jupyter cell to zip whole root for easy to grab file init!
!tar chvfz notebook.tar.gz *


#build docker
docker-compose up -d --build

#to shutdown docker compose
docker-compose down


#just in case put thus line before 'apt or place it on compose
ENV DEBIAN_FRONTEND noninteractive 
or
ARG DEBIAN_FRONTEND=noninteractive

but RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections did

#scrapy 
#######################

#create scrapy project
scrapy startproject "project_name"

#create the spider
#changed diretory to project location, inside the project scraping type :
scrapy genspider "spider_name" "website_url"
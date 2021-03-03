FROM golang:1.15
# dependencies for Go lang
ENV GO111MODULE=on \
    CGO_ENABLED=0 \
    GOOS=linux \
    GOARCH=amd64 
RUN go get -u github.com/Fullscript/go-web-server
# Move to working directory /build
WORKDIR /Users/nidumukkalasaiprasanth/Downloads/dockerlearn/gowebserver/go-web-server

# Copy and download dependency using go mod
COPY go.mod .
COPY go.sum .
RUN go mod download

# Copy the code into the container
COPY . .

# Build the application
RUN go build -o main .

# Move to /dist directory as the place for resulting binary folder
WORKDIR /Users/nidumukkalasaiprasanth/Downloads/dockerlearn/gowebserver/go-web-server

# Copy binary from build to main folder
RUN cp /Users/nidumukkalasaiprasanth/Downloads/dockerlearn/gowebserver/go-web-server
/main .

import "github.com/docker/go-healthcheck/health"

# Export necessary port
EXPOSE 8080

CMD ["go-web-server", "run"]






















#RUN go get -u github.com/Fullscript/go-web-server
#ENV GO111MODULE=on
#ENV APP_HOME /go/src/gowebserver
#HEALTHCHECK CMD curl --fail http://localhost:8080/ || exit 1
#HEALTHCHECK CMD command
#WORKDIR /go/src/gowebserver
#EXPOSE 8080
#CMD ["go-web-server", "run"]

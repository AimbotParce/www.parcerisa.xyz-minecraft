# www.parcerisa.xyz-minecraft
Simple web page to display the status of the minecraft server

## How to use

To run the server, you must mount the following volumes:
/folder/where/backups/are/stored:/backups
/folder/where/server/is/located:/server

You can also set the ammount of workers with the WORKERS environment variable.


Then, you can run the server with the following command:
```
docker run -d -p 3004:3004 -v /folder/where/backups/are/stored:/backups -v /folder/where/server/is/located:/server -e WORKERS=4
--name www.parcerisa.xyz-minecraft www.parcerisa.xyz/minecraft
```


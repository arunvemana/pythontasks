Develop a script to edit yaml data file.
-- check the sample.yml for the format

[sample format file](./Sample_in.yaml)

so when user execute jon from the jenkins and wants to update

locations it must do that like user will just pass hostname and locations from jenkins 

like:-

> ./code.py 'qcant.playerzpot.com' 'v1:3002, v2:3003' 

so it must update the yaml file with this content for the hostname
near `profile::antcandy::location`


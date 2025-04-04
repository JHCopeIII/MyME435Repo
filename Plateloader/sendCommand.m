function [outputArg1,outputArg2] = sendCommand(command)

getUrl = "" + command
% response = webread(getUrl)

options = weboptions('Timeout', 30);
response = webread(geturl,options);

end

